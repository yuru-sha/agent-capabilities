# agent-capabilities

[English](README.md) | [日本語](README.ja.md)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/yuru-sha/agent-capabilities)

Reusable Skills, specialist selectors, Profiles, and workflow capabilities
for AI coding agents.

This repository complements [OMP](https://omp.sh/) and
[oh-my-pstack](https://github.com/shrimpwtf/oh-my-pstack): OMP owns the runtime
and independent reviewer role; oh-my-pstack supplies generic development
playbooks and `interrogate` for adversarial multi-model review when the caller explicitly invokes it. This
repository owns specialist knowledge and PR-specific review composition that
OMP + oh-my-pstack do not supply.

## Contents

- 33 language, database, OpenAPI, cross-cutting, infrastructure, frontend, and platform integration Skills
- 13 GitHub workflow Skills: pull request creation/review operations, issue clarification and decomposition, issue creation, Copilot review requests, review-thread replies, GitHub releases, security alerts, post-merge cleanup, and Orca Automation lock recovery
- 2 Orca Automation prompts: scheduled Issue-to-OMP handoff and manually run PR lifecycle
- 2 thin specialist selectors: `database-reviewer`, `infrastructure-reviewer`
- 24 composable Profiles spanning languages, databases, Terraform, frontend, integrations, cross-cutting guidance, and GitHub workflows
- 1 local verification Skill under `.agents/skills/verify-agent-capabilities/`

The capabilities are physically grouped into the
[`software-engineering` pack](packs/README.md) and the
`operations/github` pack. Profiles compose pack contents for each project.

## Compose Profiles

Profiles select Skills and specialist selectors. A consumer can combine
them without creating a language/database-specific aggregate Skill:

```yaml
profiles:
  - go
  - sqlite
```

The resolver takes the union of selected Skills and de-duplicates agents by
ID. `review-mode` composes the OMP reviewer role with relevant specialists,
caller policy, and optional GitHub publication. Use pstack `interrogate` only
when the caller explicitly requests an adversarial multi-model panel.

For a Rust + SQLite project that also needs the complete repository workflow:

```yaml
profiles:
  - rust
  - sqlite
  - workflows
```

See [Profiles](profiles/README.md) and the
[software-engineering catalog](docs/software-engineering.md). The command
families and external CLIs used by the Skills are listed in the
[command reference](docs/commands.md).

For Terraform work, select the `terraform` Profile. It installs only the
provider-neutral Terraform infrastructure and policy-testing Skills.

AWS, Google Cloud, and Azure provider knowledge is intentionally not vendored here.

- AWS: use the official [Agent Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws).
  It provides Codex/Claude/Cursor plugins, AWS-maintained Agent Skills, and the AWS MCP Server.
- Google Cloud: use Google's official [Agent Skills](https://github.com/google/skills).
  It includes BigQuery, Cloud Storage, GKE, IAM, Cloud Run, observability, and other Google Cloud skills.
- Azure: use Microsoft's official [Azure Agent Skills](https://github.com/MicrosoftDocs/agent-skills).
  It includes 193+ skills sourced from Microsoft Learn and supports Codex, Claude Code, Copilot, Cursor, and other Agent Skills hosts.

Install those provider Skills directly from their upstream repositories so cloud
guidance stays aligned with vendor-maintained documentation and evaluations.
This repository remains focused on provider-neutral engineering knowledge,
project workflows, and integrations not owned by those official repositories.

The `cross-cutting` Profile includes `web-security-review` for evidence-driven,
language-independent review of web applications and HTTP APIs. It maps attack
surfaces, traces data and authority boundaries, checks state transitions, and
requires bounded findings plus paired security/normal-path regression tests.
Use `security-review` alongside it only for broader cross-engine trust boundaries.

For projects that interact with note.com's undocumented web APIs, select the
`note-com` Profile. It adds note.com-specific API research and safety guidance;
the consuming project still owns implementation and authorization boundaries.

For projects that manage advertising through X Ads API, select the `x-ads`
Profile. It adds freshness-gated, language-independent guidance for campaign and
creative resource resolution, media handling, lifecycle diagnosis, and
analytics/reporting.

For projects that integrate with Dropbox, select the `dropbox` Profile. It adds
freshness-gated, language-independent guidance for OAuth, files and folders,
streaming/upload sessions, cursor-based change tracking, sharing, namespaces,
team spaces, and retry/concurrency behavior.

For projects that integrate with YouTube, select the `youtube` Profile. It adds
freshness-gated, language-independent guidance across Data API v3, uploads,
Analytics, Reporting, Live Streaming, authentication/channel identity, quota,
batching, and retry/error behavior.

For projects that integrate with Meta advertising, select the `meta-marketing`
Profile. It adds freshness-gated, language-independent guidance for Graph and
Marketing API versioning, Ad Account/Campaign/Ad Set/Ad resources, creative and
media handling, audiences/conversions/catalogs, Ads Insights, batching,
rate-limit handling, and safe mutation/reconciliation.

For projects that integrate with TikTok API for Business, select the `tiktok-business`
Profile. It adds freshness-gated, language-independent guidance across Marketing
API, Business Center, Accounts API, Events API, Manual and Upgraded Smart+
delivery, creatives/Spark Ads, audiences/catalogs, webhooks, and sync/async reporting.

For projects that integrate with Google Ads API, select the `google-ads`
Profile. It adds freshness-gated, language-independent guidance for OAuth and
developer-token account context, GAQL reads/reporting, resource mutations,
partial failure, BatchJobService, quotas, structured errors, and ambiguous-write
reconciliation.

For projects that traffic or report LINE Yahoo Ads, select the `line-yahoo-ads`
Profile. It adds freshness-gated operational guidance for Search Ads, Display Ads
(Auction), Display Ads (Guaranteed), review/activation safety, bulk operations,
and reproducible performance reporting across current and legacy naming.

## Install profiles

Run the installer from this repository checkout. It installs selected Skills
through GitHub CLI and copies selected OMP Agent definitions separately:

```sh
/path/to/agent-capabilities/scripts/install-profile rust sqlite workflows \
  --agent codex --scope project
```

`--agent` selects the host passed to `gh skill install`; `omp` is translated to
`universal` because `gh skill install` does not accept `omp`. `--scope` selects
the project or user installation scope. Project-scope Skills use the project's
host-specific Skill directory, and OMP Agent definitions go to
`.omp/agents/`. User-scope OMP Agent definitions go to
`~/.omp/agent/agents/`.

The installer reads Profile metadata from this checkout and installs Skills
from `yuru-sha/agent-capabilities`. For development, add `--from-local` to
install Skills from the checkout instead:

```sh
/path/to/agent-capabilities/scripts/install-profile rust sqlite \
  --agent codex --scope project --from-local
```

Use `--target /path/to/project` to select a project when running the installer
from elsewhere. User scope targets the current user's home directory for OMP
Agent definitions. Existing OMP Agent files with different contents cause an
error rather than being overwritten. Repeating an installation skips identical
Agent definitions.

If a later `gh skill install` fails, Skills installed by earlier calls remain.
The installer copies OMP Agent definitions only after all Skill installs
succeed.

The installer does not remove files or manifests created by the legacy
link-and-copy workflow. Clean those up manually after checking their contents.


## Local verification Skill

`.agents/skills/verify-agent-capabilities/SKILL.md` is a local verification Skill for this installer. It is not distributed through any Profile; consumers should not reference it from their own workflows.

## GitHub workflow

Shared Issue Forms and the default Pull Request template are inherited from `yuru-sha/.github`. Shared labels, including `orca:*`, are synchronized from `yuru-sha/project-template`.

For agent-driven GitHub Release operations, `packs/operations/github/skills/github-release/SKILL.md` is the source of truth. Repository release-note categories remain in `.github/release.yml`.
