---
name: x-ads-api
description: Use when researching, designing, implementing, or maintaining X Ads API integrations for campaign management, creatives, media, audiences, catalog/lead-generation workflows, and analytics/reporting in any programming language.
---

# X Ads API

Use this Skill to translate an advertising or reporting intent into a current X
Ads API plan without assuming remembered behavior, old SDK behavior, or a fixed
Campaign -> Line Item -> Media -> Ad pipeline.

## Non-negotiable principles

- Official documentation first.
- Never assume remembered X Ads API behavior is current.
- Cross-reference official implementations in other languages when useful.
- Extract protocol behavior rather than copying language-specific code.
- Reuse existing resources when appropriate; create only missing resources.
- Resolve dependencies from the advertising type.
- Prefer the smallest mutation scope that satisfies the user's intent.
- Do not infer effective delivery from a single resource status.
- Avoid loading large media or reports entirely into memory.
- Verify supported metrics, dimensions, entity levels, and placements before querying.

## Freshness gate

The local references record `verified_at: 2026-10-03` and use a 30-day
freshness threshold. Before implementation, re-check the official X Ads API
documentation when the verification is older than 30 days.

Re-check even inside 30 days when any of these are true:

- the current API version differs from the local reference;
- an endpoint, advertising type, enum, relationship, media requirement, metric,
  dimension, or authentication requirement is unknown or inconsistent;
- a request or response schema differs from the reference;
- an unexpected 4xx validation error suggests the contract changed.

Read [references/current-api.md](references/current-api.md) first. Treat the
official endpoint reference as authoritative over an SDK or sample when they
conflict. Record the re-verification date when updating this Skill.

## Workflow

1. Parse the user intent: account, advertising type/objective, existing resource
   IDs, targeting, creative/media, schedule, status intent, and reporting needs.
2. Pass the freshness gate and resolve the current API version and endpoint
   family.
3. Identify the advertising type before constructing dependencies. Read
   [references/resource-model.md](references/resource-model.md).
4. Build a resource plan in which each resource is explicitly `create`,
   `reuse`, `upload`, or `not_required`. Never create a replacement solely
   because the integration knows how to create one.
5. Validate parent/child compatibility, permissions, funding, schedule,
   targeting, creative/media requirements, and current enum values.
6. Upload only required media using bounded-memory behavior described in
   [references/media.md](references/media.md).
7. Create or reuse the required Post/Card/Creative or other advertising object,
   then create only the required association to the line item or other parent.
8. Validate the resulting hierarchy and effective-delivery prerequisites before
   activation.
9. Apply the smallest required status mutation. Verify state through a follow-up
   read after writes.
10. For analytics/reporting intents, derive entity scope, time range,
    granularity, metric groups, placements, segmentation, and sync/async mode
    from [references/reporting.md](references/reporting.md).
11. Apply pagination, rate-limit, error, polling, and retry rules from
    [references/resilience.md](references/resilience.md).

## Language-independent implementation guidance

Do not restrict research to the target implementation language. If the target
language lacks an official Ads library, inspect current X documentation,
official protocol examples/Postman material, and official libraries or samples
in other languages to understand HTTP semantics, OAuth signing, encoding,
multipart/chunk behavior, pagination, async processing, polling, and lifecycle.

Then implement those protocol semantics idiomatically in the target language.
Prefer its established OAuth 1.0a and HTTP libraries instead of porting an SDK's
internal architecture. Keep X-specific transport and resource semantics
separate from language-specific adapters.

## Mutation safety

- Confirm account and resource ownership before mutating.
- Treat DELETE as destructive even when deleted entities remain readable with
  `with_deleted=true`.
- Do not pause a campaign to stop one child ad when a narrower line-item or
  promoted-object mutation satisfies the request.
- Preserve the user's supplied timezone, normalize only as required by the
  endpoint, and verify account-timezone constraints before scheduling.
- Do not automatically retry ambiguous non-idempotent writes after timeout or
  transport failure. Read back state first.
- Do not activate merely because a created resource reports `ACTIVE`; diagnose
  effective delivery across the hierarchy and current X constraints.

## Reference map

- [current-api.md](references/current-api.md): verified version, authentication,
  official-source priority, endpoint families, and official implementation
  research.
- [resource-model.md](references/resource-model.md): advertising types,
  dependency resolution, scheduling, lifecycle, and effective delivery.
- [media.md](references/media.md): uploads, Media Library/Account Media, bounded
  memory, chunking, polling, and processing failures.
- [reporting.md](references/reporting.md): analytics entity levels, metric
  groups, time semantics, synchronous/asynchronous retrieval, and large reports.
- [resilience.md](references/resilience.md): pagination, rate limits, errors,
  retries, concurrency, and async-job polling.
