---
name: typescript-error-handling
description: "Use when TypeScript or Node/browser code involves unknown caught values, rejected promises, causes, or error contracts."
---

# TypeScript Error handling

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only TypeScript-specific decisions for this concern.

## Rules

- Treat caught values as unknown and classify them before reading fields; preserve the original cause when wrapping.
- Make promise rejection observable and keep user-safe errors separate from diagnostic details.
- Use discriminated results when callers need a stable failure contract instead of throwing arbitrary values.

