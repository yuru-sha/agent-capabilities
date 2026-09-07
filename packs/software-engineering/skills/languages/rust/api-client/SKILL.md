---
name: rust-api-client
description: "Use when Rust code involves HTTP clients, runtimes, response validation, timeouts, or retries."
---

# Rust API clients

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Rust-specific decisions for this concern.

## Rules

- Reuse the existing reqwest/hyper or transport stack and define runtime, timeout, cancellation, status, body limits, and cleanup.
- Validate status and payloads before constructing domain values and keep transport models separate where useful.
- Retry only safe operations with bounded backoff and preserve idempotency.

