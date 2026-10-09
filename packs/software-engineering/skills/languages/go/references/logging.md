---
name: go-logging
description: "Use when Go code involves structured logging, error logs, redaction, or log levels."
---

# Go Logging

Use this specialist with pstack's TDD workflow for implementation and pstack's review workflow for review. It owns only Go-specific decisions for this concern.

## Rules

- Use the existing structured logger, preferably log/slog where the repository uses it, with operation and outcome fields.
- Log an error once at the boundary that can act on it; avoid duplicate stack traces and sensitive payloads.
- Keep log levels and messages stable enough for operators and tests to consume.

