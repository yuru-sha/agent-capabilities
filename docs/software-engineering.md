# Software Engineering Capability Pack

Go、TypeScript、Python 3、Rust、PostgreSQL、MySQL、SQLite、Redis、BullMQ、OpenAPI、Terraform、フロントエンド、外部サービス統合向けの専門 Skills を配布します。AWS / Google Cloud 固有知識は各 vendor の公式 Agent Skills を利用します。

一般的な開発ワークフローは OMP と oh-my-pstack が所有します。OMP は実行環境、Task、モデル、セッションを管理します。oh-my-pstack は計画、設計、TDD、レビュー、オーケストレーションを管理します。このリポジトリは、それらにない言語・データベース・API・インフラの専門知識と、固有の GitHub 操作を提供します。

## 構成

| 分類 | 内訳 | 数 |
|---|---|---:|
| Language | Go、TypeScript、Python 3、Rust | 4 |
| Database | PostgreSQL、MySQL、SQLite | 3 |
| OpenAPI | 契約設計、lint、生成、互換性、テスト | 1 |
| Cross-cutting | security-review、web-security-review、operational-quality、zero-downtime-migration、technical-authoring | 5 |
| Infrastructure | Terraform infrastructure、Terraform policy testing | 2 |
| Frontend | Web品質、ブラウザーテスト、フォーム、各フレームワーク | 7 |
| Data systems | Redis | 1 |
| Messaging | BullMQ | 1 |
| Integrations | note.com 非公式API、X Ads API、Dropbox API、YouTube API、Meta Marketing API、SmartNews Marketing API、TikTok API for Business、LINE Yahoo Ads、Google Ads API | 9 |
| **合計** | **専門 Skill** | **33** |

このほか GitHub 操作 Skill が13個あります。Draft/Ready PR、独立 PR review、Issue の要件整理・分割・作成、Copilot review、レビュースレッドへの返信、GitHub release、security alert、マージ後の cleanup、Orca Automation lock recovery を扱います。

### Generic data and messaging

`redis` owns provider-neutral Redis data structures, atomicity, memory,
persistence, availability, observability, and security.

`bullmq` owns BullMQ queue/worker semantics. Compose it with `redis` when
Redis topology or persistence is also in scope.

### External cloud skills

AWS, Google Cloud, and Azure service knowledge is intentionally delegated to official
vendor-maintained Agent Skills:

- AWS: https://github.com/aws/agent-toolkit-for-aws
- Google Cloud: https://github.com/google/skills
- Azure: https://github.com/MicrosoftDocs/agent-skills

Do not reimplement provider service guidance in this pack unless a project has a
genuinely repository-specific workflow that is not owned by the official
upstream Skills. Terraform remains provider-neutral and stays in this pack.

### Integrations

`note-com-unofficial-api` records observed note.com REST v1/v2/v3 and GraphQL
behavior, including authentication, article/search/creator/archive/hashtag
reads, and write-safety caveats. Its endpoint catalog is based on the linked
third-party survey and must be revalidated before implementation. It does not
add runtime code or authorize an integrating project's API operations.

`x-ads-api` uses the current official X Ads API documentation as the primary
source and applies a 30-day freshness gate. It resolves resource dependencies
from advertising type instead of a fixed hierarchy, prefers reusable assets and
minimum-scope mutations, and covers streaming/chunked media behavior plus
synchronous/asynchronous reporting without depending on a programming language.

`dropbox-api` uses the current official Dropbox HTTP API and developer guides
as primary sources with a 30-day freshness gate. It covers OAuth/PKCE and scopes,
file identity and CRUD, bounded-memory transfer and upload sessions,
cursor-based change tracking, sharing, namespace/team-space resolution, and
rate-limit/retry behavior including per-namespace write concurrency.

`youtube-api` uses current official Google/YouTube documentation as the primary
source with a 30-day freshness gate. It covers Data API v3 resources and
uploads, Analytics queries, bulk Reporting jobs/downloads, Live Streaming,
channel-aware OAuth, quota-aware collection access, multi-channel batching,
local-file/video mapping, and retry/error handling without depending on a
programming language.

`meta-marketing-api` uses current official Meta Graph API / Marketing API
reference pages, changelogs, and access documentation as primary sources with a
30-day freshness gate. It covers Business/Ad Account context, Campaign/Ad Set/Ad
resource planning, creative/media reuse and upload, targeting/placements,
Custom Audiences and conversion/catalog dependencies, Ads Insights sync/async
reporting, cursor pagination/batching, rate-limit headers, structured errors,
and ambiguous-write reconciliation without depending on a programming language.

`smartnews-marketing-api` uses current official SmartNews Marketing API docs and
OpenAPI definitions with a 30-day freshness gate. It covers OAuth client
credentials, Ad Account/Campaign/AdGroup/Ad planning, media upload, targeting,
Custom Audiences, pixels, catalogs/ProductSets, Insights JSON/CSV pagination,
micro-currency handling, rate limits, retry/error behavior, and parent/child
mutation serialization without depending on a programming language.

`tiktok-api-for-business` uses current official TikTok API for Business
documentation with a 30-day freshness gate and explicit v1.3/v2.0 migration
checks. It covers Marketing API, Business Center, Accounts API, Events API,
Manual and Upgraded Smart+ delivery, creatives/Spark Ads, audiences/catalogs,
webhooks, sync/async reporting, data latency, pagination, and resilient writes
without depending on a programming language.

`google-ads-api` uses current official Google Ads API release notes, versioned
reference pages, field metadata, and guides with a 30-day freshness gate. It
covers OAuth/developer-token and manager-account context, GAQL Search/SearchStream
reporting, resource-specific and mixed mutations, update masks, validation,
partial failure, BatchJobService, quotas, structured errors, concurrency, and
ambiguous-write reconciliation without depending on a programming language.

`line-yahoo-ads` uses current official LINEヤフー for Business product pages,
manuals, notices, media sheets, and submission/reporting guidance with a 30-day
freshness gate. It covers Search Ads, Display Ads (Auction), Display Ads
(Guaranteed), safe trafficking/review/activation, bulk-operation safeguards, and
reproducible performance reporting while preserving legacy Yahoo!広告 / LINE広告
naming needed for historical interpretation.

ORCA から OMP への Issue 引き渡しと、`orca:pr-open` Issue を手動実行で Babysit → Shipping する契約は、それぞれ `packs/operations/github/automations/issue-omp-handoff.md` と `packs/operations/github/automations/issue-pr-lifecycle.md` にある。専門セレクタは `database-reviewer` と `infrastructure-reviewer` の2個である。

## ローカル検証 Skill

`.agents/skills/verify-agent-capabilities/SKILL.md` はこのリポジトリ自身のインストーラーを検証するためのローカル Skill で、Profile や pack の配布物ではなく、リポジトリ保守時の検証手順として配置します。Profile 経由ではインストールしません。

## 所有境界

- OMP が Task 実行、モデル選択、セッション、runtime lifecycle と、独立レビュー担当を提供します。
- oh-my-pstack は一般的な開発 Playbook を提供し、caller が明示的に起動した場合に `interrogate` で adversarial multi-model review を行います。
- `review-mode` はPR文脈、専門家選択、caller指定のseverity・投稿ポリシーを構成します。汎用レビューや `interrogate` のレビュー調整は再実装しません。
- ORCA は Issue の選択、実行 state、worktree 準備、OMP の起動を所有します。
- `issue-omp-handoff` は ORCA の coarse Issue state と OMP への最小 handoff を定義します。`issue-pr-lifecycle` は手動実行で PR stack の Babysit と Shipping を進めます。いずれも Orca Automation であり、Skill ではなく、Profile からインストールしません。
- このPackは言語、データベース、OpenAPI、フロントエンド、インフラの専門知識と、technical-authoring の技術文書設計知識を所有します。
- `technical-authoring` は文書種別に応じた構成、技術的根拠、実行可能な例、検証、安全性を扱います。一般的な文章作成 workflow は installed `technical-writing` と oh-my-pstack に委ねます。
- `database-reviewer` と `infrastructure-reviewer` は適切な専門 Skill を選択します。レビューの進行方法は定義しません。
- `security-review` は既存の言語・データベース・インフラの専門知識で扱えない横断的な trust boundary を補います。WebアプリケーションとHTTP APIのレビュー方法、認証・セッション・認可、ブラウザ境界、状態遷移、診断証跡、Findingと回帰テストは `web-security-review` が担当します。

## Cloud ownership

Cloud-provider-specific Skills are not distributed from this repository. Use the official AWS and Google upstream Agent Skills directly.

## ディレクトリ

```text
agent-capabilities/
├── packs/
│   ├── software-engineering/
│   │   ├── skills/{languages,databases,openapi,cross-cutting,infrastructure,frontend,data-systems,messaging,integrations}/...
│   │   └── agents/{database-reviewer,infrastructure-reviewer}.md
│   └── operations/github/
│       ├── skills/{create-pr,create-draft-pr,mark-pr-ready,review-mode,
│       │           request-copilot-review,reply-to-review-thread,github-release,
│       │           create-issue,clarify-issue,decompose-issue,security-alerts,
│       │           post-merge-cleanup}/SKILL.md
│       ├── automations/{issue-omp-handoff,issue-pr-lifecycle}.md
├── profiles/{go,typescript,python3,rust,postgresql,mysql,sqlite,openapi,
│             cross-cutting,terraform,frontend,redis,bullmq,note-com,x-ads,dropbox,youtube,meta-marketing,smartnews-marketing,tiktok-business,line-yahoo-ads,google-ads,workflows,github}.yaml
├── scripts/install-profile
└── docs/
```

## 専門Skillの合成

選択したProfileから必要な専門Skillを組み合わせます。例:

```text
oh-my-pstack TDD / caller-triggered `interrogate`
  + go (concurrency / data-race / goroutine references)
  + postgresql (transactions / locking references)
  + openapi (contract-testing reference)
  + web-security-review (Webアプリ/APIのレビュー)
  + security-review (追加の横断的なtrust boundaryがある場合)
```

Language Skillsは言語固有の型・並行処理・エラー処理・toolchainを扱います。Database Skillsはprovider非依存のPostgreSQL、MySQL、SQLiteを扱います。Data systemsはRedis、MessagingはBullMQを扱います。Terraformはprovider非依存Infrastructureとして分離します。AWS / Google Cloud固有仕様はvendor公式 Agent Skillsへ委譲し、OpenAPI、Cross-cutting、Frontend、Integrationsはこのリポジトリで各専門境界を所有します。

## GitHub操作

13個のGitHub Skillは明示的な操作境界を持ちます。外部状態を変更する操作は、対象と権限を確認し、結果を再取得して検証します。Orca Automation Prompt はIssue handoffと、手動実行のPRライフサイクル管理を定め、Profile経由ではなくOrca Automationとして設定します。

## 検証

変更した Skill directory ごとに `quick_validate.py` を実行します。Skill 名の一意性、Profile selector、installer 出力、参照先を確認し、関連するリポジトリのテストも実行します。
