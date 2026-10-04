# Findings, severity, remediation, and regression

## Finding structure

Use a result-oriented title that states what is possible or what rule is broken. Do not put unverified downstream consequences in the title.

For each confirmed finding include:

- stable ID and status;
- severity and confidence;
- affected component, route, API, object, or code location;
- prerequisites and relevant identity/role/tenant/state;
- observed facts;
- security conclusion;
- bounded potential impact;
- concise reproduction or source-to-sink path;
- root cause at a fixable level;
- root remediation;
- optional defense-in-depth controls;
- optional temporary mitigation;
- regression or retest requirement.

## Observed fact vs conclusion vs impact

Keep the layers explicit.

**Observed fact** must be directly supported by code/runtime evidence.

**Security conclusion** names the violated rule based on that evidence.

**Potential impact** explains what may follow if the same rule applies to additional objects/users/routes. Mark unverified expansion as possibility, not fact.

Do not turn one exposed object into a claim that every object is exposed without evidence.

## Confidence

Use confidence to express evidence quality separately from severity.

- **High** — reproduced runtime behavior or a complete, reachable code path with decisive evidence.
- **Medium** — strong code-path evidence but an environmental/runtime dependency was not exercised.
- **Low** — plausible hypothesis with an incomplete path or missing precondition. Keep these out of confirmed findings unless the caller explicitly wants hypotheses.

State what was not tested.

## Severity

Do not derive severity from the vulnerability class alone. Evaluate the demonstrated condition using factors such as:

- remote/local reachability;
- authentication and required privilege;
- required user interaction;
- how predictable required identifiers or state are;
- confidentiality, integrity, and availability impact;
- one object versus broad scope;
- sensitivity/importance of affected data or function;
- existing effective mitigations.

If the project has an explicit severity rubric, map facts to that rubric. CVSS may communicate rationale when requested, but it does not replace the application context.

Keep remediation priority separate from severity when business urgency, exposure, or ease of exploitation changes prioritization.

## Remediation hierarchy

Recommend in this order:

1. **Root fix** — remove or correctly enforce the broken trust boundary.
2. **Defense in depth** — reduce impact or make bypass harder.
3. **Temporary mitigation** — short-lived exposure reduction when the root fix cannot ship immediately.

Do not present blocklists or compensating controls as equivalent to a root fix when the unsafe interpretation/boundary remains.

## Regression design

Translate the violated security rule into tests.

Pair a negative security test with a positive legitimate-path test. Include identity, role, tenant, object relationship, state, method, and relevant input preconditions explicitly.

For authorization, prefer a matrix that covers permitted and denied combinations. For business logic, encode valid/invalid state transitions, replay/idempotency, and concurrency cases where applicable.

For output/security headers, test the effective final response rather than only helper configuration. For deployment/configuration, test environment-specific contracts when the project supports such tests.

## Retest result

When verifying a fix, update the finding with:

- version/commit tested;
- original reproduction condition;
- result of the formerly unsafe case;
- result of the legitimate control case;
- residual limitations or related paths not tested.

A security fix is not complete if the malicious path is blocked only because the legitimate feature no longer works.
