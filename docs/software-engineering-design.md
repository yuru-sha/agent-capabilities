# Software Engineering Skill Set design

## Goal

Provide installable specialist Skills for Go, TypeScript, Python 3, Rust, PostgreSQL, MySQL, SQLite, OpenAPI, Terraform, AWS infrastructure, and frontend work. Each Skill owns one concrete domain concern. OMP and oh-my-pstack own the generic runtime and development workflow.

## Ownership boundaries

- OMP owns task execution, model routing, session persistence, and runtime lifecycle.
- oh-my-pstack owns generic development workflow, including planning, architecture workflow, TDD, review, orchestration, and recovery.
- Language Skills own language-specific mechanics for one concern.
- Database Skills own one engine and one database concern.
- OpenAPI Skills own one contract concern.
- Infrastructure Skills own one Terraform or AWS concern.
- Frontend Skills own cross-framework web quality, browser testing, forms, and framework mechanics.
- `database-reviewer` and `infrastructure-reviewer` select specialist Skills. They do not own review workflow.
- `security-review` adds cross-cutting trust-boundary checks not already owned by engine-specific security Skills.
- oh-my-pstack owns fixed-point diff review and the Standards/Spec split.
- oh-my-pstack owns TDD. This repository does not define a second TDD workflow.

There are no language, database, OpenAPI, or infrastructure umbrella `SKILL.md` files. Skill descriptions provide the selection boundary. README and this design document are the human-facing catalog.

## Package shape

| Area | Count | Examples |
|---|---:|---|
| Language | 98 | `go-testing`, `go-goroutine-leak-deadlock-check`, `python3-type-checking`, `rust-unsafe-audit` |
| Database | 42 | `postgresql-roles-rls`, `mysql-online-ddl`, `sqlite-wal-checkpoint` |
| OpenAPI | 13 | `openapi-lint`, `openapi-codegen`, `openapi-breaking-change-detection` |
| Cross-cutting | 4 | `security-review`, `operational-quality`, `zero-downtime-migration`, `technical-authoring` |
| Infrastructure | 7 | `terraform-infrastructure`, `aws-infrastructure`, `terraform-policy-testing` |
| Frontend | 7 | `frontend-web-quality`, `frontend-browser-testing`, `frontend-form-validation`, framework and styling Skills |
| **Total** | **171** | specialist Skills |

The repository ships 11 GitHub operation Skills: `create-pr`, `create-draft-pr`, `mark-pr-ready`, `request-copilot-review`, `reply-to-review-thread`, `github-release`, `create-issue`, `clarify-issue`, `decompose-issue`, `security-alerts`, and `post-merge-cleanup`. The `implement-issue` Skill was removed because OMP with oh-my-pstack owns Issue implementation.

Each specialist has a `SKILL.md` with a discriminating description. Profiles compose Skill sets; they are distribution metadata, not another instruction layer.

## Profiles and composition

Profiles select Skill paths and only the specialist selectors needed for their domain. A consumer composes profiles by ID:

```yaml
profiles:
  - go
  - sqlite
```

The installer unions selected Skills and de-duplicates selected agents by ID. A generated `go+sqlite` bundle is an output artifact, not a source Profile.

The `github` profile selects GitHub operation Skills. `workflows` selects the complete GitHub operations pack. The separate ORCA prompt at `packs/operations/github/automations/issue-omp-handoff.md` defines the ORCA-to-OMP Issue handoff, not a Profile Skill or development workflow.

The infrastructure profile selects seven Terraform and AWS specialists plus the `infrastructure-reviewer` selector. Database profiles select the matching engine skills and the `database-reviewer` selector.

## Capability map

### Languages

Common concerns include testing, error handling, concurrency, performance, API clients, dependencies, security, refactoring, logging, observability, database access, CLI design, documentation, configuration, resource management, serialization, networking, data races, and idiomatic code.

Each language keeps its own rules. Examples include Go table-driven tests and `t.Run`, race-enabled commands and JSON tag generation; TypeScript `unknown` catches and `AbortSignal`; Python context managers, `Any` boundaries, and asyncio; Rust `Result`, ownership, `Send`/`Sync`, and RAII.

Language-specific additions cover Go goroutine liveness, fuzzing, HTTP servers, code generation, and API compatibility; TypeScript type design, module builds, runtime validation, package publishing, and DOM accessibility; Python typing, packaging, subprocesses, data modeling, and web servers; Rust unsafe code, FFI, MSRV, workspaces, and async runtimes.

### Databases

PostgreSQL, MySQL, and SQLite each have skills for design, SQL, indexes, transactions, locking, migrations, performance, and review. Engine-specific skills cover access control, backup/restore, maintenance, partitioning, replication, online DDL, query-plan regression, WAL, integrity recovery, version compatibility, and extensions.

### OpenAPI

Thirteen concerns cover design, schema governance, review, lint, spec generation, code generation, mocks and samples, authentication/security, documentation, versioning, breaking-change detection, and contract testing.

### Infrastructure

Seven Skills keep Terraform state and policy testing separate from AWS topology, IAM/OIDC, deployment handoffs, operations, and Lambda packaging. `github-actions-aws-deploy` is a review/design Skill, not a GitHub mutation workflow.

### Frontend

`frontend-web-quality` covers platform-first HTML/CSS/JS, responsive behavior, explicit UI states, URL state, progressive enhancement, Core Web Vitals, compatibility, and user flows. `frontend-browser-testing` covers public browser flows. `frontend-form-validation` covers form contracts. `frontend-react`, `frontend-nextjs`, `frontend-svelte`, and `frontend-tailwind` own their framework and styling mechanics. These do not replace TypeScript mechanics or oh-my-pstack workflow.

### Cross-cutting and GitHub operations

`security-review` covers only trust-boundary checks not already handled by language, database, OpenAPI, or infrastructure specialists. `operational-quality` covers runtime operation and reproducibility. `zero-downtime-migration` composes database migration, locking, compatibility, and API-versioning knowledge.

GitHub operation Skills each own a narrow operation. `request-copilot-review` changes only the reviewer request on an existing PR. `reply-to-review-thread` resolves a unique GraphQL thread ID, replies, and verifies the stored reply. `security-alerts` inventories alerts in read-only mode. Alert remediation remains separate.

## Specialist selectors

- `database-reviewer`: identify the engine, select relevant engine and primary-language Skills, and hand them to the pstack review workflow.
- `infrastructure-reviewer`: select Terraform/AWS Skills for the changed surface and hand them to the pstack review workflow.

These selectors do not plan changes, run review loops, coordinate workers, or report generic Standards/Spec findings. OMP and oh-my-pstack own those responsibilities.

## Validation

Run `quick_validate.py` for every changed Skill directory. Check that Skill
names are unique, Profile selectors resolve, installer results match the
selected Profiles, and references point to existing Skills or Agents. Run the
repository's relevant validation tests.