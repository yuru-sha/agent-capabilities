# Files and folders

verified_at: 2026-10-03

## Identity and references

Dropbox file arguments may support several reference forms depending on the
endpoint:

- relative path;
- file ID;
- revision ID;
- namespace-relative path.

Do not assume these are interchangeable on every endpoint. Confirm accepted
formats in the HTTP reference.

Use a file ID when stable identity must survive moves or renames. A path is a
location, not a permanent identity.

## Metadata

Preserve useful server metadata such as:

- id;
- name;
- path_lower and path_display when present;
- rev for file revisions;
- size;
- client/server modification timestamps;
- content_hash when present;
- sharing/member indicators when requested.

Treat tagged metadata variants explicitly; a folder and file do not have the
same fields.

## CRUD semantics

For create/copy/move/delete operations:

- validate the target namespace/root first;
- choose write/conflict behavior explicitly;
- do not assume a missing path means permanent nonexistence;
- expect users or other clients to move/delete content concurrently;
- read back metadata when the resulting identity or path matters.

Batch APIs can reduce round trips for many operations, but still require
per-entry result/error handling.

## Revisions

Use revisions when the product needs version-aware behavior, conflict
detection, restore, or audit-like workflows. Treat rev values as opaque.

Do not confuse revision identity with file identity.

## Deletion

Treat deletion as destructive. Dropbox may expose restore/revision behavior for
ordinary content, but do not promise recoverability without confirming the
account/endpoint behavior.

Team-folder permanent deletion is a stronger destructive operation and requires
explicit intent; see [namespaces-and-teams.md](namespaces-and-teams.md).

## Paths

- Preserve Unicode exactly as supplied/returned.
- Do not implement identity using case-sensitive path strings.
- Avoid manually constructing namespace-relative syntax without the current API definition.
- Expect mounted shared folders and team-space migration to change visible paths.
