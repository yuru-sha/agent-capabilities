---
name: aws-cloudfront
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon CloudFront distributions, origins, cache policies, origin request policies, behaviors, OAC, signed access, invalidations, edge functions, or CDN security."
---

# aws-cloudfront

Use this skill for cloudfront-specific AWS behavior. Compose it with adjacent service Skills when broader architecture is in scope.

## Reference routing

- origins-behaviors-and-policies -> references/origins-behaviors-and-policies.md
- security-cache-and-operations -> references/security-cache-and-operations.md

## Rules

- Separate cache policy from origin request policy.
- Forward only required headers, cookies, and query strings.
- Prefer OAC for private S3 origins where supported.
- Treat TTL, invalidation, and asset versioning as one cache strategy.
- Keep WAF and TLS responsibilities explicit.
- Treat references/ as detailed guidance, not independently selectable skills.
