# Software Engineering Skill Set design

## Goal

Provide installable, automatically selectable specialist Skills for Go,
TypeScript, Python 3, Rust, PostgreSQL, MySQL, SQLite, and OpenAPI. The skill
boundary
is the smallest named engineering concern from the requested catalog.

## Non-duplication boundaries

- `$tdd` owns red-green-refactor, seam selection, and test anti-patterns.
- `$code-review` owns fixed-point diff review and the Standards/Spec split.
- `$gh-fix-ci` owns GitHub Actions failure diagnosis and approved remediation.
- Language specialists own language mechanics for one concern.
- Database specialists own one engine and one database concern.
- OpenAPI specialists own one contract concern.
- Cross-cutting specialists own security, operational quality, or review lenses.

There are no language, database, or OpenAPI umbrella `SKILL.md` files. A broad
router would compete with the specialist descriptions and duplicate their
content. README and this document are the human-facing catalog instead.

## P0 package shape

| Area | Count | Examples |
|---|---:|---|
| Language | 98 | `go-testing`, `go-goroutine-leak-deadlock-check`, `python3-type-checking`, `rust-unsafe-audit` |
| Database | 42 | `postgresql-roles-rls`, `mysql-online-ddl`, `sqlite-wal-checkpoint` |
| OpenAPI | 13 | `openapi-lint`, `openapi-codegen`, `openapi-breaking-change-detection` |
| Cross-cutting | 9 | `change-review`, `benchmark-regression`, `zero-downtime-migration` |
| **Total** | **162** | specialist Skills |

Each specialist has a required `SKILL.md` with a discriminating description.
The three original cross-cutting adapter Skills retain their existing
`agents/openai.yaml`; specialist UI metadata for the additional Skills is
intentionally omitted until a concrete install/catalog surface needs it.

The repository also ships nine workflow Skills: `commit-push`, `create-pr`,
`create-draft-pr`, `mark-pr-ready`, `request-copilot-review`, `github-release`,
`create-issue`, `security-alerts`, and `post-merge-cleanup`. They are selected
through `profiles/workflows.yaml` and are separate from the 162 language,
database, OpenAPI, and cross-cutting specialists.

## Profiles and composition

Profiles are distribution metadata, not additional Skills. `profiles/go.yaml`
selects `languages/go/**` and its Agent set; `profiles/sqlite.yaml` selects
`databases/sqlite/**` and its database-review Agent set. A consumer composes
them by ID:

```yaml
profiles:
  - go
  - sqlite
```

The resolver unions selected Skills and de-duplicates Agents by ID. A generated
`go+sqlite` bundle is an output artifact, not a new aggregate Skill.

Workflow consumers can select `workflows` for the complete local/GitHub
lifecycle. Consumers that need only remote GitHub operations can select
`github`, which declares `$gh-fix-ci` as an external Skill.

## Capability map

### Language: 19 common concerns × 4 languages, plus 22 language-specific skills

`testing`, `error-handling`, `concurrency`, `performance`, `api-client`,
`dependencies`, `security`, `refactoring`, `logging`, `observability`,
`database-review`, `cli`, `documentation`, `configuration`,
`resource-management`, `serialization`, `networking`, `data-race-check`,
`idiomatic-code-check`.

Each language keeps its own rules. Examples include Go table-driven tests and
`t.Run`, Go race-enabled commands and JSON tag generation, TypeScript `unknown`
catches and `AbortSignal`, Python context managers and asyncio, and Rust
`Result`, ownership, `Send`/`Sync`, and RAII.

Go additionally has `go-struct-json-tags` for deterministic Go struct and
`json`-tag generation from JSON examples, JSON Schema, or API payloads.

Language-specific additions are intentionally separate review triggers:

- Go: `go-goroutine-leak-deadlock-check`, `go-fuzzing`, `go-http-server`,
  `go-code-generation`, `go-api-compatibility`, and `go-struct-json-tags`.
  The leak/deadlock skill covers liveness, ownership, shutdown, channel
  progress, `WaitGroup`, and lock ordering; it is not a second race detector.
- TypeScript: `typescript-type-design`, `typescript-module-build`,
  `typescript-runtime-validation`, `typescript-package-publishing`, and
  `typescript-dom-accessibility`.
- Python 3: `python3-type-checking`, `python3-packaging`,
  `python3-subprocess`, `python3-data-modeling`, and `python3-web-server`.
  Type checking explicitly reviews `Any` contagion, boundary typing,
  `cast`/ignore use, and the separation between static and runtime checks.
- Rust: `rust-unsafe-audit`, `rust-ffi-abi`, `rust-api-compatibility`,
  `rust-msrv`, `rust-features-workspaces`, and `rust-async-runtime`.

### Database: 8 common concerns × 3 engines, plus 6 engine-specific concerns each

`design`, `sql`, `indexes`, `transactions`, `locking`, `migrations`,
`performance`, `review`.

PostgreSQL covers isolation, lock types, query plans, grants, and expand/contract
migrations. Its additional specialists cover roles/RLS, backup/restore,
vacuum/maintenance, partitioning, replication/HA, and query-plan regression.
MySQL covers InnoDB transaction and locking behavior, SQL modes, charset and
collation, optimizer behavior, and connector semantics. Its additional
specialists cover roles/privileges, backup/restore, replication/HA, online DDL,
partitioning, and compatibility/upgrade work.
SQLite covers type affinity, foreign-key enforcement, the single-writer model,
journal/WAL behavior, busy handling, table rebuilds, and file/workload-specific
plans. Its additional specialists cover backup/restore, WAL checkpointing,
integrity/recovery, vacuum/maintenance, version compatibility, and extensions.

### OpenAPI: 13 concerns

`design`, `schema-governance`, `review`, `lint`, `generate-spec`, `codegen`,
`mock-generation`, `sample-generation`, `auth-security-review`,
`documentation`, `versioning-migration`, `breaking-change-detection`,
`contract-testing`.

### GitHub workflow boundaries

`request-copilot-review` changes only the reviewer request on an existing PR.
`security-alerts` inventories Dependabot, code scanning, and secret scanning in
read-only mode. `security-review` remains the code and trust-boundary review;
alert remediation is intentionally outside both Skills.

## Composition

Agents select the smallest set of specialists that covers the change. Several
specialists in one domain are expected when the task crosses concerns:

```text
$tdd
  + go-concurrency + go-resource-management
  + go-data-race-check + go-idiomatic-code-check
  + go-goroutine-leak-deadlock-check
  + go-struct-json-tags
  + postgresql-transactions + postgresql-locking
  + postgresql-roles-rls
  + mysql-transactions + mysql-locking + mysql-online-ddl
  + openapi-contract-testing
  + security-review
```

Other common compositions include `python3-type-checking` for typed Python
boundaries, `rust-unsafe-audit` + `rust-ffi-abi` for native interfaces,
`sqlite-backup-restore` + `sqlite-wal-checkpoint` for file recovery,
`mysql-roles-privileges` + `mysql-compatibility-upgrade` for access or upgrade
work, and `fuzzing-property-testing` + `benchmark-regression` for parser or
performance work. `zero-downtime-migration` composes the database migration, locking,
compatibility, and OpenAPI versioning specialists; it does not replace them.

The `tdd-implementer` agent composes `$tdd` with these specialists and does not
restate TDD. The `reviewer` agent composes `$code-review` with the relevant
specialists and keeps Standards, Spec, security, database, and test findings
separate.

## Agents

- `planner`: select specialists, scope, seams, acceptance criteria, and checks.
- `tdd-implementer`: implement vertical slices using `$tdd` plus specialists.
- `reviewer`: review standards/spec plus relevant specialist contracts.
- `database-reviewer`: review engine-specific correctness and migration risk.
- `security-reviewer`: review trust boundaries and security evidence.
- `test-reviewer`: review tests at public seams without implementing fixes.
- `repo-doctor`: inspect instructions, toolchain, dependencies, CI, and
  reproducibility without changing the repository.

Agents do not own a second catalog. `planner` selects specialists by trigger,
`tdd-implementer` combines `$tdd` with implementation concerns, and review
agents add liveness, compatibility, security, database, or test specialists
only when the change crosses those boundaries.

## Priority after P0

P1 adds repository-specific tool references and scripts only after the target
repository selects its generator, linter, driver, runtime, and CI commands.
P2 adds real fixtures and golden/compatibility tests. No placeholder directories
are needed before those inputs exist.

## Validation

Run the bundled `quick_validate.py` once for every `SKILL.md`, including the
workflow Skills. Also check that
specialist names are unique, descriptions contain the language/engine/contract
boundary, data-race and goroutine-liveness checks state their evidence limits,
Python typing instructions handle `Any` propagation, generated JSON-tag
instructions handle nullability/collisions, and no Agent references a removed
umbrella Skill.
