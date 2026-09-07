---
name: rust-observability
description: "Use when Rust code involves spans, metrics, correlation, latency, or cardinality."
---

# Rust Observability

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Rust-specific decisions for this concern.

## Rules

- Create spans and metrics for requests, jobs, migrations, and external calls with bounded fields.
- Preserve error, timeout, cancellation, retry, and partial-result state across async boundaries.
- Do not instrument every helper or put high-cardinality values into labels.

