# ORCA to OMP Issue handoff

This Orca Automation defines the boundary between ORCA's Issue execution state and OMP. ORCA selects the Issue, provisions the worktree, launches OMP in that worktree, and records coarse execution outcomes. OMP with oh-my-pstack owns the software-development lifecycle.

## Issue state

Keep one ORCA state label on the selected Issue:

The current `yuru-sha/agent-capabilities` GitHub repository has no `orca:` labels. Configure the labels used by this contract in the target repository before enabling its automation. This prompt does not create GitHub labels.

| Label | ORCA meaning |
|---|---|
| `orca:ready` | Eligible for ORCA to select. |
| `orca:queued` | ORCA claimed the Issue and is preparing its worktree or starting OMP. |
| `orca:running` | ORCA delivered the Issue handoff to OMP and execution is in progress. |
| `orca:completed` | OMP reported successful completion. |
| `orca:failed` | ORCA or OMP execution failed without requiring a human decision. |
| `orca:human-escalation` | Execution needs a human decision or intervention. |

ORCA owns every transition. Before a transition, re-fetch the Issue and confirm its expected state and claim. Replace the old state label, then re-fetch and verify exactly one ORCA state label.

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

Set `running` only after OMP has started in the prepared worktree and accepted the handoff instruction. If worktree setup, launch, or prompt delivery cannot be verified, do not claim `running`; use `failed` when execution definitively failed, or `human-escalation` when a decision or intervention is needed. `completed` is terminal. `failed` and `human-escalation` do not resume automatically. Re-entry requires an explicit ORCA or user decision to return the Issue to `ready`.

Do not add labels for investigation, planning, architecture, TDD, implementation, verification, review, fixes, PRs, or CI. Those are OMP and oh-my-pstack work, not ORCA execution states.

## OMP handoff

ORCA selects and claims the Issue, prepares or selects its worktree, sets that worktree as OMP's current working directory, and launches OMP there. OMP treats its current repository/worktree as the supplied workspace. Do not create another worktree from pstack by default.

Send OMP only this instruction, substituting the selected Issue number:

```text
/poteto-mode issue #<issue-number> を対応して
```

The GitHub Issue remains the source of truth. Do not copy its body or generate a separate requirements, plan, implementation, test, review, PR, or CI prompt.
