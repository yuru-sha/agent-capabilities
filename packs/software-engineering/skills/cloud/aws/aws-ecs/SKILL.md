---
name: aws-ecs
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon ECS task definitions, services, deployments, capacity providers, service discovery, autoscaling, IAM roles, or container workload reliability."
---

# aws-ecs

Use this skill for ECS orchestration semantics. Compose it with `fargate` for Fargate runtime concerns, `ecr` for image registry behavior, and `alb` for load balancing.

## Reference routing

- `tasks-services-and-deployments` → `references/tasks-services-and-deployments.md`
- `capacity-networking-and-identity` → `references/capacity-networking-and-identity.md`
- `scaling-observability-and-recovery` → `references/scaling-observability-and-recovery.md`

## Rules

- Separate task role from execution role.
- Treat task definitions as immutable application runtime contracts.
- Align container health, ECS deployment health, load-balancer health, and application readiness.
- Use capacity providers deliberately; keep Fargate-specific rules in the Fargate Skill.
- Make deployment circuit breaker/rollback and minimum healthy capacity explicit.
- Bound autoscaling and downstream dependency pressure.
- Treat `references/` as detailed guidance, not independently selectable skills.
