---
name: python3-api-client
description: "Use when Python 3 code involves HTTP clients, sessions, response validation, timeouts, or retries."
---

# Python 3 API clients

Use the project's TDD workflow for implementation and its review workflow for review. This specialist owns only Python 3-specific decisions for this concern.

## Rules

- Reuse the existing HTTP client and session conventions; set timeout, cancellation, status, response-size, cleanup, and retry behavior.
- Validate external payloads before domain use and keep transport conversion separate when it protects a boundary.
- Do not retry non-idempotent calls or authentication/validation failures by default.

