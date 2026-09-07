---
name: openapi-auth-security-review
description: "Use when reviewing OpenAPI authentication, authorization, scopes, security schemes, and abuse boundaries."
---

# OpenAPI Auth and security review

Use this specialist with the repository's selected OpenAPI version, source of truth, and existing tools. Pair it with the matching language/database specialist when implementation behavior is in scope.

## Rules

- Define securitySchemes, scopes/roles, operation-level requirements, and unauthenticated exceptions explicitly.
- Review 401 versus 403, object-level authorization, tenant/resource scoping, sensitive fields, input limits, and error leakage.
- A declared security scheme documents intent, not enforcement; compare it with implementation and contract-test evidence.

