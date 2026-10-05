---
name: aws-emr
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon EMR clusters, EMR Serverless, Spark/Hadoop workloads, bootstrap actions, instance fleets, scaling, Spot usage, storage, or distributed-job reliability."
---

# aws-emr

Use this skill for emr-specific AWS behavior. Compose it with adjacent service Skills when broader architecture or data-platform behavior is in scope.

## Reference routing

- `deployment-models-and-cluster-design` → `references/deployment-models-and-cluster-design.md`
- `spark-scaling-storage-and-operations` → `references/spark-scaling-storage-and-operations.md`

## Rules

- Choose the EMR deployment model before implementation.
- Pin release/runtime and dependency expectations.
- Treat bootstrap and cluster configuration as versioned artifacts.
- Design Spark parallelism, shuffle, and memory from measured workloads.
- Treat Spot interruption and cluster termination as normal operational paths where used.
- Treat `references/` as detailed guidance, not independently selectable skills.
