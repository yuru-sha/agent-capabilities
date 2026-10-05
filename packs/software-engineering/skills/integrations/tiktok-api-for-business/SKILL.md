---
name: tiktok-api-for-business
description: Use when researching, designing, implementing, or maintaining TikTok API for Business integrations across Marketing API, Business Center, Accounts API, Events API, creatives, audiences, catalogs, webhooks, and reporting in any programming language.
---

# TikTok API for Business

Use this Skill to translate TikTok advertising, business-account, measurement, and reporting intent into a current, language-independent API plan.

## Core principles

- Use current official TikTok API for Business documentation as the primary source of truth.
- Treat API versioning as active compatibility work. TikTok's v2.0 documentation is incremental: some unchanged endpoints may only require a version-path update and therefore may not appear in the v2.0 reference.
- Do not assume remembered fields, enums, objectives, optimization goals, placements, metrics, identities, creative constraints, or access requirements are current.
- Separate product families and authorization boundaries before choosing endpoints.
- Model advertiser, campaign, ad group, ad, identity, creative asset, audience, catalog/store, Business Center, account, and event-source dependencies explicitly.
- Distinguish Manual campaigns from Upgraded Smart+ workflows; do not force one hierarchy or endpoint family onto the other.
- Prefer reuse of compatible assets and the smallest safe mutation.
- Create delivery objects disabled or paused unless immediate activation is explicitly requested and currently supported by the chosen endpoint.
- Verify effective delivery state rather than trusting configured operation status alone.
- Stream large media uploads and report downloads; do not require whole-file buffering.
- Reconcile ambiguous writes before retrying non-idempotent operations.
- Never log access tokens, app secrets, advertiser secrets, customer audience data, or event identifiers that should be treated as sensitive.

## Freshness gate

The bundled references were verified against official TikTok API for Business documentation on `2026-10-05`.

Re-check the official documentation before implementation when:

- 30 days have passed;
- the current API version, migration guide, or endpoint path differs;
- a field, enum, objective, placement, metric, dimension, identity type, or creative requirement is uncertain;
- app approval, scope, advertiser authorization, Business Center permission, or token behavior differs;
- an unexpected 4xx/5xx or TikTok return code suggests contract drift;
- a deprecated Legacy Smart+ or ad format is involved.

Read [references/current-api.md](references/current-api.md) first.

## Workflow

1. Identify the product family and use case with [references/product-boundaries.md](references/product-boundaries.md).
2. Pass the freshness gate and resolve the current endpoint/API version using [references/current-api.md](references/current-api.md).
3. Resolve developer app, advertiser/business identity, token, scope, permissions, and asset authorization using [references/authentication-and-access.md](references/authentication-and-access.md).
4. Resolve advertiser/account context, currency, timezone, Business Center ownership, identities, and connected assets using [references/account-context.md](references/account-context.md).
5. Build the resource plan using [references/resource-model-and-delivery.md](references/resource-model-and-delivery.md).
6. Resolve creative, media, Spark Ads/identity, and upload behavior using [references/creatives-and-media.md](references/creatives-and-media.md).
7. Resolve audiences, catalogs/TikTok Store, lead-generation dependencies, and measurement/event sources using [references/audiences-catalogs-and-measurement.md](references/audiences-catalogs-and-measurement.md).
8. Resolve synchronous/asynchronous Reporting API shape, dimensions, metrics, filters, attribution, latency, and download behavior using [references/reporting.md](references/reporting.md).
9. Apply pagination, sorting, rate-limit, retry, polling, webhook, and ambiguous-write rules from [references/collections-and-resilience.md](references/collections-and-resilience.md).
10. Verify final resource state with follow-up reads.

## Language-independent implementation guidance

Inspect official HTTP documentation, current examples, and official SDKs or samples in any language when useful. Extract protocol behavior rather than copying an SDK's architecture.

Implement idiomatically in the target language with mature HTTP, JSON, multipart/streaming, cancellation, retry, polling, secret-storage, and observability libraries.

## Reference map

- [current-api.md](references/current-api.md): current documentation/version strategy and source priority.
- [product-boundaries.md](references/product-boundaries.md): Marketing API, Business Center, Accounts API, Events API, webhooks, and ownership boundaries.
- [authentication-and-access.md](references/authentication-and-access.md): authorization, advertiser tokens, scopes, permissions, and secret handling.
- [account-context.md](references/account-context.md): advertiser/business context, timezone, currency, identities, and connected assets.
- [resource-model-and-delivery.md](references/resource-model-and-delivery.md): Campaign/Ad Group/Ad, Manual vs Upgraded Smart+, budgets, targeting, bidding, schedules, and lifecycle.
- [creatives-and-media.md](references/creatives-and-media.md): images/video/playables, Spark Ads, identities, creative reuse, upload and processing.
- [audiences-catalogs-and-measurement.md](references/audiences-catalogs-and-measurement.md): audiences, catalogs/store, leads, pixels/events, and Events API boundary.
- [reporting.md](references/reporting.md): sync/async reporting, dimensions, metrics, filters, attribution, latency, and downloads.
- [collections-and-resilience.md](references/collections-and-resilience.md): pagination, sorting, rate limits, retries, polling, return codes, webhooks, and ambiguous writes.
