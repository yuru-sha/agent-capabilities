---
name: dropbox-api
description: Use when researching, designing, implementing, reviewing, or maintaining Dropbox API integrations for authentication, files/folders, transfers, change tracking, sharing, namespaces, team content, and resilience in any programming language.
---

# Dropbox API

Use this Skill to translate Dropbox integration intent into current API behavior
without depending on a specific programming language or assuming that user paths,
team namespaces, transfer limits, or SDK behavior are stable.

## Non-negotiable principles

- Official Dropbox HTTP API documentation is the source of truth.
- Never assume remembered endpoint, scope, limit, namespace, or SDK behavior is current.
- Cross-reference official Dropbox SDKs when useful, but extract protocol semantics rather than copying SDK architecture.
- Request the minimum OAuth scopes and content access required.
- Prefer stable file IDs when identity must survive moves or renames.
- Treat paths, file IDs, revisions, and namespace-relative paths as distinct references.
- Stream file content; do not load large uploads or downloads entirely into memory.
- Use upload sessions for large, resumable, or chunked uploads.
- Persist and resume cursors for incremental change tracking.
- Treat shared links, shared files, shared folders, and team-managed content as distinct sharing models.
- Resolve root namespace and team-space behavior explicitly before traversing team content.
- Respect Retry-After, bound retries, and limit concurrent writes per namespace.
- Log X-Dropbox-Request-Id for operational troubleshooting.
- Verify write results with a follow-up read when state matters.

## Freshness gate

The local references record `verified_at: 2026-10-03` and use a 30-day
freshness threshold. Re-check official Dropbox documentation before
implementation when verification is older than 30 days.

Re-check even inside 30 days when:

- an endpoint, scope, enum, content limit, upload-session rule, or error variant is unknown;
- App Folder versus Full Dropbox access changes the intended behavior;
- the target account may use Dropbox team folders or team space;
- an SDK or generated type disagrees with the HTTP reference;
- an unexpected 4xx error suggests the contract changed.

Read [references/current-api.md](references/current-api.md) first.

## Workflow

1. Parse intent: user/team context, app access type, required scopes, file/folder
   operations, transfer sizes, sharing needs, sync/change-tracking needs, and
   whether mutations are allowed.
2. Pass the freshness gate and identify the current HTTP endpoints and scopes.
3. Resolve authentication with
   [references/authentication.md](references/authentication.md).
4. Resolve identifiers, metadata semantics, and basic CRUD with
   [references/files-and-folders.md](references/files-and-folders.md).
5. For upload/download intents, choose bounded-memory transfer behavior from
   [references/transfers.md](references/transfers.md).
6. For traversal or synchronization, use cursor semantics from
   [references/changes-and-collections.md](references/changes-and-collections.md).
7. For collaboration, distinguish link, file-member, folder-member, and mount
   semantics using [references/sharing.md](references/sharing.md).
8. For team content, resolve root/home namespaces and required headers using
   [references/namespaces-and-teams.md](references/namespaces-and-teams.md).
9. Confirm concrete endpoint families in
   [references/endpoints.md](references/endpoints.md).
10. Apply retry, rate-limit, concurrency, ambiguity, and logging rules from
    [references/resilience.md](references/resilience.md).
11. After mutations, read back metadata or relevant state when correctness
    depends on the resulting server state.

## Language-independent implementation guidance

Implement the Dropbox wire contract idiomatically in the target language.
Official SDKs are useful reference implementations for OAuth refresh, content
routes, path-root handling, pagination, upload sessions, typed errors, and
request construction, but the target integration does not need to reproduce an
SDK's internal abstractions.

For languages without an official SDK:

- use a mature OAuth 2.0 implementation;
- keep API RPC routes and content upload/download routes distinct;
- serialize Dropbox API arguments exactly as required by the HTTP reference;
- stream request and response bodies;
- represent tagged unions and endpoint errors in a way natural to the language;
- preserve server cursors, file IDs, revisions, and namespace IDs as opaque values.

## Mutation safety

- Never print or persist access tokens, refresh tokens, app secrets, or PKCE verifier values in logs.
- Do not broaden App Folder access to Full Dropbox unless required by the product intent.
- Do not retry ambiguous non-idempotent writes blindly after transport failure; inspect server state first.
- Use conflict/write modes intentionally instead of assuming overwrite semantics.
- Treat permanent deletion and team-folder permanent deletion as destructive operations requiring explicit intent.
- Bound parallel writes to the same namespace.
- Do not assume a path still refers to the same object after users move, rename, delete, mount, or unmount content.

## Reference map

- [current-api.md](references/current-api.md): verification date, source priority, freshness rules, and SDK research.
- [authentication.md](references/authentication.md): OAuth 2.0, PKCE, refresh tokens, scopes, App Folder, Full Dropbox, and secret handling.
- [endpoints.md](references/endpoints.md): endpoint-family catalog and common intent-to-endpoint mapping.
- [files-and-folders.md](references/files-and-folders.md): metadata, IDs, paths, revisions, CRUD, conflicts, and destructive operations.
- [transfers.md](references/transfers.md): upload/download streaming, upload sessions, chunking, integrity, and resumability.
- [changes-and-collections.md](references/changes-and-collections.md): list_folder cursors, continuation, incremental sync, pagination, and batching.
- [sharing.md](references/sharing.md): shared links, shared files/folders, members, policies, and mount state.
- [namespaces-and-teams.md](references/namespaces-and-teams.md): root/home namespaces, Path-Root, Select-User/Admin, team folders, and team space.
- [resilience.md](references/resilience.md): HTTP/error classification, Retry-After, backoff, namespace write concurrency, request IDs, and ambiguous writes.
