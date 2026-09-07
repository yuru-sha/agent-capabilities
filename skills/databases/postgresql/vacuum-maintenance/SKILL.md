---
name: postgresql-vacuum-maintenance
description: "Use when PostgreSQL MVCC bloat, autovacuum, ANALYZE, freezing, long transactions, or table/index maintenance are involved."
---

# PostgreSQL Vacuum and Maintenance

Use with `postgresql-performance`, `postgresql-query-plan-regression`, and
`postgresql-transactions`.

## Check

- Relate dead tuples, table/index bloat, visibility maps, transaction age, and statistics quality to the observed workload.
- Check autovacuum/analyze thresholds, per-table overrides, freeze age, long-running transactions, replication slots, and maintenance windows.
- Distinguish ordinary `VACUUM`, `VACUUM FULL`, `ANALYZE`, reindexing, and online alternatives by lock and disk impact.
- Verify that maintenance settings match write volume and table size rather than accepting global defaults blindly.
- Capture before/after statistics and query-plan evidence; do not claim improvement from a maintenance command alone.

