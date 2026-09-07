---
name: go-networking
description: "Use when Go code involves timeouts, TLS, proxies, body limits, retries, or network errors."
---

# Go Networking

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Go-specific decisions for this concern.

## Rules

- Set context, timeout, TLS/proxy policy, response-size limits, and connection cleanup at every network boundary.
- Make retry safety and idempotency explicit; do not retry authentication, validation, or non-idempotent failures blindly.
- Reuse the repository's transport and record network errors with operation context.

