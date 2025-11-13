# English Learning Presentation

このフォルダには英語学習に関する発表資料が含まれています。

## GitHub Pages での公開方法

1. GitHubリポジトリの Settings に移動
2. 左メニューから "Pages" を選択
3. "Source" で "Deploy from a branch" を選択
4. "Branch" で `claude/explain-file-structure-011CUKFDmNU2Ca461PtHxyKv` ブランチと `/docs` フォルダを選択
5. "Save" をクリック

数分後、サイトが公開されます。

## ローカルでのプレビュー

```bash
# シンプルなHTTPサーバーを起動（Python 3）
cd docs
python3 -m http.server 8000

# ブラウザで http://localhost:8000 にアクセス
```

## ファイル構成

```
docs/
├── index.html          # メインHTML
├── css/
│   └── style.css      # スタイルシート
├── js/
│   └── main.js        # JavaScript
└── README.md          # このファイル
```

## カスタマイズ

- `index.html`: コンテンツを編集
- `css/style.css`: デザインを変更
- `js/main.js`: インタラクション機能を追加

## 機能

- レスポンシブデザイン（モバイル対応）
- スムーズスクロール
- アニメーション効果
- 学習計画の視覚化
- 単語集のカテゴリ分け
