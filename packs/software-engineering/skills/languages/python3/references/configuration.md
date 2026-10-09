---
name: python3-configuration
description: "Use when Python 3 code involves CLI, environment, files, defaults, or secret handling."
---

# Python 3 Configuration

Use pstack's TDD workflow for implementation and its review workflow for review. This specialist owns only Python 3-specific decisions for this concern.

## Rules

- Make precedence among CLI, environment, files, and defaults explicit and validate typed values at the boundary.
- Distinguish missing, empty, invalid, and default configuration; fail safely instead of guessing.
- Keep secrets out of defaults, repr output, diagnostics, and fixtures.

