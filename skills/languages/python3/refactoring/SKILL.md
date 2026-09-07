---
name: python3-refactoring
description: "Use when Python 3 code involves module boundaries, imports, decorators, classes, or adapters."
---

# Python 3 Refactoring

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Python 3-specific decisions for this concern.

## Rules

- Keep modules cohesive and imports stable; prefer a small function or module refactor over speculative base classes or registries.
- Preserve public call signatures unless the contract explicitly changes and keep adapters at integration boundaries.
- Avoid decorators and metaprogramming that hide ownership or error flow without a concrete need.

