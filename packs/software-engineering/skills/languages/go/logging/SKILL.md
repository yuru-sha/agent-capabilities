---
name: go-logging
description: "Use when Go code involves structured logging, error logs, redaction, or log levels."
---

# Go Logging

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Go-specific decisions for this concern.

## Rules

- Use the existing structured logger, preferably log/slog where the repository uses it, with operation and outcome fields.
- Log an error once at the boundary that can act on it; avoid duplicate stack traces and sensitive payloads.
- Keep log levels and messages stable enough for operators and tests to consume.

