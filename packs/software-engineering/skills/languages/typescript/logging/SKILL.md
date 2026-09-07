---
name: typescript-logging
description: "Use when TypeScript or Node/browser code involves structured logging, error reporting, redaction, or console usage."
---

# TypeScript Logging

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only TypeScript-specific decisions for this concern.

## Rules

- Use the existing structured logger rather than ad hoc console output for library or service behavior.
- Include operation, outcome, and correlation fields while redacting tokens, cookies, personal data, and raw payloads.
- Log once at the boundary that can act on the error and preserve useful cause information.

