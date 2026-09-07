---
name: python3-cli
description: "Use when Python 3 code involves CLI parsing, streams, exit codes, signals, or command errors."
---

# Python 3 CLI

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Python 3-specific decisions for this concern.

## Rules

- Reuse argparse or the repository's existing CLI layer and define stdin, stdout, stderr, exit codes, signals, and cancellation.
- Validate flags and environment values before side effects and keep user-facing errors free of credentials and internal paths.
- Do not add a CLI framework for a small command when the standard library is enough.

