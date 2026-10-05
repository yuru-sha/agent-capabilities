---
name: kinesis
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon Kinesis Data Streams producers, consumers, partitioning, shards, ordering, replay, scaling, retention, Lambda integrations, or stream-processing reliability."
---

# Amazon Kinesis Data Streams

Use this skill for Kinesis Data Streams-specific event-stream semantics and integrations. It does not cover Amazon Data Firehose as a separate delivery service. Compose it with the existing AWS/infrastructure profile when broader IAM, networking, Terraform, Lambda, ECS, or CloudWatch infrastructure is in scope.

## Reference routing

- `stream-selection-and-event-model` → `references/stream-selection-and-event-model.md`
- `partitioning-ordering-and-throughput` → `references/partitioning-ordering-and-throughput.md`
- `consumers-checkpointing-and-replay` → `references/consumers-checkpointing-and-replay.md`
- `scaling-retention-and-backpressure` → `references/scaling-retention-and-backpressure.md`
- `lambda-security-observability-and-recovery` → `references/lambda-security-observability-and-recovery.md`

## Rules

- Choose Kinesis when ordered partitioned event streams, multiple independent consumers, or replay are requirements; do not use it as a generic substitute for a work queue.
- Choose partition keys from ordering and load-distribution requirements together; a correct ordering key can still create a hot shard.
- Treat consumers as at-least-once processors and make idempotency/checkpoint behavior explicit.
- Model shard capacity, batching, record size, consumer lag, and retry amplification before production rollout.
- Prefer KCL or a similarly explicit lease/checkpoint model for stateful consumers that need resharding support; understand its DynamoDB dependency.
- Use Enhanced Fan-Out when dedicated per-consumer throughput/latency justifies the cost and registration model.
- Define replay, poison-record handling, retention, and downstream backpressure procedures before incidents occur.
- Load the smallest set of references that covers the current concern.
- Treat `references/` as detailed guidance, not independently selectable skills.
