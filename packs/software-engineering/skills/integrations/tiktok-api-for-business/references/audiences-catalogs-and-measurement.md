# Audiences, catalogs, leads, and measurement

## Audiences

TikTok supports multiple audience workflows including Custom Audience, customer-file audience, rule-based audience, Lookalike Audience, Saved Audience, and streaming-related audience integrations.

Verify:

- identifier normalization/hash requirements;
- source permissions;
- upload/streaming constraints;
- audience readiness/status;
- minimum-size/privacy requirements;
- update semantics.

Never log raw customer identifiers or uploaded audience payloads.

## Catalog and TikTok Store

Resolve catalog/store/product dependencies before ad creation. Treat catalog, product set, storefront/store, and advertiser ownership as explicit resources.

Do not assume a catalog visible in the UI is available to the calling app/token.

## Lead generation

Keep lead retrieval/export permissions and CRM postback/event operations separate from campaign creation. Use webhooks when current documentation supports them for timely lead updates.

## Measurement

Separate:

- Marketing API campaign configuration;
- reporting/attribution;
- pixel/dataset/event-source configuration;
- Events API server-to-server ingestion.

TikTok documents Events API 2.0 `/event/track/` as the recommended unified event endpoint for web, app, offline, and CRM sources. Verify deduplication identifiers, event schema, consent/privacy requirements, and source-specific fields from the current Events API documentation.
