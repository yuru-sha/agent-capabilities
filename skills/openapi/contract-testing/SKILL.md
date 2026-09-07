---
name: openapi-contract-testing
description: "Use when testing OpenAPI provider and consumer contracts for request, response, auth, and status compatibility."
---

# OpenAPI Contract testing

Use this specialist with the repository's selected OpenAPI version, source of truth, and existing tools. Pair it with the matching language/database specialist when implementation behavior is in scope.

## Rules

- Validate method/path/parameters, auth, content type, request constraints, response schema, headers, status codes, and representative errors.
- Test both directions when the repository owns both client and server and exercise generated artifacts where they are part of the contract.
- Keep provider and consumer fixtures independent enough to catch a spec and implementation agreeing on the same mistake.

