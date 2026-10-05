---
name: typescript-networking
description: "Use when TypeScript or Node/browser code involves fetch, AbortSignal, redirects, TLS, body limits, retries, or SSRF."
---

# TypeScript Networking

Use this specialist with oh-my-pstack's TDD workflow for implementation and oh-my-pstack's review workflow for review. It owns only TypeScript-specific decisions for this concern.

## Rules

- Use the existing fetch/HTTP transport with AbortSignal, timeout, redirect, TLS, response-size, and connection semantics explicit.
- Review SSRF and credential forwarding when URLs or headers are influenced by input.
- Retry only safe operations with bounded backoff and preserve idempotency behavior.

