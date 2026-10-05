---
name: redis
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Redis-backed data, caching, coordination, streaming, or ephemeral state. Load only the references relevant to the current concern."
---

# Redis

Use this domain skill as the entry point for Redis work. Keep working context small by loading only the references needed for the task.

## Reference routing

- `data-model-and-keys` → `references/data-model-and-keys.md`
- `atomicity-and-coordination` → `references/atomicity-and-coordination.md`
- `performance-and-memory` → `references/performance-and-memory.md`
- `persistence-and-availability` → `references/persistence-and-availability.md`
- `operations-and-security` → `references/operations-and-security.md`

## Rules

- Start from the workload: access pattern, cardinality, payload size, consistency needs, failure tolerance, latency target, and retention.
- Treat Redis as an in-memory data system with explicit durability and eviction tradeoffs, not as a generic replacement for a relational database.
- Prefer native atomic commands and bounded scripts over distributed locking when a single-key or single-slot atomic primitive can express the invariant.
- Make TTL, eviction, persistence, reconnect, retry, and failover behavior explicit for production use.
- Never use `KEYS` on unbounded production keyspaces; prefer bounded iteration with `SCAN` and workload-aware limits.
- Load the smallest set of references that covers the current concern.
- Treat `references/` as detailed guidance, not independently selectable skills.
