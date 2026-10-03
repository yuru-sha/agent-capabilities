# Current X Ads API reference

verified_at: 2026-10-03
freshness_threshold_days: 30
verified_current_version: 12

## Authority and revalidation

Use sources in this order:

1. Current X Ads API documentation at `https://docs.x.com/x-ads-api`.
2. Current endpoint reference pages.
3. Current official protocol examples or official Postman material.
4. Current official Ads SDKs.
5. Current official XDKs or samples.
6. Community implementations only as corroborating evidence.

Official SDKs can lag the API. When an SDK or sample conflicts with current
endpoint documentation, follow the current endpoint documentation.

At verification time, the official version table listed v12 (`/12/`) as the
latest version and showed v11 as also not yet deprecated. Do not hard-code that
assumption beyond the freshness window. Inspect the `x-current-api-version`
response header and `x-api-warn` deprecation header when available.

## Authentication and transport

At verification time:

- base URL: `https://ads-api.x.com`;
- the version is the first path segment;
- HTTPS is required;
- Ads API calls use OAuth 1.0a signed requests with an API key/secret and an
  access token for a user who can access the Ads account;
- identifiers are strings and responses are JSON.

Use a mature OAuth 1.0a library for the target language. Correctly percent-encode
reserved characters before generating the signature base string.

## Endpoint families

This catalog is intentionally a navigation aid, not a replacement for the
official parameter tables. Re-check the linked current reference before coding.

| Area | Current resource families / representative v12 routes |
|---|---|
| Accounts | `GET /12/accounts`, account-scoped reads |
| Campaigns | `/12/accounts/:account_id/campaigns` and `.../campaigns/:campaign_id` |
| Line Items | `/12/accounts/:account_id/line_items` and `.../line_items/:line_item_id` |
| Funding Instruments | `/12/accounts/:account_id/funding_instruments` |
| Targeting | targeting criteria plus targeting constants / lookup resources |
| Promoted content | promoted posts/accounts and line-item associations exposed by Campaign Management |
| Posts | account-scoped promoted-only/scheduled Post creation and retrieval exposed by Creatives |
| Cards | account card endpoints for supported card types |
| Media Library | `/12/accounts/:account_id/media_library` and `.../:media_key` |
| Account Media | `/12/accounts/:account_id/account_media` and `.../:account_media_id` |
| Media Creatives | account-scoped media-creative associations for supported placements/products |
| Audiences | Tailored/Custom Audience endpoints in the Audiences reference |
| Analytics | `GET /12/stats/accounts/:account_id`, async `/12/stats/jobs/accounts/:account_id`, Active Entities, reach/frequency |
| Catalog | product catalogs, products, product sets, and scheduled feeds in Catalog Management |
| Lead Generation | lead forms, LEAD_FORM card integration, lead export jobs |
| Measurement | mobile conversions, web conversions/Conversion API, A/B testing |

Official navigation pages:

- Campaign Management API Reference
- Creatives API Reference
- Audiences API Reference
- Catalog Management API Reference
- Lead Generation API Reference
- Analytics

Do not list a legacy path as current merely because it appears in an old guide
or SDK. Some overview examples still show old version numbers; use the resource
URL in the current reference page.

## Official implementation research

At verification time, X's Tools and Libraries page identifies these official
Ads API implementation resources:

- `twitter-python-ads-sdk` for Python;
- `twitter-ruby-ads-sdk` for Ruby;
- the official Ads API Postman collection.

The same page lists PHP, Java, and JavaScript/Node.js libraries under
**community tools and libraries**, not as X-maintained SDKs. Preserve that
distinction. An official repository can still lag the current endpoint
reference, so use it to understand protocol behavior rather than as a current
contract.

When the target language has weak or no Ads API support:

1. Inspect current official docs and Postman examples for request shape.
2. Inspect the official Python/Ruby SDKs and any current official samples in
   other languages for OAuth signing, serialization, pagination, media
   streaming/chunk boundaries, async polling, and error handling.
3. Use community implementations only as supporting evidence.
4. Extract protocol behavior rather than copying language-specific client
   architecture.
5. Re-implement those semantics using the target language's normal HTTP,
   streaming, cancellation, and resource-management primitives.

Do not copy an old SDK's endpoint version, enum set, buffering strategy, or
retry behavior without confirming each item against the current reference.
