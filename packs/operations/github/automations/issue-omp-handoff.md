# ORCA to OMP Issue handoff

ORCA creates a fresh worktree for each Automation run. Use that run worktree as the parent for all Issue worktrees; do not create an extra parent card or branch. After admission, this Automation finds every eligible GitHub Issue and processes them sequentially, with only one Issue active in OMP at a time. Runs must be mutually exclusive per configured target repository. Use ORCA's native repository-scoped concurrency control if available; otherwise, acquire the shared local filesystem lock described in step 1. This prevents overlapping runs from claiming or starting the same Issue. The filesystem lock works only for runs on the same machine with the same home directory. OMP with pstack owns implementation and opens the Issue's pull request stack from each child worktree. ORCA hands off each Issue and verifies its resulting PR stack.

Use the installed `show-me-your-work` Skill to initialize an append-only `decisions.tsv` in this Automation run worktree immediately after run provenance is verified and before attempting the lock. Log each lock attempt, Issue claim, phase transition, PR manifest, failure, and escalation with evidence.

Never set an Issue to `orca:failed` or `orca:human-escalation` without a verified GitHub Issue comment and a matching log row. First append the log row. Then post the comment with `gh issue comment --body-file` and re-fetch the Issue comments to verify it. Only after the comment is verified, remove any existing `orca:` state labels, add the intended state label, and re-fetch the Issue to verify exactly one `orca:` state label. The comment must include the Automation run ID, Issue number, phase, intended state label, exact blocker and last successful step, child card/worktree and terminal handle as applicable, PR URLs/heads if known, evidence pointer, and next safe human action or resume phase. If either record cannot be verified, stop processing Issues, append the verification error to `decisions.tsv`, retain the repository lock, and report the exact problem in the Automation run worktree. Never leave an Issue with only a failed or escalation label.

## Run flow

1. Before querying GitHub or creating any Issue child worktree, resolve the canonical target repository identity (`github.com/<owner>/<repo>`, with owner and repository normalized to lowercase). The Automation run worktree already exists before this prompt starts; use `orca worktree current --json` and `orca worktree show --worktree active --json` to verify its exact worktree ID, repository, `automationProvenance.automationId`, and `automationProvenance.automationRunId`. Stop if this is not the configured `issue-omp-handoff` Automation run for the target repository. Prefer ORCA's native repository-scoped concurrency control when available. Otherwise, create a lock directory under `$HOME/.omp/automations/issue-omp-handoff/`, using the lowercase repository identity with `/` replaced by `_` and `.lock` appended. For example, `github.com/yuru-sha/kumoumi-v5` maps to `$HOME/.omp/automations/issue-omp-handoff/github.com_yuru-sha_kumoumi-v5.lock`. Create the parent directory if needed, then use `mkdir <lock-directory>` as the atomic acquisition operation. Do not check for the directory before creating it. If `mkdir` fails because it already exists, or for any other reason, do not inspect or claim Issues, create child worktrees, or start OMP; report that the lock is held or unavailable. After `mkdir` succeeds, generate a unique `run_id` with `uuidgen`. Write an `owner.json` record containing `run_id`, `automation_run_id` from Orca provenance, `parent_worktree_id` from the current Automation worktree, `repository`, `automation_key` (`issue-omp-handoff`), UTC `acquired_at`, and `phase` (`locked`); write via a temporary file in the lock directory followed by rename, then read it back and verify every field. If generation, writing, or verification fails, leave the lock in place and escalate for human recovery. Update the current run worktree's comment to `Issue OMP handoff run_id=<run_id>`, then read back the worktree and verify the comment and Automation run ID. Atomically update `owner.json` via temporary file and rename to `phase` (`admitted`), then verify the owner record still matches the current worktree and Automation run. Do not inspect or claim Issues or create child worktrees until this correlation is verified. Keep the lock until every child Issue has a terminal outcome and the Automation run is finished; release it only if `owner.json` still identifies this `run_id`, `automation_run_id`, and `parent_worktree_id`, by removing that exact file and then removing the now-empty lock directory. If ownership cannot be verified or the lock cannot be released, stop claiming or handing off Issues and escalate to a human. If the run detects that it has lost the lock, immediately stop claiming or handing off Issues, escalate to a human, and ensure the repository's admission control continues refusing new runs. If OMP is active, confirm it has stopped before allowing any subsequent run for this repository. Never automatically steal an abandoned lock. If recovery is needed, leave the lock in place until a human confirms the Automation run and all its OMP processes have stopped, then authorize removal of this exact repository lock.
2. In the configured target repository, fetch every page of open `orca:ready` items from GitHub in ascending creation order with `gh api --paginate 'repos/<owner>/<repo>/issues?state=open&labels=orca%3Aready&sort=created&direction=asc&per_page=100'`. `--paginate` must exhaust the result set; do not substitute `gh issue list`, impose an arbitrary limit, or stop after the first page. GitHub's Issues endpoint also returns pull requests, so exclude entries containing `pull_request` before treating results as Issues (for example, pipe the paginated JSON through `jq -s 'add | map(select(has("pull_request") | not))'`). Use the configured target repository's owner and repository in the endpoint.
3. If no eligible Issues exist, report that the run found none and finish without asking the user for an Issue number.
4. Process the listed Issues in ascending creation order, one at a time. For each Issue, fetch it again immediately before claiming it. Skip it if it is closed or no longer has `orca:ready`. Otherwise, transition it to `orca:queued`, re-fetch it, and verify exactly one ORCA state label. Do not claim or start another Issue until this Issue reaches a terminal outcome.
5. Create one child Orca card under the Automation run worktree for each Issue and provision a dedicated worktree for it. Keep each Issue's worktree and branch separate; never combine Issues in one child worktree. Use the repository's configured base and pull-request target. Update the exact child worktree's comment to `Issue OMP handoff run_id=<run_id> automation_run_id=<automation_run_id> parent_worktree_id=<parent_worktree_id> issue=#<issue-number>` and re-fetch it to verify the worktree ID, comment, exact `parentWorktreeId`, and run correlation.
6. Start OMP in that child worktree and send only this instruction, replacing the number:

   ```text
   /poteto-mode issue #<issue-number> を対応して。必要なコミット、push、ready-for-review PR（必要ならPR stack）の作成まで明示的に許可します。マージは許可しません。
   ```

7. Set the Issue to `orca:running` only after OMP starts in the child worktree and accepts the instruction. If setup or handoff fails, mark that Issue `orca:failed` or `orca:human-escalation` as appropriate. Before moving to the next listed Issue, confirm this Issue reached `orca:pr-open`, `orca:failed`, or `orca:human-escalation`. If OMP started, do not move on until it has finished or ORCA has confirmed it stopped. Continue to the next Issue unless the run itself cannot continue; never run multiple OMP Issue handoffs concurrently.
8. The instruction in step 6 is the user's explicit authorization for OMP to complete the Issue work, including required commits, pushing branches, and creating ready-for-review PRs or PR stacks. Do not ask for PR authorization again. This does not authorize running Babysit or Shipping, enabling merge-when-ready, or merging any PR. Wait for OMP to finish the Issue playbook and return all pull request URLs for the Issue, ordered bottom to top. The `opening-a-pr` playbook runs at the end of other playbooks and stops after opening the PR or stack. The handoff succeeds only after ORCA verifies the complete PR stack; if PR creation or verification cannot be completed, report the blocker and set `orca:failed` or `orca:human-escalation` as appropriate.
9. Fetch every returned pull request. Verify each is open and ready for review, and that the full list forms the reported stack for this Issue's child worktree. Verify the stack's bottom PR targets the configured base, each higher PR targets the prior PR's head branch, and the bottom PR links to the Issue. Post an Issue comment with the exact marker `<!-- ORCA PR stack handoff_run_id=<run_id> automation_run_id=<automation_run_id> parent_worktree_id=<parent_worktree_id> -->`, followed by the heading `ORCA PR stack`, the Issue number, exact Issue worktree ID, and complete PR list bottom to top. For each PR include its number, URL, base branch, head branch, and current head SHA. Use `gh issue comment --body-file`, then re-fetch the comment and every PR; verify the comment, order, worktree, and SHAs match. Only then set the Issue to `orca:pr-open`. If OMP returns no PRs or any PR or manifest cannot be verified, use `orca:failed` for a definitive execution failure or `orca:human-escalation` when a decision is needed, and follow the required comment-and-log procedure. Stop after this handoff. Do not run Babysit, review PRs, merge, or enable merge-when-ready.
10. Finish the Automation run only after every child has reached a terminal outcome for this handoff: `orca:pr-open`, `orca:failed`, or `orca:human-escalation`. Report the Automation run worktree, each Issue, child card, worktree, and every PR URL bottom to top, or the failure/escalation reason. The Automation run worktree replaces a separate parent card and does not replace the per-Issue state labels.

Do not inspect unrelated repository files before listing Issues. The GitHub Issue remains the source of truth. Do not copy Issue bodies or generate separate implementation prompts.

## Issue state

Configure these labels in the target repository before using either Automation. These prompts do not create GitHub labels.

| Label | ORCA meaning |
|---|---|
| `orca:ready` | Eligible for this run to claim. |
| `orca:queued` | Claimed; child card and worktree are being prepared or OMP is starting. |
| `orca:running` | OMP accepted the handoff in the Issue's child worktree. |
| `orca:pr-open` | Handoff verified and recorded the complete PR stack; waiting for a manual PR lifecycle run. |
| `orca:babysitting` | The manual PR lifecycle run is driving this stack to merge-ready. |
| `orca:shipping` | Shipping is independently verifying and merging this stack. |
| `orca:completed` | Every PR in the Issue's stack is merged and verified. |
| `orca:failed` | Execution failed without requiring a human decision. |
| `orca:human-escalation` | A human decision or intervention is needed. |

ORCA owns every transition. Before each transition, re-fetch the Issue and confirm its expected state and claim. Replace the old state label, then re-fetch and verify exactly one ORCA state label.

```text
ready → queued
queued → running
queued → failed
queued → human-escalation
running → pr-open
running → failed
running → human-escalation
pr-open → babysitting
pr-open → human-escalation
babysitting → shipping
babysitting → failed
babysitting → human-escalation
shipping → completed
shipping → failed
shipping → human-escalation
failed → ready                  explicit Issue retry only
failed → pr-open                explicit PR lifecycle retry only
human-escalation → <safe phase> explicit human decision after resolving the blocker
```

`completed` is terminal. `failed` and `human-escalation` do not resume automatically. Re-entry requires an explicit decision to return the Issue to the phase appropriate to its remaining work.
Do not add labels for individual checks, review comments, fixes, or PR numbers. The lifecycle labels above record ORCA's coarse processing phase; CI and review details remain in GitHub and the PR stack manifest.
