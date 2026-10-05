---
name: smartnews-marketing-api
description: Use when researching, designing, implementing, or maintaining SmartNews Marketing API integrations for ad accounts, campaigns, ad groups, ads, media, targeting, audiences, catalogs, and Insights/reporting in any programming language.
---

# SmartNews Marketing API

Use this Skill to translate SmartNews Ads management and reporting intent into a current, language-independent Marketing API plan.

## Core invariants

- Official SmartNews developer documentation and current OpenAPI definition are authoritative.
- Use Marketing API v3 endpoints. API v2 is disabled and returns `410 Gone`.
- Treat authentication, account context, money units, pagination, rate limits, and parent/child mutation ordering as first-class correctness concerns.
- Reuse an access token for its validity period instead of generating one per request.
- Never log client secrets, access tokens, customer identifiers, or uploaded audience data.
- Do not assume list endpoints return complete collections in one response.
- Serialize related Campaign / AdGroup / Ad mutations when they share a parent or involve a parent and child; otherwise SmartNews may return `409 Conflict`.
- Prefer the smallest safe mutation and verify resulting state with follow-up reads.
- Stream uploads and large CSV/JSON report exports; do not require whole-file buffering.

## Freshness gate

The bundled references were verified against SmartNews Marketing API **3.0.4** on
`2026-10-05`. Re-check the official docs before implementation when:

- 30 days have passed;
- the published API version or changelog changed;
- an enum, objective, targeting field, metric, creative constraint, or error differs;
- an endpoint returns unexpected validation, authorization, or business errors.

Read [references/current-api.md](references/current-api.md) first.

## Workflow

1. Resolve ad account, region, currency, timezone, objective, budget, targeting, creative, schedule, lifecycle intent, and reporting needs.
2. Verify API freshness and authentication with [references/authentication.md](references/authentication.md).
3. Build the resource plan from [references/resource-model.md](references/resource-model.md).
4. Validate endpoint families using [references/endpoints.md](references/endpoints.md).
5. Resolve delivery settings and lifecycle with [references/delivery.md](references/delivery.md).
6. Resolve media and creative inputs with [references/media.md](references/media.md).
7. Resolve targeting, custom audiences, pixels, catalogs, and product sets with [references/targeting-audiences-and-catalogs.md](references/targeting-audiences-and-catalogs.md).
8. Resolve Insights/reporting shape and export format with [references/insights-and-reporting.md](references/insights-and-reporting.md).
9. Apply pagination, sorting, rate-limit, retry, and concurrency rules from [references/collections-and-resilience.md](references/collections-and-resilience.md).
10. Reconcile ambiguous writes before retrying and verify the final resource state.

## Language-independent implementation guidance

Use the OpenAPI contract and HTTP behavior as the source model. SDKs or examples in
any language may be inspected for protocol details, but implement idiomatically in
the target language using mature HTTP, JSON, multipart streaming, retry,
cancellation, secret-storage, and observability libraries.

## Reference map

- [current-api.md](references/current-api.md): current version, base URL, source priority, freshness.
- [authentication.md](references/authentication.md): OAuth client credentials, Bearer token handling, token reuse/revocation.
- [resource-model.md](references/resource-model.md): account/campaign/ad group/ad hierarchy and mutation ordering.
- [endpoints.md](references/endpoints.md): endpoint-family navigation.
- [delivery.md](references/delivery.md): objectives, budgets, schedules, lifecycle, money units.
- [media.md](references/media.md): media list/upload behavior and streaming guidance.
- [targeting-audiences-and-catalogs.md](references/targeting-audiences-and-catalogs.md): targeting helpers, audiences, pixels, catalogs/product sets.
- [insights-and-reporting.md](references/insights-and-reporting.md): Insights layers, fields, JSON/CSV, breakdowns.
- [collections-and-resilience.md](references/collections-and-resilience.md): pagination, sorting, rate limits, retries, 409 serialization, errors.
