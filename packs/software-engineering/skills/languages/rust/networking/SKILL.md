---
name: rust-networking
description: "Use when Rust code involves timeouts, TLS, proxies, redirects, body limits, retries, or SSRF."
---

# Rust Networking

Use this specialist with oh-my-pstack's TDD workflow for implementation and oh-my-pstack's review workflow for review. It owns only Rust-specific decisions for this concern.

## Rules

- Set timeout, cancellation, TLS, proxy, response-size, connection, and cleanup behavior at the network boundary.
- Review SSRF, credential forwarding, redirect policy, and retry safety when targets or headers are input-controlled.
- Preserve protocol and transport context in errors without exposing secrets.

