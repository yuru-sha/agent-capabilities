---
name: python3-data-race-check
description: "Use when checking Python 3 for thread races, asyncio ordering bugs, shared-memory races, or task interleavings."
---

# Python 3 data-race check

Use this specialist with the global `$tdd` skill for implementation work and `$code-review` for review work. It owns only this language-specific concern.

## Rules

- Do not treat the GIL as a race-free guarantee; review threads, native extensions, shared mutable objects, multiprocessing shared memory, and asyncio tasks.
- Check task cancellation, queue ownership, lock scope, callback ordering, and read-modify-write sequences.
- Use deterministic barriers, events, or the repository's concurrency test support; do not make sleeps the proof of a race fix.
- Report which scheduler/runtime paths were exercised and distinguish memory races from logical ordering races.

