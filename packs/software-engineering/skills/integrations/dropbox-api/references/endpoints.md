# Endpoint catalog

verified_at: 2026-10-03

This is an intent-oriented index, not a substitute for the current HTTP API
reference. Confirm the concrete request, scope, errors, and limits before use.

## Files and folders

- metadata: `/files/get_metadata`
- list folder: `/files/list_folder`
- continue listing / consume changes: `/files/list_folder/continue`
- create folder: `/files/create_folder_v2`
- copy: `/files/copy_v2`
- move/rename: `/files/move_v2`
- delete: `/files/delete_v2`
- restore revision: `/files/restore`
- list revisions: `/files/list_revisions`
- search: current `/files/search_v2` family
- batch copy/move/delete: use the current `*_batch*` families when suitable

## Content transfer

- simple upload: `/files/upload`
- download: `/files/download`
- upload-session start: `/files/upload_session/start`
- upload-session append: `/files/upload_session/append_v2`
- upload-session finish: `/files/upload_session/finish`
- batch finish: current `/files/upload_session/finish_batch*` family when appropriate

Use content-host semantics for upload/download routes and RPC-host semantics for
ordinary JSON endpoints, exactly as documented by the current HTTP reference.

## Sharing

- create shared link: `/sharing/create_shared_link_with_settings`
- modify shared link: `/sharing/modify_shared_link_settings`
- list shared links: `/sharing/list_shared_links`
- share folder: `/sharing/share_folder`
- add folder member: `/sharing/add_folder_member`
- list folder members: `/sharing/list_folder_members` plus continuation
- add file member: `/sharing/add_file_member`
- list file members: `/sharing/list_file_members` plus continuation
- list received files/folders: use the current list/continue families
- mount/unmount shared folder: `/sharing/mount_folder`, `/sharing/unmount_folder`

## Users and account context

- current account/root info: `/users/get_current_account`
- user feature values: `/users/features/get_values`

## Team and namespaces

- team features: `/team/features/get_values`
- team namespaces: `/team/namespaces/list` plus continuation as documented
- team members: `/team/members/list` plus continuation
- legacy/team-folder management: current `/team/team_folder/*` family where the team's model supports it

## Selection rule

Prefer:

1. the narrowest endpoint that satisfies intent;
2. batch endpoints for many independent operations when supported;
3. list/continue or cursor APIs instead of repeated full rescans;
4. upload sessions for large/resumable transfers;
5. IDs or namespace-relative references when path stability is not guaranteed.
