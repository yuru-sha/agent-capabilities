# Command reference

This document is a human-facing index of commands named by the bundled Skills
and used to maintain this repository. It is not an installation manifest or a
universal toolchain requirement. A consumer only needs the commands required by
the selected Profiles and the target repository.

## Bundled workflow commands

| Command | Used for | Availability |
|---|---|---|
| `git` | inspect, commit, push, branch, worktree, and remote-state operations | Required for repository workflows |
| `gh` | pull requests, issues, releases, Copilot review requests, and GitHub security APIs | Required for GitHub workflows |
| `rtk` | command output reduction and the configured shell wrapper | Optional; use when the environment provides it |
| `python3` + `quick_validate.py` | validate Skill frontmatter and descriptions | Maintainer check; provided by the local Skill Creator installation |

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
