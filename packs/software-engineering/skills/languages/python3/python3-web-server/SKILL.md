---
name: python3-web-server
description: "Use when Python 3 implements or reviews a WSGI or ASGI server, request lifecycle, middleware, startup/shutdown, or async web handler."
---

# Python 3 Web Server

Use with the existing framework and compose with `python3-subprocess`,
`python3-resource-management`, and `python3-type-checking` as needed.

## Rules

- Identify the WSGI/ASGI lifecycle, worker model, event loop, startup/shutdown hooks, and cancellation semantics before changing handlers.
- Do not block the event loop with synchronous I/O or CPU work; use the repository's established worker boundary for unavoidable blocking work.
- Bound request bodies, uploads, concurrency, timeouts, and downstream calls; make backpressure and disconnect behavior explicit.
- Keep middleware order, authentication, authorization, exception mapping, logging, and secret redaction testable.
- Test malformed requests, cancellation, timeout, streaming, shutdown, and repeated startup/shutdown paths.

