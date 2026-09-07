---
name: commit-push
description: Commit the current scoped changes and push the branch to its Git remote after explicit user authorization. Use when the user asks to commit, push, or commit and push without creating a pull request.
---

# Commit and push

Use this skill for a bounded commit-and-push operation. If the user also asks
for a pull request, use `create-pr` or `create-draft-pr` so the PR state is
verified separately.

1. Identify the repository, worktree, current branch, remote, and push target.
   Inspect `git status --short --branch`, tracked and untracked files, and the
   repository instructions. If the branch is the default/protected branch or
   the target is ambiguous, stop before mutating and ask.
2. Separate the requested changes from unrelated work. Run the repository's
   documented focused checks and follow its command-wrapper rules when present.
   Do not claim checks passed when they were not run.
3. Stage only the intended paths. Inspect `git diff --cached --stat`, the full
   staged diff, and `git diff --cached --check`. Keep secrets, credentials,
   generated artifacts, and unrelated edits out of the commit.
4. Create one concise commit with a message that describes the change. Do not
   reset, checkout, amend, squash, or force-push unless explicitly requested.
5. Push the exact branch with upstream tracking, for example:
   `git push -u <remote> <branch>`. Recheck the local status and remote branch,
   then report the commit, branch, remote, and verification results.

Do not create, edit, merge, or close a pull request as part of this skill.
