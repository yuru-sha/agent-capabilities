---
name: waf
description: "Use when designing, implementing, reviewing, operating, or troubleshooting AWS WAF web ACLs, managed or custom rules, rate-based rules, IP sets, regex matching, logging, bot controls, or false-positive handling."
---

# waf

Use this skill for waf-specific AWS behavior. Compose it with adjacent service Skills when broader architecture is in scope.

## Reference routing

- web-acls-rules-and-managed-groups -> references/web-acls-rules-and-managed-groups.md
- rate-controls-rollout-and-observability -> references/rate-controls-rollout-and-observability.md

## Rules

- Start new rules in Count mode where practical.
- Keep managed-rule overrides explicit and justified.
- Treat rate rules as abuse controls, not autoscaling.
- Preserve visibility into false positives.
- Do not use WAF as a substitute for application authorization.
- Treat references/ as detailed guidance, not independently selectable skills.
