---
name: aws-eventbridge
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon EventBridge event buses, rules, patterns, targets, retries, DLQs, archives/replay, schemas, or Scheduler integrations."
---

# aws-eventbridge

Use this skill for eventbridge-specific AWS behavior. Compose it with adjacent service Skills when broader architecture is in scope.

## Reference routing

- events-patterns-and-routing -> references/events-patterns-and-routing.md
- delivery-retries-dlq-and-replay -> references/delivery-retries-dlq-and-replay.md

## Rules

- Define event contract and ownership before rules.
- Keep patterns selective and review broad matches carefully.
- Treat target delivery as retryable and consumers as idempotent.
- Use DLQs and archives/replay with explicit recovery procedures.
- Keep cross-account event-bus policies narrow.
- Treat references/ as detailed guidance, not independently selectable skills.
