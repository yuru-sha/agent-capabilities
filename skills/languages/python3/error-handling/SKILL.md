---
name: python3-error-handling
description: "Use when Python 3 code involves exceptions, exception translation, causes, or failure contracts."
---

# Python 3 Error handling

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Python 3-specific decisions for this concern.

## Rules

- Catch the narrowest expected exception and preserve the cause with raise ... from when translating across a boundary.
- Do not convert operational failures into successful defaults; keep user-safe messages separate from diagnostics.
- Define whether callers receive an exception, a result value, or a partial outcome and test that contract.

