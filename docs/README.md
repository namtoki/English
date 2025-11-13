# English Learning Presentation

Slidevを使った英語学習プレゼンテーション

## 🚀 セットアップ

### 必要なもの
- Node.js (v16以上)
- npm または yarn

### インストール

```bash
cd docs
npm install
```

## 🎨 開発

```bash
npm run dev
```

ブラウザで http://localhost:3030 が自動的に開きます。

## 📦 ビルド

静的ファイルとしてエクスポート:

```bash
npm run build
```

ビルド結果は `dist/` フォルダに出力されます。

## 📤 PDFエクスポート

```bash
npm run export
```

プレゼンテーションをPDFとしてエクスポートできます。

## 🌐 GitHub Pagesへのデプロイ

### 手動デプロイ

1. ビルドを実行
```bash
npm run build
```

2. `dist/` フォルダ内容をGitHub Pagesブランチにプッシュ

### 自動デプロイ (GitHub Actions)

`.github/workflows/deploy.yml` を設定することで、プッシュ時に自動デプロイできます。

## 📝 スライドの編集

`slides.md` ファイルを編集してスライドを変更できます。

### 基本的な構文

```markdown
---
# スライドの設定
layout: default
---

# スライドタイトル

コンテンツをここに書く

---

# 次のスライド

別のコンテンツ
```

### 便利な機能

- **レイアウト**: `layout: center`, `layout: two-cols`, `layout: section` など
- **クリックアニメーション**: `<v-clicks>` タグで要素を順番に表示
- **コードハイライト**: 自動的にシンタックスハイライト
- **アイコン**: Carbon iconsを使用可能

## 📚 ドキュメント

- [Slidev公式ドキュメント](https://sli.dev/)
- [テーマ一覧](https://sli.dev/themes/gallery.html)
- [アドオン](https://sli.dev/addons/use.html)

## 🎯 このプレゼンテーションの内容

1. 学習目標と計画
2. 理論（発音・文法）
3. 単語集の構成
4. 実践練習
5. 学習の成果
6. リポジトリ構造
7. まとめ

## 🛠️ カスタマイズ

### テーマの変更

`slides.md` の先頭部分でテーマを変更できます:

```yaml
---
theme: seriph  # default, seriph, apple-basic など
---
```

### 背景の変更

各スライドで背景を指定:

```yaml
---
background: https://source.unsplash.com/collection/94734566/1920x1080
---
```

## 🤝 Contributing

改善提案や問題報告は Issues または Pull Requests でお願いします。
