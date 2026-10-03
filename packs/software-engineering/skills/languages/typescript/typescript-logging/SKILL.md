---
name: typescript-logging
description: "Use when TypeScript or Node/browser code involves structured logging, error reporting, redaction, or console usage."
---

# TypeScript Logging

Use this specialist with oh-my-pstack's TDD workflow for implementation and oh-my-pstack's review workflow for review. It owns only TypeScript-specific decisions for this concern.

## Rules

- Use the existing structured logger rather than ad hoc console output for library or service behavior.
- Include operation, outcome, and correlation fields while redacting tokens, cookies, personal data, and raw payloads.
- Log once at the boundary that can act on the error and preserve useful cause information.

