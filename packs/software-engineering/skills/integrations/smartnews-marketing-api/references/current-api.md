# Current SmartNews Marketing API

verified_at: 2026-10-05
api_version: 3.0.4
base_url: https://ads.smartnews.com/

## Source priority

1. Current SmartNews Marketing API docs and downloadable OpenAPI definition.
2. SmartNews changelog and official help.
3. Existing implementation behavior only when still consistent with the current contract.

## Version policy

Marketing API v3 is current. v2 has been fully disabled; `/api/ma/v2/*`
returns `410 Gone`.

v3 introduced pagination behavior for Insights and Campaign / AdGroup /
Ad collection endpoints. Never port v2 collection assumptions into new code.

## Known 2026 changes worth re-checking

- January: v3 released; pagination added to major list/Insights endpoints; CSV Insights supported.
- April: Catalog and ProductSet APIs added for allowlisted developer apps.
- May: OAuth token issuance rate limit documented; tokens remain valid for 24 hours.
- July: v2 fully disabled.
- September: Insights breakdown `target_ids` became optional; non-hourly maximum removed while hourly remains limited.

## Base families

- OAuth: `/api/oauth/v1/*`
- Marketing API: `/api/ma/v3/*`
- Business/catalog external APIs: `/api/bm-external/v1/*`

Do not assume all features are available to every developer app or region.
