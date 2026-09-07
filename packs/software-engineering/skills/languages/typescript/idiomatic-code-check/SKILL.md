---
name: typescript-idiomatic-code-check
description: "Use when checking whether TypeScript code follows repository idioms for types, async control flow, modules, errors, and runtime boundaries."
---

# TypeScript idiomatic-code check

Use this specialist with the global `$tdd` skill for implementation work and `$code-review` for review work. It owns only this language-specific concern.

## Rules

- Use the repository's formatter, lint, typecheck, and test commands and inspect the configured strictness before judging style.
- Check narrow types, unknown-before-use, explicit async error flow, discriminated unions, module boundaries, and consistent import/runtime conventions.
- Flag any, non-null assertions, swallowed promises, unnecessary type assertions, hidden mutation, and abstractions that bypass the actual contract.
- Prefer established project patterns over a new library or framework and keep browser/server boundaries visible.

