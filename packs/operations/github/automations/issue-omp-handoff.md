# ORCA to OMP Issue handoff

This Automation creates one parent Orca card for each run. It finds every eligible GitHub Issue, then creates one child Orca card and one isolated worktree for each Issue. OMP with oh-my-pstack owns implementation and opens the Issue's pull request stack from that child worktree. ORCA hands off the Issue and verifies every returned PR; it does not create PRs or run Babysit.

## Run flow

1. Start the run with its parent Orca card and parent branch.
2. In the configured target repository, fetch every page of open `orca:ready` items from GitHub in ascending creation order with `gh api --paginate 'repos/<owner>/<repo>/issues?state=open&labels=orca%3Aready&sort=created&direction=asc&per_page=100'`. `--paginate` must exhaust the result set; do not substitute `gh issue list`, impose an arbitrary limit, or stop after the first page. GitHub's Issues endpoint also returns pull requests, so exclude entries containing `pull_request` before treating results as Issues (for example, pipe the paginated JSON through `jq -s 'add | map(select(has("pull_request") | not))'`). Use the configured target repository's owner and repository in the endpoint.
3. If no eligible Issues exist, report that the run found none and finish without asking the user for an Issue number.
4. For each listed Issue, fetch it again immediately before claiming it. Skip it if it is closed or no longer has `orca:ready`. Otherwise, transition it to `orca:queued`, re-fetch it, and verify exactly one ORCA state label.
5. Create one child Orca card under the run's parent card for that Issue and provision a dedicated worktree for it. Keep each Issue's worktree and branch separate; never combine Issues in one child worktree. Use the repository's configured base and pull-request target.
6. Start OMP in that child worktree and send only this instruction, replacing the number:

   ```text
   /poteto-mode issue #<issue-number> を対応して
   ```

7. Set the Issue to `orca:running` only after OMP starts in the child worktree and accepts the instruction. If setup or handoff fails, mark that Issue `orca:failed` or `orca:human-escalation` as appropriate. Continue processing other eligible Issues unless the run itself cannot continue.
8. Wait for OMP to finish the Issue playbook and return all pull request URLs for the Issue, ordered bottom to top. The `opening-a-pr` playbook runs at the end of other playbooks and stops after opening the PR or stack.
9. Fetch every returned pull request. Verify each is open and ready for review, and that the full list forms the reported stack for this Issue's child worktree. Verify the stack's bottom PR targets the configured base, each higher PR targets the prior PR's head branch, and the bottom PR links to the Issue. Only then set the Issue to `orca:completed`. If OMP returns no PRs or any PR cannot be verified, use `orca:failed` for a definitive execution failure or `orca:human-escalation` when a decision is needed. Stop after this verification. Do not run Babysit, review PRs, merge, or enable merge-when-ready.
10. Finish the parent run only after every child has reached a terminal outcome. Report each Issue, child card, worktree, and every PR URL in stack order, or the failure/escalation reason. The parent run does not replace the per-Issue state labels.

Do not inspect unrelated repository files before listing Issues. The GitHub Issue remains the source of truth. Do not copy Issue bodies or generate separate implementation prompts.

## Issue state

Configure these labels in the target repository before enabling this Automation. This prompt does not create GitHub labels.

| Label | ORCA meaning |
|---|---|
| `orca:ready` | Eligible for this run to claim. |
| `orca:queued` | Claimed; child card and worktree are being prepared or OMP is starting. |
| `orca:running` | OMP accepted the handoff in the Issue's child worktree. |
| `orca:completed` | OMP returned a PR stack that ORCA verified as open, ready for review, and linked to this Issue's child worktree. |
| `orca:failed` | Execution failed without requiring a human decision. |
| `orca:human-escalation` | A human decision or intervention is needed. |

ORCA owns every transition. Before each transition, re-fetch the Issue and confirm its expected state and claim. Replace the old state label, then re-fetch and verify exactly one ORCA state label.

```text
ready → queued
queued → running
queued → failed
queued → human-escalation
running → completed
running → failed
running → human-escalation
failed → ready                 explicit retry only
human-escalation → ready       after the human resolves the blocker
```

`completed` is terminal. `failed` and `human-escalation` do not resume automatically. Re-entry requires an explicit ORCA or user decision to return the Issue to `ready`.

Do not add labels for investigation, planning, architecture, implementation, verification, review, fixes, PRs, or CI. Those are OMP and oh-my-pstack work, not ORCA execution states.
