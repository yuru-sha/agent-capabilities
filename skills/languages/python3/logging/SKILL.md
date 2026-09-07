---
name: python3-logging
description: "Use when Python 3 code involves logging configuration, fields, exception traces, or redaction."
---

# Python 3 Logging

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Python 3-specific decisions for this concern.

## Rules

- Use the existing logging configuration instead of print for library/service behavior and include operation and outcome context.
- Redact secrets and personal data before logging; avoid duplicate exception traces at multiple layers.
- Keep messages and fields stable enough for operators and tests to consume.

