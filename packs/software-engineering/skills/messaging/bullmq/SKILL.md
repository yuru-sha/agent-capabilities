---
name: bullmq
description: "Use when designing, implementing, reviewing, operating, or troubleshooting BullMQ queues, workers, job flows, scheduling, retries, or Redis-backed background processing."
---

# BullMQ

Use this skill for BullMQ-specific job-queue design and operations. Use the `redis` skill separately when the task concerns Redis topology, persistence, memory, ACL/TLS, or general Redis behavior.

## Reference routing

- `queue-and-job-design` → `references/queue-and-job-design.md`
- `delivery-retries-and-idempotency` → `references/delivery-retries-and-idempotency.md`
- `workers-and-concurrency` → `references/workers-and-concurrency.md`
- `scheduling-and-flows` → `references/scheduling-and-flows.md`
- `redis-operations-and-observability` → `references/redis-operations-and-observability.md`

## Rules

- Model jobs as retriable messages, not exactly-once function calls.
- Make idempotency, timeout, retry, backoff, retention, and failure ownership explicit.
- Keep queue producers responsive to caller-facing latency; keep workers resilient to temporary Redis disconnects.
- Treat stalled jobs as possible re-deliveries and test duplicate execution.
- Prefer multiple worker processes/instances for availability; use local concurrency primarily for I/O-bound work.
- BullMQ 2 and later do not require the legacy `QueueScheduler` for delayed/stalled bookkeeping; verify version-specific behavior before copying older examples.
- Treat `references/` as detailed guidance, not independently selectable skills.
