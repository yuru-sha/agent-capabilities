---
name: github-release
description: Create a GitHub Release as a draft or publish an existing draft after explicit user authorization. Use when release tags, release notes, assets, or publishing state are in scope.
---

# GitHub release

Use this skill for one explicitly requested release operation. Treat release
publishing as an external, potentially irreversible mutation and verify the
exact tag and target before changing state.

## Draft creation

1. Resolve the repository, release tag, target commit, title, notes, and assets.
   Inspect repository instructions, `git status --short --branch`, the tag
   object and commit, and `gh release list --limit 20`.
2. Reuse an existing tag by default. If the tag does not exist or its target is
   wrong, stop and ask whether the user wants tag creation or correction; never
   force-move a tag implicitly.
3. Confirm that no release already exists for the tag. Create the draft with
   `gh release create <tag> --draft --verify-tag` and the approved title,
   notes, and assets. Use generated notes only when the user requests them.
4. Re-fetch the release and verify its URL, tag, target commit, `isDraft`, notes,
   and assets. Report the draft URL without publishing it.

## Publish an existing draft

1. Resolve one exact draft release and inspect it with
   `gh release view <tag> --json name,tagName,targetCommitish,isDraft,isPrerelease,url,assets`.
   Stop if it is missing, already published, points to an unexpected commit, or
   its notes/assets are not approved.
2. Publish it with `gh release edit <tag> --draft=false`. Do not change
   prerelease/latest state unless separately requested.
3. Re-fetch the release and verify `isDraft` is false. Report the final URL and
   any tag or asset details that differ from the request.

Do not delete releases, replace tags, rewrite notes, upload unrequested assets,
or publish a release implicitly while creating a draft.
