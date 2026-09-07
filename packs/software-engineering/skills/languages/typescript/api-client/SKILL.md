---
name: typescript-api-client
description: "Use when TypeScript or Node/browser code involves fetch/API client behavior, response validation, aborts, or retries."
---

# TypeScript API clients

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only TypeScript-specific decisions for this concern.

## Rules

- Reuse the existing fetch or HTTP wrapper and define AbortSignal, timeout, status, content type, response-size, and retry behavior.
- Validate untrusted response payloads at the boundary with an existing schema library or small local checks.
- Keep transport types separate from domain types when conversion protects the contract.

