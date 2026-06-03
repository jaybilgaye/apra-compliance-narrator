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

## Planned usage

```bash
# Generate an APRA CPS 234 narrative report from Prowler output
narrator generate \
  --input prowler-findings.json \
  --framework cps234 \
  --output apra-cps234-report.pdf
```

---

## Report sections

1. **Executive summary** — posture in board language
2. **Paragraph-by-paragraph mapping** — each CPS 234 control → status → evidence
3. **Evidence cited** — the specific findings backing each claim
4. **Remediation roadmap** — prioritised, owner-assignable actions

---

## Status

🚧 **Flagship — scaffold + README first (Day 0).** Proof-of-concept targeted for the Days 27–30 window; becomes a real demo in the 60-day plan. Currently in private design.

---

## Related

- 📖 Blog: [Using Bedrock to turn AWS security findings into APRA-paragraph narrative](https://aiopsone.com/blog/bedrock-apra-narrative) *(link goes live with the post)*
- 🧰 Feeds from: [`cps234-aws-config-pack`](https://github.com/jaybilgaye/cps234-aws-config-pack) + Prowler APRA frameworks
- 🌐 More at **[aiopsone.com](https://aiopsone.com)** — AI-powered AWS Security & Cloud Operations for APRA-regulated Australia.
