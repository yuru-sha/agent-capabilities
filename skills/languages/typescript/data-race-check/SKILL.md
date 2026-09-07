---
name: typescript-data-race-check
description: "Use when checking TypeScript or JavaScript for async races, stale responses, worker sharing, SharedArrayBuffer, or interleaving bugs."
---

# TypeScript data-race check

Use this specialist with the global `$tdd` skill for implementation work and `$code-review` for review work. It owns only this language-specific concern.

## Rules

- Distinguish single-threaded event-loop ordering bugs from true shared-memory races in workers, SharedArrayBuffer, or native extensions.
- Check stale responses, duplicate submits, cancellation, timer callbacks, shared caches, and out-of-order Promise completion.
- Use the repository's fake clock, worker test, or scheduler support when available; coordinate events instead of relying on arbitrary delays.
- A type check or linter does not prove interleaving safety; report the schedule exercised and any worker/shared-memory paths not covered.

