---
name: go-api-client
description: "Use when Go code involves HTTP/API client behavior, response validation, timeouts, or retries."
---

# Go API clients

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Go-specific decisions for this concern.

## Rules

- Reuse the repository's net/http client and transport conventions; set context, timeout, status, body-limit, and close behavior at the boundary.
- Validate response status and payload before constructing domain values.
- Retry only idempotent operations with bounded backoff and cancellation.

