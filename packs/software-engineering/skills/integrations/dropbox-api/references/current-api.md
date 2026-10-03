# Current Dropbox API

verified_at: 2026-10-03
freshness_days: 30

## Source priority

Use sources in this order:

1. Dropbox HTTP API reference:
   https://www.dropbox.com/developers/documentation/http/documentation
2. Dropbox developer guides:
   https://developers.dropbox.com/
3. Official Dropbox SDKs and generated API types.
4. Official examples and blog posts.
5. Third-party material only when official sources do not cover the question.

If an SDK conflicts with the current HTTP reference, follow the HTTP reference.

## Freshness rules

Re-verify official behavior after 30 days and sooner when:

- scopes, app permissions, or token behavior appear different;
- an endpoint or tagged-union error differs from this Skill;
- documented file-size, batching, pagination, or upload-session behavior changes;
- team-space or namespace behavior is uncertain;
- the official SDK contains newer endpoint or type definitions.

Do not encode a permanent API-version assumption. Dropbox API v2 route names
are stable-looking identifiers, but endpoint contracts and supported fields can
still evolve.

## Official implementation research

When the target language has an official SDK, inspect it for implementation
details such as:

- token refresh and PKCE handling;
- API RPC versus content-host routing;
- Dropbox-API-Arg construction;
- upload-session offset handling;
- Path-Root and Select-User/Admin support;
- cursor continuation;
- generated tagged unions and endpoint-specific errors.

Official SDK repositories are linked from Dropbox developer documentation.
Use them to understand protocol behavior, not as authority over newer HTTP docs.

## Verified guide set

The following official guides were checked for this Skill:

- OAuth Guide:
  https://developers.dropbox.com/oauth-guide
- Error Handling Guide:
  https://developers.dropbox.com/error-handling-guide
- Team Files Guide:
  https://developers.dropbox.com/dbx-team-files-guide
- Sharing Guide:
  https://developers.dropbox.com/dbx-sharing-guide

Before implementing a concrete endpoint, open the current HTTP endpoint
reference and confirm its required scope, request shape, response type, errors,
and limits.
