---
name: go-security
description: "Use when Go code involves untrusted input, authorization, secrets, paths, commands, or network targets."
---

# Go Security

Use this specialist with the project's TDD workflow for implementation and the project's review workflow for review. It owns only Go-specific decisions for this concern.

## Rules

- Validate untrusted input before path, command, SQL, template, or network use and keep secrets out of source, fixtures, and logs.
- Review authorization at each resource boundary and constrain file and network targets.
- Use the repository's vulnerability checks as evidence, not as a substitute for code-path review.

