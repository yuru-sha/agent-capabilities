# agent-capabilities

[English](README.md) | [日本語](README.ja.md)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/yuru-sha/agent-capabilities)

AI コーディングエージェント向けに、再利用可能な Skills、専門セレクタ、Profiles、ワークフロー機能を提供します。

このリポジトリは [OMP](https://omp.sh/) と [oh-my-pstack](https://github.com/shrimpwtf/oh-my-pstack) を補完します。OMP は実行環境と独立レビュー担当を提供し、oh-my-pstack は一般的な開発 Playbook と、callerが明示した場合に使う adversarial multi-model panel `interrogate` を提供します。このリポジトリは専門知識と、両者が持たないPR固有のレビュー構成を提供します。

## 内容

- 言語、データベース、OpenAPI、横断機能、インフラ、フロントエンド、外部サービス統合向けのエンジニアリング Skills 174 個
- GitHub 操作 Skills 13 個。PR の作成・独立レビュー、Issue の要件整理・分割・作成、Copilot review、レビュースレッドへの返信、GitHub release、security alert、マージ後の cleanup、Orca Automation のロック復旧を扱います。
- Issue を ORCA から OMP に引き渡す Automation と、PR stack を手動で Babysit → Shipping する Automation Prompt 2 個
- 薄い専門セレクタ 2 個: `database-reviewer`、`infrastructure-reviewer`
- `frontend.yaml`、`go.yaml`、`sqlite.yaml`、`infrastructure.yaml`、`note-com.yaml`、`x-ads.yaml`、`dropbox.yaml`、`github.yaml` など、組み合わせ可能な Profiles 16 個
- `.agents/skills/verify-agent-capabilities/` 配下のローカル検証 Skill 1 個

機能は [`software-engineering` pack](packs/README.md) と `operations/github` pack に分類されています。各プロジェクトでは Profiles を使って pack の機能を組み合わせます。

## Profiles の構成

Profiles で Skills と専門セレクタを選択できます。言語やデータベースごとの統合 Skill を作らずに、必要な機能を組み合わせられます。

```yaml
profiles:
  - go
  - sqlite
```

resolver は選択された Skills を統合し、エージェントは ID ごとに重複を取り除きます。コードレビューと TDD は oh-my-pstack のワークフローが提供します。

Rust と SQLite を使い、リポジトリ運用ワークフローもすべて必要な場合は、次のように指定します。

```yaml
profiles:
  - rust
  - sqlite
  - workflows
```

[Profiles](profiles/README.md) と [software-engineering カタログ](docs/software-engineering.md) を参照してください。Skills が使うコマンド群と外部 CLI は[コマンドリファレンス](docs/commands.md)に記載しています。

Terraform と AWS のインフラ作業では infrastructure Profile を選択します。7 個の専門 Skills と、読み取り専用の `infrastructure-reviewer` 専門セレクタが含まれます。利用プロジェクトで言語やデータベースの機能も必要な場合は、それらの Profile と組み合わせてください。

フロントエンド作業では `frontend` Profile を選択します。フレームワークに依存しない Web 品質、ブラウザーテスト、フォーム検証の Skills に加え、React 19、Next.js、Svelte 5、Tailwind CSS v4 以降の専門機能が含まれます。

note.com の非公式Web APIを使うプロジェクトでは `note-com` Profile を選択します。note.com 固有のAPI調査・安全境界を導入します。実装や認可の範囲は、利用するプロジェクト側の契約に従います。

X Ads API を扱うプロジェクトでは `x-ads` Profile を選択します。現行仕様の freshness 確認を前提に、広告タイプからのリソース依存解決、メディア処理、ライフサイクル診断、分析・レポート取得を言語非依存で支援します。

Dropbox API を扱うプロジェクトでは `dropbox` Profile を選択します。OAuth、ファイル/フォルダー、ストリーミングと upload session、cursor ベースの差分追跡、共有、namespace/team space、retry と並列 write 制御を現行仕様の確認付きで言語非依存に支援します。

## Profile のインストール

このリポジトリの checkout にあるインストーラーを実行します。

```sh
/path/to/agent-capabilities/scripts/install-profile rust sqlite workflows \
  --agent codex --scope project
```

`--agent` は `gh skill install` に渡すホスト名です。`omp` を指定した場合は、同コマンドが `omp` を受け付けないため `universal` に読み替えます。`--scope` は `project` または `user` を指定します。OMP Agent 定義は Skill とは別に、project scope では `.omp/agents/`、user scope では `~/.omp/agent/agents/` にコピーされます。

デフォルトでは Skill を `yuru-sha/agent-capabilities` からインストールします。開発中の checkout からインストールする場合は `--from-local` を追加します。Profile metadata はどちらの場合もこの checkout から読み込みます。

別の場所から project scope で実行する場合は `--target /path/to/project` を指定します。既存の OMP Agent 定義と内容が同じなら変更しません。内容が異なるファイルがある場合は上書きせずエラーにします。従来の link/copy 方式が作成したファイルや manifest は変更しません。手動で削除する場合は、先に内容を確認してください。


## ローカル検証 Skill

`.agents/skills/verify-agent-capabilities/SKILL.md` はこのインストーラー向けのローカル検証 Skill です。Profile 経由では配布しないため、利用プロジェクトのワークフローから参照しないでください。

## GitHub運用

Issue Form と既定の Pull Request テンプレートは `yuru-sha/.github` の共通設定を利用します。`orca:*` を含む共通ラベルは `yuru-sha/project-template` から同期します。

エージェントによる GitHub Release 操作は `packs/operations/github/skills/github-release/SKILL.md` を唯一の実行手順とし、Release Notes のカテゴリは `.github/release.yml` で管理します。
