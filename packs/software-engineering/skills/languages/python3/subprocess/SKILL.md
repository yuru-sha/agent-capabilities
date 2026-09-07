---
name: python3-subprocess
description: "Use when Python 3 starts external processes, invokes shell commands, streams output, or manages child-process timeouts and cleanup."
---

# Python 3 Subprocess

Use with `python3-security`, `python3-resource-management`, and the repository
contract for external tools.

## Rules

- Pass an argument list and keep `shell=False` unless shell semantics are explicitly required and safely constrained.
- Set bounded timeouts, handle return codes, close or drain pipes, and clean up child processes on errors and cancellation.
- Define encoding, output-size limits, stdin behavior, signal/process-group handling, and platform differences.
- Keep secrets out of command lines, logs, exceptions, inherited environments, and temporary files.
- Test missing executables, non-zero exit, timeout, partial output, cancellation, and cleanup deterministically.

