---
name: dynamodb
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon DynamoDB tables, access patterns, indexes, capacity, conditional writes, transactions, Streams, global tables, or DynamoDB-backed applications."
---

# Amazon DynamoDB

Use this skill for DynamoDB-specific data modeling, correctness, performance, and operations. Compose it with the existing AWS/infrastructure profile when broader IAM, networking, Terraform, Lambda, CloudWatch, or deployment concerns are in scope.

## Reference routing

- `access-patterns-and-key-design` → `references/access-patterns-and-key-design.md`
- `indexes-query-and-pagination` → `references/indexes-query-and-pagination.md`
- `writes-transactions-and-concurrency` → `references/writes-transactions-and-concurrency.md`
- `capacity-performance-and-hot-partitions` → `references/capacity-performance-and-hot-partitions.md`
- `streams-ttl-global-tables-and-operations` → `references/streams-ttl-global-tables-and-operations.md`

## Rules

- Start from concrete access patterns before defining keys or indexes.
- Prefer `Query` over `Scan`; treat broad scans as explicit operational or analytical exceptions.
- Design partition keys for even activity distribution and verify that secondary indexes do not introduce new hot partitions.
- Make consistency, conditional-write behavior, retry policy, and idempotency explicit for every mutation path.
- Treat GSIs as independently capacity-constrained projections with eventual consistency; model their write amplification and backfill impact.
- Use transactions only when a real multi-item invariant requires them; do not substitute them for good key design.
- Treat DynamoDB Streams, TTL, global tables, backup/PITR, and table-class choices as operational contracts rather than invisible defaults.
- Load the smallest set of references that covers the current concern.
- Treat `references/` as detailed guidance, not independently selectable skills.
