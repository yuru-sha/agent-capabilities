---
name: aws-route53
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon Route 53 public or private hosted zones, records, aliases, routing policies, health checks, Resolver, DNS failover, or domain delegation."
---

# aws-route53

Use this skill for route53-specific AWS behavior. Compose it with adjacent service Skills when broader architecture is in scope.

## Reference routing

- zones-records-and-routing -> references/zones-records-and-routing.md
- health-private-dns-and-operations -> references/health-private-dns-and-operations.md

## Rules

- Treat hosted-zone ownership and delegation as explicit boundaries.
- Prefer alias records where appropriate.
- Choose routing policy from real traffic and failover requirements.
- Do not equate DNS failover with data recovery.
- Treat private DNS and hybrid Resolver design together.
- Treat references/ as detailed guidance, not independently selectable skills.
