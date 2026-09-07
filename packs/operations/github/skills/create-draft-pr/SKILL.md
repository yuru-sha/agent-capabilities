---
name: create-draft-pr
description: Create a GitHub pull request as a draft after explicit user authorization, with scoped diff checks, verification, commit/push, and post-creation status review. Use when the user asks for a draft PR.
---

# Create a draft pull request

Use this skill when the user explicitly asks to create or open a draft GitHub
pull request. A draft PR request authorizes the normal scoped
commit/push/creation workflow; it does not authorize marking the PR ready,
merging, force-pushing, deleting branches/worktrees, or changing unrelated
files.

1. Identify the repository, worktree, branch, remote, and base branch. Check
   `git status --short --branch` and inspect tracked and untracked changes. Do
   not create a second open PR for the same head branch.
2. Read repository instructions and run documented focused checks. Preserve
   failures and pending checks in the result instead of presenting them as
   successful.
3. Stage only intended files, inspect the staged diff, and create one concise
   commit when local changes need committing. Never reset, checkout, amend, or
   force-push unless explicitly requested.
4. Push the branch with upstream tracking, then use `gh pr create --draft`
   (or the repository's existing GitHub tooling). Include the requested issue
   link such as `Closes #N` when applicable. Keep title, body, and logs free of
   secrets and private session data.
5. Re-fetch the PR URL, head/base, commit, changed files, `isDraft`, CI/check
   state, and mergeability. Confirm that the PR remains a draft. Do not mark it
   ready or merge it.

If authentication, the remote, the target issue, or the intended scope is
unclear, report the exact blocker and leave local changes untouched.
