# Targeting, audiences, pixels, catalogs

## Targeting

Use current targeting-option endpoints/dictionaries rather than hard-coding
remembered enum values. Validate region-specific availability and combinations.

SmartNews added a `channel_alias_labels` endpoint in May 2026; re-check the
current schema when channel alias targeting is requested.

## Custom audiences

Custom Audiences can be listed by ad account. Treat uploaded/user-derived
identifiers as sensitive data: minimize retention and never log raw identifiers.

## Pixels

Resolve the correct account/business ownership before wiring conversion-dependent campaigns.

## Catalogs and product sets

Catalog APIs are documented under the Business external API family. They were
introduced for certain allowlisted developer apps.

- confirm the developer app is allowlisted;
- resolve business ownership and ad-account access;
- verify catalog review/status before dependent delivery;
- validate product-set filter rules against the current schema.
