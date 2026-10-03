# Sharing and collaboration

verified_at: 2026-10-03

Dropbox exposes multiple sharing models. Do not represent them as one generic
"share" operation.

## Shared links

Use shared links when access is URL-based. Relevant behavior includes:

- link visibility/audience;
- expiration;
- password or policy restrictions where supported;
- existing links and modification of their settings;
- parent-folder links that may affect visibility of nested content.

Create and modify link settings with the current sharing endpoints and verify
the effective permissions returned by Dropbox.

## Shared folders

A shared folder has membership and policy separate from shared links.

Model:

- folder membership;
- owner/editor/viewer or current access roles;
- invitation and notification behavior;
- policy governing who may invite/remove members;
- team restrictions;
- mount state.

Listing folder members and folder shares may require continuation cursors.

## Mounted versus unmounted folders

An invited shared folder may be unmounted and therefore absent from ordinary
`/files/list_folder` traversal at the expected mount point. Use sharing APIs
to discover mountable/unmounted shares when the product requires them.

Do not interpret "not present in list_folder" as proof that the user has no
share invitation.

## Shared files

Files may be explicitly shared with users/groups without creating a shared
folder or relying on a public/shared link. Use file-member endpoints and
distinguish explicit from inherited access when the response provides that
information.

## Team considerations

Shared-link ownership can be associated with the user who created the link.
Team-wide discovery may therefore require enumerating members and querying on
behalf of each relevant member using authorized team-selection headers.

Team folders/team space add namespace and admin-selection constraints. See
[namespaces-and-teams.md](namespaces-and-teams.md).

## Safety

- Do not silently broaden visibility.
- Preserve existing folder/team policy unless the request explicitly changes it.
- Before removing members or links, identify whether access is inherited or explicit.
- Verify resulting permissions after write operations where authorization is security-sensitive.
