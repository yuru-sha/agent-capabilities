---
name: typescript-serialization
description: "Use when TypeScript or Node/browser code involves JSON, undefined/null, dates, numbers, enums, or wire compatibility."
---

# TypeScript Serialization

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only TypeScript-specific decisions for this concern.

## Rules

- Define behavior for undefined, null, empty, defaults, numbers, dates, enums, unknown fields, and large payloads.
- Validate external JSON before domain use and avoid silently coercing values that change meaning.
- Keep public serialized forms versioned and review consumer compatibility before changing them.

