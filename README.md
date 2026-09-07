# agent-capabilities

Reusable Skills, Agents, Profiles, and workflow capabilities for AI coding
agents.

## Contents

- 162 language, database, OpenAPI, and cross-cutting engineering Skills
- 2 repository workflow Skills: `create-pr` and `post-merge-cleanup`
- 7 reusable Agents
- composable Profiles such as `go.yaml` and `sqlite.yaml`

## Compose Profiles

Profiles select both Skills and Agents. A consumer can combine them without
creating a language/database-specific aggregate Skill:

```yaml
profiles:
  - go
  - sqlite
```

The resolver takes the union of selected Skills and de-duplicates Agents by
ID. `$tdd` and `$code-review` remain external global dependencies and are not
redefined here.

See [Profiles](profiles/README.md) and the
[software-engineering catalog](docs/software-engineering.md).
