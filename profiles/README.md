# Profiles

Profiles are composable distribution metadata. They select Skills and Agents;
they are not additional `SKILL.md` files and are not loaded as instructions.

For a Go project using SQLite, the consumer selects:

```yaml
profiles:
  - go
  - sqlite
```

The resolver takes the union of the selected Skill paths and de-duplicates
Agents by ID. `go+sqlite` is a generated bundle name, not a source Profile.

The `workflows` Profile contains every Skill in the
`packs/operations/github` pack: commit/push, ready and draft pull requests,
Copilot review requests, releases, security alerts, issue creation, and
post-merge cleanup.

The narrower `github` Profile selects the same pack except `commit-push`. It
declares the official global `$gh-fix-ci` Skill as an external dependency and
does not copy it.

The engineering Profiles select content from
`packs/software-engineering/skills/` and their Agent IDs resolve from
`packs/software-engineering/agents/`.

`external_skills` names existing global Skills such as `$tdd` and
`$code-review` and `$gh-fix-ci`; the profiles do not copy or redefine them.

## Project-local installation

From the project that should use the capabilities, run:

```sh
/path/to/agent-capabilities/scripts/install-profile rust sqlite workflows
```

The installer resolves the union of the selected profiles and copies Skills to
`.agents/skills/` and Agents to `.codex/agents/`. It skips existing entries by
default; pass `--force` to replace them. Pass `--link` to reference the
checkout instead of copying it. External Skills are printed as requirements and
remain managed by the consumer's global Skill installation.
