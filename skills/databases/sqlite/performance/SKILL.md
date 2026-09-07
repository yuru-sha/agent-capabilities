---
name: sqlite-performance
description: "Use when SQLite work involves query performance and workload evidence."
---

# SQLite Performance

Use this specialist with the primary language skill and `$code-review` when reviewing a change. It owns only engine-specific decisions for this concern.

## Rules

- Use EXPLAIN QUERY PLAN and representative file/workload data before changing SQL or indexes.
- Check single-writer contention, cache behavior, N+1 access, transaction length, file growth, ANALYZE, and checkpoint cost.
- Record SQLite version, journal mode, dataset, and measurement command behind a claim.

