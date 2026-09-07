---
name: security-alerts
description: Inspect GitHub Dependabot, code scanning, and secret scanning alerts for a repository in read-only mode. Use for GitHub security findings and alert status, not source-code security review or alert remediation.
---

# GitHub security alerts

Use this skill to inventory and summarize GitHub security findings without
changing their state. Resolve one exact repository and preserve the distinction
between no alerts, a disabled feature, and insufficient permissions.

1. Resolve the repository and authenticated account. Check `gh auth status` and
   the repository's security feature availability before querying alerts.
2. List the requested alert classes with paginated GitHub API requests:
   `/repos/<owner>/<repo>/dependabot/alerts`,
   `/repos/<owner>/<repo>/code-scanning/alerts`, and
   `/repos/<owner>/<repo>/secret-scanning/alerts`. Filter by state only when the
   user requests a specific state; do not treat a 403 or 404 as an empty result.
3. Normalize results by alert class. Include state, severity or rule, package or
   tool, manifest or file/location metadata, created/updated timestamps, and the
   GitHub alert URL. Include fixed-version information for Dependabot when it is
   available.
4. Never request, print, store, or transmit literal secret values. If details
   or locations are needed for a secret alert, request masked metadata only and
   report the minimum necessary location.
5. Report per-class counts, permission or feature blockers, and high-priority
   findings. Re-fetch the summary when pagination or a transient API failure
   could make the count incomplete.

This skill is read-only. Do not dismiss, resolve, reopen, assign, enable, or
disable alerts or repository security features. Use a separate remediation
workflow after explicit approval.
