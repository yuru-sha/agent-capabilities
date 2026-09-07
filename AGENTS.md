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

## Capability boundaries

- Keep specialist Skills narrow and model-selectable; do not add language,
  database, OpenAPI, or GitHub umbrella `SKILL.md` files.
- Profiles select Skills and Agents. They are distribution metadata, not another
  instruction layer.
- `$tdd`, `$code-review`, and `$gh-fix-ci` are external Skills. Do not copy or
  redefine them in this repository.
- `security-review` reviews code and trust boundaries. `security-alerts` reads
  GitHub security findings. Alert remediation is a separate mutation concern.
- `gh-fix-ci` diagnoses and fixes failed GitHub Actions after approval. A
  future CI-status Skill must remain read-only and must not duplicate that flow.
- `request-copilot-review` only requests or re-requests a Copilot review. It does
  not review findings, reply to threads, or merge a PR.

## Editing Skills and Profiles

- Read the Skill Creator and writing-for-agents guidance before creating or
  substantially changing a Skill or Agent document.
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
- Check that Skill names are unique and all Profile selectors resolve.
- Run `git diff --check` before committing.
- Do not claim checks passed unless they were actually run.

## Git and GitHub

- Preserve unrelated work and stage only files in the requested change.
- Do not merge a pull request, delete branches, or change repository settings
  unless the user explicitly requests that operation.
- Keep the official global `gh-fix-ci` Skill installed; this repository may
  declare it through `external_skills` but does not own its files.
