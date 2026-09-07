---
name: openapi-mock-generation
description: "Use when generating OpenAPI mock servers, stubs, or test doubles."
---

# OpenAPI Mock generation

Use this specialist with the repository's selected OpenAPI version, source of truth, and existing tools. Pair it with the matching language/database specialist when implementation behavior is in scope.

## Rules

- Generate mocks from the same contract consumed by clients and keep request validation and response schemas enabled.
- Include failure, latency, auth, pagination, and invalid-input cases when they represent real consumer behavior.
- Label mocked behavior and avoid using mocks as evidence that production authorization or side effects are correct.

