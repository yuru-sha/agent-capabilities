---
name: go-observability
description: "Use when Go code involves metrics, traces, correlation, latency, or cardinality."
---

# Go Observability

Use this specialist with pstack's TDD workflow for implementation and pstack's review workflow for review. It owns only Go-specific decisions for this concern.

## Rules

- Instrument request, job, and external-call boundaries with stable operation, outcome, latency, and correlation fields.
- Propagate cancellation and error status into metrics and traces without instrumenting every helper.
- Bound cardinality and redact credentials, tokens, and raw sensitive data.

