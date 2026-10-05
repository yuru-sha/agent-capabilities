---
name: fargate
description: "Use when designing, reviewing, operating, or troubleshooting AWS Fargate workloads across Amazon ECS or EKS, including sizing, networking, ephemeral storage, platform versions, scaling, Fargate Spot, and EC2-vs-Fargate tradeoffs."
---

# AWS Fargate

Use this skill for Fargate-specific serverless compute characteristics shared across ECS and EKS. Use `ecs` or `eks` for orchestrator-specific semantics.

## Reference routing

- `selection-sizing-and-platform` → `references/selection-sizing-and-platform.md`
- `networking-storage-and-runtime` → `references/networking-storage-and-runtime.md`
- `scaling-cost-and-operations` → `references/scaling-cost-and-operations.md`

## Rules

- Choose Fargate from operational/control requirements, not only from "no servers".
- Validate supported CPU/memory/platform combinations and architecture for each workload.
- Treat each task/pod network interface, subnet IP capacity, security group, DNS, and egress path as production capacity.
- Model ephemeral storage and external persistent storage explicitly.
- Use Spot only for interruption-tolerant workloads with graceful termination behavior.
- Keep ECS-specific deployment/task semantics in `ecs` and EKS-specific pod/cluster semantics in `eks`.
- Treat `references/` as detailed guidance, not independently selectable skills.
