---
name: rust-logging
description: "Use when Rust code involves tracing, spans, error fields, redaction, or log levels."
---

# Rust Logging

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Rust-specific decisions for this concern.

## Rules

- Use the existing tracing/log stack with operation, outcome, and correlation fields at meaningful boundaries.
- Record errors once where they can be acted on and redact tokens, credentials, and sensitive payloads.
- Preserve source error context without dumping internal state into user-facing output.

