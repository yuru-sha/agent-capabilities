---
name: postgresql-locking
description: "Use when PostgreSQL work involves locking, contention, and concurrency."
---

# PostgreSQL Locking

Use this specialist with the primary language skill and `$code-review` when reviewing a change. It owns only engine-specific decisions for this concern.

## Rules

- Document row/table/advisory lock ownership and lock order; use FOR UPDATE or advisory locks for a stated invariant.
- Keep lock duration short and analyze deadlock and timeout behavior before adding retries.
- Do not use a lock to compensate for missing constraints or unclear ownership.

