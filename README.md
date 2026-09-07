# agent-capabilities

Reusable Skills, Agents, Profiles, and workflow capabilities for AI coding
agents.

## Contents

- 162 language, database, OpenAPI, and cross-cutting engineering Skills
- 9 repository workflow Skills: commit/push, pull requests, Copilot review,
  GitHub releases, security alerts, issues, and post-merge cleanup
- 7 reusable Agents
- 11 composable Profiles, including `go.yaml`, `sqlite.yaml`, and `github.yaml`

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

## Install profiles into a project

Run the installer from the project that should use the capabilities, using an
absolute or relative path to this repository:

```sh
/path/to/agent-capabilities/scripts/install-profile rust sqlite workflows
```

Use `github` instead of `workflows` when `commit-push` is not needed.

The command links the selected Skill directories into the project's
`.agents/skills/` and the selected Agent definitions into `.codex/agents/`.
Use `--target /path/to/project` when running it from elsewhere. Use `--copy`
for a self-contained copy, and `--force` to replace entries installed by an
earlier run. `--link` is also accepted as an explicit spelling of the default.
External Skills such as `$tdd` and `$code-review` are reported but not copied.
