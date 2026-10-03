# Authentication and request signing

verified_at: 2026-10-03

## Current authentication model

At verification time the X Ads API uses OAuth 1.0a signed HTTPS requests.

The integration needs:

- API key / consumer key;
- API secret / consumer secret;
- user access token;
- user access-token secret;
- an authenticated user with access to the target Ads account.

Do not treat OAuth 2.0 bearer-token behavior from other X APIs as
interchangeable with Ads API authentication without current official evidence.

## Signing rules

Use a mature OAuth 1.0a implementation in the target language. Avoid writing
custom signing code unless the environment leaves no alternative.

Verify:

- HTTP method;
- normalized request URL;
- percent-encoding;
- query/body parameters that participate in the signature;
- nonce/timestamp generation;
- signature method;
- Authorization header construction.

A request can be semantically correct yet fail authentication because of
incorrect encoding or signature-base construction.

## Account access

Authentication proves the user identity; it does not prove access to every Ads
account or resource.

Before an account-scoped workflow:

1. list or read accessible accounts;
2. verify the intended account ID;
3. verify any current role/permission requirement;
4. verify resource ownership before mutation.

Treat authorization errors separately from signature errors.

## Secret handling

Never log or persist:

- API secrets;
- access-token secrets;
- full OAuth Authorization headers;
- raw credential-bearing requests;
- secret values from environment/configuration.

Logging may include:

- operation name;
- Ads account ID where appropriate;
- resource ID;
- HTTP status;
- X request/correlation ID if returned;
- structured non-secret error code.

## Clock skew

OAuth 1.0a depends on timestamps. When signature failures appear intermittent,
check system clock synchronization before changing request logic.

## Cross-language research

When the target language has no maintained Ads SDK, inspect X-maintained
Python/Ruby SDKs and the official Postman collection for protocol intent, then
implement with the target language's established OAuth 1.0a and HTTP stack.

Do not copy SDK credential-loading patterns, global mutable clients, or retry
behavior merely because they are convenient in another language.
