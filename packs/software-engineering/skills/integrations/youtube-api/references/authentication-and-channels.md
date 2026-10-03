# Authentication and channel identity

verified_at: 2026-10-03

## Public data versus authorized operations

Use API keys only for methods that support public/unauthenticated access and only when no user authorization is needed.

Use OAuth 2.0 when the operation:

- accesses private channel/user data;
- uploads, updates, deletes, rates, comments, moderates, or otherwise mutates resources;
- queries YouTube Analytics or Reporting;
- manages live broadcasts, streams, or live chat in an authenticated context.

Always verify the current method's accepted scopes in its official reference.

## Scope selection

Request the minimum set of scopes required for the product.

Common families include:

- YouTube read-only access;
- YouTube full/force-ssl mutation access;
- upload-specific access;
- Analytics read-only;
- Analytics monetary read-only.

Do not request a broad YouTube mutation scope merely because it simplifies implementation when a narrower scope satisfies the operation.

## Channel identity

An authenticated Google identity is not itself a channel ID.

Before a channel-scoped mutation:

1. resolve the authenticated YouTube channel identity using the current supported channel lookup;
2. compare it with the user/application's intended channel;
3. persist the mapping between credential profile and channel ID if the integration manages multiple channels;
4. reject or require explicit remapping when credentials resolve to an unexpected channel.

Do not infer the target channel from a display name.

## Multi-channel credentials

For multiple channels, model credential context explicitly:

- credential/profile ID;
- Google account authorization;
- resolved YouTube channel ID;
- granted scopes;
- token expiry/refresh capability;
- optional human-readable label.

Never reuse a token for another channel merely because both channels are controlled by the same organization.

For batch uploads, bind every work item to a resolved credential/channel context before starting the upload.

## Token handling

- Store access/refresh tokens using the host platform's secret storage.
- Never log bearer tokens, refresh tokens, client secrets, auth codes, or redirect query strings containing credentials.
- Refresh only through the OAuth flow supported for the client type.
- Treat revocation or insufficient scope as authorization failures, not ordinary retryable network errors.
- If the application rotates credentials, update the channel mapping atomically.

## Service accounts

Do not assume a Google service account can act as a normal YouTube channel owner. Verify current YouTube authorization support and the exact content-owner/delegation model before designing around service-account credentials.

## Verification after authorization changes

When scopes, Google accounts, or channel ownership change:

- re-resolve the channel ID;
- re-check required scopes;
- invalidate stale credential-to-channel mappings;
- test a read-only identity lookup before performing writes.
