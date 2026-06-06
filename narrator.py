#!/usr/bin/env python3
"""apra-compliance-narrator — turn AWS security findings into a board-ready,
APRA-paragraph narrative compliance report.

Pipeline:  Prowler compliance CSV  +  APRA framework JSON
           -> aggregate per CPS 234 control (status + evidence)
           -> narrate (template engine, or Amazon Bedrock / Claude)
           -> Markdown report (exec summary, control-by-control, remediation roadmap)

Engines:
  --engine template   deterministic, offline, uses the framework's rationale/remediation (default)
  --engine bedrock    sends each control's structured data to Claude on Amazon Bedrock

Examples:
  python narrator.py --findings compliance.csv --framework apra_cps_234_aws.json -o report.md
  python narrator.py --findings compliance.csv --framework apra_cps_234_aws.json \
      --engine bedrock --model apac.anthropic.claude-sonnet-4-20250514-v1:0 --region ap-southeast-2
"""
import argparse
import csv
import json
import os
from collections import OrderedDict

SYSTEM_PROMPT = (
    "You are an APRA CPS 234 compliance analyst. Write a concise, board-ready paragraph "
    "(3-5 sentences) for one control, in plain professional English for a risk committee. "
    "State the compliance position, what the evidence shows, why it matters under CPS 234, "
    "and the priority remediation. Do not invent findings beyond those provided."
)


def load_framework(path):
    """control_id -> {name, paragraph, section, rationale, remediation, reference, status}."""
    data = json.load(open(path))
    meta = {}
    for r in data["Requirements"]:
        a = r["Attributes"][0]
        meta[r["Id"]] = {
            "name": r.get("Name") or r["Id"],
            "description": r["Description"],
            "section": a.get("Section", ""),
            "paragraph": a.get("ItemId", ""),
            "assessment": a.get("AssessmentStatus", ""),
            "rationale": a.get("RationaleStatement", ""),
            "impact": a.get("ImpactStatement", ""),
            "remediation": a.get("RemediationProcedure", ""),
            "reference": a.get("References", ""),
        }
    return data, meta


def aggregate(csv_path):
    """control_id -> {status, fails:[{detail,resource,check}], pass_count, total}."""
    rows = list(csv.DictReader(open(csv_path), delimiter=";"))
    agg = OrderedDict()
    account = region = date = ""
    for r in rows:
        # keep first non-empty value (manual-control rows leave these blank)
        account = r.get("ACCOUNTID") or account
        region = r.get("REGION") or region
        date = r.get("ASSESSMENTDATE") or date
        cid = r["REQUIREMENTS_ID"]
        a = agg.setdefault(cid, {"status": None, "fails": [], "pass_count": 0, "total": 0})
        st = (r.get("STATUS") or "").upper()
        a["total"] += 1
        if st == "FAIL":
            a["fails"].append({
                "detail": r.get("STATUSEXTENDED", ""),
                "resource": r.get("RESOURCEID", ""),
                "check": r.get("CHECKID", ""),
            })
        elif st == "PASS":
            a["pass_count"] += 1
        # worst-case rollup: FAIL > MANUAL > PASS
        rank = {"FAIL": 0, "MANUAL": 1, "PASS": 2, "": 3}
        if a["status"] is None or rank.get(st, 3) < rank.get(a["status"], 3):
            a["status"] = st or "MANUAL"
    return agg, {"account": account, "region": region, "date": date}


def narrate_template(meta, agg):
    """Deterministic narrative paragraph from structured data (no LLM)."""
    if agg["status"] == "FAIL":
        n = len(agg["fails"])
        lead = (f"**Not compliant.** {n} issue(s) detected against this control. "
                f"{meta['rationale']} {meta['impact']}")
        rem = f"Priority remediation: {meta['remediation']}"
        return f"{lead} {rem}"
    if agg["status"] == "PASS":
        return (f"**Compliant.** All {agg['pass_count']} automated check(s) for this control "
                f"passed. {meta['rationale']}")
    return (f"**Manual assessment required.** {meta['rationale']} This obligation is not "
            f"observable from AWS APIs and must be evidenced via documentation/process: "
            f"{meta['remediation']}")


def narrate_bedrock(client, model_id, meta, agg):
    """Generate the paragraph with Claude on Amazon Bedrock (Converse API)."""
    findings = "\n".join(f"- {f['detail']} ({f['check']})" for f in agg["fails"]) or "None"
    user = (
        f"Control: {meta['name']} (CPS 234 paragraph {meta['paragraph']})\n"
        f"Status: {agg['status']}\n"
        f"Requirement: {meta['description']}\n"
        f"Rationale: {meta['rationale']}\n"
        f"Findings:\n{findings}\n"
        f"Remediation guidance: {meta['remediation']}\n"
    )
    resp = client.converse(
        modelId=model_id,
        system=[{"text": SYSTEM_PROMPT}],
        messages=[{"role": "user", "content": [{"text": user}]}],
        inferenceConfig={"maxTokens": 400, "temperature": 0.2},
    )
    return resp["output"]["message"]["content"][0]["text"].strip()


def build_report(framework, meta, agg, ctx, engine, model_id, region):
    fw_name = framework.get("Name", "APRA CPS 234")
    controls = [cid for cid in meta if cid in agg]
    fails = [c for c in controls if agg[c]["status"] == "FAIL"]
    passes = [c for c in controls if agg[c]["status"] == "PASS"]
    manual = [c for c in controls if agg[c]["status"] == "MANUAL"]
    automated = len(fails) + len(passes)
    score = round(100 * len(passes) / automated) if automated else 0

    bedrock = None
    if engine == "bedrock":
        import boto3  # noqa: deferred so template mode needs no AWS deps
        bedrock = boto3.client("bedrock-runtime", region_name=region)

    def narrate(cid):
        if engine == "bedrock":
            try:
                return narrate_bedrock(bedrock, model_id, meta[cid], agg[cid])
            except Exception as e:  # fall back so a PoC run never hard-fails
                return f"_(Bedrock unavailable: {e}; template fallback)_ " + narrate_template(meta[cid], agg[cid])
        return narrate_template(meta[cid], agg[cid])

    L = []
    L.append(f"# {fw_name} — AWS Compliance Report")
    L.append("")
    L.append(f"**Account:** {ctx['account']}  ·  **Region:** {ctx['region']}  ·  "
             f"**Assessed:** {ctx['date']}  ·  **Engine:** {engine}")
    L.append("")
    L.append("## Executive summary")
    L.append("")
    L.append(f"This report assesses the account against **{fw_name}**. Of "
             f"**{automated} automated controls**, **{len(passes)} passed** and "
             f"**{len(fails)} failed** — an automated compliance score of **{score}%**. "
             f"A further **{len(manual)} controls require manual assessment** (governance/process "
             f"obligations not observable from AWS APIs).")
    L.append("")
    if fails:
        L.append("**Priority controls not met:**")
        for c in fails:
            L.append(f"- CPS 234 ¶{meta[c]['paragraph']} — {meta[c]['name']} "
                     f"({len(agg[c]['fails'])} finding(s))")
        L.append("")

    # Group by section
    sections = OrderedDict()
    for c in controls:
        sections.setdefault(meta[c]["section"], []).append(c)

    L.append("## Control-by-control assessment")
    icon = {"FAIL": "❌", "PASS": "✅", "MANUAL": "📋"}
    for section, cids in sections.items():
        L.append("")
        L.append(f"### {section}")
        for c in cids:
            a = agg[c]
            L.append("")
            L.append(f"#### {icon.get(a['status'],'•')} CPS 234 ¶{meta[c]['paragraph']} — {meta[c]['name']}  · {a['status']}")
            L.append("")
            L.append(narrate(c))
            if a["fails"]:
                L.append("")
                L.append("> **Evidence:**")
                for f in a["fails"][:8]:
                    L.append(f"> - {f['detail']}")
            if meta[c]["reference"]:
                L.append("")
                L.append(f"_Reference: {meta[c]['reference']}_")

    # Remediation roadmap
    if fails:
        L.append("")
        L.append("## Remediation roadmap")
        for i, c in enumerate(fails, 1):
            L.append(f"{i}. **¶{meta[c]['paragraph']} {meta[c]['name']}** — {meta[c]['remediation']}")

    L.append("")
    L.append("---")
    L.append("_Generated by apra-compliance-narrator. Automated controls reflect AWS Config / "
             "Prowler findings; manual controls require human assessment. Verify against the "
             "official APRA CPS 234 standard._")
    return "\n".join(L)


def main():
    p = argparse.ArgumentParser(description="APRA CPS 234 narrative compliance report generator")
    p.add_argument("--findings", required=True, help="Prowler APRA compliance CSV")
    p.add_argument("--framework", required=True, help="apra_cps_234_aws.json")
    p.add_argument("--engine", choices=["template", "bedrock"], default="template")
    p.add_argument("--model", default=os.environ.get("BEDROCK_MODEL_ID", "apac.anthropic.claude-sonnet-4-20250514-v1:0"))
    p.add_argument("--region", default=os.environ.get("AWS_REGION", "ap-southeast-2"))
    p.add_argument("-o", "--output", default="apra-report.md")
    args = p.parse_args()

    framework, meta = load_framework(args.framework)
    agg, ctx = aggregate(args.findings)
    report = build_report(framework, meta, agg, ctx, args.engine, args.model, args.region)
    with open(args.output, "w") as f:
        f.write(report)
    fails = sum(1 for c in meta if c in agg and agg[c]["status"] == "FAIL")
    print(f"Wrote {args.output} ({len(report)} chars) · engine={args.engine} · failing controls={fails}")


if __name__ == "__main__":
    main()
