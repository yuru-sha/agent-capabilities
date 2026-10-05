---
name: athena
description: "Use when designing, implementing, reviewing, operating, or optimizing Amazon Athena SQL queries, workgroups, result locations, partitioning, file formats, CTAS/UNLOAD, Glue Catalog integration, access control, or query cost."
---

# athena

Use this skill for athena-specific AWS behavior. Compose it with adjacent service Skills when broader architecture or data-platform behavior is in scope.

## Reference routing

- `tables-partitions-and-formats` → `references/tables-partitions-and-formats.md`
- `workgroups-cost-and-operations` → `references/workgroups-cost-and-operations.md`

## Rules

- Optimize S3 layout and partitions before query micro-tuning.
- Avoid SELECT * on large analytical tables unless all columns are required.
- Use workgroups for access, configuration, metrics, and cost controls.
- Keep result location and encryption explicit.
- Treat Glue Catalog schema/partition changes as query-contract changes.
- Treat `references/` as detailed guidance, not independently selectable skills.
