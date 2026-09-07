---
name: python3-testing
description: "Use when Python 3 code involves tests, parametrization, fixtures, async tests, or test isolation."
---

# Python 3 Testing

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Python 3-specific decisions for this concern.

## Rules

- Use the repository's existing test runner and fixtures at public seams; parametrization is useful for independent cases, not a blanket requirement.
- Cover exception paths, async cancellation, cleanup, and boundary payloads when they are part of the behavior.
- Keep expected values independent and avoid tests that merely mirror the implementation.

