---
name: aws-ecs
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon ECS task definitions, services, deployments, capacity providers, service discovery, autoscaling, IAM roles, or container workload reliability."
---

# aws-ecs

Use this skill for ECS orchestration semantics, including ECS on Fargate. Compose it with `aws-ecr` for image registry behavior and `aws-alb` for load balancing.

## Reference routing

- `tasks-services-and-deployments` → `references/tasks-services-and-deployments.md`
- `capacity-networking-and-identity` → `references/capacity-networking-and-identity.md`
- `scaling-observability-and-recovery` → `references/scaling-observability-and-recovery.md`
- `fargate-runtime` → `references/fargate-runtime.md`

## Rules

- Separate task role from execution role.
- Treat task definitions as immutable application runtime contracts.
- Align container health, ECS deployment health, load-balancer health, and application readiness.
- Use capacity providers deliberately and choose EC2 vs Fargate from workload control, startup, density, networking, and cost requirements.
- Make deployment circuit breaker/rollback and minimum healthy capacity explicit.
- Bound autoscaling and downstream dependency pressure.
- Treat `references/` as detailed guidance, not independently selectable skills.
