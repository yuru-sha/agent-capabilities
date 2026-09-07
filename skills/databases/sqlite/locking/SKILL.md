---
name: sqlite-locking
description: "Use when SQLite work involves locking, contention, and concurrency."
---

# SQLite Locking

Use this specialist with the primary language skill and `$code-review` when reviewing a change. It owns only engine-specific decisions for this concern.

## Rules

- Understand rollback-journal versus WAL, busy timeouts, checkpoints, and reader/writer interactions for the deployment.
- Make the single-writer boundary visible and avoid assuming a lock provides PostgreSQL-style row ownership.
- Keep lock duration bounded and test contention rather than adding blind retries.

