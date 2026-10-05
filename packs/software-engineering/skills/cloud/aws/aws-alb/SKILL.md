---
name: aws-alb
description: "Use when designing, implementing, reviewing, operating, or troubleshooting AWS Application Load Balancers, listeners, rules, target groups, health checks, TLS, stickiness, slow start, routing, or draining."
---

# aws-alb

Use this skill for ALB L7 routing and target health behavior.

## Reference routing

- `listeners-rules-and-tls` → `references/listeners-rules-and-tls.md`
- `target-groups-health-and-draining` → `references/target-groups-health-and-draining.md`
- `routing-observability-and-operations` → `references/routing-observability-and-operations.md`

## Rules

- Make listener, rule priority, host/path routing, redirects, and TLS policy explicit.
- Treat target-group health as an application readiness contract.
- Align deregistration delay, deployment draining, keep-alive, and application shutdown.
- Use stickiness only when application/session requirements justify it.
- Apply slow start when new targets need warm-up before full request share.
- Bound public exposure with VPC/security-group/WAF controls as applicable.
- Treat `references/` as detailed guidance, not independently selectable skills.
