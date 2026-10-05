---
name: google-ads-api
description: Use when integrating with Google Ads API to manage accounts, campaigns, ad groups, ads, assets, criteria, conversions, or reporting with GAQL, mutations, batch jobs, and resilient quota-aware execution.
---

# Google Ads API

Use this Skill to design and operate language-independent Google Ads API integrations safely against the current official API.

## Core invariants

- Treat official Google Ads API documentation, reference pages, release notes, field metadata, and deprecation notices as authoritative.
- Verify the API version before implementation. Do not assume a previously used version, resource, field, enum, or service still exists.
- Separate the target customer ID from the login customer ID. Use the manager account as `login-customer-id` only when access is through that manager.
- Require OAuth 2.0 credentials and a developer token. Never log access tokens, refresh tokens, service-account private keys, client secrets, or developer tokens.
- Prefer resource names returned by the API or official helper builders over manually constructed identifiers.
- Read existing state before mutating unless the caller already provides a verified resource name and intended current state.
- Use the minimum mutation set. Keep newly created delivery objects paused where supported until budget, bidding, targeting, creative, policy, tracking, and schedule are explicitly ready.
- Use `validate_only` when available before high-impact or structurally complex mutations.
- Use partial failure only when independent operations may safely succeed separately. Do not use it as a substitute for dependency ordering or reconciliation.
- Treat reporting as a reproducible query contract: record customer, API version, GAQL, date range, account timezone, selected fields, segments, metrics, and any attribution/conversion interpretation.
- Retry only transient failures. Reconcile ambiguous writes before resubmitting to avoid duplicate or conflicting resources.

## Freshness gate

The bundled references were verified against official Google Ads API documentation on `2026-10-05`. At that time the latest documented line is Google Ads API v25, with v25.2 released on 2026-09-23.

Re-check official documentation before execution when:
- 30 days have passed;
- a newer major or minor version is available;
- a referenced field, enum, service, campaign type, bidding strategy, conversion feature, or report field differs from the bundled notes;
- the operation involves a deprecated feature or migration;
- quota, access level, batching, or authentication behavior matters to correctness.

Read [references/current-api.md](references/current-api.md) first.

## Workflow

1. Identify the target customer, manager/login customer context, required access, and intended API version.
2. Pass the freshness gate and confirm the resource/service/field contracts in the current reference.
3. Resolve authentication and headers using [references/authentication-and-account-context.md](references/authentication-and-account-context.md).
4. For reads and reports, build a GAQL query from the target resource outward and validate field compatibility before execution.
5. For writes, resolve the resource dependency graph, current state, update masks, temporary IDs, validation, and partial-failure policy.
6. Choose synchronous mutate or BatchJobService according to dependency, volume, latency, and recovery needs.
7. Capture request IDs and structured GoogleAdsFailure details for diagnostics.
8. Verify the resulting resource state or report completeness after execution.
9. For ambiguous write outcomes, search/reconcile before retrying.

## Reference map

- [current-api.md](references/current-api.md): versioning, official sources, current v25/v25.2 baseline, deprecations, and freshness.
- [authentication-and-account-context.md](references/authentication-and-account-context.md): OAuth 2.0, developer tokens, customer IDs, manager accounts, headers, and secrets.
- [resource-and-mutation-model.md](references/resource-and-mutation-model.md): resources, services, mutate patterns, update masks, temporary IDs, validation, and partial failure.
- [gaql-and-reporting.md](references/gaql-and-reporting.md): GAQL, Search/SearchStream, pagination/streaming, field compatibility, reporting, dates, segments, and reproducibility.
- [batching-quotas-and-errors.md](references/batching-quotas-and-errors.md): BatchJobService, operation limits, quotas, retries, concurrency, structured errors, and reconciliation.
