---
name: python3-resource-management
description: "Use when Python 3 code involves context managers, files, sessions, locks, queues, or cleanup."
---

# Python 3 Resource management

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Python 3-specific decisions for this concern.

## Rules

- Use with/async with for files, locks, database resources, temporary paths, and client sessions whenever ownership is local.
- Close or cancel async resources on exceptions and define who owns background tasks and queues.
- Test failure and cancellation cleanup, not only successful completion.

