# apra-compliance-narrator

> An **AI compliance-report generator for AWS**: feed it findings from **Prowler, Security Hub, or AWS Config**, and it uses **Amazon Bedrock (Claude)** to produce a board-ready, **APRA-paragraph-mapped narrative report** (PDF) — exec summary, paragraph-by-paragraph mapping, cited evidence, and a remediation roadmap.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Amazon Bedrock](https://img.shields.io/badge/Amazon-Bedrock-orange.svg)](https://aws.amazon.com/bedrock/)

**Keywords:** AI compliance report AWS Bedrock · APRA CPS 234 report generator · AWS security findings to narrative · Bedrock Claude compliance · automated APRA evidence

---

## Why this exists

Security tools produce **findings**. Regulators and boards want **narrative evidence** — "demonstrate, in plain language mapped to CPS 234 paragraph 35, that your information assets are encrypted." The translation from raw findings to a board-ready compliance story is manual, slow, and the single biggest time-sink in an APRA review.

This tool closes that gap. It's the artifact that makes the CISO conversation real: **AI + AWS + compliance in one demonstrable piece** — and the seed of the flagship product.

---

## How it works

```
  Prowler / Security Hub / Config findings (JSON)
                    │
                    ▼
        ┌───────────────────────┐
        │  Mapping engine        │  findings → CPS 234 paragraphs
        └───────────┬───────────┘
                    ▼
        ┌───────────────────────┐
        │  Amazon Bedrock (Claude)│  paragraph-by-paragraph narrative
        └───────────┬───────────┘
                    ▼
        Board-ready PDF: exec summary · mapping · evidence · roadmap
```

---

## Usage

Generate the Prowler input, then narrate it:

```bash
# 1. Produce a CPS 234 compliance report with Prowler (the companion framework)
prowler aws --compliance apra_cps_234_aws --region ap-southeast-2

# 2a. Narrate it — template engine (offline, no AWS calls, default)
python narrator.py \
  --findings output/compliance/<...>_apra_cps_234_aws.csv \
  --framework apra_cps_234_aws.json \
  -o apra-report.md

# 2b. Narrate it — Amazon Bedrock (Claude) for polished prose
python narrator.py \
  --findings <compliance.csv> --framework apra_cps_234_aws.json \
  --engine bedrock --model apac.anthropic.claude-sonnet-4-20250514-v1:0 \
  --region ap-southeast-2 -o apra-report.md
```

**Two engines:**
- `template` — deterministic, offline, builds the narrative from the framework's rationale/remediation. No AWS/LLM dependency. Great for CI and air-gapped review.
- `bedrock` — sends each control's structured findings to Claude on Amazon Bedrock (Converse API) for board-grade prose. Requires Bedrock model access in the account; falls back to the template per-control if Bedrock is unavailable.

A worked example is in [`samples/`](samples/) — real Prowler findings (`sample-compliance.csv`) → [`sample-apra-report.md`](samples/sample-apra-report.md).

---

## Report sections

1. **Executive summary** — posture in board language (automated score + manual-control count)
2. **Control-by-control assessment** — each CPS 234 paragraph → status → narrative
3. **Evidence cited** — the specific findings backing each claim
4. **Remediation roadmap** — prioritised actions

---

## Status

✅ **Working proof-of-concept.** `narrator.py` runs end-to-end (template + Bedrock engines) and has been validated against a real account's Prowler CPS 234 findings — see `samples/`. Next: PDF rendering and Security Hub / Config (OCSF) ingestion in addition to the Prowler CSV.

---

## Related

- 📖 Blog: [Turning AWS Security Findings into APRA-Paragraph Narrative with Bedrock](https://aiopsone.com/blog/bedrock-apra-narrative)
- 🧰 Feeds from: [`cps234-aws-config-pack`](https://github.com/jaybilgaye/cps234-aws-config-pack) + Prowler APRA frameworks
- 🌐 More at **[aiopsone.com](https://aiopsone.com)** — AI-powered AWS Security & Cloud Operations for APRA-regulated Australia.
