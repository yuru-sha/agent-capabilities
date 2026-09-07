---
name: python3-observability
description: "Use when Python 3 code involves metrics, traces, correlation, latency, or dimensions."
---

# Python 3 Observability

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Python 3-specific decisions for this concern.

## Rules

- Instrument request, job, and external-call boundaries with operation, outcome, latency, and correlation context.
- Preserve exception, timeout, cancellation, retry, and partial-result state in metrics and traces.
- Bound dimensions and avoid logging or tracing every helper call.

