# README

```
cheatsheet/
│
├── discourse/                  # 話の流れ・文脈制御に関わる表現群
│   ├── framing.md              # 話題の設定 (framing, condition)
│   ├── structuring.md          # 順序立てする修飾句
│   └── emphasis.md             # 対比や気持ちなど、以降の構文を引き立たせる表現 (emphasis, concession)
│
├── stance.md                   # core を内包する表現
│
├── core/                       # 最小単位の SV(O/C) または、O
│   ├── cliche.md               # 定型表現
│   ├── verb.md                 # 動詞表現
│   ├── noun.md                 # 名詞表現
│   ├── modifier.md             # 修飾
│   └── question.md             # 疑問形
│
├── supplement/                 # 補足的な修飾句
│   ├── time.md                 # when, after, since など
│   ├── place.md                # where など
│   ├── cause.md                # 何故
│   ├── how.md                  # どのように
│   └── purpose.md              # 何のために
│
├── tag_endings.md              # if that makes sense, you know, right? など
└── response_cues.md            # あいづち
```

組み立て方のイメージは以下。

```
    <-- response_cues -->

                          <-- stance --><-- core -->
    <-- discourse --> <---------- supplement ----------> <-- discourse --> <-- tag_endings -->
```

- 大方針
  - 既に会話が始まっている場合は、都度 `response_cues` を使う
  - 何か言いたいときは `core` にて本質的な内容を伝える
  - `core` だけでも十分
- 表現を豊かにする場合
  - まず `discourse` にて話したい内容の方向性を示す
  - `core` にニュアンスを加えたい場合は、前に `stance` を付ける
  - `stance` ないし `core` に補足情報を肉付けする場合は、任意の場所に `supplement` を付ける
  - 後で `discourse` を付け足しても OK
  - 最後に `tag_endings` で終えると長い発言の良い切れ目となる
