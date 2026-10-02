# agent-capabilities

This repository distributes reusable Codex Skills, Agents, and composable
Profiles for software engineering and GitHub workflows.

## Language and documentation

- Communicate with the maintainer in Japanese unless another language is requested.
- Keep `SKILL.md`, Agent definitions, and Profile instruction text in English so
  they remain portable across projects and human languages.
- README and catalog documents may use Japanese when that is clearer for the
  intended maintainer.
- Preserve code identifiers, Skill IDs, command names, and API names exactly.

## Agent behavior

- Infer routine choices from the request and repository context; ask only when an unresolved choice could materially change the result, scope, or authority.
- Follow explicit user instructions over general Skill guidance, and report verification limits plainly.
- Keep responses concise, direct, and focused on the result.

## Capability boundaries

- Keep specialist Skills narrow and model-selectable; do not add language,
  database, OpenAPI, or GitHub umbrella `SKILL.md` files.
- Keep engineering capabilities under `packs/software-engineering/` and GitHub
  operation capabilities under `packs/operations/github/`. Add a Profile and
  catalog entry when introducing a new pack.
- Profiles select Skills and Agents. They are distribution metadata, not another
  instruction layer.
- `request-copilot-review` only requests or re-requests a Copilot review. It does
  not review findings, reply to threads, or merge a PR.
- `reply-to-review-thread` only replies to an existing PR review thread after
  resolving its GraphQL thread ID and verifying the stored reply. It does not
  create new review comments or resolve threads unless explicitly requested.

## Editing Skills and Profiles

- Follow the repository's structure, existing Skill examples, validation scripts,
  and Profile conventions when creating or substantially changing a Skill or
  Agent document.
- Give every Skill a unique frontmatter `name` and a discriminating
  `description` that states when it applies.
- Keep external mutations explicit, scoped, and followed by state verification.
- Do not expose secrets. In particular, never print literal values from secret
  scanning alerts.
- Update the README/catalog and relevant Profile when adding or removing a
  capability; do not create speculative placeholder Skills.
- Update `docs/commands.md` when a Skill introduces a concrete external CLI or
  changes a required command family; keep repository-specific scripts in the
  consumer repository.

## Validation

- Run `quick_validate.py` for every changed Skill directory.
- Check that Skill names are unique, Profile selectors resolve, and references
  point to existing capabilities.
- Run `git diff --check` before committing.
- Do not claim checks passed unless they were actually run.

## Branch And Pull Request Workflow

- Do not edit, commit, or push directly to `main`. Make changes on a feature branch and merge them through a pull request.
- Direct work on `main` is allowed only when the user explicitly authorizes it.

## GitHub workflow

- GitHub Issues are the canonical work tracker.
- Shared Bug / Feature / Question forms and the default Pull Request template are inherited from `yuru-sha/.github`.
- Shared non-default labels, including `orca:*`, are synchronized from `yuru-sha/project-template`.
- Use `orca:*` labels only for ORCA execution state; do not treat them as release categories.
- For release execution behavior, `packs/operations/github/skills/github-release/SKILL.md` is the source of truth.

## Commit Messages

- Follow the commit-message policy in [`CONTRIBUTING.md`](CONTRIBUTING.md#commit-messages).
- Do not create commits unless the user explicitly requests it.

## Git and GitHub

- Preserve unrelated work and stage only files in the requested change.
- Do not merge a pull request, delete branches, or change repository settings
  unless the user explicitly requests that operation.
