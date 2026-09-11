# agent-capabilities

Reusable Skills, Agents, Profiles, and workflow capabilities for AI coding
agents.

## Contents

- 169 language, database, OpenAPI, cross-cutting, and infrastructure engineering Skills
- 9 repository workflow Skills: commit/push, pull requests, Copilot review,
  GitHub releases, security alerts, issues, and post-merge cleanup
- 8 reusable Agents
- 12 composable Profiles, including `go.yaml`, `sqlite.yaml`, `infrastructure.yaml`, and `github.yaml`

The capabilities are physically grouped into the
[`software-engineering` pack](packs/README.md) and the
`operations/github` pack. Profiles compose pack contents for each project.

## Compose Profiles

Profiles select both Skills and Agents. A consumer can combine them without
creating a language/database-specific aggregate Skill:

```yaml
profiles:
  - go
  - sqlite
```

The resolver takes the union of selected Skills and de-duplicates Agents by
ID. `$tdd`, `$code-review`, and `$gh-fix-ci` remain external global
dependencies and are not redefined here.

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
It provides seven narrow Skills and the read-only infrastructure-reviewer
Agent; compose it with a language or database Profile when the consumer
repository needs those concerns too.

## Install profiles into a project

Run the installer from the project that should use the capabilities, using an
absolute or relative path to this repository:

```sh
/path/to/agent-capabilities/scripts/install-profile rust sqlite workflows
```

Use `github` instead of `workflows` when `commit-push` is not needed.

The command links the selected Skill directories into the project's
`.agents/skills/` and the selected Agent definitions into `.codex/agents/`.
The installer records ownership in
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
the default. External Skills such as `$tdd` and `$code-review` are reported
but not copied. Legacy link-only installs without a manifest are also removed
when their links still point to this checkout; untracked copies are left in
place.
