---
name: note-com-unofficial-api
description: Use when researching, integrating, or maintaining note.com's undocumented web APIs from any project. Covers observed REST and GraphQL behavior, authentication, and safe revalidation; it is not a general private-API skill.
---

# note.com unofficial API

This Skill is specifically about note.com's undocumented web APIs and can be
used by projects that integrate with note.com. It is not an official API
contract. The endpoint details are based on a third-party survey last updated
2026-09-14 and can become stale without notice. Read
[references/endpoints.md](references/endpoints.md) for the observed routes and
their caveats before relying on an endpoint.

## Operating assumptions

- Treat the APIs as unstable and intended only for low-frequency personal use,
  consistent with the survey's guidance. Do not build bulk crawlers or high-
  rate polling around them.
- Keep note.com API facts separate from the consuming project's supported
  interface. Before implementing, read that project's instructions,
  specification, authentication client, data ownership rules, and tool/API
  boundary. An endpoint listed here is not permission to add or call it.
- Reuse the project's existing client and session handling. Preserve its
  identity and ownership checks, confirmation rules, secret redaction, and
  failure behavior. Request explicit scope approval before expanding the
  project's public surface.

## Authentication

- The observed REST session cookie is `_note_session_v5`. Use only an
  authorized, project-supported session source and verify the current account
  identity before account-scoped operations.
- GraphQL requests use `https://graphql.note.com/graphql`. The survey reports
  a short-lived JWT issued by `POST /api/v3/graphql/auth`, sent in
  `Authorization: Bearer ...`. Cookie-only dashboard queries may silently
  return anonymous-viewer results; verify the resolved viewer before treating
  empty or zero-valued results as account data.
- The survey reports that `POST /api/v1/sessions/sign_in` began requiring a
  browser-issued reCAPTCHA v3 token in May 2026. Do not generate, fake,
  outsource, or bypass CAPTCHA. If the supported session expires, stop and use
  the project's authorized reauthentication path.
- Never log, print, commit, or persist passwords, cookies, XSRF/CSRF values,
  bearer/CAPTCHA tokens, authorization headers, or full credential-bearing
  requests/responses. Log operation names and HTTP status only.

## Reading and revalidating behavior

1. Check the survey's last-updated date and relevant caveats in
   `references/endpoints.md`; treat source-only details as observations, not
   guarantees.
2. Re-observe the specific action in note.com's web UI through the user's
   normal authorized browser session. Prefer harmless reads and inspect only
   the relevant Network request.
3. Record only method, route, non-secret query and payload shape, required
   header names, status, and redacted response shape. Do not save raw header or
   body dumps, browser storage, or unrelated account data.
4. Label findings **re-observed**, **survey-only**, **inferred**, or
   **unknown**, including the observation date. If the live behavior conflicts
   with the survey, stop and document the difference before changing code.
5. Revalidate authentication, pagination, response fields, and write effects
   after relevant note.com changes. Do not claim live compatibility from
   offline tests or source inspection alone.

## Write safety

- Treat every non-GET request as a possible mutation. Use only an explicitly
  authorized account and a designated test object for write verification.
- Preserve the consuming project's CSRF/XSRF and ownership safeguards. Never
  replay captured writes, fabricate client-identity headers, evade throttling,
  or automatically retry a write after a timeout or 5xx response.
- The survey describes `X-Note-Client-Code` on v3 comment mutations and
  different payload shapes for other write families. Those details do not
  authorize comments, likes, publication, scheduling, paid-content changes,
  deletion, memberships, or uploads. Require explicit scope authorization
  and the consuming project's specification update before implementing them.
- Confirm a write's result through an authorized read before deciding whether
  to retry or continue. Stop on authentication, ownership, rate-limit, or
  server errors.

## note-ops integration

When applying this Skill in the `note-ops` repository, also follow its `AGENTS.md`,
`docs/SPEC.md`, `skills/note-management-workflow/SKILL.md`, and
`.agents/skills/verify-note-ops/SKILL.md`. Its current server contract remains
exactly six tools and draft-only content writes; this Skill does not expand it.
