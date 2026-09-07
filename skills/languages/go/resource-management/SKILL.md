---
name: go-resource-management
description: "Use when Go code involves files, response bodies, rows, statements, timers, goroutines, or cleanup."
---

# Go Resource management

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Go-specific decisions for this concern.

## Rules

- Defer cleanup immediately after successful acquisition when ownership is local; close response bodies, files, rows, statements, and timers.
- Define who owns goroutines, channels, transactions, and client transports and how cancellation releases them.
- Test failure and cancellation paths, not only the happy path.

