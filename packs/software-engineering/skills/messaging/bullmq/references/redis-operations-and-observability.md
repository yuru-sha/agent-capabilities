# BullMQ Redis operations and observability

Use the separate `redis` skill for general Redis design and production topology.

## Connections

- `Queue`, `Worker`, `QueueEvents`, and related classes consume Redis connections differently; blocking classes may duplicate connections.
- Producers serving interactive requests should fail in bounded time during Redis outages.
- Workers should generally keep reconnecting so background processing can resume.
- When supplying an existing ioredis connection to a Worker, account for BullMQ's retry requirements; verify adapter/client-specific behavior for non-ioredis clients.
- Bound total connections across workers, queues, events, replicas, and deployments.

## Observability

Track:
- waiting, active, delayed, completed, failed, and stalled jobs;
- oldest-job age / queue latency;
- retry count and failure reasons;
- processing duration;
- worker availability and concurrency;
- Redis connection errors and command latency.

Alert on sustained backlog age, repeated stalls, retry storms, DLQ-like failed-job accumulation, and downstream saturation.
