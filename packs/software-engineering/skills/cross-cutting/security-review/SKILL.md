---
name: security-review
description: Cross-engine trust-boundary checklist for application, dependency, database, network, and OpenAPI surfaces when no engine-specific security specialist fits.
---

# Trust-boundary specialist

Use this skill when a security concern spans multiple surfaces and the
language, database, OpenAPI, or infrastructure specialists already cover
the engine-specific rules. Engine-specific security rules live in each
language `*-security` skill and database `*-roles-rls` /
`*-roles-privileges` skill. This skill adds only the cross-cutting checks
those specialists do not own.

For web applications and HTTP APIs, use `web-security-review` for the
web-specific review workflow, browser/HTTP semantics, authentication and
session lifecycle, authorization matrices, business-logic/state analysis,
runtime evidence discipline, and regression requirements. Use this Skill
alongside it only for cross-engine concerns that extend beyond the web
boundary or are not already owned by a more specific specialist.

## Cross-cutting boundary

- Trace untrusted input to storage, output, logs, subprocesses, files, and
  network calls across trust transitions.
- Verify default-deny authorization, tenant isolation, and failure responses
  at request boundaries.
- Check validation and encoding for injection, path traversal, SSRF, unsafe
  redirects, command execution, and unsafe deserialization when no
  engine-specific skill already covers the surface.

## Cross-cutting data and availability

- Search for secrets in source, configuration, examples, generated artifacts,
  fixtures, logs, traces, errors, and metrics. Verify redaction at boundaries.
- Review timeouts, body/file/queue limits, pagination, concurrency bounds,
  retry storms, lock contention, and expensive input paths not covered by
  engine specialists.
- Review dependency provenance, lockfiles, known-vulnerability gates, and
  permissions without claiming a clean result from an unrun tool.

## Evidence and output

For every finding, state the asset, attack path, precondition, impact,
changed location, and a minimal remediation direction. Distinguish confirmed
behavior, code-path inference, and checks that were not run. Do not
reproduce secret values in the report. Keep this skill read-only unless the
user explicitly requests remediation.