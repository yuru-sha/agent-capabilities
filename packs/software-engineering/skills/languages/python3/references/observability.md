---
name: python3-observability
description: "Use when Python 3 code involves metrics, traces, correlation, latency, or dimensions."
---

# Python 3 Observability

Use the project's TDD workflow for implementation and its review workflow for review. This specialist owns only Python 3-specific decisions for this concern.

## Rules

- Instrument request, job, and external-call boundaries with operation, outcome, latency, and correlation context.
- Preserve exception, timeout, cancellation, retry, and partial-result state in metrics and traces.
- Bound dimensions and avoid logging or tracing every helper call.

