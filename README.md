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

- 171 language, database, OpenAPI, cross-cutting, infrastructure, and frontend engineering Skills
- 13 GitHub workflow Skills: pull request creation/review operations, issue clarification and decomposition, issue creation, Copilot review requests, review-thread replies, GitHub releases, security alerts, post-merge cleanup, and Orca Automation lock recovery
- 2 Orca Automation prompts: Issue-to-OMP handoff and manually run PR lifecycle
- 2 thin specialist selectors: `database-reviewer`, `infrastructure-reviewer`
- 13 composable Profiles, including `frontend.yaml`, `go.yaml`, `sqlite.yaml`, `infrastructure.yaml`, and `github.yaml`
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

For Terraform and AWS infrastructure work, select the infrastructure Profile.
It provides seven narrow Skills and the read-only `infrastructure-reviewer`
specialist selector; compose it with a language or database Profile when the
consumer repository needs those concerns too.

For frontend work, select the `frontend` Profile. It provides the
framework-agnostic web-quality, browser-testing, and form-validation Skills
plus React 19, Next.js, Svelte 5, and Tailwind CSS v4+ specialists.

## Install profiles

Run the installer from this repository checkout. It installs selected Skills
through GitHub CLI and copies selected OMP Agent definitions separately:

```sh
/path/to/agent-capabilities/scripts/install-profile rust sqlite workflows \
  --agent codex --scope project
```

`--agent` selects the host passed to `gh skill install`. `--scope` selects the
project or user installation scope. Project-scope Skills use the project's
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
