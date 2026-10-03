# Endpoint-family catalog

verified_at: 2026-10-03

This is navigation guidance, not a frozen specification. Verify methods, fields,
parameters, enums, permissions, and response schemas on current official pages.

## Accounts and Businesses

Representative families:

- `/me/adaccounts`
- `/act_{ad-account-id}`
- Business-owned/assigned ad-account edges
- Pages, Instagram accounts, catalogs, Pixels/Datasets, system users and assets

## Campaign delivery objects

Common account-scoped creation/listing edges:

- `/act_{ad-account-id}/campaigns`
- `/act_{ad-account-id}/adsets`
- `/act_{ad-account-id}/ads`
- `/act_{ad-account-id}/adcreatives`

Individual object IDs support reads and current-version-supported updates.

## Media and creative support

Common families include ad images, ad videos, creatives, Pages / Instagram
identity resources, lead forms, catalogs/product resources, and creative
previews where currently supported.

## Targeting and delivery helpers

Current Marketing API documentation exposes targeting search/suggestion
resources and delivery/estimate-related helpers. Treat estimate helpers as
version-sensitive because fields and behavior can be removed independently.

## Audiences and measurement

Representative families include Custom/Lookalike Audiences, Pixels/Datasets,
conversion/event configuration, catalogs, products/product sets, and related
commerce assets.

Conversions API/event ingestion is related but separate from Marketing API ad
configuration and Ads Insights.

## Insights

Ads Insights can be queried from account or advertising-object nodes/edges,
typically through `/{object-id}/insights` or account-level Insights with a
`level` parameter.

For larger requests, use the current async Insights flow rather than assuming a
single synchronous response can cover arbitrary ranges and breakdowns.

## Deprecated/legacy handling

Never call an endpoint current merely because it appears in an old blog post,
an official SDK generated for an older version, a community wrapper, or an Ads
Manager network capture from another API version.
