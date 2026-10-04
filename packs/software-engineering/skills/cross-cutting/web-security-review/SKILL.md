---
name: web-security-review
description: Evidence-driven security review for web applications and HTTP APIs, covering attack-surface mapping, authentication, sessions, authorization, injection, browser boundaries, business logic, deployment, logging, remediation, and regression verification.
---

# Web security review

Use this Skill for source-code, pull-request, architecture, or authorized runtime review of web applications and HTTP APIs. It is language-independent and focuses on web security semantics: HTTP boundaries, browser behavior, identity, authorization, data flow, state transitions, and externally observable effects.

Use engine-specific language, database, OpenAPI, frontend, and infrastructure Skills for framework- or runtime-specific details. Use \`security-review\` for non-web cross-cutting trust boundaries. This Skill owns the web-specific review method and evidence standard.

## Core model

Do not begin with vulnerability names. Reduce the application to three questions:

1. **Data** — Where does input enter, what transformations does it cross, where does it leave, and can it become code, a query, a path, a URL, markup, a template, a log record, or another interpreted value?
2. **Subject and authority** — Who is acting, which object is targeted, which action is allowed, and does the server verify that decision at every entry point?
3. **State** — What state is current, which transitions are legal, can steps be skipped or replayed, and can ordering, repetition, timing, or concurrency violate an invariant?

Use vulnerability classes only after the relevant behavior is understood well enough to name it.

## Review workflow

Follow this order unless the request scopes the review more narrowly:

1. Establish authorization and test scope. For runtime testing, confirm allowed targets, prohibited actions, accounts, data, and stop conditions before sending attack-like requests.
2. Map the attack surface from routes, APIs, forms, uploads, redirects, callbacks, webhooks, WebSockets, background jobs, browser code, and administrative paths.
3. Record a normal baseline before mutating input. Compare unauthenticated/authenticated roles and multiple users where authorization matters.
4. Identify trust boundaries and trace untrusted values from source to security-sensitive sinks and side effects.
5. Build explicit authorization and state-transition expectations instead of inferring them from UI visibility or identifier secrecy.
6. Form one testable hypothesis at a time. Change one variable where practical and compare response, state, side effects, and logs.
7. Separate observed facts from interpretation and predicted impact. Do not name a vulnerability from an error code or dangerous API alone.
8. Confirm only the minimum impact necessary to prove the issue. Stop on instability, unexpected external reachability, real-data mutation, scope expansion, or evidence of active compromise.
9. Recommend the smallest root fix first; distinguish compensating controls and temporary mitigations.
10. Pair the security regression with a normal-path regression. A fix is incomplete if it blocks the attack by breaking legitimate behavior.

Read [review-workflow.md](references/review-workflow.md) for evidence discipline and runtime-testing boundaries.

## Select review modules

Load only the references relevant to the changed or reviewed surface:

- Identity, login, password reset, MFA, cookies, JWT, object/function authorization: [identity-and-authorization.md](references/identity-and-authorization.md)
- Validation, SQL/command/template injection, path traversal, uploads, SSRF, XML and deserialization: [input-and-interpreters.md](references/input-and-interpreters.md)
- XSS, CSRF, CORS, security headers, browser storage, \`postMessage\`, WebSocket, client-side trust boundaries: [browser-and-api-boundaries.md](references/browser-and-api-boundaries.md)
- Workflow abuse, replay, races, API resource limits, information disclosure, dependency and deployment concerns, logging and monitoring: [application-and-operations.md](references/application-and-operations.md)
- Finding format, severity, confidence, remediation, retest, and regression requirements: [findings-and-regression.md](references/findings-and-regression.md)

## Review rules

- Treat every externally influenced value as input, including headers, cookies, JSON, uploaded metadata, stored content, external API responses, queue messages, files, and browser-controlled state.
- Treat UI hiding as presentation, not authorization.
- Treat unguessable identifiers as defense-in-depth, not object authorization.
- Do not let the client choose values the server can derive authoritatively, such as owner, role, price, approval state, or tenant.
- Check the same protected object through every entry point: HTML, JSON API, admin route, batch endpoint, background job, and alternate version where present.
- Do not confuse CORS with authentication, authorization, or CSRF protection.
- Do not assume JSON, ORM use, \`shell=False\`, framework auto-escaping, containers, JWT, or admin-only reachability removes the underlying boundary problem.
- Distinguish prevention controls from detection controls. Logging a violation does not prevent it.
- Distinguish "not reproduced" from "does not exist". State untested paths and environmental limits.

## Evidence standard

For each candidate issue, capture enough evidence to answer:

- What input or action was controlled?
- Which identity, role, tenant, and object were involved?
- What exact code path or runtime behavior was reached?
- What state or side effect changed?
- What comparison demonstrates the security rule was violated?
- What was directly observed versus inferred?
- What scope was not tested?

Prefer small, comparable evidence over large dumps. Redact cookies, tokens, credentials, personal data, and unrelated secret material while preserving the fields needed to reproduce the condition.

## Output

Report confirmed findings first, ordered by severity and then confidence. For each finding include:

- ID and result-oriented title
- severity and confidence
- affected component/route and changed location when reviewing code
- preconditions, identity/role, object, and relevant state
- observed facts
- security conclusion
- bounded potential impact
- concise reproduction or code path
- root cause
- root remediation; optional defense-in-depth and temporary mitigation separately
- regression test or retest requirement

Then include unresolved hypotheses, checks not run, and scope limitations. Do not inflate impact beyond demonstrated behavior. Do not claim a clean review when relevant paths or tools were not exercised.

Keep the review read-only unless the user explicitly requests remediation.
