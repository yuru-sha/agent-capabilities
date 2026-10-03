# Namespaces and Dropbox teams

verified_at: 2026-10-03

## Core model

Keep these concepts separate:

- user/account identity;
- home namespace;
- root namespace;
- shared-folder namespace;
- team space;
- visible path within the selected root.

A path is interpreted relative to the API call root. The same textual path can
mean different content under a different namespace/root.

## Discovering root context

Call `/users/get_current_account` and inspect `root_info`.

Important fields include:

- `root_namespace_id`;
- `home_namespace_id`;
- team/root tag and home path when present.

For team-space accounts, root and home namespace IDs may differ.

## Dropbox-API-Path-Root

Use `Dropbox-API-Path-Root` to root file operations to the intended namespace.
This is important for code that must work across personal accounts, team-folder
models, and team-space models.

Without the correct Path-Root, team-space content may be invisible even though
the token has access to it.

Treat namespace IDs as opaque.

## Team-linked selection

With appropriate team authorization:

- `Dropbox-API-Select-User` performs authorized user API calls on behalf of a team member.
- `Dropbox-API-Select-Admin` performs authorized calls as a selected admin and
  is required for some team-managed sharing operations.

These headers select actor/context; they do not grant scopes the token lacks.

## Team organizational model

Do not assume every team uses the same model. Check current team/user feature
values to distinguish team-folder and team-space behavior.

A team using a shared team space may require ordinary files/sharing endpoints
rooted to the team namespace, whereas older/different configurations may use
team-folder management endpoints.

A migration from team folders to team space can change a member's root
namespace and visible paths while existing shared/team folder namespace IDs may
remain stable.

## Enumerating team content

For authorized administrative traversal, current Dropbox guidance describes
enumerating namespaces and then traversing the relevant namespaces with the
proper Select-Admin/Path-Root context.

Do not flatten content from multiple namespaces without retaining namespace
identity; paths alone are insufficient for collision-free global identity.

## Destructive team operations

Team-folder archive/permanent-delete operations have stronger consequences than
ordinary file deletion. Require explicit intent and confirm that the team's
current organizational model supports the endpoint before invoking it.
