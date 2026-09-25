# agent-capabilities

[English](README.md) | [日本語](README.ja.md)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/yuru-sha/agent-capabilities)

AI コーディングエージェント向けに、再利用可能な Skills、Agents、Profiles、ワークフロー機能を提供します。

## 内容

- 言語、データベース、OpenAPI、横断機能、インフラ、フロントエンド向けのエンジニアリング Skills 176 個
- コミットと push、Pull Request、Issue の要件整理・分割・実装・作成、Copilot review、レビュー スレッドへの返信、GitHub release、security alert、マージ後の cleanup を扱うリポジトリ運用 Skills 13 個
- Issue Tree開発向けの再利用可能なOrca AutomationパイプラインPrompt 1 個
- 再利用可能な Agents 8 個
- `frontend.yaml`、`go.yaml`、`sqlite.yaml`、`infrastructure.yaml`、`github.yaml` など、組み合わせ可能な Profiles 13 個

機能は [`software-engineering` pack](packs/README.md) と `operations/github` pack に分類されています。各プロジェクトでは Profiles を使って pack の機能を組み合わせます。

## Profiles の構成

Profiles で Skills と Agents の両方を選択できます。言語やデータベースごとの統合 Skill を作らずに、必要な機能を組み合わせられます。

```yaml
profiles:
  - go
  - sqlite
```

resolver は選択された Skills を統合し、Agents は ID ごとに重複を取り除きます。`$tdd`、`$code-review`、`$gh-fix-ci` は外部のグローバル依存関係であり、このリポジトリでは再定義しません。

Rust と SQLite を使い、リポジトリ運用ワークフローもすべて必要な場合は、次のように指定します。

```yaml
profiles:
  - rust
  - sqlite
  - workflows
```

[Profiles](profiles/README.md) と [software-engineering カタログ](docs/software-engineering.md) を参照してください。Skills が使うコマンド群と外部 CLI は[コマンドリファレンス](docs/commands.md)に記載しています。

Terraform と AWS のインフラ作業では infrastructure Profile を選択します。7 個の専門 Skills と、読み取り専用の infrastructure-reviewer Agent が含まれます。利用するプロジェクトで言語やデータベースの機能も必要な場合は、それらの Profile と組み合わせてください。

フロントエンド作業では `frontend` Profile を選択します。フレームワークに依存しない Web 品質、ブラウザーテスト、フォーム検証の Skills に加え、React 19、Next.js、Svelte 5、Tailwind CSS v4 以降の専門機能が含まれます。

## プロジェクトへの Profile のインストール

機能を利用するプロジェクトから、絶対パスまたはこのリポジトリへの相対パスを指定してインストーラーを実行します。

```sh
/path/to/agent-capabilities/scripts/install-profile rust sqlite workflows
```

`commit-push` が不要な場合は、`workflows` の代わりに `github` を指定します。

このコマンドは、選択した Skill ディレクトリをプロジェクトの `.agents/skills/` に、Agent 定義を `.codex/agents/` にリンクします。所有情報は `.agents/agent-capabilities/manifest.json` に記録されるため、後で Profile を削除できます。

```sh
/path/to/agent-capabilities/scripts/install-profile \
  --target /path/to/project --uninstall rust sqlite workflows
```

別の場所から実行する場合は `--target /path/to/project` を指定します。独立したコピーを作成するには `--copy` を、以前にインストールした項目を置き換えるには `--force` を指定します。アンインストール時、管理対象のコピーに変更が加えられている場合は `--force` を指定しない限り保持します。デフォルトを明示する場合は `--link` も指定できます。外部 Skills（`$tdd`、`$code-review` など）は一覧に表示しますが、コピーしません。manifest がない従来のリンクのみのインストールも、リンク先がこの checkout を指していれば削除します。未追跡のコピーはそのまま残します。

## GitHub Release

リリースノートの形式と作成手順は [docs/agents/release.md](docs/agents/release.md) を参照してください。リリース本文のテンプレートは [.github/release-notes-template.md](.github/release-notes-template.md)、自動生成ノートのカテゴリは [.github/release.yml](.github/release.yml) で管理します。
