---
name: go-error-handling
description: "Use when Go code involves error wrapping, classification, or failure propagation."
---

# Go Error handling

Use this specialist with oh-my-pstack's TDD workflow for implementation and oh-my-pstack's review workflow for review. It owns only Go-specific decisions for this concern.

## Rules

- Wrap errors with %w when callers need the cause and classify them with errors.Is or errors.As at decision boundaries.
- Preserve operation and resource context; return failures instead of logging and continuing with an invalid value.
- Use sentinel or typed errors only when a caller needs stable classification.

