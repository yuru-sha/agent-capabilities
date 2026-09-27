# Software Engineering Capability Pack

Go、TypeScript、Python 3、Rust、PostgreSQL、MySQL、SQLite、OpenAPI、
フレームワーク横断のFrontendを対象にした、専門領域単位のCodex Skill/Agentセットです。全体リポジトリは
`agent-capabilities` で、Profilesは `profiles/` にあります。

## 現在の構成

集約Skillは作っていません。専門Skillのdescriptionを自動選択の境界にし、
READMEと設計書だけを人間向けのカタログにしています。
TerraformとAWSのインフラ領域も、同じ専門Skillの境界で提供します。

| 分類 | 内訳 | 数 |
|---|---|---:|
| Language | 4言語 × 基本19領域 + 言語固有追加22領域 | 98 |
| Database | PostgreSQL/MySQL/SQLite × 基本8領域 + 固有6領域 | 42 |
| OpenAPI | 13領域 | 13 |
| Cross-cutting | 基本3領域 + 追加6領域 | 9 |
| Infrastructure | Terraform/AWSの7領域 | 7 |
| Frontend | Web UI品質、browser testing、form validation、React 19/Next.js/Svelte 5/Tailwind v4+ | 7 |
| **合計** | **専門Skill** | **176** |

このPackとは別に、リポジトリには13個のWorkflow Skillも含まれます。
`commit-push`、`create-pr`、`create-draft-pr`、`mark-pr-ready`、
`request-copilot-review`、`reply-to-review-thread`、`github-release`、
`create-issue`、`clarify-issue`、`decompose-issue`、`implement-issue`、
`security-alerts`、`post-merge-cleanup`です。

Issue Treeを自動選択・Claimし、専用Worktree、Recovery、Review、Draft PR、CIまで管理するOrca Automation Promptは
`packs/operations/github/automations/issue-development-pipeline.md`です。

Agent定義は8個です。

## 既存Skillとの境界

- `$tdd` がTDDの定義、red → green、seam、テストのアンチパターンを所有します。
- `$code-review` が固定点からの差分、Standards/Specの二軸レビューを所有します。
- `$gh-fix-ci` がGitHub Actionsの失敗調査と承認後の修正を所有します。
- このセットは専門領域固有の判断材料だけを追加します。
- `tdd-implementer` は `$tdd` を読み、TDD詳細を再定義しません。

## ディレクトリ

```text
agent-capabilities/
├── packs/
│   ├── software-engineering/
│   │   ├── skills/{languages,databases,openapi,cross-cutting,infrastructure,frontend}/...
│   │   └── agents/{planner,tdd-implementer,reviewer,database-reviewer,
│   │              security-reviewer,test-reviewer,repo-doctor,
│   │              infrastructure-reviewer}.md
│   └── operations/github/
│       ├── skills/{commit-push,create-pr,create-draft-pr,mark-pr-ready,
│       │           request-copilot-review,reply-to-review-thread,
│       │           github-release,create-issue,clarify-issue,decompose-issue,
│       │           implement-issue,security-alerts,post-merge-cleanup}/SKILL.md
│       └── automations/issue-development-pipeline.md
├── profiles/{go,typescript,python3,rust,postgresql,mysql,sqlite,openapi,
│             cross-cutting,infrastructure,frontend,workflows,github}.yaml
├── shared/
├── scripts/install-profile
└── docs/
```

## Skillの合成

専門Skillは必要な領域だけを複数選びます。

```text
$tdd
  + go-concurrency + go-resource-management
  + go-data-race-check + go-idiomatic-code-check
  + go-goroutine-leak-deadlock-check
  + go-struct-json-tags (JSON payloadから構造体を生成するなら)
  + postgresql-transactions + postgresql-locking
  + mysql-transactions + mysql-locking + mysql-online-ddl
  + openapi-contract-testing (API契約が対象なら)
  + security-review (セキュリティリスクがあるなら)
  + terraform-infrastructure + terraform-policy-testing
  + aws-infrastructure + aws-iam-oidc-security
  + github-actions-aws-deploy + cloudwatch-operations + nodejs-lambda
  + frontend-web-quality (user-facing web UI)
  + frontend-browser-testing + frontend-form-validation (browser flows and forms)
  + frontend-react + frontend-nextjs + frontend-svelte (framework-specific)
  + frontend-tailwind (styling)
```

専門Skillはmodel-invokedです。`go-concurrency` のdescriptionはGoの並行処理に、
`postgresql-locking` のdescriptionはPostgreSQLのロックにだけ反応します。

## 追加した重点領域

レビューで頻出するが、集約Skillに埋めると見落としやすい領域を独立させています。

- Go: `go-goroutine-leak-deadlock-check`, `go-fuzzing`, `go-http-server`,
  `go-code-generation`, `go-api-compatibility`
- TypeScript: `typescript-type-design`, `typescript-module-build`,
  `typescript-runtime-validation`, `typescript-package-publishing`,
  `typescript-dom-accessibility`
- Python 3: `python3-type-checking`, `python3-packaging`,
  `python3-subprocess`, `python3-data-modeling`, `python3-web-server`
- Rust: `rust-unsafe-audit`, `rust-ffi-abi`, `rust-api-compatibility`,
  `rust-msrv`, `rust-features-workspaces`, `rust-async-runtime`
- PostgreSQL: `postgresql-roles-rls`, `postgresql-backup-restore`,
  `postgresql-vacuum-maintenance`, `postgresql-partitioning`,
  `postgresql-replication-ha`, `postgresql-query-plan-regression`
- SQLite: `sqlite-backup-restore`, `sqlite-wal-checkpoint`,
  `sqlite-integrity-recovery`, `sqlite-vacuum-maintenance`,
  `sqlite-version-compatibility`, `sqlite-extensions`
- MySQL: `mysql-roles-privileges`, `mysql-backup-restore`,
  `mysql-replication-ha`, `mysql-online-ddl`, `mysql-partitioning`,
  `mysql-compatibility-upgrade`
- 横断: `fuzzing-property-testing`, `benchmark-regression`,
  `package-release-compatibility`, `sbom-license-review`,
  `test-fixture-design`, `zero-downtime-migration`
- Infrastructure: terraform-infrastructure, aws-infrastructure,
  aws-iam-oidc-security, github-actions-aws-deploy, cloudwatch-operations,
  nodejs-lambda, terraform-policy-testing
- Frontend: `frontend-web-quality` for framework-agnostic semantic HTML, responsive
  behavior, UI state, browser support, performance, and user-flow verification;
  `frontend-browser-testing` for public browser flows and
  `frontend-form-validation` for cross-framework form contracts; and
  `frontend-react`, `frontend-nextjs`, `frontend-svelte`, and
  `frontend-tailwind` for the named framework and styling boundaries.

特に `go-goroutine-leak-deadlock-check` は `go-data-race-check` と別物です。
race detectorが検出する実行時の競合だけでなく、停止不能・待ち合わせ不能・
ロック順序・キャンセル漏れをレビューします。`python3-type-checking` は
`Any` の無制限な伝播、`cast`/ignoreの濫用、runtime validationとの境界を明示的に扱います。

## Agentの使い分け

| Agent | 主な出力 | 変更 |
|---|---|---|
| `planner` | 必要な専門Skill、受け入れ条件、検証計画 | なし |
| `tdd-implementer` | `$tdd`に沿った実装 | あり |
| `reviewer` | Standards/Specを分離したレビュー | なし |
| `database-reviewer` | SQL・index・transaction・migrationの所見 | なし |
| `security-reviewer` | trust boundaryと攻撃面の所見 | なし |
| `test-reviewer` | 公開seam上のテスト品質の所見 | なし |
| `repo-doctor` | instructions・toolchain・依存・CIの健康診断 | なし |
| infrastructure-reviewer | Terraform/AWSのtrust、配布、運用境界の所見 | なし |

## 優先順位

- **P0**: 明示された176個の専門Skill、13個のWorkflow Skill、Issue開発Orca Automation Prompt 1個、8 Agent、設計書、README、静的検証。
- **P1**: 実リポジトリで使うgenerator/linter/driver固有のreferencesと補助script。
- **P2**: 実プロジェクト由来のfixture、golden test、生成物の互換性テスト。

P1/P2は対象リポジトリとツールチェーンが決まらないまま作ると、使われない
ルールや未検証の保証を固定するため保留しています。

## 検証

176個の専門 `SKILL.md` と13個のWorkflow `SKILL.md`をCodex同梱の
`quick_validate.py` で検証します。
この成果物は指示とメタデータなので、アプリケーションruntime fixtureは作りません。
