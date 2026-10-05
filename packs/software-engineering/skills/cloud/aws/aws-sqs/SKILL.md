---
name: aws-sqs
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon SQS producers, consumers, FIFO/Standard queues, visibility, retries, DLQs, or AWS queue integrations."
---

# aws-sqs

Use this skill for SQS-specific messaging semantics and integrations. Compose it with the existing AWS/infrastructure profile when broader IAM, networking, Terraform, Lambda, ECS, or CloudWatch infrastructure is in scope.

## Reference routing

- `queue-selection-and-message-model` → `references/queue-selection-and-message-model.md`
- `delivery-visibility-and-idempotency` → `references/delivery-visibility-and-idempotency.md`
- `consumers-and-batching` → `references/consumers-and-batching.md`
- `dlq-and-recovery` → `references/dlq-and-recovery.md`
- `security-observability-and-integrations` → `references/security-observability-and-integrations.md`

## Rules

- Choose Standard vs FIFO from ordering, deduplication, throughput, and message-group requirements before implementation.
- Treat SQS consumers as idempotent; Standard queues use at-least-once delivery and duplicate deliveries remain possible.
- Size visibility timeout from real processing latency and extend it deliberately for long-running work.
- Prefer long polling and batch APIs where appropriate.
- Use DLQs with an explicit redrive and replay procedure; a DLQ without recovery ownership is incomplete.
- With Lambda event source mappings, use partial batch responses when individual-record failures should not replay successful records.
- Treat `references/` as detailed guidance, not independently selectable skills.
