---
name: rust-logging
description: "Use when Rust code involves tracing, spans, error fields, redaction, or log levels."
---

# Rust Logging

Use this specialist with oh-my-pstack's TDD workflow for implementation and oh-my-pstack's review workflow for review. It owns only Rust-specific decisions for this concern.

## Rules

- Use the existing tracing/log stack with operation, outcome, and correlation fields at meaningful boundaries.
- Record errors once where they can be acted on and redact tokens, credentials, and sensitive payloads.
- Preserve source error context without dumping internal state into user-facing output.

