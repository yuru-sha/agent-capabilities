---
name: go-observability
description: "Use when Go code involves metrics, traces, correlation, latency, or cardinality."
---

# Go Observability

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Go-specific decisions for this concern.

## Rules

- Instrument request, job, and external-call boundaries with stable operation, outcome, latency, and correlation fields.
- Propagate cancellation and error status into metrics and traces without instrumenting every helper.
- Bound cardinality and redact credentials, tokens, and raw sensitive data.

