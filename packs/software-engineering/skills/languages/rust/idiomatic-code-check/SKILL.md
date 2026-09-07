---
name: rust-idiomatic-code-check
description: "Use when checking whether Rust code follows repository idioms for ownership, Result, iterators, traits, async, and public APIs."
---

# Rust idiomatic-code check

Use this specialist with the global `$tdd` skill for implementation work and `$code-review` for review work. It owns only this language-specific concern.

## Rules

- Run the pinned rustfmt, clippy, build, and test commands when available; use the repository's lint policy as the baseline.
- Check ownership and borrowing before cloning, Result/Option flow before panicking, and iterator or match forms for readability rather than cleverness.
- Flag needless clones, broad traits, hidden blocking in async code, unnecessary unsafe, ignored must-use values, and feature/API drift.
- Prefer local types and explicit boundaries over macros or generic abstractions with one consumer.

