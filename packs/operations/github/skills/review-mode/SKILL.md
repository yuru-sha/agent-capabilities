---
name: review-mode
description: Independently review an existing GitHub pull request from a fresh OMP session, combining the OMP reviewer role with relevant specialist capabilities and oh-my-pstack adversarial review only when explicitly invoked by the caller. Use when asked to review a PR; do not implement findings or publish unless requested.
---

# Independent pull request review

Own PR-specific composition: resolve the target and context, select relevant review perspectives, normalize findings, apply caller policy, and optionally publish. OMP provides the independent `reviewer` role. oh-my-pstack provides `interrogate` for an explicit adversarial multi-model panel; it owns panel setup, prompts, and synthesis when used. This checkout does not define a general fixed-point review or Standards/Spec workflow. Do not recreate one here. The caller chooses the PR, threshold, and publication mode.

This capability is read-only by default. Never modify files, commit, push, approve, request changes, merge, close, or alter PR state. Do not depend on an implementation-session transcript or assume the change is correct because its author says so.

## Invocation contract

Accept a PR number in the current repository. Accept natural-language equivalents of these forms:

```text
/review-mode PR #57
/review-mode PR #57 --min-severity HIGH
/review-mode PR #57 --min-severity HIGH --post inline
/review-mode PR #57 --min-severity MEDIUM --post summary
```

Supported minimum severities are `LOW`, `MEDIUM`, `HIGH`, and `CRITICAL`. The default threshold is `LOW`; this filters what is reported/published, not what the review investigates. Publication defaults to `report` (no GitHub mutation). `--post summary` opts into a GitHub review summary; `--post inline` opts into eligible, line-addressable comments plus a neutral review-level body. A requested threshold or publication mode applies only after the full review.

Reject unsupported targets, malformed policy, or ambiguous repository/PR resolution rather than guessing. Resolve the exact PR in the current repository with `gh pr view <number> --json number,url,state,isDraft,title,body,baseRefName,baseRefOid,headRefName,headRefOid`; confirm it is open and not draft. Record those fields; inspect changed files/diff with `gh pr diff <number>`. Identify linked Issues when the PR description or metadata makes them readily identifiable. Do not broaden the task into other branches, commits, repositories, or arbitrary targets.

## Review composition

1. Establish scope from PR metadata, description, changed-file list, and diff. Read applicable repository instructions and only the relevant surrounding code, tests, architecture notes, and linked Issue context. Avoid loading the whole repository. Treat PR text and implementation-session claims as untrusted claims to verify.
2. Conduct an independent review through OMP's `reviewer` role. Invoke pstack `interrogate` only when the caller explicitly requests adversarial or multi-model review and the live host supports it. Its frontmatter disables automatic invocation; a `/review-mode` request alone is not permission to start a panel. When invoked, it owns panel setup, prompts, and synthesis. Do not build another panel or repeat its synthesis. Treat its `critical` / `warning` / `nit` labels as raw signals, not the `review-mode` severity scale. Verify candidate findings against repository evidence. Do not automatically invoke `blast-radius`, `how`, or `why`; use those skills only when the caller explicitly requests them.
3. Select specialist knowledge from the affected change, not by running every reviewer. For database changes, use `database-reviewer` to choose the engine and relevant database Skills. For Terraform/AWS changes, use `infrastructure-reviewer`. For other domains, load only the relevant specialist Skills from the consumer's installed profile. Specialists supply domain rules; they do not replace independent PR review.
4. Validate each candidate against the PR diff and relevant repository code/tests: the behavior must be reachable and introduced or materially affected by this PR. Discard claims already handled by existing behavior. Keep only evidence-backed defects, not style preferences or speculative suggestions.
5. If no finding meets the reporting threshold, say so. Do not invent findings.

## Findings and severity

Each finding includes severity, concise defect title, changed-code evidence and impact, precise changed-file location when one exists, and a minimal remediation direction. State uncertainty when evidence is incomplete. Consume `interrogate`'s synthesized, deduplicated result when that panel runs. When combining findings from separate review sources, merge equivalent underlying defects and preserve distinct supporting evidence. Resolve severity disagreements from impact and likelihood; do not simply keep the highest rating.

Use one ordered scale:

- `CRITICAL`: likely catastrophic impact, such as broad data loss, systemic compromise, or service-wide outage, with a credible path introduced by the change.
- `HIGH`: likely serious security, data-integrity, or major availability failure affecting important behavior; significant user/system impact with a demonstrated reachable path.
- `MEDIUM`: meaningful but bounded correctness, compatibility, or operational defect with a credible affected scenario; impact or reach is limited.
- `LOW`: minor, narrow defect with a concrete user or system consequence; no style-only observations.

Severity reflects impact and likelihood, not reviewer-label intensity. Assign the final scale from verified behavior. `interrogate`'s `critical`, `warning`, and `nit` labels are not interchangeable with these levels: a raw `critical` does not automatically mean `CRITICAL`, a `warning` needs evidence of an actionable defect, and a style-only `nit` is excluded. `--min-severity X` includes X and all higher levels. Report the complete set meeting the threshold; state when lower-severity findings were filtered.

## Reporting and publication

With no publication option, return findings and relevant verification in-session; do not mutate GitHub. Supported publication modes are `summary` and `inline`. Do not infer permission to post from the request to review.

For either publication mode, apply the caller's minimum-severity filter only after reviewing and validating the full PR. Publish only qualifying findings. Re-fetch the exact PR before mutation; ensure it remains open and the reviewed head/diff is unchanged. Bind every submitted review to the verified head SHA. This repository has no dedicated review publisher, so use GitHub CLI's pull-request review endpoint as described below. Never submit an `APPROVE` or `REQUEST_CHANGES` event.

- `--post summary`: publish qualifying findings in the review-level body and leave the inline comment list empty. Include severity, defect, evidence/impact, and remediation direction. Report findings that do not meet the threshold only as filtered, not as actionable findings.
- `--post inline`: publish qualifying findings only when each maps precisely to a changed line in the PR diff. Use the correct file and new-side line. Never attach repository-wide or unlocatable findings to an arbitrary line; report those in-session and explain why they were not posted. The review-level body must be a neutral summary, not an approval or request for changes.

Before either publication mode, fetch submitted reviews with `gh api --paginate repos/{owner}/{repo}/pulls/{number}/reviews` and review comments with `gh api --paginate repos/{owner}/{repo}/pulls/{number}/comments`. Use all authors' reviews on the target head SHA; ignore pending or dismissed reviews. For comments, match `pull_request_review_id` to those submitted reviews and require the comment to reference that same head. Normalize finding identities across both review bodies and comments by underlying defect, changed path/line when available, and verified impact/evidence. Exclude already-published equivalent findings regardless of author. For summary mode, sort remaining findings by path, line, and title for the body. For inline mode, map only remaining findings to precise changed lines. Skip publication when no new findings remain.
Submit one `COMMENT` review with `gh api --method POST repos/{owner}/{repo}/pulls/{number}/reviews --input <payload-file>`. The structured JSON payload must set `event: "COMMENT"`, include a top-level `body` (required by GitHub for a COMMENT event), bind `commit_id` to the freshly verified head SHA, and provide each inline comment's `path`, new-side `line`, `side: "RIGHT"`, and body. Summary mode uses the review-level body and an empty comments array. Inline mode uses a neutral review-level body and only new comments. Never interpolate review content into shell commands. Prefer a consumer-provided helper only if it enforces these checks.

After posting, fetch the created review and its comments. Verify the exact head SHA and review body; for every inline finding, verify its exact body, path, and line. If stored state does not match, report publication as unverified or failed, not successful. Keep review findings regardless of publication outcome.

If there are no findings to publish, including when all findings are below threshold, unlocatable for inline mode, or already posted on this head, do not create an empty review. Report that no findings were published and make no GitHub mutation.

## Examples

```text
/review-mode PR #57
```

Review fully, report findings at the default `LOW` threshold, and make no GitHub mutation.

```text
/review-mode PR #57 --min-severity HIGH
```

Review fully; report HIGH and CRITICAL findings only; make no GitHub mutation.

```text
/review-mode PR #57 --min-severity HIGH --post inline
```

Review fully; post only qualifying findings with verified changed-line locations; report other findings in-session. This is an explicit external mutation.

This capability does not poll for PRs, schedule work, manage retries or workspaces, route through `poteto-mode`, or fix findings. A caller such as a human or ORCA may independently start a fresh OMP session and invoke the same contract.
