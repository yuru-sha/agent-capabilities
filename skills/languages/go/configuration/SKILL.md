---
name: go-configuration
description: "Use when Go code involves flags, environment, configuration files, defaults, or secret handling."
---

# Go Configuration

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Go-specific decisions for this concern.

## Rules

- Make precedence among flags, environment, files, and defaults explicit and validate once at startup or command entry.
- Represent missing, empty, and invalid configuration distinctly; fail safely instead of silently selecting an unsafe default.
- Keep secrets out of defaults and diagnostics.

