---
name: create-issue
description: Create a scoped GitHub Issue after explicit user authorization, with duplicate and repository checks and post-creation verification. Use when the user asks to open or file an Issue.
---

# Create a GitHub issue

Use this skill to file one issue in the explicitly selected repository. Issue
creation is an external mutation; keep the content scoped and free of secrets
or private session data.

1. Resolve the target repository and inspect its instructions. Confirm the
   authenticated GitHub account and search for likely duplicates with
   `gh issue list --state all --search "<keywords>" --limit 20`.
2. Agree on a concise title and actionable body containing the observed
   behavior, expected behavior, reproduction or context, and acceptance
   criteria when applicable. Apply labels, assignees, milestones, or projects
   only when requested or specified by repository instructions.
3. Create the issue with `gh issue create` using the exact repository and
   approved content. Do not add comments, close issues, or modify project
   metadata as a side effect.
4. Re-fetch the created issue and verify its URL, number, repository, title,
   state, body, and requested metadata. Report the URL and any omitted optional
   fields.

If the repository, issue scope, or duplicate status is ambiguous, stop before
creating anything and report the blocker.
