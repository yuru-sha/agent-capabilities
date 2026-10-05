# Authentication and account context

## Required credentials

Google Ads API calls require:
- OAuth 2.0 authorization;
- a Google Ads developer token;
- the target customer ID;
- a `login-customer-id` when the authenticated principal reaches the target through a manager account.

Official REST authorization guidance:
https://developers.google.com/google-ads/api/rest/auth

The Google Ads OAuth scope is:
`https://www.googleapis.com/auth/adwords`.

Use the authentication flow appropriate to the application and deployment model. Official guides support user OAuth and service-account based setups where the service account has been granted access to the relevant Google Ads account hierarchy.

## Customer identity

Keep these concepts separate:

- **target customer ID**: the customer whose resources are queried or mutated;
- **login customer ID**: the manager customer through which access is established;
- **authenticated principal**: the Google user or service account represented by the OAuth token.

Customer IDs are ten digits and must be sent without hyphens.

When access is direct to the client account, `login-customer-id` can generally be omitted. When access is through an MCC/manager hierarchy, set it to the manager account that provides the access path.

Do not guess the manager context from a resource name alone.

## HTTP metadata

For REST calls, expect:
- `Authorization: Bearer <access-token>`
- `developer-token: <developer-token>`
- `login-customer-id: <manager-customer-id>` when required
- normal content headers for the chosen transport.

Capture the response `request-id` for support and diagnostics. Do not log secret-bearing request headers.

## Access and developer token levels

Developer-token access level controls allowed environments and daily operation limits. Verify the current access level and quota before designing bulk jobs.

Do not assume that a token that works for test accounts can access production accounts.

## Secret handling

Never commit or print:
- refresh tokens;
- OAuth client secrets;
- service-account private keys or key files;
- access tokens;
- developer tokens.

Use the consuming project's secret manager and least-privilege access controls. Rotate credentials when exposure is suspected.

## Preflight

Before the first mutation, verify:
1. the target customer ID;
2. the login customer ID or direct-access path;
3. OAuth principal access to that hierarchy;
4. developer-token access level;
5. API version;
6. whether the target is test or production;
7. billing/funding and account status when delivery is in scope.
