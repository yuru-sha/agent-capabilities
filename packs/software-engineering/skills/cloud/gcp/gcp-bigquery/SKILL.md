---
name: gcp-bigquery
description: "Use when designing, implementing, reviewing, operating, or optimizing Google BigQuery datasets, tables, partitioning, clustering, SQL, slots/reservations, ingestion, exports, schema evolution, cost, or row/column-level security."
---

# gcp-bigquery

Use this skill for BigQuery-specific analytical data modeling, SQL execution, cost/performance, ingestion, and governance.

## Reference routing

- `table-design-partitioning-and-clustering` → `references/table-design-partitioning-and-clustering.md`
- `query-performance-and-cost` → `references/query-performance-and-cost.md`
- `ingestion-streaming-and-export` → `references/ingestion-streaming-and-export.md`
- `schema-governance-and-security` → `references/schema-governance-and-security.md`

## Rules

- Start from analytical access patterns, freshness, retention, and scan volume.
- Partition and cluster only when they reduce real query work; verify pruning with actual query plans/statistics.
- Avoid `SELECT *` on wide production tables unless every column is required.
- Treat bytes scanned, slot usage, reservations, materialization, and repeated queries as explicit cost/performance concerns.
- Use append/streaming/load patterns with clear deduplication and late-arriving-data behavior.
- Model nested/repeated fields deliberately; denormalization is a workload choice, not a blanket rule.
- Make dataset/table IAM, row-level security, policy tags, and authorized views explicit for sensitive data.
- Treat `references/` as detailed guidance, not independently selectable skills.
