---
name: go-api-client
description: "Use when Go code involves HTTP/API client behavior, response validation, timeouts, or retries."
---

# Go API clients

Use this specialist with pstack's TDD workflow for implementation and pstack's review workflow for review. It owns only Go-specific decisions for this concern.

## Rules

- Reuse the repository's net/http client and transport conventions; set context, timeout, status, body-limit, and close behavior at the boundary.
- Validate response status and payload before constructing domain values.
- Retry only idempotent operations with bounded backoff and cancellation.

