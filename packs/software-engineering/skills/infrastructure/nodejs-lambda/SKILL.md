---
name: nodejs-lambda
description: Use when implementing or reviewing Node.js Lambda handlers, AWS SDK v3 usage, npm lockfiles, zip packaging, or Lambda runtime alignment.
---

# Node.js Lambda

Keep the runtime, source build, dependency graph, artifact, and infrastructure
configuration aligned. Use the repository's package manager and runtime
version rather than assuming a Node.js release.

## Rules

- Align the configured Lambda runtime, local and CI Node.js versions,
  package.json engines, module format, handler path, architecture, and
  compiled output. Test the actual module format and handler entry point.
- Use AWS SDK v3 clients and import only required clients or commands. Pin
  application dependencies in the repository's single authoritative npm
  lockfile; use the configured lockfile-aware install command and avoid
  silently mixing package managers.
- When reproducibility matters, package the pinned SDK dependencies instead of
  relying on a runtime-provided SDK version.
- Produce a deterministic staging directory and zip with the handler and
  production dependencies at the layout the runtime expects. Exclude
  development-only material and credentials, and verify the artifact rather
  than trusting a local directory listing.
- Reuse SDK clients outside the handler when safe, configure bounded retries
  and timeouts, and keep handlers idempotent for event retries and partial
  failures. Use environment variables for non-secret configuration and the
  approved secret-reference mechanism for secrets.
- Check event-source visibility, reserved concurrency, timeout, memory,
  dead-letter or destination behavior, and downstream retry semantics
  together. Do not claim exactly-once processing from a Lambda trigger.
- Test handler behavior at its public event boundary and add a package smoke
  check when packaging or module resolution can fail independently of unit
  behavior.

## Verification

Run the consumer repository's pinned Node.js and package-manager commands,
including its lockfile-aware install, tests, build, and zip/artifact check.
Verify the artifact contents and configured runtime without printing secrets or
deploying the function as part of this specialist.
