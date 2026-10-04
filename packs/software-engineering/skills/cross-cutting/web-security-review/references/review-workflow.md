# Review workflow and evidence discipline

## Establish scope before active testing

For runtime testing, define the permitted hostnames, environments, accounts, data, time window, forbidden actions, and stop conditions before sending attack-like traffic. Prefer local, test, or otherwise explicitly authorized environments. Code review can proceed without runtime authorization, but label runtime claims as unverified unless reproduced.

Stop active testing when the service becomes unstable, an unexpected external system is reached, real data changes or is deleted, the next step requires leaving the authorized scope, or there are signs of an active incident.

## Observe normal behavior first

Build a baseline before attempting security mutations:

- enumerate endpoints and methods;
- note parameters from URL path/query, form, JSON, headers, cookies, multipart fields, and files;
- record authentication state, role, tenant, object identity, and relevant application state;
- preserve representative normal requests/responses or code paths;
- compare logged-out, ordinary-user, alternate-user, privileged-user, and administrative behavior when relevant.

The baseline is the control sample for later hypotheses.

## Convert the attack surface into review units

A useful unit contains entry point, subject/identity, input source, target object/resource, action, expected policy or invariant, sink or side effect, and observable result. Do not review routes in isolation when multiple routes reach the same object or operation.

## Form narrow hypotheses

Change one dimension at a time where practical: identity/role, object identifier, state, one request field/header, method/content type, order/repetition/timing, destination URL/path, or output context.

A suspicious 4xx/5xx, response length, timing change, stack trace, or dangerous API call is evidence to investigate, not proof of a named vulnerability.

## Trace source to sink and side effect

For controlled values, identify:

1. source;
2. parsing/decoding/normalization;
3. validation and authorization;
4. transformation;
5. sink or security-sensitive operation;
6. resulting state, output, network request, file access, process execution, log event, or browser behavior.

When output is not directly visible, inspect state or a bounded side effect rather than assuming failure or success from the HTTP response alone.

## Separate fact, conclusion, and potential impact

Write notes in three layers:

- **Observed fact** — what the request, code path, database/file state, browser execution, or log actually showed.
- **Security conclusion** — the rule that the evidence shows is violated.
- **Potential impact** — what may follow if the same rule applies elsewhere. Mark this as inference until verified.

## Prove only the minimum necessary impact

Once a security rule is proven, do not continue merely to maximize data access or command capability. Prefer inert markers, disposable test records, bounded object samples, and non-destructive comparisons.

If unexpected secret or third-party data appears, stop expanding the proof and follow the authorized reporting path.

## Record reproducible evidence

Evidence should allow a third party to reproduce the condition without collecting unnecessary sensitive data. Keep request/response excerpts small, preserve security-relevant headers and fields, and redact literal secrets.

For code review, include the source, transformation, policy check, and sink locations. For runtime review, include the minimum request/state difference that demonstrates the broken rule.

## Retest as a pair

Every remediation verification should pair:

- the formerly unsafe case, which must now fail safely; and
- the legitimate case, which must continue to succeed.

Where the issue depends on state or role, keep those preconditions explicit in the regression test.
