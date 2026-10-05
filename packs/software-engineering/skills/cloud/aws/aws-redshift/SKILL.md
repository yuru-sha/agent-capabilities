---
name: aws-redshift
description: "Use when designing, implementing, reviewing, operating, or optimizing Amazon Redshift provisioned or Serverless warehouses, table design, distribution/sort strategy, workload management, Spectrum, COPY/UNLOAD, scaling, security, or query performance."
---

# aws-redshift

Use this skill for redshift-specific AWS behavior. Compose it with adjacent service Skills when broader architecture or data-platform behavior is in scope.

## Reference routing

- `warehouse-table-and-query-design` → `references/warehouse-table-and-query-design.md`
- `ingestion-wlm-scaling-and-operations` → `references/ingestion-wlm-scaling-and-operations.md`

## Rules

- Choose provisioned vs Serverless deliberately.
- Design distribution/sort/compression from real query patterns.
- Prefer bulk ingestion over row-by-row loading.
- Separate workload classes and protect the warehouse from runaway queries.
- Test snapshot/restore or recovery procedures.
- Treat `references/` as detailed guidance, not independently selectable skills.
