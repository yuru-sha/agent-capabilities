---
name: typescript-security
description: "Use when TypeScript or Node/browser code involves browser/server trust boundaries, injection, redirects, secrets, or authorization."
---

# TypeScript Security

Use this specialist with pstack's TDD workflow for implementation and pstack's review workflow for review. It owns only TypeScript-specific decisions for this concern.

## Rules

- Review prototype pollution, injection, XSS/CSRF boundaries, SSRF, unsafe redirects, path handling, authorization, and client/server secret exposure.
- Validate untrusted data before DOM, URL, SQL, template, or command use and keep tokens out of logs and bundles.
- Use security tooling as evidence about configured paths, not as proof that business authorization is correct.

