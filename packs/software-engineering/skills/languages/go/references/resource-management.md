---
name: go-resource-management
description: "Use when Go code involves files, response bodies, rows, statements, timers, goroutines, or cleanup."
---

# Go Resource management

Use this specialist with pstack's TDD workflow for implementation and pstack's review workflow for review. It owns only Go-specific decisions for this concern.

## Rules

- Defer cleanup immediately after successful acquisition when ownership is local; close response bodies, files, rows, statements, and timers.
- Define who owns goroutines, channels, transactions, and client transports and how cancellation releases them.
- Test failure and cancellation paths, not only the happy path.

