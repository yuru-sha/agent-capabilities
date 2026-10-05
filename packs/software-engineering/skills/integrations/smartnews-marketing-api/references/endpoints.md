# Endpoint families

Verify exact request/response schemas in the current OpenAPI definition.

## OAuth

- Generate access token: `POST /api/oauth/v1/access_tokens`
- Revoke active tokens: `POST /api/oauth/v1/access_tokens/revoke`

## Delivery

Marketing API v3 uses ad-account-scoped resources for Campaigns, AdGroups, and Ads.
Important collection forms include:

- `/api/ma/v3/ad_accounts/{ad_account_id}/campaigns`
- `/api/ma/v3/ad_accounts/{ad_account_id}/campaigns/{campaign_id}/ad_groups`
- `/api/ma/v3/ad_accounts/{ad_account_id}/ad_groups`
- `/api/ma/v3/ad_accounts/{ad_account_id}/ad_groups/{ad_group_id}/ads`
- `/api/ma/v3/ad_accounts/{ad_account_id}/ads`

Use single-resource GET/PATCH/DELETE forms from the current OpenAPI contract.

## Insights

- `GET /api/ma/v3/ad_accounts/{ad_account_id}/insights/{layer}`

Layers cover Campaign / AdGroup / Ad reporting.

## Media

Ad-account media APIs support paginated listing and multipart image/video upload.
Use the current OpenAPI path definitions rather than guessing URI suffixes.

## Custom audiences

- `GET /api/ma/v3/ad_accounts/{ad_account_id}/custom_audiences`

## Catalogs and product sets

Catalog APIs use `/api/bm-external/v1/businesses/{business_id}/...` and may
require allowlisting. Do not assume availability merely because the endpoint is documented.
