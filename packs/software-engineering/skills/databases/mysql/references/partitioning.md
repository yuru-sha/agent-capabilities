---
name: mysql-partitioning
description: "Use when MySQL RANGE, LIST, HASH, or KEY partitioning, pruning, partition maintenance, or partition-key constraints are in scope."
---

# MySQL Partitioning

Use with `mysql-indexes`, `mysql-migrations`, `mysql-online-ddl`, and
`mysql-performance`.

## Check

- Choose a partition expression that matches retention and access predicates; verify pruning with representative literals and parameters.
- Check unique/primary-key requirements involving the partition key, partitioning expression limits, foreign-key behavior, and generated/default values.
- Design add/drop/truncate/exchange or rebuild operations with locks, disk, binlog, replication, and recovery impact explicit.
- Handle `MAXVALUE`, out-of-range data, time boundaries, missing partitions, and statistics per partition.
- Test old and new application versions, full scans, cross-partition uniqueness, and query plans before and after the change.

