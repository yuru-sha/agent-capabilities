---
name: sqlite-indexes
description: "Use when SQLite work involves index design and query plans."
---

# SQLite Indexes

Use this specialist with the primary language skill and `$code-review` when reviewing a change. It owns only engine-specific decisions for this concern.

## Rules

- Design indexes from predicates, joins, and sort order while accounting for file size, writes, and the single-writer model.
- Use partial or covering indexes only when EXPLAIN QUERY PLAN and representative data justify them.
- Check whether ANALYZE, cache behavior, and a large scan change the observed plan.

