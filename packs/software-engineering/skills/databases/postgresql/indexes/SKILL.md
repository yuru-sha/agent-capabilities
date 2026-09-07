---
name: postgresql-indexes
description: "Use when PostgreSQL work involves index design and query plans."
---

# PostgreSQL Indexes

Use this specialist with the primary language skill and `$code-review` when reviewing a change. It owns only engine-specific decisions for this concern.

## Rules

- Design indexes from real predicates, joins, sort order, and selectivity; check write and storage cost.
- Choose multicolumn order, partial, covering, GIN, or GiST indexes only for a measured query shape.
- Verify representative plans with EXPLAIN or EXPLAIN ANALYZE and account for statistics and data distribution.

