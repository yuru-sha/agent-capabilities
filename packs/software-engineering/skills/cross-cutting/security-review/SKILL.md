---
name: security-review
description: Use for a security review of application code, dependencies, configuration, database access, network/API boundaries, secrets, authentication, authorization, or untrusted input.
---

# Security review adapter

Use this skill for a focused, evidence-based security pass. Load the matching
language, database, and OpenAPI skills for implementation details. Keep the
review read-only unless the user explicitly requests remediation.

## Review the boundary

- Identify untrusted inputs, trust transitions, identities, assets, and the
  operation that authorizes access. Trace the value to storage, output, logs,
  subprocesses, files, and network calls.
- Check authentication, object/function authorization, tenant isolation,
  default-deny behavior, privilege changes, and failure responses.
- Check validation and encoding for injection, path traversal, SSRF, unsafe
  redirects, command execution, unsafe deserialization, and resource abuse.

## Protect data and availability

- Search for secrets in source, configuration, examples, generated artifacts,
  fixtures, logs, traces, errors, and metrics. Verify redaction at the boundary.
- Review timeouts, body/file/queue limits, pagination, concurrency bounds,
  retry storms, lock contention, and expensive input paths.
- Review dependency provenance, lockfiles, known-vulnerability gates, and
  permissions without claiming a clean result from an unrun tool.

## Evidence and output

For every finding, state the asset, attack path, precondition, impact, changed
location, and a minimal remediation direction. Distinguish confirmed behavior,
code-path inference, and checks that were not run. Do not reproduce secret
values in the report.

