# agent-capabilities

Reusable Skills, Agents, Profiles, and workflow capabilities for AI coding
agents.

## Contents

- 162 language, database, OpenAPI, and cross-cutting engineering Skills
- 9 repository workflow Skills: commit/push, pull requests, Copilot review,
  GitHub releases, security alerts, issues, and post-merge cleanup
- 7 reusable Agents
- 11 composable Profiles, including `go.yaml`, `sqlite.yaml`, and `github.yaml`

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

See [Profiles](profiles/README.md) and the
[software-engineering catalog](docs/software-engineering.md). The command
families and external CLIs used by the Skills are listed in the
[command reference](docs/commands.md).
