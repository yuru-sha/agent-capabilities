# Profiles

Profiles are composable distribution metadata. They select Skills and
specialist selectors; they are not additional `SKILL.md` files and are not
loaded as instructions.

For a Go project using SQLite, the consumer selects:

```yaml
profiles:
  - go
  - sqlite
```

The resolver takes the union of the selected Skill paths and de-duplicates
agents by ID. `go+sqlite` is a generated bundle name, not a source Profile.

The `workflows` Profile contains every Skill in the
`packs/operations/github` pack: ready and draft pull requests, Copilot
review requests, releases, security alerts, issue creation, clarification,
decomposition and implementation, and post-merge cleanup.

The `github` and `workflows` Profiles install the `clarify-issue`,
`decompose-issue`, and `implement-issue` Skills. The separate Orca Automation
prompt at `packs/operations/github/automations/issue-development-pipeline.md`
is not selected by a Profile; configure it as an Orca Automation for a specific
repo, provider, and schedule.

The `github` Profile selects the GitHub operation Skills without the removed
generic commit/push Skill. It includes both read and mutation workflows such as
creating PRs and issues, publishing releases, and security-alert operations.
It declares the official global `$gh-fix-ci` Skill as an external dependency
and does not copy it.

The engineering Profiles select content from
`packs/software-engineering/skills/` and their agent IDs resolve from
`packs/software-engineering/agents/`. Most profiles select no generic agent;
specialist selectors (`database-reviewer`, `infrastructure-reviewer`) are
added only when the profile's domain touches those concerns.

The `cross-cutting` Profile includes `technical-authoring` for document-type
structure, technical evidence, executable examples, verification, and
operational safety. Compose it with a language, database, OpenAPI, or
infrastructure Profile when both document design and domain-specific behavior
are in scope. Language-specific documentation Skills remain focused on their
language's docstrings, examples, CLI help, and toolchain support.

The infrastructure Profile selects the Terraform and AWS infrastructure
specialists and the read-only `infrastructure-reviewer` specialist selector.
It is intended to compose with a language or database Profile rather than
replacing one.

The frontend Profile selects seven frontend Skills spanning framework-agnostic
web quality, browser testing, form validation, and framework/styling mechanics.
It composes with a language Profile and the TypeScript DOM, performance, or
security specialists where those concerns apply.

`external_skills` names external Skills such as `$gh-fix-ci`; the profiles do
not copy or redefine them. The installed oh-my-pstack review and TDD workflows
are used directly.

## Project-local installation

From the project that should use the capabilities, run:

```sh
/path/to/agent-capabilities/scripts/install-profile rust sqlite workflows
```

The installer resolves the union of the selected profiles and links Skills
into `.agents/skills/` and specialist selectors into `.codex/agents/` by
default. It skips existing entries; pass `--force` to replace them. Pass
`--copy` for a self-contained installation. Installation ownership is
recorded in `.agents/agent-capabilities/manifest.json`, which enables
profile-specific uninstallation:

```sh
/path/to/agent-capabilities/scripts/install-profile \
  --target /path/to/project --uninstall rust sqlite
```

Modified managed copies are kept by default; pass `--force` to remove them.
External Skills are printed as requirements and remain managed by the
consumer's global Skill installation. Legacy link-only installs without a
manifest are recognized when their links still point to this checkout.