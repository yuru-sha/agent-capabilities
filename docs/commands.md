# Command reference

This document is a human-facing index of commands named by the bundled Skills
and used to maintain this repository. It is not an installation manifest or a
universal toolchain requirement. A consumer only needs the commands required by
the selected Profiles and the target repository.

## Bundled workflow commands

| Command | Used for | Availability |
|---|---|---|
| `git` | inspect, commit, push, branch, worktree, and remote-state operations | Required for repository workflows |
| `gh` | GitHub workflows and `gh skill install` for Profile Skills | Required for GitHub workflows and Profile installation |
| `jq` | filter paginated Issue results and read or update lock owner metadata | Required only when using either Orca Issue Automation |
| `orca` | Orca-managed worktrees, scheduled Issue handoff, manual PR lifecycle, and run-state inspection | Required only when using either Orca Issue Automation or recovering its shared lock |
| `uuidgen` | generate unique lock run IDs for Orca Issue Automations | Required only when using either Automation |
| `gt` | Graphite merge-when-ready flow used by pstack Shipping | Required only when using the manual PR lifecycle Automation |
| `python3` + `quick_validate.py` | validate Skill frontmatter and descriptions | Maintainer check; use the locally available validator |

The Profile installer requires Python 3 and GitHub CLI with `gh skill install`
support. Run it from this repository checkout:

```sh
/path/to/agent-capabilities/scripts/install-profile rust sqlite workflows \
  --agent codex --scope project
```

`--agent` selects the host passed to `gh skill install`. `--scope` selects
`project` or `user`. OMP Agent definitions are copied separately to
`.omp/agents/` for project scope or `~/.omp/agent/agents/` for user scope.
Add `--from-local` to install Skills from the checkout instead of the published
`yuru-sha/agent-capabilities` repository. Use `--target /path/to/project` to
select a project when running the installer from elsewhere.

If a later `gh skill install` fails, earlier successful Skill installations
remain. OMP Agent definitions are copied after all Skill installs succeed.

Structured external Skills declared by Profiles are installed for project scope
through their upstream installer. Legacy scalar entries and user-scope external
dependencies are reported without automatic installation. Legacy link-and-copy installs and their manifests are not modified;
inspect their recorded paths before removing them manually.

The workflow Skills contain the exact operation-specific forms, including
`git status`, `git diff --check`, `git push`, `gh pr`, `gh issue`, `gh release`,
`gh api`, and `gh auth status`. Follow the target repository's instructions
and authentication state before running them.

## Language and runtime command families

Language Skills are intentionally toolchain-aware but toolchain-agnostic. They
use the target repository's existing scripts, wrappers, versions, and CI
commands rather than requiring one package manager or test framework.

| Profile | Representative commands | Typical concerns |
|---|---|---|
| `go` | `go test`, `go run`, `gofmt`, `go vet`, `go generate`, `go tool` | tests, race checks, formatting, generation, profiling |
| `typescript` | `node`, the repository's package manager (`npm`, `pnpm`, `yarn`, or `bun`), `tsc` | runtime, build, type checking, linting, tests |
| `python3` | `python3`, the repository's environment tool (`uv` or `pip`), `pytest`, `ruff`, `mypy`, or `pyright` | tests, formatting, linting, and static typing |
| `rust` | `cargo`, `rustc`, `cargo fmt`, `cargo clippy`, and `cargo miri` when configured | build, tests, formatting, lints, MSRV, and unsafe-code checks |

The representative commands are examples, not additional requirements. A
repository's `Makefile`, task runner, package scripts, CI configuration, and
toolchain files remain the source of truth.

## Infrastructure command families

Infrastructure Skills use the consumer repository's configured versions and
wrappers. Common command families include:

| Profile | Representative commands | Typical concerns |
|---|---|---|
| `terraform` | `terraform`, `tflint`, `tfsec`, Trivy, Checkov | module validation, provider locks, plans, policy tests, and provider-neutral infrastructure review |

These commands are review and verification inputs, not automatic permission to
run Terraform apply/destroy, mutate remote state, or change external systems.
Record exact versions and repository-specific commands in the consumer
repository when they affect evidence.

## External cloud skills

Cloud-provider service Skills are installed from their official upstream
repositories rather than from this repository.

AWS:

```sh
npx skills add aws/agent-toolkit-for-aws/skills
```

For Codex, the AWS Agent Toolkit also supports the official plugin marketplace:

```sh
codex plugin marketplace add aws/agent-toolkit-for-aws
```

Google Cloud:

```sh
npx skills add google/skills
```

For Codex, Google also provides its plugin marketplace:

```sh
codex plugin marketplace add google/skills
```

Azure:

```sh
codex plugin marketplace add MicrosoftDocs/agent-skills
```

Then install **azure-agent-skills** from the Codex `/plugins` browser.

Use each vendor's current upstream installation guidance as the source of truth.

## External platform skills

Convex:

```sh
# Choose individual official Skills interactively.
npx skills add get-convex/agent-skills

# Or install the complete official collection.
npx skills add get-convex/agent-skills --all
```

For Codex, Convex also provides an official plugin that bundles Skills,
specialist agents, MCP access, and runtime diagnostics:

```sh
codex plugin marketplace add get-convex/convex-codex-plugin
codex plugin add convex@convex-codex-plugin
```

The `convex` Profile declares `get-convex/agent-skills` with `skills: all`.
For project scope, `install-profile` runs the official `npx skills add ... --all`
flow in the target repository. User-scope installs remain explicit because the
upstream CLI's project-local behavior should not be silently changed.

## Database command families

Database Skills describe engine behavior and review evidence. They do not force
a client or migration framework. Use the target repository's configured
connection, migration, backup, and plan-inspection commands.

| Profile | Common command family | Examples of evidence |
|---|---|---|
| `postgresql` | `psql` and the repository's PostgreSQL tooling | `EXPLAIN`, transaction behavior, locks, roles, RLS, backups |
| `mysql` | `mysql` and the repository's MySQL tooling | `EXPLAIN`, InnoDB locks, SQL modes, online DDL, replication |
| `sqlite` | `sqlite3` or the application's database wrapper | `EXPLAIN QUERY PLAN`, `PRAGMA`, WAL, integrity, migrations |

## OpenAPI and cross-cutting tools

OpenAPI Skills do not mandate a particular vendor CLI. Select the repository's
lint, specification-diff, code-generation, mock, documentation, and contract
testing commands, then record the exact command and tool version in review or
release evidence when the result is material.

The same rule applies to security scanners, benchmark runners, profilers,
formatters, linters, and package-release tools: use configured repository
commands and do not infer a clean result from an unrun tool.

## Updating this reference

Add a command here when a bundled Skill introduces a concrete external CLI or
changes a required command family. Keep repository-specific scripts and exact
versions in the consumer repository rather than expanding this file into a
second build manifest.
