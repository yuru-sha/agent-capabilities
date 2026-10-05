# Contributing

This repository distributes reusable Codex Skills, Agents, and composable
Profiles. Keep contributions focused, portable, and consistent with the
existing capability boundaries.

## Before contributing

- Check the existing README, catalogs, Profiles, and related capabilities first.
- Model a Skill as an independently selectable capability or domain. Put
  concern-level guidance that is useful only after selecting that capability
  under the parent Skill's `references/` directory.
- Keep engineering capabilities under `packs/software-engineering/` and GitHub
  operations under `packs/operations/github/`.
- Use oh-my-pstack for generic TDD and code-review workflows; do not copy or
  redefine those workflows here.
- Do not include secrets, credentials, or personal data.

## Skill granularity

Use this question as the default boundary test:

> Does the agent need to select this capability independently?

If yes, keep it as a Skill. If the material is detailed guidance that is
normally needed only after a broader capability or domain has already been
selected, make it a reference of that Skill.

Examples:

- Language domains such as Go, TypeScript, Python, and Rust are Skills;
  concurrency, error handling, API clients, testing, and serialization are
  references within the selected language Skill.
- Database engines such as PostgreSQL, MySQL, and SQLite are Skills; locking,
  indexes, migrations, transactions, performance, and backup/restore are
  references within the selected database Skill.
- OpenAPI is a Skill; design, linting, code generation, contract testing,
  compatibility, and versioning are references within the OpenAPI Skill.
- Frameworks, external APIs/integrations, security-review capabilities,
  browser testing, infrastructure domains, and operational workflows may
  remain separate Skills when they are useful to select on their own.

Keep the parent `SKILL.md` thin: define when the capability applies, its core
invariants, and how to route to the relevant references. Use progressive
disclosure rather than eagerly loading every reference.

Do not create compatibility alias Skills for a migrated concern unless a
demonstrated consumer requires the old independently selectable name. Aliases
reintroduce routing ambiguity and selection noise.

## Adding or changing capabilities

- Give every Skill a unique frontmatter `name` and a description that clearly
  states when it applies.
- Keep `SKILL.md`, Agent definitions, and Profile instructions in English so
  they remain portable across projects.
- Update the relevant README/catalog and Profile when adding or removing a
  capability. Update `docs/commands.md` when a capability introduces a
  concrete external CLI or changes a command family.
- Keep Profiles as distribution metadata; they are not another instruction
  layer.
- Prefer existing dependencies and repository conventions. Keep the diff
  small and avoid unrelated cleanup.

## Validation

From the repository root:

- Run `python3 scripts/validate` to validate Skill frontmatter, unique names,
  local references, Profile structure/resolution, and documented catalog counts.
- Run `python3 -m unittest discover -s tests` for installer and validation tests.
- Run `git diff --check`.
- Run any additional checks relevant to the files changed and report what was
  run in the pull request.

## Commit messages

Use [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) for commit messages. The format is:

```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Use these types as the default vocabulary:

- `feat`: add a new feature
- `fix`: fix a bug
- `refactor`: change code without changing behavior
- `docs`: change documentation
- `test`: add or change tests
- `chore`: make maintenance changes
- `ci`: change continuous integration configuration
- `build`: change the build system or dependencies
- `perf`: improve performance
- `revert`: revert a previous change

Use a scope when it adds useful context, for example `fix(forecast): handle missing observations`.
Mark a breaking change with `!` after the type or scope, or with a `BREAKING CHANGE:` footer.

## Pull requests

Open a focused pull request with:

- a short summary of the change and its motivation;
- the affected Skills, Agents, Profiles, or catalog entries; and
- the verification commands and their results.

Keep external mutations explicit and scoped. Do not merge a pull request,
delete branches, or change repository settings unless that work is explicitly
authorized.
