# Audiences, conversions, and catalogs

verified_at: 2026-10-03

## Custom Audiences

Treat audience source data as sensitive.

- Never log raw emails, phones, mobile advertising IDs, or customer-list records.
- Normalize/hash only according to current Meta requirements for the audience type.
- Stream/batch large member sets rather than holding unnecessary copies in memory.
- Verify add/remove/replace semantics and processing status before retrying.
- Reuse existing audiences when the intent is targeting reuse, not duplication.

## Lookalike audience workflows

Validate current source-audience, country/region, ratio/range, privacy, and
availability semantics. Product naming and supported controls can change.

## Pixel / Dataset / Conversions API context

Keep ad configuration and event ingestion separate:

- Marketing API configures promoted objects, optimization, Ads assets, and reporting.
- Conversions API/event APIs ingest measurement events.

Verify current Dataset/Pixel identifiers, event names, attribution/deduplication
requirements, domain/app context, and permissions before wiring optimization.

## Catalogs and product sets

Catalog-driven ads depend on:

- Business ownership/permissions;
- catalog and product-set state;
- feed/item health;
- destination and identity;
- campaign/ad-set objective and promoted object;
- current dynamic/catalog creative requirements.

Do not create a new catalog merely to satisfy a missing ID if a compatible
Business-owned catalog already exists.

## Leads and forms

Lead-generation campaigns can depend on Page-owned instant forms or other
current lead destinations. Verify form ownership, Page permission, retrieval
permissions, webhook/export behavior, and data-retention obligations separately
from ad creation.
