---
name: request-copilot-review
description: Request or re-request a GitHub Copilot code review for an existing pull request after explicit user authorization. Use when the user asks to send a PR to Copilot for review; do not use to create, review, fix, or merge the PR.
---

# Request a Copilot review

Use this skill for the reviewer-request operation only. It changes the review
requests on one existing PR and does not change commits or review content.

1. Resolve one exact PR from the supplied URL, number, or current branch. Use
   `gh pr view <pr> --json number,url,state,isDraft,headRefOid,reviewRequests`.
   Stop if the PR is missing, closed, or belongs to another repository.
2. Inspect existing review requests. If Copilot is already requested and the
   user did not ask for a re-request, report the existing state without sending
   a duplicate request.
3. Request or re-request Copilot with
   `gh pr edit <pr> --add-reviewer "@copilot"`.
4. Re-fetch the PR and verify that the Copilot review request is present. A
   review request is not evidence that the review has completed; report the
   pending state and any permission or platform limitation separately.

Do not approve, request changes, reply to review comments, resolve threads,
modify files, mark the PR ready, or merge it as part of this skill.
