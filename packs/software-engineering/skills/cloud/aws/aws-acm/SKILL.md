---
name: aws-acm
description: "Use when designing, implementing, reviewing, operating, or troubleshooting AWS Certificate Manager certificates, validation, renewal, exportable public certificates, Private CA integration, or certificate deployment."
---

# aws-acm

Use this skill for acm-specific AWS behavior. Compose it with adjacent service Skills when broader architecture is in scope.

## Reference routing

- issuance-validation-and-renewal -> references/issuance-validation-and-renewal.md
- deployment-export-and-security -> references/deployment-export-and-security.md

## Rules

- Prefer automatable validation where practical.
- Keep Region constraints aligned with consuming services.
- Monitor renewal and expiry.
- Protect exported private keys and passwords as secrets.
- Distinguish public ACM and Private CA lifecycles.
- Treat references/ as detailed guidance, not independently selectable skills.
