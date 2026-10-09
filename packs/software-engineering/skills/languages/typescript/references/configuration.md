---
name: typescript-configuration
description: "Use when TypeScript or Node/browser code involves environment variables, config files, flags, defaults, or browser/server config."
---

# TypeScript Configuration

Use this specialist with pstack's TDD workflow for implementation and pstack's review workflow for review. It owns only TypeScript-specific decisions for this concern.

## Rules

- Parse and validate environment, config files, and flags at the boundary with explicit precedence and server/client separation.
- Distinguish absent, empty, invalid, and default values; fail safely instead of silently using an unsafe value.
- Keep secrets out of client bundles, defaults, diagnostics, and test fixtures.

