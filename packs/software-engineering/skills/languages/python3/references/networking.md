---
name: python3-networking
description: "Use when Python 3 code involves timeouts, TLS, redirects, body limits, retries, or SSRF."
---

# Python 3 Networking

Use the project's TDD workflow for implementation and its review workflow for review. This specialist owns only Python 3-specific decisions for this concern.

## Rules

- Set timeout, cancellation, connection reuse, TLS/redirect policy, response limits, cleanup, and retry safety at the network boundary.
- Review SSRF and credential forwarding when URLs or headers are input-controlled.
- Preserve operation context in network errors and avoid unbounded streaming or buffering.

