# Authentication and authorization

verified_at: 2026-10-03

## OAuth model

Dropbox uses OAuth 2.0 bearer access tokens. Choose the flow from the runtime
and trust boundary rather than from the implementation language.

- Server application that can protect a client secret: Authorization Code flow.
- Desktop, mobile, SPA, CLI, or other public client: Authorization Code with PKCE.
- Long-lived/background access: request offline access and securely retain the refresh token.
- Interactive-only access: avoid requesting persistent access when it is not needed.

Never embed a reusable app secret in software distributed to untrusted clients.

## Access scope

Dropbox app configuration has two separate concerns:

1. Content access:
   - App Folder: limited to the app-specific folder.
   - Full Dropbox: access across authorized Dropbox content.
2. OAuth scopes:
   - account info;
   - files/content read or write;
   - sharing/collaboration;
   - team/admin capabilities for Business API use.

Request the smallest combination that satisfies the product intent. Do not ask
for Full Dropbox because it is easier if App Folder is sufficient.

## Token handling

- Send the access token only in the Authorization bearer header where required.
- Treat access tokens, refresh tokens, app secrets, authorization codes, and PKCE verifier values as secrets.
- Encrypt secrets at rest where the host platform supports it.
- Redact them from errors, traces, crash reports, and structured logs.
- On refresh, replace stored token metadata atomically when the implementation persists it.
- A revoked authorization requires re-authentication; repeated retry is not a recovery strategy.

## Scope failures

Differentiate:

- invalid/expired token;
- valid token missing endpoint scope;
- app type/content-access restriction;
- team/admin permission restriction;
- member suspension or revoked authorization.

Do not collapse these into a generic network retry.

## Team tokens

Team-linked applications may need team scopes and may act on behalf of a member
or admin using Dropbox-API-Select-User or Dropbox-API-Select-Admin. Those
headers do not replace OAuth authorization; the underlying token still needs
the required team/member scopes.

See [namespaces-and-teams.md](namespaces-and-teams.md).
