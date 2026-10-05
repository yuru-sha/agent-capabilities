---
name: msk
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon MSK provisioned or Serverless Apache Kafka clusters, topics, partitions, replication, producers/consumers, IAM/SASL auth, networking, scaling, or broker reliability."
---

# msk

Use this skill for msk-specific AWS behavior. Compose it with adjacent service Skills when broader architecture or data-platform behavior is in scope.

## Reference routing

- `cluster-topics-partitions-and-delivery` → `references/cluster-topics-partitions-and-delivery.md`
- `consumers-security-scaling-and-operations` → `references/consumers-security-scaling-and-operations.md`

## Rules

- Choose provisioned vs Serverless deliberately.
- Design partitions from ordering, throughput, and consumer concurrency.
- Treat consumer lag and rebalances as first-class operational signals.
- Keep authentication, TLS, and VPC connectivity explicit.
- Do not claim exactly-once business processing solely from Kafka producer/transaction features.
- Treat `references/` as detailed guidance, not independently selectable skills.
