---
name: go-http-server
description: "Use when implementing or reviewing a Go net/http server, handler, middleware, request lifecycle, or graceful shutdown."
---

# Go HTTP Server

Use with `go-security`, `go-observability`, `go-resource-management`, and
`go-goroutine-leak-deadlock-check` when the server lifecycle is in scope.

## Rules

- Carry the request context to downstream work and define cancellation behavior after the client disconnects.
- Set appropriate read, write, idle, header, body-size, and upstream timeouts; do not rely on a single global timeout.
- Make middleware order, authentication, authorization, error mapping, panic handling, and sensitive-data redaction explicit.
- Implement graceful shutdown with bounded draining and verify active requests, background workers, and listeners all terminate.
- Test handlers through `httptest` with malformed input, cancellation, timeout, status, headers, and response-body assertions.

