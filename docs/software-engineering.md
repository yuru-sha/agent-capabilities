# Software Engineering Capability Pack

Go、TypeScript、Python 3、Rust、PostgreSQL、MySQL、SQLite、OpenAPI、Terraform、AWS、フロントエンド向けの専門 Skills を配布します。

一般的な開発ワークフローは OMP と oh-my-pstack が所有します。OMP は実行環境、Task、モデル、セッションを管理します。oh-my-pstack は計画、設計、TDD、レビュー、オーケストレーションを管理します。このリポジトリは、それらにない言語・データベース・API・インフラの専門知識と、固有の GitHub 操作を提供します。

## 構成

| 分類 | 内訳 | 数 |
|---|---|---:|
| Language | Go、TypeScript、Python 3、Rust | 98 |
| Database | PostgreSQL、MySQL、SQLite | 42 |
| OpenAPI | 契約設計、lint、生成、互換性、テスト | 13 |
| Cross-cutting | security-review、operational-quality、zero-downtime-migration、technical-authoring | 4 |
| Infrastructure | Terraform、AWS | 7 |
| Frontend | Web品質、ブラウザーテスト、フォーム、各フレームワーク | 7 |
| **合計** | **専門 Skill** | **171** |

このほか GitHub 操作 Skill が11個あります。Draft/Ready PR、Issue の要件整理・分割・作成、Copilot review、レビュー スレッドへの返信、GitHub release、security alert、マージ後の cleanup を扱います。

ORCA から OMP への Issue 引き渡し契約は `packs/operations/github/automations/issue-omp-handoff.md` にあります。専門セレクタは `database-reviewer` と `infrastructure-reviewer` の2個です。

## 所有境界

- OMP が Task 実行、モデル選択、セッション、runtime lifecycle を所有します。
- oh-my-pstack が一般的な開発 workflow を所有します。
- ORCA は Issue の選択、実行 state、worktree 準備、OMP の起動を所有します。
- `issue-omp-handoff` は ORCA の coarse Issue state と OMP への最小 handoff を定義する Orca Automation です。Skill ではなく、Profile からインストールしません。
- このPackは言語、データベース、OpenAPI、フロントエンド、インフラの専門知識と、technical-authoring の技術文書設計知識を所有します。
- `technical-authoring` は文書種別に応じた構成、技術的根拠、実行可能な例、検証、安全性を扱います。一般的な文章作成 workflow は installed `technical-writing` と oh-my-pstack に委ねます。
- `database-reviewer` と `infrastructure-reviewer` は適切な専門 Skill を選択します。レビューの進行方法は定義しません。
- `security-review` は既存の言語・データベース・インフラの専門知識で扱えない横断的な trust boundary を補います。

## ディレクトリ

```text
agent-capabilities/
├── packs/
│   ├── software-engineering/
│   │   ├── skills/{languages,databases,openapi,cross-cutting,infrastructure,frontend}/...
│   │   └── agents/{database-reviewer,infrastructure-reviewer}.md
│   └── operations/github/
│       ├── skills/{create-pr,create-draft-pr,mark-pr-ready,request-copilot-review,
│       │           reply-to-review-thread,github-release,create-issue,clarify-issue,
│       │           decompose-issue,security-alerts,post-merge-cleanup}/SKILL.md
│       └── automations/issue-omp-handoff.md
├── profiles/{go,typescript,python3,rust,postgresql,mysql,sqlite,openapi,
│             cross-cutting,infrastructure,frontend,workflows,github}.yaml
├── scripts/install-profile
└── docs/
```

## 専門Skillの合成

選択したProfileから必要な専門Skillを組み合わせます。例:

```text
oh-my-pstack TDD / review workflow
  + go-concurrency + go-data-race-check
  + go-goroutine-leak-deadlock-check
  + postgresql-transactions + postgresql-locking
  + openapi-contract-testing
  + security-review (横断的なtrust boundaryがある場合)
```

Language Skillsは、Goのgoroutineとrace検出、TypeScriptの型設計とAbortSignal、Pythonの`Any`伝播とasyncio、Rustの所有権・`Result`・unsafe/FFIなど、言語ごとの規則を扱います。Database Skillsは各エンジンのtransaction、locking、migration、運用特性を扱います。OpenAPI Skillsは契約、生成、breaking change、contract testingを扱います。Infrastructure SkillsはTerraform state/policy、AWS trust、deploy、Lambda、CloudWatchを扱います。Frontend Skillsはブラウザー挙動、form contract、React/Next.js/Svelte/Tailwindを扱います。

## GitHub操作

11個のGitHub Skillは明示的な操作境界を持ちます。外部状態を変更する操作は、対象と権限を確認し、結果を再取得して検証します。Orca Automation Prompt はIssueの選択、coarse state、worktreeの準備、OMPへのhandoffだけを定め、Profile経由ではなくOrca Automationとして設定します。

## 検証

変更した Skill directory ごとに `quick_validate.py` を実行します。Skill 名の一意性、Profile selector、installer 出力、参照先を確認し、関連するリポジトリのテストも実行します。