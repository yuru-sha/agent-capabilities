---
name: api-gateway
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon API Gateway REST, HTTP, or WebSocket APIs, routes, stages, integrations, authorizers, throttling, deployments, or observability."
---

# api-gateway

Use this skill for api-gateway-specific AWS behavior. Compose it with adjacent service Skills when broader architecture is in scope.

## Reference routing

- api-types-routing-and-integrations -> references/api-types-routing-and-integrations.md
- auth-throttling-and-operations -> references/auth-throttling-and-operations.md

## Rules

- Choose REST, HTTP, or WebSocket API before implementation.
- Keep route matching, integration behavior, timeout, and payload contracts explicit.
- Separate authentication from backend business authorization.
- Treat throttling as protective backpressure, not a hard guaranteed ceiling.
- Version stage, deployment, custom-domain, and mapping configuration deliberately.
- Treat references/ as detailed guidance, not independently selectable skills.
