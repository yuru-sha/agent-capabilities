# Product boundaries

TikTok API for Business is broader than one advertising endpoint family.

## Marketing API

Use for scaled advertising management such as campaigns, ad groups, ads, creative assets/tools, audiences, reporting, catalogs/store, lead generation, and related advertiser workflows.

## Business Center

Use for Business Center membership, partners, assets, organization accounts, finance/balance allocation, and related ownership/permission workflows.

Do not treat Business Center membership as equivalent to advertiser authorization for every Marketing API action.

## Accounts API

Use for supported TikTok Business Account / Personal Account operations such as account insights, comment moderation, and video publishing.

As of the verified date, TikTok documents an additional access application requirement for new apps or scope increases involving the TikTok Accounts permission. Re-check before implementation.

## Events API

Use server-to-server event sharing for website, app, offline, or CRM events. TikTok documents Events API 2.0 `/event/track/` as the recommended unified event endpoint.

Keep event ingestion credentials and semantics separate from Marketing API advertiser-token assumptions.

## Webhooks / Subscription APIs

Use for supported event-driven updates such as leads, ad review status, account events, mentions, business messaging, or creator-marketplace events.

Do not poll when a supported webhook is the more reliable and efficient contract, but preserve reconciliation reads because webhook delivery can be delayed or duplicated.
