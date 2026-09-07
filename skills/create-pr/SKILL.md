---
name: create-pr
description: Create a GitHub pull request from the current implementation branch after explicit user authorization, with scoped diff checks, verification, commit/push, and post-creation status review.
---

# Create a pull request

Use this skill when the user explicitly asks to create, open, or submit a GitHub
pull request. A PR request authorizes the normal commit/push/PR workflow for the
current scoped changes; it does not authorize merging, force-pushing, deleting
branches/worktrees, or changing unrelated files.

1. Identify the repository, current worktree, branch, remote, and base branch.
   Check `git status --short --branch` and inspect both tracked and untracked
   changes. If unrelated changes cannot be separated confidently, stop before
   staging and ask.
2. Read the repository instructions and run its documented focused checks. Do
   not hide failures or claim checks passed when they were not run. When RTK is
   configured, prefix shell commands with `rtk`; use `rtk proxy` when RTK
   intercepts a command's arguments.
3. Stage only the intended files, inspect the staged diff, and create one
   concise commit. Never reset, checkout, amend, or force-push unless the user
   explicitly requests it. If the current branch is the default branch, make
   a descriptive feature branch before committing.
4. Push the feature branch to the intended remote with upstream tracking. Use
   `gh pr create` (or the repository's existing GitHub tooling), with the
   requested issue linked as `Closes #N` when an issue is known. Keep the title,
   body, and logs free of secrets and private session data.
5. Immediately re-fetch the PR URL, head/base, commit, changed files, CI/check
   state, and mergeability. Report pending or missing external checks as such;
   do not merge the PR.

If GitHub authentication, the remote, the target issue, or the intended scope
is genuinely unavailable, report the exact blocker and leave local changes
untouched. Do not create a second PR when an open PR already exists for the
same head branch unless the user asks for that explicitly.
