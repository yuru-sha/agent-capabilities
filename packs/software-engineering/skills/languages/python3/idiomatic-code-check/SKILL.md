---
name: python3-idiomatic-code-check
description: "Use when checking whether Python 3 code follows repository idioms for exceptions, context managers, typing, modules, and APIs."
---

# Python 3 idiomatic-code check

Use this specialist with the global `$tdd` skill for implementation work and `$code-review` for review work. It owns only this language-specific concern.

## Rules

- Run the repository's formatter, linter, type checker, and tests when available; inspect the supported Python version first.
- Check clear names, small cohesive functions, context managers, pathlib/resource APIs, narrow exception handling, and ordinary data structures.
- Flag broad catches, mutable defaults, hidden global state, needless classes/decorators, implicit coercion, and imports that obscure ownership.
- Prefer the project's existing typing and async style; do not turn a local fix into a style migration.

