---
name: aws-sns
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon SNS topics, subscriptions, fan-out, filtering, FIFO topics, retries, DLQs, mobile or HTTP delivery, or cross-account access."
---

# aws-sns

Use this skill for sns-specific AWS behavior. Compose it with adjacent service Skills when broader architecture is in scope.

## Reference routing

- topics-subscriptions-and-filtering -> references/topics-subscriptions-and-filtering.md
- delivery-fifo-security-and-recovery -> references/delivery-fifo-security-and-recovery.md

## Rules

- Choose Standard vs FIFO deliberately.
- Use subscription filters with visible ownership and change impact.
- Treat subscribers as idempotent.
- Use DLQs where failed delivery needs operator recovery.
- Keep topic and subscriber policies aligned.
- Treat references/ as detailed guidance, not independently selectable skills.
