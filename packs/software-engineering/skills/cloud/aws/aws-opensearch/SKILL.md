---
name: opensearch
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon OpenSearch Service domains or OpenSearch Serverless collections, indexes, mappings, shards, replicas, ingestion, query/search behavior, security, scaling, or observability."
---

# opensearch

Use this skill for opensearch-specific AWS behavior. Compose it with adjacent service Skills when broader architecture or data-platform behavior is in scope.

## Reference routing

- `domains-serverless-index-and-shard-design` → `references/domains-serverless-index-and-shard-design.md`
- `ingestion-security-scaling-and-operations` → `references/ingestion-security-scaling-and-operations.md`

## Rules

- Choose domain vs Serverless deliberately.
- Define mappings before large-scale ingestion when possible.
- Avoid oversharding and uncontrolled dynamic mappings.
- Use bulk ingestion and backpressure for high-volume writes.
- Treat search indexes as rebuildable unless explicitly used as a system of record.
- Treat `references/` as detailed guidance, not independently selectable skills.
