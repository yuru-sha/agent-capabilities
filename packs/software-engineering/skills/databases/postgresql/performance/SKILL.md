---
name: postgresql-performance
description: "Use when PostgreSQL work involves query performance and workload evidence."
---

# PostgreSQL Performance

Use this specialist with the primary language skill and `$code-review` when reviewing a change. It owns only engine-specific decisions for this concern.

## Rules

- Use representative EXPLAIN ANALYZE, cardinality, and workload evidence before changing SQL or indexes.
- Check N+1 queries, unnecessary columns, pagination, pool limits, statement timeouts, vacuum/analyze, and contention.
- Record the query shape, dataset assumptions, and measurement command behind a performance claim.

