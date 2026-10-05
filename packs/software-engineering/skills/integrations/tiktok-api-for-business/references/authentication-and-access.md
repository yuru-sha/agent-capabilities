# Authentication and access

## Advertiser access

Marketing API calls commonly use an advertiser access token. Current official examples send it in the `Access-Token` request header.

Resolve before calls:

- developer app identity;
- authorization flow and currently supported token lifetime/refresh behavior;
- advertiser IDs authorized by the token;
- required app scopes/products;
- Business Center/asset permissions when relevant;
- environment and account ownership.

TikTok documentation includes operations to obtain, refresh, and revoke advertiser access tokens. Verify current endpoint versions and token lifetime rules before implementation.

## Rules

- Store tokens in a secret manager or equivalent secure store.
- Never place tokens in URLs, logs, exception messages, analytics, or fixtures.
- Redact request/response headers in diagnostics.
- Treat authorization failure separately from advertiser/business-state failure.
- Do not assume one token authorizes every advertiser or Business Center asset.
- Re-authorize or refresh only according to current documented behavior; do not build speculative refresh loops.
- For Events API, Accounts API, or other product families, verify that product's authentication model independently instead of reusing Marketing API assumptions.
