# agent-capabilities

[English](README.md) | [日本語](README.ja.md)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/yuru-sha/agent-capabilities)

Reusable Skills, specialist selectors, Profiles, and workflow capabilities
for AI coding agents.

This repository complements [OMP](https://omp.sh/) and
[oh-my-pstack](https://github.com/shrimpwtf/oh-my-pstack): OMP owns the
runtime, oh-my-pstack owns generic development workflow (TDD, architecture,
review, orchestration), and this repository owns specialist domain
capabilities that OMP + oh-my-pstack do not supply.

## Contents

- 171 language, database, OpenAPI, cross-cutting, infrastructure, and frontend engineering Skills
- 12 repository workflow Skills: pull requests (ready and draft), issue clarification, decomposition and implementation, issue creation, Copilot review, review-thread replies, GitHub releases, security alerts, and post-merge cleanup
- 1 reusable Orca Automation pipeline prompt for Issue-tree development
- 2 thin specialist selectors: `database-reviewer`, `infrastructure-reviewer`
- 13 composable Profiles, including `frontend.yaml`, `go.yaml`, `sqlite.yaml`, `infrastructure.yaml`, and `github.yaml`

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
ID. oh-my-pstack provides the review and TDD workflows.

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

For Terraform and AWS infrastructure work, select the infrastructure Profile.
It provides seven narrow Skills and the read-only `infrastructure-reviewer`
specialist selector; compose it with a language or database Profile when the
consumer repository needs those concerns too.

For frontend work, select the `frontend` Profile. It provides the
framework-agnostic web-quality, browser-testing, and form-validation Skills
plus React 19, Next.js, Svelte 5, and Tailwind CSS v4+ specialists.

## Install profiles into a project

Run the installer from the project that should use the capabilities, using an
absolute or relative path to this repository:

```sh
/path/to/agent-capabilities/scripts/install-profile rust sqlite workflows
```

Use `github` to select the GitHub operation Skills without the generic
commit/push Skill; these include both read and mutation workflows. `workflows`
selects the complete GitHub operations pack.

The command links the selected Skill directories into the project's
`.agents/skills/` and the selected specialist selectors into
`.codex/agents/`. The installer records ownership in
`.agents/agent-capabilities/manifest.json`, so selected profiles can be
removed later:

```sh
/path/to/agent-capabilities/scripts/install-profile \
  --target /path/to/project --uninstall rust sqlite workflows
```

Use `--target /path/to/project` when running it from elsewhere. Use `--copy`
for a self-contained copy, and `--force` to replace entries installed by an
earlier run. During uninstall, modified managed copies are kept unless
`--force` is specified. `--link` is also accepted as an explicit spelling of
the default. Legacy link-only installs without a manifest are also removed when
their links still point to this checkout; untracked copies are left in place.

## GitHub Release

See [docs/agents/release.md](docs/agents/release.md) for the release note format and creation procedure. The shared body template is [.github/release-notes-template.md](.github/release-notes-template.md), and the generated-note categories are managed in [.github/release.yml](.github/release.yml).