---
name: postgresql-partitioning
description: "Use when PostgreSQL tables are partitioned, partition keys or pruning change, or retention and attach/detach operations are designed."
---

# PostgreSQL Partitioning

Use with `postgresql-indexes`, `postgresql-migrations`, and
`postgresql-query-plan-regression`.

## Check

- Choose a partition key that matches access and retention patterns; verify pruning with representative predicates and parameters.
- Check partition constraints, default partitions, indexes, uniqueness limitations, foreign keys, generated values, and cross-partition queries.
- Design attach/detach, backfill, retention, and creation workflows with lock duration and validation cost made explicit.
- Handle out-of-range rows, missing partitions, timezone or boundary semantics, and statistics per partition.
- Test old and new application versions during partition changes and prove that the intended plan is used.

