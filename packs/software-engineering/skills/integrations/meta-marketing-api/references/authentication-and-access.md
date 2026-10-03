# Authentication and access

verified_at: 2026-10-03

## Identity choices

Choose identity from the integration model rather than convenience:

- User access token for user-authorized workflows.
- System User access token for Business-owned server-to-server automation where
  current Meta Business requirements permit it.
- App access tokens are not a substitute for user/system-user permissions on Ads assets.

Verify token type, expiry, permissions, Business assignment, Ad Account access,
Page/Instagram asset access, and app mode before any mutation.

## Common permissions

Advertising integrations commonly involve permissions such as:

- `ads_read` for reading advertising data;
- `ads_management` for ad-management mutations;
- `business_management` for Business asset-management workflows;
- Page/Instagram permissions when creative identity or Page-owned resources are involved.

Do not assume a historically used permission remains sufficient. Resolve
permissions from the exact current endpoint/resource docs.

## App Review and Marketing API Access Tier

Separate three concerns:

1. API permission on the token.
2. Asset assignment/role for the user or system user.
3. App-level access tier / App Review feature requirements.

A token containing `ads_management` does not by itself guarantee Full Access
capacity or access to every account/resource.

At verification time Meta uses the term **Marketing API Access Tier**. Re-check
current App Dashboard eligibility and feature documentation before operational
rollout.

## Token handling

- Keep tokens and app secrets in a secret manager.
- Never commit or print them.
- Prefer Authorization headers when current endpoint guidance supports them.
- Do not place secrets in logs, exception strings, analytics, or retained URLs.
- Track token owner, app, Business, granted permissions, issue/expiry time, and
  asset scope as metadata without persisting the raw token in normal tables.
- Rotate compromised or stale system-user tokens deliberately.

## Preflight

Before writes, perform low-risk reads that prove:

- the token resolves successfully;
- the intended Ad Account is visible;
- the current user/system user has the required role;
- required Page/Instagram/catalog/pixel/dataset assets are visible when used;
- the app is in the correct mode and access tier for the requested operation.

Fail early with a precise access diagnosis rather than trying multiple mutations.
