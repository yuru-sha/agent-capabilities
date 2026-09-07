---
name: openapi-design
description: "Use when designing OpenAPI resources, operations, parameters, statuses, errors, pagination, or idempotency."
---

# OpenAPI Design

Use this specialist with the repository's selected OpenAPI version, source of truth, and existing tools. Pair it with the matching language/database specialist when implementation behavior is in scope.

## Rules

- Make resources, methods, parameters, status codes, content types, errors, pagination, idempotency, and retry behavior explicit.
- Keep request and response contracts honest about required, nullable, absent, read-only, write-only, and default values.
- Review neighboring operations for consistent semantics instead of designing the changed path in isolation.

