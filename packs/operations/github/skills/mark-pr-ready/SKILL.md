---
name: mark-pr-ready
description: Convert an existing open GitHub draft pull request to ready for review after explicit user authorization. Use when the user asks to mark a draft PR ready; do not use to create or merge a PR.
---

# Mark a pull request ready

Use this skill only for an existing draft PR. This operation changes the PR's
review state and removes a leading `Draft: ` title marker when present; it does
not change repository files, merge the PR, push commits, or edit its body.

1. Resolve one exact PR from the supplied URL, number, or current branch. Use
   `gh pr view <pr> --json number,url,state,isDraft,title,headRefName,baseRefName,headRepository`.
   Stop if the PR is missing, closed, already ready, or the branch/repository
   does not match the user's target.
2. Inspect the current head commit, changed-files summary, and check state. A
   pending or missing check is evidence to report, not evidence of success.
3. Before running `gh pr ready <pr>`, if the title begins with `Draft: `, remove
   exactly that prefix with `gh pr edit <pr> --title "<title without prefix>"`
   and re-fetch the title to verify the edit. Run `gh pr ready <pr>` only after
   the exact open draft PR and any required title edit are confirmed.
4. Re-fetch the PR and verify `state` is open, `isDraft` is false, and the title
   no longer begins with `Draft: `. Report the URL and any pending or failed
   checks.

Do not merge, close, force-push, delete branches, or silently fix unrelated
failures as part of this skill.
