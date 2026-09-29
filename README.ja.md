# agent-capabilities

[English](README.md) | [日本語](README.ja.md)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/yuru-sha/agent-capabilities)

AI コーディングエージェント向けに、再利用可能な Skills、専門セレクタ、Profiles、ワークフロー機能を提供します。

このリポジトリは [OMP](https://omp.sh/) と [oh-my-pstack](https://github.com/shrimpwtf/oh-my-pstack) を補完します。OMP は実行環境と独立レビュー担当を提供し、oh-my-pstack は一般的な開発 Playbook と、callerが明示した場合に使う adversarial multi-model panel `interrogate` を提供します。このリポジトリは専門知識と、両者が持たないPR固有のレビュー構成を提供します。

## 内容

- 言語、データベース、OpenAPI、横断機能、インフラ、フロントエンド向けのエンジニアリング Skills 171 個
- GitHub 操作 Skills 12 個。PR の作成・独立レビュー、Issue の要件整理・分割・作成、Copilot review、レビュースレッドへの返信、GitHub release、security alert、マージ後の cleanup を扱います。
- Issue を ORCA から OMP に引き渡す Orca Automation Prompt 1 個
- 薄い専門セレクタ 2 個: `database-reviewer`、`infrastructure-reviewer`
- `frontend.yaml`、`go.yaml`、`sqlite.yaml`、`infrastructure.yaml`、`github.yaml` など、組み合わせ可能な Profiles 13 個

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

## プロジェクトへの Profile のインストール

機能を利用するプロジェクトから、絶対パスまたはこのリポジトリへの相対パスを指定してインストーラーを実行します。

```sh
/path/to/agent-capabilities/scripts/install-profile rust sqlite workflows
```

`github` を指定すると、一般的な commit/push を除く GitHub 操作 Skills を選択します。読み取りと PR 作成・release 公開などの変更操作の両方が含まれます。

このコマンドは、選択した Skill ディレクトリをプロジェクトの `.agents/skills/` に、専門セレクタ定義を `.codex/agents/` にリンクします。所有情報は `.agents/agent-capabilities/manifest.json` に記録されるため、後で Profile を削除できます。

```sh
/path/to/agent-capabilities/scripts/install-profile \
  --target /path/to/project --uninstall rust sqlite workflows
```

別の場所から実行する場合は `--target /path/to/project` を指定します。独立したコピーを作成するには `--copy` を、以前にインストールした項目を置き換えるには `--force` を指定します。アンインストール時、管理対象のコピーに変更が加えられている場合は `--force` を指定しない限り保持します。デフォルトを明示する場合は `--link` も指定できます。manifest がない従来のリンクのみのインストールも、リンク先がこの checkout を指していれば削除します。未追跡のコピーはそのまま残します。

## GitHub Release

リリースノートの形式と作成手順は [docs/agents/release.md](docs/agents/release.md) を参照してください。リリース本文のテンプレートは [.github/release-notes-template.md](.github/release-notes-template.md)、自動生成ノートのカテゴリは [.github/release.yml](.github/release.yml) で管理します。