---
name: meta-marketing-api
description: Use when researching, designing, implementing, or maintaining Meta Marketing API integrations for ad accounts, campaigns, ad sets, ads, creatives, audiences, conversions, and Insights/reporting in any programming language.
---

# Meta Marketing API

Use this Skill to translate advertising, measurement, or reporting intent into a
current Meta Marketing API plan without assuming remembered Graph API behavior,
old SDK behavior, or stale Ads Manager semantics.

## Non-negotiable principles

- Official Meta documentation first.
- Treat Graph API and Marketing API versioning as an active compatibility concern.
- Never assume remembered endpoint fields, enums, objectives, placements, metrics,
  permissions, or policy requirements are current.
- Cross-reference official SDKs and samples in other languages when useful, but
  extract protocol behavior rather than copying language-specific architecture.
- Model Business, Ad Account, Campaign, Ad Set, Ad, Creative, Pixel/Dataset,
  Audience, Catalog, Page, Instagram account, and related assets explicitly.
- Reuse compatible existing resources where appropriate.
- Prefer the smallest mutation scope that satisfies the user's intent.
- Create new delivery objects paused unless immediate activation is explicitly requested.
- Do not infer effective delivery from configured status alone.
- Avoid loading large uploads, exports, or async report results entirely into memory.
- Verify current Insights fields, breakdowns, and attribution semantics before querying.

## Freshness gate

The local references record `verified_at: 2026-10-03` and use a 30-day
freshness threshold. Before implementation, re-check official Meta developer
documentation when verification is older than 30 days.

Re-check even inside 30 days when any of these are true:

- the current Graph API / Marketing API version differs from the local reference;
- a field, enum, objective, optimization goal, placement, permission, metric,
  breakdown, attribution setting, or resource relationship is unknown or inconsistent;
- App Review / Marketing API Access Tier requirements appear different;
- an unexpected 4xx validation error suggests the contract changed;
- a changelog or out-of-cycle change applies to the requested workflow.

Read [references/current-api.md](references/current-api.md) first. Treat current
official reference pages and changelogs as authoritative over SDKs, examples,
blog posts, or remembered behavior when they conflict.

## Workflow

1. Parse intent: Business, app, user/system-user identity, Ad Account, objective,
   budget, targeting, placements, creative/media, schedule, lifecycle intent,
   attribution, conversion source, audience/catalog dependencies, and reporting.
2. Pass the freshness gate and resolve the current Graph/Marketing API version.
3. Validate authentication, token type, permissions, asset assignments, App Review,
   and Marketing API Access Tier requirements using
   [references/authentication-and-access.md](references/authentication-and-access.md).
4. Resolve account timezone, currency, funding, Business ownership, and connected
   assets using [references/account-context.md](references/account-context.md).
5. Build an explicit resource plan from
   [references/resource-model.md](references/resource-model.md), marking each
   resource `create`, `reuse`, `upload`, `update`, or `not_required`.
6. Validate endpoint families in [references/endpoints.md](references/endpoints.md).
7. Resolve campaigns, ad sets, ads, budgets, schedules, targeting, placements,
   optimization, and bids using
   [references/delivery.md](references/delivery.md).
8. Create or reuse creative assets using
   [references/creatives-and-media.md](references/creatives-and-media.md).
9. Resolve Custom Audiences, conversion sources, catalogs, and related assets from
   [references/audiences-conversions-and-catalogs.md](references/audiences-conversions-and-catalogs.md).
10. Apply the smallest safe lifecycle mutation and verify state with follow-up reads.
11. For reporting, derive level, date range, time increment, fields, breakdowns,
    attribution semantics, filters, sorting, pagination, and sync/async mode from
    [references/insights-and-reporting.md](references/insights-and-reporting.md).
12. Apply pagination/batch rules from
    [references/collections-and-batching.md](references/collections-and-batching.md)
    and rate-limit/error/retry rules from
    [references/resilience.md](references/resilience.md).

## Language-independent implementation guidance

Do not restrict research to the target language. Inspect current official Meta
HTTP reference pages, official Business SDKs, and current samples in other
languages to understand Graph request structure, token handling, multipart or
resumable upload behavior, field expansion, pagination, batch requests, async
jobs, polling, and error metadata.

Implement those protocol semantics idiomatically in the target language. Prefer
mature HTTP, JSON, secret-storage, streaming, cancellation, retry, and
observability libraries instead of porting an SDK's internal architecture.

## Mutation safety

- Verify Business/Ad Account/resource ownership before writes.
- Preserve the user's requested account, budget unit, timezone, and schedule.
- Verify current money-field semantics before converting human currency values.
- Prefer PAUSED creation for campaign/ad set/ad objects until review is complete.
- Never activate merely because one object reports `ACTIVE`; verify parent state,
  schedule, review/policy state, billing/funding, audience, creative readiness,
  account status, and current delivery constraints.
- Do not automatically retry ambiguous non-idempotent writes after transport
  failure. Reconcile state first.
- Avoid destructive replacement when an update or narrower mutation is sufficient.
- Never log access tokens, app secrets, system-user tokens, or customer-list identifiers.

## Reference map

- [current-api.md](references/current-api.md): verified version, source priority,
  changelog/out-of-cycle policy, and cross-language research guidance.
- [authentication-and-access.md](references/authentication-and-access.md):
  tokens, permissions, system users, asset assignments, App Review, and access tier.
- [account-context.md](references/account-context.md): timezone, currency,
  Business ownership, identities, funding, and connected assets.
- [resource-model.md](references/resource-model.md): hierarchy, reuse planning,
  dependencies, and effective-delivery diagnosis.
- [endpoints.md](references/endpoints.md): endpoint-family navigation.
- [delivery.md](references/delivery.md): campaign/ad-set/ad lifecycle, targeting,
  placements, optimization, bidding, schedules, and delivery checks.
- [creatives-and-media.md](references/creatives-and-media.md): creatives,
  identities, images/video, uploads, reuse, and processing.
- [audiences-conversions-and-catalogs.md](references/audiences-conversions-and-catalogs.md):
  Custom Audiences, Pixels/Datasets/CAPI context, catalogs, product sets, and leads.
- [insights-and-reporting.md](references/insights-and-reporting.md): Ads Insights,
  sync/async reporting, fields, breakdowns, attribution, actions, and large exports.
- [collections-and-batching.md](references/collections-and-batching.md): cursors,
  field selection/expansion, filtering, sorting, batching, and memory bounds.
- [resilience.md](references/resilience.md): rate limits, BUC headers, errors,
  retries, ambiguous writes, concurrency, polling, and observability.
