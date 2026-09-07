---
name: openapi-codegen
description: "Use when generating OpenAPI clients, servers, or models and reviewing generated code."
---

# OpenAPI Code generation

Use this specialist with the repository's selected OpenAPI version, source of truth, and existing tools. Pair it with the matching language/database specialist when implementation behavior is in scope.

## Rules

- Pin generator version and configuration when reproducibility matters and keep generated output separate from hand-written adapters.
- Inspect generated diffs for status, nullability, error, auth, timeout, and naming behavior before accepting them.
- Generated code does not remove the need for runtime validation, authorization, cancellation, or resource cleanup.

