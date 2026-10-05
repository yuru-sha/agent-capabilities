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

The `sqs` Profile installs the `sqs` Skill for Amazon SQS messaging. It owns
Standard/FIFO selection, visibility/idempotency, polling/batching, and DLQ
recovery. Compose it with `infrastructure` when broader AWS/IAM/Lambda/ECS or
Terraform concerns are in scope:

```yaml
profiles:
  - go
  - sqs
  - infrastructure
```

The `dynamodb` Profile installs the `dynamodb` Skill and the
`database-reviewer` selector for DynamoDB-backed applications. It owns
access-pattern-driven key/index design, conditional writes, transactions,
capacity/hot-partition behavior, Streams/TTL, global tables, and recovery.
Compose it with the target language and `infrastructure` Profiles as needed:

```yaml
profiles:
  - go
  - dynamodb
  - infrastructure
```

The `kinesis` Profile installs the `kinesis` Skill for Amazon Kinesis Data
Streams. It owns stream selection, partitioning/order, producer batching,
consumer checkpoints/replay, scaling/retention/backpressure, and Lambda stream
integration. Compose it with `dynamodb` when KCL lease-table behavior or a
DynamoDB sink is part of the design:

```yaml
profiles:
  - typescript
  - kinesis
  - dynamodb
  - infrastructure
```

The core AWS service Profiles are intentionally composable instead of bundled
into `infrastructure`:

- `vpc` — subnets, routes, egress, endpoints, security groups, DNS, and network capacity.
- `ec2` — instance/AMI/EBS/IMDS lifecycle and fleet operations.
- `ecs` — task definitions, services, deployments, capacity providers, IAM roles, and autoscaling.
- `ecr` — image identity, scanning, lifecycle, replication, and pull/push permissions.
- `alb` — listeners/rules/TLS, target groups, health checks, draining, and routing.
- `s3` — object transfer, versioning/lifecycle/replication, Object Lock, events, and access control.
- `rds` — RDS/Aurora topology, Multi-AZ, backups, replicas, failover, connectivity, and scaling.
- `secrets-manager` — secret access, caching, rotation, resource policies, and recovery.
- `kms` — key policies, IAM/grants, envelope encryption, rotation, and multi-Region keys.

A typical ECS service behind an ALB can compose, for example:

```yaml
profiles:
  - vpc
  - ecs
  - fargate
  - ecr
  - alb
  - secrets-manager
  - kms
  - infrastructure
```

The second-wave AWS service Profiles remain independently composable:

- `api-gateway` — REST/HTTP/WebSocket APIs, integrations, auth, throttling, deployment, and operations.
- `eventbridge` — event buses, patterns, targets, retries, DLQs, archives/replay, and Scheduler boundary.
- `sns` — topics, subscriptions, filters, Standard/FIFO fan-out, retries, and delivery recovery.
- `step-functions` — Standard/Express workflow orchestration, retries/catches, integrations, and Map concurrency.
- `cloudfront` — origins, cache/origin request policy, OAC, signed access, invalidation, and edge delivery.
- `route53` — public/private DNS, records/aliases, routing policy, health checks, Resolver, and failover.
- `acm` — certificate issuance, validation, renewal, export, Private CA, and service association.
- `waf` — web ACLs, managed/custom rules, rate controls, safe rollout, logging, and false-positive handling.
- `efs` — mount targets, access points, NFS/POSIX access, throughput/performance, lifecycle, backup, and operations.

The `eks` Profile installs the `eks` Skill and the
`infrastructure-reviewer` selector for Amazon EKS. It owns cluster/node
lifecycle, workload identity, AWS networking/ingress integration, autoscaling,
add-ons, upgrades, and EKS operational behavior. Compose it with `fargate`
when EKS Fargate profiles are part of the design:

```yaml
profiles:
  - eks
  - fargate
  - infrastructure
```

The `fargate` Profile installs the `fargate` Skill for the AWS Fargate
runtime model shared by ECS and EKS. It owns sizing/platform constraints,
workload networking, ephemeral storage, scaling, Spot interruption behavior,
cost, and runtime operations. Keep ECS/EKS orchestrator semantics in their own
service Skills.

The `bigquery` Profile installs the `bigquery` Skill for analytical data
workloads on Google BigQuery. It covers partitioning/clustering, SQL
performance and cost, ingestion/streaming/export, schema evolution, governance,
and fine-grained access controls.

The `gcs` Profile installs the `gcs` Skill for Google Cloud Storage. It
covers bucket/object semantics, resumable transfers, generation preconditions,
lifecycle/storage classes, versioning/retention, signed URLs, IAM, and
public-access prevention.

The `cross-cutting` Profile includes `technical-authoring` for document-type
structure, technical evidence, executable examples, verification, and
operational safety. Compose it with a language, database, OpenAPI, or
infrastructure Profile when both document design and domain-specific behavior
are in scope. Language-specific documentation Skills remain focused on their
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

The infrastructure Profile selects Terraform plus the AWS `aws-architecture`,
`iam`, `lambda`, `cloudwatch`, and GitHub Actions deployment specialists,
together with the read-only `infrastructure-reviewer` selector. Cross-service
architecture stays thin; service-specific behavior belongs to each AWS service
Skill. Compose the Profile with a language or database Profile rather than
replacing one.

Older installations may still contain the superseded Skill directories
`aws-infrastructure`, `aws-iam-oidc-security`, `nodejs-lambda`, and
`cloudwatch-operations`. Remove those generated directories before
reinstalling the infrastructure Profile; the replacements are
`aws-architecture`, `iam`, `lambda`, and `cloudwatch`. Node.js-specific
Lambda build/package guidance now lives under the TypeScript Skill.

The frontend Profile selects seven frontend Skills spanning framework-agnostic
web quality, browser testing, form validation, and framework/styling mechanics.
It composes with a language Profile and the TypeScript DOM, performance, or
security specialists where those concerns apply.
Profiles may declare `external_skills` requirements. The installer reports
those requirements but does not copy external Skills. The installed oh-my-pstack
review and TDD workflows are used directly.

## Provider namespaces

Cloud-provider-specific source Skills are grouped beneath provider namespaces
without changing Profile IDs or installed Skill names:

- AWS: `infrastructure/aws/`, `databases/aws/`, and `messaging/aws/`
- Google Cloud: `data-systems/gcp/`

This is a source-layout change only. Consumers should continue selecting
Profiles such as `dynamodb`, `sqs`, `kinesis`, `eks`, `fargate`,
`bigquery`, and `gcs` by the same IDs.

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
