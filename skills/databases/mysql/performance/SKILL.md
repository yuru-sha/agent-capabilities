---
name: mysql-performance
description: "Use when MySQL query performance, optimizer plans, statistics, buffer usage, slow queries, or workload regressions are reviewed."
---

# MySQL Performance

Use with `mysql-indexes`, `mysql-sql`, `mysql-locking`, and
`benchmark-regression` when a measurable regression is claimed.

## Check

- Capture representative SQL, parameters, data distribution, MySQL version, SQL mode, schema, indexes, and relevant configuration.
- Compare `EXPLAIN`/`EXPLAIN ANALYZE` plans, row estimates, access paths, joins, temporary tables, filesorts, rows examined, and actual latency.
- Check statistics freshness, optimizer changes, collation/type conversions, locking/queue time, buffer-pool effects, and replication impact.
- Separate query-plan, workload, data-volume, cache, hardware, and application-pool causes before changing indexes or settings.
- Use repeated workloads and record exact commands; do not treat one wall-clock sample as a regression proof.

