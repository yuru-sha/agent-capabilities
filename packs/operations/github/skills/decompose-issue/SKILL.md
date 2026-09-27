---
name: decompose-issue
description: Split an oversized GitHub issue into complete, independently deliverable sub-issues with verified parent links, acceptance criteria, and dependency order; use when a parent issue needs a tracked implementation plan.
---

# Decompose a GitHub issue

Use this Skill to turn an oversized Issue into a complete, trackable set of independently verifiable child Issues. It creates and links Issues only; it does not implement code, create PRs, or close the parent.

1. Resolve the exact repository and parent Issue. Fetch its title, body, state, comments, existing children (open and closed), task list, native dependencies, linked PRs, labels, and likely duplicate Issues. Confirm repository identity and `gh auth status`. Stop for a closed parent unless explicitly requested.
2. Read repository policy/specifications and inspect the affected code boundaries enough to estimate work and identify dependencies. If requirements or decomposition choices materially depend on an unresolved product decision, use `clarify-issue` and wait for the agreed Issue update before proceeding.
3. Plan the full requested scope as children small enough for one coherent implementation and independently testable Draft PR each. For every child define the objective, acceptance criteria, dependencies/blockers, and out-of-scope boundary. Preserve the entire parent scope; do not split off only easy work. Order children by dependencies, not by convenience.
4. Compare the plan against existing children and open PRs. Reuse matching children; do not create duplicates or rewrite completed children. Create only missing child Issues in the same repository with the planned fields, then attach them to the parent using GitHub's sub-issue API (`POST /repos/{owner}/{repo}/issues/{parent_number}/sub_issues` with `sub_issue_id`). Add `orca:ready` only when the repository's configured workflow uses that label.
5. Re-fetch the parent and every child. Verify child IDs, titles, acceptance criteria, dependencies, parent relationships, and the complete scope map. Keep the parent open and tracking-only. If any create/link operation cannot be verified, report the exact partial state and stop before implementation.

Report the ordered child Issue links, dependencies, reused children, remaining scope, and any blockers. Child implementation and per-child PRs belong to the configured Issue-development pipeline.
