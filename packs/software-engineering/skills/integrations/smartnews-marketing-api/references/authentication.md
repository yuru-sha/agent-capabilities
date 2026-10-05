# Authentication

SmartNews uses OAuth client credentials for developer applications.

## Token issuance

`POST /api/oauth/v1/access_tokens`

Form fields:

- `grant_type=client_credentials`
- `client_id`: developer app ID
- `client_secret`: developer app secret

Successful responses include `access_token`, `expires_in` (currently 86400
seconds), `token_type=Bearer`, and scope information.

Send API requests with:

`Authorization: Bearer <access token>`

## Token lifecycle

- Reuse a token during its validity period.
- Do not issue a token for each API call.
- Token issuance is currently limited to 5 requests/minute per developer app.
- Support secret rotation and explicit revocation:
  `POST /api/oauth/v1/access_tokens/revoke`.
- On `401`, distinguish invalid/expired token from malformed credentials and
  refresh once only when the request can be safely retried.
- Never persist tokens or client secrets in logs, traces, URLs, crash dumps, or metrics labels.

## Access checks

A valid token does not imply access to every ad account, business, catalog, or
feature. Handle `403` separately from `401`; handle `404` as either absent
resource or hidden-by-permission according to endpoint semantics.
