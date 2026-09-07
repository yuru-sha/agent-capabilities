---
name: post-merge-cleanup
description: "Safely clean up the worktree, local branch, and remote branch for your PR after it is merged. Apply when the user asks to clean up a merged PR's development resources."
---

# Post-Merge Cleanup

Clean up only the specific worktree and branches associated with the merged PR. This is a destructive workflow: inspect first, preserve unrelated work, and stop when any safety precondition is unclear.

## Preconditions

- Inspect `git worktree list --porcelain`, `git status`, `git branch -vv`, and the relevant PR or task state before mutating anything.
- Resolve one exact worktree path, one exact local branch, and one exact remote branch. Do not use broad globs, `git worktree prune`, `git clean`, or bulk branch deletion.
- Confirm the PR is merged or otherwise confirm that the user explicitly authorizes deleting an unmerged task. A completed PR's merge commit remains in the base branch, but the topic branch itself may not be recoverable after deletion.
- Never remove the current worktree, the worktree containing the user's active changes, the default/base/protected branch, or a branch checked out by another worktree.
- If the target worktree has staged, unstaged, or untracked changes, stop and report the exact path and status. Never stash, reset, checkout, or discard changes as part of cleanup.
- If the target, completion state, remote, or ownership is ambiguous, ask for clarification instead of guessing.

## Safe cleanup sequence

1. Record the resolved target path, local branch, remote name, remote branch, and completion evidence. Also record the active worktree so it can be verified unchanged.
2. Re-check the target worktree status immediately before removal. It must be clean.
3. Remove only the resolved worktree path with `git worktree remove <absolute-path>`.
4. Delete the local topic branch with safe deletion (`git branch -d <branch>`). Do not use `-D` unless the user explicitly authorizes deleting an unmerged branch after the risk is explained.
5. Delete only the exact remote topic branch with `git push <remote> --delete <branch>`. Do not delete `main`, the default branch, or any protected branch. If GitHub rejects deletion, report the permission/protection blocker and leave it intact.
6. Verify with `git worktree list --porcelain`, `git branch --list`, and `git ls-remote --heads <remote> <branch>`. Confirm the active worktree and its uncommitted changes are unchanged.

The operations are intentionally ordered so an unsafe or dirty worktree blocks branch deletion. If a later operation fails, report which cleanup steps completed and which target remains; do not retry with a stronger destructive command automatically.

## GitHub and PR checks

Use the available GitHub connector or authenticated `gh` CLI to inspect the PR before deletion. Prefer the PR's exact head branch and repository over inferred names. A merged PR is sufficient completion evidence for normal cleanup. A closed-but-unmerged PR, a branch with commits not reachable from the base, or an unknown PR requires explicit user confirmation before deletion.

Do not change PR content, merge a PR, alter branch protection, or modify repository settings unless separately requested. Do not print tokens or credentials. If the GitHub plan or permissions prevent remote deletion, explain the blocker rather than attempting a workaround.

## Final handoff

Report:

- removed worktree path;
- deleted local and remote branch names;
- completion evidence and any surviving merge commit;
- verification result;
- any skipped or blocked cleanup.

Keep the result concise and state explicitly when nothing was deleted because a safety check failed.
