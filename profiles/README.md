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

The infrastructure Profile selects the Terraform and AWS infrastructure
specialists and the read-only infrastructure-reviewer Agent. It is intended
to compose with a language or database Profile rather than replacing one.

`external_skills` names existing global Skills such as `$tdd` and
`$code-review` and `$gh-fix-ci`; the profiles do not copy or redefine them.

## Project-local installation

From the project that should use the capabilities, run:

```sh
/path/to/agent-capabilities/scripts/install-profile rust sqlite workflows
```

The installer resolves the union of the selected profiles and links Skills into
`.agents/skills/` and Agents into `.codex/agents/` by default. It skips existing
entries; pass `--force` to replace them. Pass `--copy` for a self-contained
installation. Installation ownership is recorded in
`.agents/agent-capabilities/manifest.json`, which enables profile-specific
uninstallation:

```sh
/path/to/agent-capabilities/scripts/install-profile \
  --target /path/to/project --uninstall rust sqlite
```

Modified managed copies are kept by default; pass `--force` to remove them.
External Skills are printed as requirements and remain managed by the
consumer's global Skill installation. Legacy link-only installs without a
manifest are recognized when their links still point to this checkout.
