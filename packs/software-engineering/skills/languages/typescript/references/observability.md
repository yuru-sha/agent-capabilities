---
name: typescript-observability
description: "Use when TypeScript or Node/browser code involves metrics, traces, correlation, latency, or cardinality."
---

# TypeScript Observability

Use this specialist with the project's TDD workflow for implementation and the project's review workflow for review. It owns only TypeScript-specific decisions for this concern.

## Rules

- Instrument request, job, and external-call boundaries with operation, outcome, latency, and correlation fields.
- Preserve error status, cancellation, retry, and partial-result state in metrics and traces.
- Bound label/cardinality growth and avoid instrumenting every pure helper.

