---
name: typescript-refactoring
description: "Use when TypeScript or Node/browser code involves types, modules, generated code, interfaces, or abstraction removal."
---

# TypeScript Refactoring

Use this specialist with pstack's TDD workflow for implementation and pstack's review workflow for review. It owns only TypeScript-specific decisions for this concern.

## Rules

- Keep public module and type boundaries narrow; avoid any as a substitute for a contract and preserve runtime validation at untrusted edges.
- Prefer a local refactor over a new framework, registry, or generic abstraction with one consumer.
- Keep generated clients and models separate from hand-written adapters.

