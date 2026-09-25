---
name: implement-issue
description: Implement one already-scoped leaf GitHub issue in its own Issue-linked worktree using test-first vertical slices; use when requirements and acceptance criteria are clear and code changes are ready to begin.
---

# Implement a GitHub issue

Implement one bounded leaf Issue in a dedicated worktree associated only with that Issue. This Skill owns code and tests only. Use `clarify-issue` for unresolved requirements, `decompose-issue` for oversized or tracking-parent scope, and the issue-development pipeline plus its review/PR/CI Skills to deliver the change.

1. Re-fetch the exact Issue and verify its repository, open state, acceptance criteria, and leaf scope. If requirements are materially ambiguous, stop and route to `clarify-issue`. If the Issue is a parent, has unresolved children, or cannot fit one coherent change, stop and route to `decompose-issue`. Do not silently narrow scope.
2. Enforce a one-to-one mapping: one Issue or sub-issue has exactly one implementation worktree, and one worktree belongs to exactly one Issue or sub-issue. Reuse a worktree only after verifying its Issue association, branch, owner, base, and state, and that no other Issue uses it. Otherwise create a dedicated worktree and Issue-specific branch before inspecting implementation code or making code/test/generated-file changes. Use the repository's supported worktree mechanism; in Orca, create/link it with the Issue number and preserve the workflow-worktree parent. Never implement in the default/automation worktree, another Issue's worktree, or multiple worktrees for the same Issue. If the correct worktree cannot be created or verified, stop without code changes.
3. In the verified Issue worktree, read repository instructions, applicable specifications/decisions, relevant code/tests, toolchain, and test commands. Preserve existing user changes and keep edits within the agreed scope. Prepare a concise implementation plan covering expected behavior, affected public seams/files, test slices, risks, and required verification. Avoid unrelated dependencies, abstractions, configuration, migrations, and cleanup.
4. Follow the installed `$tdd` Skill and repository test conventions. For each slice, add a behavior-focused test at the relevant public seam, observe the expected failure, implement the minimum behavior, and observe the test pass before the next slice. Confirm a test seam with the user when its choice is itself unclear. Refactor after red/green slices while preserving passing behavior.
5. Update relevant documentation when the behavior or maintenance contract changes. Run targeted tests and a changed-path smoke scenario, then repository-required build/type/lint checks that apply. Classify failures before acting; fix implementation failures, but report unavailable environment, infrastructure, external-service, permission, or flaky checks without masking them.
6. Inspect the final diff in this Issue's worktree for acceptance-criteria coverage, regressions, secrets, generated/unrelated files, and scope drift. Leave commit, push, code review, Draft PR, CI repair, and merge decisions to their designated workflow Skills and the parent pipeline.

Report the implemented behavior, changed files, observed checks and smoke result, known limitations, and any acceptance criteria still unmet. Do not describe unrun checks as passing.
