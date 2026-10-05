---
name: aws-elasticache
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon ElastiCache for Valkey, Redis OSS, or Memcached, including topology, replication, sharding, failover, eviction, TTL, security, scaling, and client behavior."
---

# aws-elasticache

Use this skill for elasticache-specific AWS behavior. Compose it with adjacent service Skills when broader architecture or data-platform behavior is in scope.

## Reference routing

- `engine-topology-and-data-model` → `references/engine-topology-and-data-model.md`
- `clients-scaling-failover-and-operations` → `references/clients-scaling-failover-and-operations.md`

## Rules

- Choose engine from semantics, not familiarity.
- Keep memory headroom and eviction behavior explicit.
- Treat cache misses and failover as normal application paths.
- Use topology-aware clients for clustered deployments.
- Do not treat a cache as the sole durable source of truth unless the workload explicitly accepts that risk.
- Treat `references/` as detailed guidance, not independently selectable skills.
