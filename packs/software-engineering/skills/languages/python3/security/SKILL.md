---
name: python3-security
description: "Use when Python 3 code involves unsafe deserialization, subprocesses, paths, SSRF, secrets, or authorization."
---

# Python 3 Security

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Python 3-specific decisions for this concern.

## Rules

- Review unsafe deserialization, pickle/YAML loaders, subprocess arguments, path traversal, SSRF, injection, secrets, and authorization boundaries.
- Validate untrusted values before filesystem, template, SQL, shell, or network use.
- Keep credentials out of source, fixtures, logs, tracebacks shown to users, and generated documentation.

