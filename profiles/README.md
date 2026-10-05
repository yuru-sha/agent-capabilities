# Profiles

Profiles are composable distribution metadata. They select Skills and
specialist selectors; they are not additional `SKILL.md` files and are not
loaded as instructions.

For a Go project using SQLite, the consumer selects:

```yaml
profiles:
  - go
  - sqlite
```

The resolver takes the union of the selected Skill paths and de-duplicates
agents by ID. `go+sqlite` is a generated bundle name, not a source Profile.

The `workflows` Profile contains every Skill in the
`packs/operations/github` pack: ready and draft pull requests, Copilot
review requests, releases, security alerts, issue creation, clarification,
decomposition, post-merge cleanup, and Orca Automation lock recovery.

The `review-mode` Skill is included in both `github` and `workflows`. It uses the OMP `reviewer` role for an independent session and composes relevant specialists. Invoke oh-my-pstack `interrogate` only when the caller explicitly requests an adversarial panel. Report-only is the default; explicit caller policy is required for GitHub comments. Review never fixes the PR.

The `github` and `workflows` Profiles do not install an Issue implementation
Skill. The two Orca Automation prompts are
`packs/operations/github/automations/issue-omp-handoff.md` and
`issue-pr-lifecycle.md`. Configure them in Orca for the target repository and
provider. Schedule the Issue handoff Automation. Keep the PR lifecycle
Automation disabled; start it only from the Orca UI so Babysit and Shipping
require a manual run.
Use `scripts/sync-issue-automations --repo <repo-path> --enable-handoff` to
enable the scheduled handoff and keep lifecycle manual. Use
`--disable-automations` to disable both.

The `github` Profile selects the GitHub operation Skills without the removed
generic commit/push Skill. It includes both read and mutation workflows such as
creating PRs and issues, publishing releases, and security-alert operations.

The engineering Profiles select content from
`packs/software-engineering/skills/` and their agent IDs resolve from
`packs/software-engineering/agents/`. Most profiles select no generic agent;
specialist selectors (`database-reviewer`, `infrastructure-reviewer`) are
added only when the profile's domain touches those concerns.

The `redis` Profile installs the `redis` Skill for projects using Redis as
a cache, data structure server, coordination primitive, stream, or ephemeral
state store. It is language-independent. Compose it with the target language
Profile and with `bullmq` when BullMQ is also used:

```yaml
profiles:
  - typescript
  - redis
  - bullmq
```

The `bullmq` Profile installs the `bullmq` Skill for Redis-backed background
jobs. It owns BullMQ queue/worker semantics and does not duplicate general Redis
operations. Select `redis` separately when topology, persistence, memory, or
Redis security are in scope.

Cloud Profiles are provider-namespaced and map one-to-one to installed Cloud
Skills. Use the exact service Profile instead of selecting a broad AWS bundle.

Examples:

```yaml
profiles:
  - terraform
  - aws-vpc
  - aws-ecs
  - aws-ecr
  - aws-alb
  - aws-secrets-manager
```

```yaml
profiles:
  - gcp-bigquery
  - gcp-gcs
```

AWS Profile IDs use `aws-*`; Google Cloud Profile IDs use `gcp-*`.
The Profile ID, Skill directory basename, and Skill frontmatter `name` are
identical.

Representative AWS groups:

- compute/runtime: `aws-ec2`, `aws-ecs`, `aws-eks`, `aws-lambda`
- network/edge/API: `aws-vpc`, `aws-alb`, `aws-api-gateway`,
  `aws-cloudfront`, `aws-route53`, `aws-acm`, `aws-waf`
- identity/security/ops: `aws-iam`, `aws-kms`, `aws-secrets-manager`,
  `aws-cloudwatch`, `aws-github-actions-deploy`
- data: `aws-s3`, `aws-efs`, `aws-dynamodb`, `aws-rds`,
  `aws-elasticache`, `aws-opensearch`
- messaging/workflow: `aws-sqs`, `aws-sns`, `aws-eventbridge`,
  `aws-kinesis`, `aws-msk`, `aws-step-functions`
- analytics: `aws-glue`, `aws-athena`, `aws-emr`, `aws-redshift`
- registry: `aws-ecr`

Fargate is intentionally not a separate Profile. Select `aws-ecs` for ECS
Fargate or `aws-eks` for EKS Fargate. Cross-service AWS architecture is also
not a separate Skill/Profile; compose the concrete service Profiles in use.

The `terraform` Profile is provider-neutral and contains only Terraform
infrastructure and policy-testing Skills.

The `cross-cutting` Profile includes `technical-authoring` for document-type
structure, technical evidence, executable examples, verification, and
operational safety. Compose it with a language, database, OpenAPI, `terraform`, or provider-namespaced
Cloud Profile when both document design and domain-specific behavior are in scope. Language-specific documentation Skills remain focused on their
language's docstrings, examples, CLI help, and toolchain support.

The `note-com` Profile installs the `note-com-unofficial-api` Skill for
projects that interact with note.com's undocumented web APIs. Select it only
for note.com integrations; it does not add runtime code or authorize API
operations. The consuming project retains its own API and write boundaries.
Compose it with the project's language or database Profile as needed:

```yaml
profiles:
  - typescript
  - note-com
```

The `x-ads` Profile installs the `x-ads-api` Skill for projects that create,
manage, or report on X advertising. It is language-independent and requires
fresh official API verification before relying on endpoint, enum, metric, or
media behavior. Compose it with the target language Profile as needed:

```yaml
profiles:
  - go
  - x-ads
```

The `dropbox` Profile installs the `dropbox-api` Skill for projects that read,
write, synchronize, or share Dropbox content. It is language-independent and
requires current official API verification for scopes, transfer limits,
namespace/team-space behavior, and endpoint contracts. Compose it with the
target language Profile as needed:

```yaml
profiles:
  - python3
  - dropbox
```

The `youtube` Profile installs the `youtube-api` Skill for projects that
work with YouTube Data API v3, uploads, Analytics, Reporting, or Live Streaming.
It is language-independent and requires current official API verification for
scopes, quota behavior, resources, metrics/dimensions, upload protocol, and live
state transitions. Compose it with the target language Profile as needed:

```yaml
profiles:
  - go
  - youtube
```

The `meta-marketing` Profile installs the `meta-marketing-api` Skill for projects
that manage or report on Meta advertising. It is language-independent and
requires current official verification for Graph/Marketing API versions,
permissions and Marketing API Access Tier, campaign-delivery schemas, creative
and media behavior, Insights fields/breakdowns/attribution, and rate limits.
Compose it with the target language Profile as needed:

```yaml
profiles:
  - typescript
  - meta-marketing
```

The `smartnews-marketing` Profile installs the `smartnews-marketing-api` Skill
for projects that manage or report on SmartNews advertising. It is
language-independent and requires current official verification for Marketing
API versions, OAuth, Campaign/AdGroup/Ad schemas, media, targeting, Insights,
pagination, rate limits, and catalog allowlisting. Compose it with the target
language Profile as needed:

```yaml
profiles:
  - go
  - smartnews-marketing
```

The `tiktok-business` Profile installs the `tiktok-api-for-business` Skill
for projects that integrate with TikTok advertising and business APIs. It is
language-independent and requires current official verification for API
versions, advertiser authorization, Manual/Upgraded Smart+ schemas, identities
and Spark Ads, reporting dimensions/metrics, event/webhook contracts, and rate
limits. Compose it with the target language Profile as needed:

```yaml
profiles:
  - typescript
  - tiktok-business
```

The `google-ads` Profile installs the `google-ads-api` Skill for projects
that manage or report on Google advertising. It is language-independent and
requires current official verification for API versions, OAuth/developer-token
access, manager/customer context, GAQL field compatibility, mutation schemas,
batch-job support, quotas, and retry behavior. Compose it with the target
language Profile as needed:

```yaml
profiles:
  - go
  - google-ads
```

The `line-yahoo-ads` Profile installs the `line-yahoo-ads` Skill for projects
that traffic, review, launch, or report LINE Yahoo advertising. It is
language-independent and requires current official verification for product/UI
migration, Search Ads, Display Ads (Auction), Display Ads (Guaranteed), creative
and targeting rules, review/activation state, and report definitions. Compose it
with the target language Profile as needed:

```yaml
profiles:
  - typescript
  - line-yahoo-ads
```

The frontend Profile selects seven frontend Skills spanning framework-agnostic
web quality, browser testing, form validation, and framework/styling mechanics.
It composes with a language Profile and the TypeScript DOM, performance, or
security specialists where those concerns apply.
Profiles may declare `external_skills` requirements. The installer reports
those requirements but does not copy external Skills. The installed oh-my-pstack
review and TDD workflows are used directly.

## Provider namespaces

Cloud-provider-specific source Skills use a provider-first namespace:

- AWS: `packs/software-engineering/skills/cloud/aws/aws-*`
- Google Cloud: `packs/software-engineering/skills/cloud/gcp/gcp-*`

The provider prefix is part of both the installed Skill name and Profile ID.

## Installation

Run the installer from this repository checkout:

```sh
/path/to/agent-capabilities/scripts/install-profile rust sqlite workflows \
  --agent codex --scope project
```

The installer resolves the union of selected Profiles. It installs each
selected Skill with `gh skill install`, passing `--agent` as the host selector;
`omp` is translated to `universal`, the supported generic host. `--scope`
selects the project or user scope. OMP Agent definitions are copied separately
to `.omp/agents/` for project scope or `~/.omp/agent/agents/` for user scope.

By default, Skills come from `yuru-sha/agent-capabilities`. Add `--from-local`
to install Skills from the checkout for development. Profile metadata is
resolved from the checkout in either mode.

Use `--target /path/to/project` when installing into a project from elsewhere.
Existing OMP Agent definitions with matching contents are left unchanged;
different contents cause an error. The installer does not remove files or
manifests created by the legacy link-and-copy flow. Check those paths before
removing them manually.

If a later `gh skill install` fails, earlier successful Skill installations
remain. The installer copies OMP Agent definitions after all Skill installs
succeed.

Profiles may declare `external_skills` requirements. The installer reports
those requirements but does not install them. The installed oh-my-pstack
review and TDD workflows are used directly.


## Monorepos and Skill directory names

Profiles are additive. A monorepo may select multiple language, database, contract,
and frontend Profiles at the same time, for example:

```yaml
profiles:
  - go
  - typescript
  - postgresql
  - openapi
  - frontend
```

Every distributable Skill directory is globally namespaced and its directory
basename must exactly match the Skill frontmatter `name`. For example,
`languages/go/go-api-client/SKILL.md` declares `name: go-api-client`, while
`languages/typescript/typescript-api-client/SKILL.md` declares
`name: typescript-api-client`. This lets `gh skill install` place both Skills
under the same project scope without one replacing the other.

Consumers that installed older revisions may have stale unnamespaced directories
such as `.agents/skills/api-client/`, `.agents/skills/design/`, or
`.agents/skills/testing/`. Remove those stale generated Skill directories and
reinstall the selected Profiles so the namespaced directories are populated.
Do not remove project-owned Skills that were not installed from this repository.
