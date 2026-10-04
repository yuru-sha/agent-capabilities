# Business logic, information exposure, supply chain, deployment, and monitoring

## Business logic and state transitions

Write important business rules as invariants and state transitions before testing misuse. Correctly typed input can still represent an invalid operation.

Review whether an attacker can skip required steps, reorder steps, replay a completed operation, submit duplicates, exceed limits, reuse stale approvals, race valid requests to violate a shared invariant, exploit TOCTOU gaps, or force partial failure states.

Keep server-derived values authoritative and use database constraints/transactions where they provide the final integrity boundary. Test idempotency deliberately where retries are expected.

## API and workflow resource abuse

Bound body size, upload size, decoded size, pagination, batch size, query complexity, concurrency, queue growth, retries, outbound fetches, process execution time, and output size where the feature can consume disproportionate resources.

For valuable workflows such as invitation, reset, coupon, export, messaging, payment-like actions, or content creation, review automated abuse even when each individual request is valid.

## Information disclosure

Map all egress paths:

- API and HTML responses;
- error pages and stack traces;
- response headers and server versions;
- redirects and caches;
- source maps and browser bundles;
- backups, configuration, repository artifacts, and debug endpoints;
- uploaded image/document metadata;
- logs, traces, and metrics.

Separate user-facing errors from internal diagnostic detail. Do not expose production debug consoles.

Evaluate disclosure by the value, sensitivity, and reachable scope of the information actually exposed.

## Dependencies and software supply chain

Review direct and transitive dependencies, manifests versus lockfiles, package source/index configuration, artifact hashes or provenance where supported, install/build-time code execution, and dependency-confusion risks.

Known-vulnerability scanning is continuous work. A finding requires component/version and whether the vulnerable code path or artifact is actually relevant; a scanner alert alone does not determine application impact.

Include CI/CD, container/base images, frontend packages, build tools, and generated release artifacts in the supply-chain boundary. Prefer an SBOM or equivalent release inventory where the project uses one.

## Deployment boundary

Review the effective production state, including reverse proxies and platform defaults:

- externally bound ports and interfaces;
- trusted proxy/TLS termination configuration;
- \`Host\` handling;
- secret injection rather than baking secrets into images;
- non-root/least-privilege runtime;
- limited writable filesystem paths;
- avoiding Docker socket or unnecessary host mounts;
- inbound exposure separately from outbound egress;
- request/resource/time limits;
- fail-closed production configuration validation;
- final security headers;
- exclusion of debug/test/source artifacts not needed at runtime;
- separation of migration, initialization, backup, and runtime privileges.

Containers constrain impact; they do not eliminate application vulnerabilities.

## Logging and monitoring

Separate recording, monitoring, alerting, and incident response.

Useful security events identify when, where/service, who/subject, what/action, target/object, result, and correlation/request ID without storing full sensitive requests or responses.

Review consistent recording of authentication outcomes, authorization denials, privileged/important successful actions, and relevant security-control failures. Protect logs from application-level tampering and unauthorized access.

Prevent log injection by structured serialization rather than concatenating user-controlled text into ad-hoc log lines. Treat correlation identifiers as potentially sensitive metadata.

Detection controls do not replace prevention controls. In findings, state whether a control prevents, limits, detects, or only records the behavior.
