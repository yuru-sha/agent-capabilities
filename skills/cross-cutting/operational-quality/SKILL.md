---
name: operational-quality
description: Use when a change affects logging, metrics, tracing, configuration, resource limits, serialization, networking, CLI behavior, documentation, or production operability.
---

# Operational quality adapter

Use this skill for production-facing behavior that crosses implementation
modules. Pair it with the language skill for mechanics and the database/OpenAPI
skill when those boundaries are involved.

## Logging and observability

- Instrument request, job, migration, and external-call boundaries with stable
  operation, outcome, latency, and correlation fields.
- Preserve error, timeout, cancellation, retry, and partial-result state. Avoid
  duplicate logs and high-cardinality or sensitive fields.
- Treat metrics and traces as contracts with owners and useful dimensions; do
  not add telemetry to every helper.

## Configuration and resources

- Define source precedence, required values, defaults, validation, reload, and
  safe failure behavior at the boundary.
- Bound memory, files, sockets, queues, request bodies, retries, and concurrency.
  Make ownership and cleanup visible on success, cancellation, and failure.

## Serialization and networking

- Specify missing/null/empty/default, numeric precision, time zone, enum, and
  unknown-field behavior. Validate external data before domain use.
- Define timeout, cancellation, status, response limits, connection reuse,
  retry safety, and idempotency for every external call.

## CLI and documentation

- Keep stdin, stdout, stderr, exit codes, signals, quiet/verbose modes, and
  user-safe errors consistent with the existing CLI.
- Document behavior, configuration, failure modes, compatibility boundaries,
  and runnable examples. Keep generated documentation tied to its source of
  truth and do not promise an unverified guarantee.

