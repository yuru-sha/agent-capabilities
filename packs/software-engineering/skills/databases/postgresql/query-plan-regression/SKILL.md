---
name: postgresql-query-plan-regression
description: "Use when PostgreSQL query plans, indexes, statistics, schema changes, or performance regressions need evidence-based comparison."
---

# PostgreSQL Query Plan Regression

Use with `postgresql-performance`, `postgresql-indexes`, and
`postgresql-vacuum-maintenance`.

## Check

- Capture representative `EXPLAIN`/`EXPLAIN ANALYZE` plans, parameters, data distribution, statistics state, and PostgreSQL version.
- Compare row estimates, join order, scan type, sort/hash spills, buffers, planning time, and actual latency rather than a single wall-clock sample.
- Check whether schema, index, partition, configuration, or data-volume changes explain the plan shift.
- Use stable thresholds and repeated workloads; do not gate on noisy microbenchmarks without a baseline.
- Keep plan evidence safe for the environment and redact sensitive literals before sharing it.

