---
name: aws-glue
description: "Use when designing, implementing, reviewing, operating, or troubleshooting AWS Glue Data Catalog, crawlers, ETL jobs, job bookmarks, connections, schema discovery, workflows, or data integration pipelines."
---

# aws-glue

Use this skill for glue-specific AWS behavior. Compose it with adjacent service Skills when broader architecture or data-platform behavior is in scope.

## Reference routing

- `catalog-crawlers-and-schema` → `references/catalog-crawlers-and-schema.md`
- `jobs-bookmarks-and-operations` → `references/jobs-bookmarks-and-operations.md`

## Rules

- Keep Data Catalog ownership and schema evolution explicit.
- Use crawlers only where automatic discovery is appropriate.
- Treat ETL outputs as idempotent/recoverable.
- Use job bookmarks deliberately rather than assuming exactly-once processing.
- Validate row counts, partitions, schema, and output quality after jobs.
- Treat `references/` as detailed guidance, not independently selectable skills.
