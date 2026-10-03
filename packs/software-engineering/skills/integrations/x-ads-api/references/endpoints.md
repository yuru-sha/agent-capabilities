# Endpoint catalog

verified_at: 2026-10-03

This file is a current-navigation catalog, not a frozen API specification.
Before implementing any request, open the current official endpoint page and
verify the path, method, parameters, enums, and response shape.

## Accounts and funding

Representative v12 families:

- `GET /12/accounts`
- account detail/read endpoints under `/12/accounts/:account_id`
- `GET /12/accounts/:account_id/funding_instruments`

Use account reads first to verify access, account timezone, currency, and
relevant capabilities before constructing mutations.

## Campaign management

Representative resource families:

- campaigns
- line items
- targeting criteria
- promoted posts
- promoted accounts
- media creatives
- placement/product-specific associations

Typical account-scoped patterns:

- `/12/accounts/:account_id/campaigns`
- `/12/accounts/:account_id/line_items`
- targeting resources under the same account scope

Do not assume every advertising type uses promoted posts. In-stream/pre-roll,
catalog-driven, account-promotion, and other products can have different
associations.

## Targeting

The current Campaign Management documentation exposes targeting criteria and
targeting-value lookup/reference resources.

Before writing targeting:

- resolve the current targeting type;
- validate supported operator/value combinations;
- resolve required location, platform, device, audience, conversation/topic, or
  other targeting IDs through current lookup resources;
- verify whether criteria are inclusive/exclusive and whether combinations are
  allowed for the selected objective/product.

Do not reuse stale targeting enum tables from an SDK.

## Creatives, Posts, Cards, and media

Current Creatives navigation includes:

- Posts, including promoted-only and scheduled posting flows where supported;
- Cards for supported card types;
- Media Library;
- Account Media;
- media-creative association resources;
- account-scoped creative asset reads.

Exact card and creative endpoints vary by creative family. Resolve the current
card type and required payload from the official Creatives reference before
implementation.

## Audiences

Current Audiences documentation includes account-scoped audience management for
supported tailored/custom audience workflows.

Verify:

- audience type;
- creation vs reuse;
- member upload/replace/remove semantics;
- processing state;
- size/privacy restrictions;
- whether the selected campaign objective/product can target that audience.

## Catalog management

Current Catalog Management documentation covers:

- catalogs;
- products;
- product sets;
- scheduled feeds and related catalog assets.

Dynamic Product Ads depend on catalog state and product-set eligibility. Resolve
those dependencies before creating campaign-side associations.

## Lead Generation

Current Lead Generation documentation covers:

- lead forms;
- lead-form/card integration;
- lead retrieval/export job workflows where currently supported.

Do not assume a lead form alone is promotable. Resolve the current creative/card
and campaign-side association requirements.

## Analytics and measurement

Current Analytics navigation includes:

- synchronous stats: `GET /12/stats/accounts/:account_id`;
- asynchronous stats jobs under `/12/stats/jobs/accounts/:account_id`;
- active-entity helpers;
- reach/frequency reporting where supported.

Measurement documentation also covers conversion-related APIs. Treat conversion
ingestion and Ads reporting as related but separate API responsibilities.

## Deprecated/legacy handling

Do not promote a route to "current" status just because:

- it appears in an old X/Twitter developer guide;
- it exists in an official SDK;
- a community library still calls it;
- a search result shows an older version path.

When documentation conflicts, use the current official endpoint reference and
record the re-verification date.
