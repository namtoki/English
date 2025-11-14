---
theme: default
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## English Learning Journey
  英語学習の体系的アプローチ
drawings:
  persist: false
transition: slide-left
title: English Learning Journey
mdc: true
base: /English/
---

<style>
.title-container {
  font-size: 3rem;
  font-weight: 700;
  color: white;
  margin-bottom: 2rem;
  min-height: 5rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.title-text {
  display: inline-block;
  position: relative;
}

.crumble-text {
  display: inline-block;
  position: relative;
}

.crumble-char {
  display: inline-block;
}

.crumble-text.slidev-vclick-hidden {
  opacity: 1 !important;
}

.crumble-text.slidev-vclick-hidden .crumble-char {
  animation: crumble 0.8s ease-in forwards;
  animation-delay: calc(var(--delay) * 0.1s);
}

@keyframes crumble {
  0% {
    transform: translateY(0) rotate(0deg);
    opacity: 1;
  }
  30% {
    transform: translateY(10px) rotate(calc(var(--delay) * 5deg));
    opacity: 0.9;
  }
  60% {
    opacity: 0.5;
  }
  100% {
    transform: translateY(400px) rotate(calc(var(--delay) * 50deg + 180deg));
    opacity: 0;
  }
}

.new-text {
  display: inline-block;
  opacity: 0;
}

.new-text.slidev-vclick-current {
  animation: fade-in-up 1.2s ease-out forwards;
  animation-delay: 0s;
}

@keyframes fade-in-up {
  0% {
    transform: translateY(30px) scale(0.9);
    opacity: 0;
  }
  50% {
    transform: translateY(-5px) scale(1.02);
  }
  100% {
    transform: translateY(0) scale(1);
    opacity: 1;
  }
}

.subtitle {
  font-size: 1.5rem;
  opacity: 0;
}

.subtitle.slidev-vclick-current {
  animation: fade-in 1s ease-out forwards;
  animation-delay: 1s;
}

@keyframes fade-in {
  to {
    opacity: 1;
  }
}
</style>

<div class="title-container">
  <div class="title-text">
    英語の学習方法<span v-click.hide="1" class="crumble-text"><span class="crumble-char" style="--delay: 0">教</span><span class="crumble-char" style="--delay: 1">え</span><span class="crumble-char" style="--delay: 2">ま</span><span class="crumble-char" style="--delay: 3">す</span><span class="crumble-char" style="--delay: 4">！</span></span><span v-click="1" class="new-text">見てください！</span>
  </div>
</div>

<div v-click="1" class="subtitle">
  📚 継続的な学習で英語力を向上させる旅
</div>

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    始める <carbon:arrow-right class="inline"/>
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <a href="https://github.com/namtoki/English" target="_blank" alt="GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

---
transition: fade-out
---

# 英語遍歴

<div class="chart-container">
  <canvas id="englishJourneyChart"></canvas>
</div>

<script setup>
import { onMounted, ref, watchEffect } from 'vue'

const chartInstance = ref(null)

const allData = [
  { x: '2008-01-01', y: 40 },
  { x: '2015-01-01', y: 30 },
  { x: '2022-01-01', y: 15 },
  { x: '2024-05-01', y: 35 },
  { x: '2024-11-01', y: 35 },
  { x: '2025-06-01', y: 50 }
]

onMounted(() => {
  // Load Chart.js
  const chartScript = document.createElement('script')
  chartScript.src = 'https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js'

  chartScript.onload = () => {
    // Load date adapter
    const adapterScript = document.createElement('script')
    adapterScript.src = 'https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns@3.0.0/dist/chartjs-adapter-date-fns.bundle.min.js'

    adapterScript.onload = () => {
      const ctx = document.getElementById('englishJourneyChart')
      if (ctx) {
        chartInstance.value = new Chart(ctx, {
          type: 'line',
          data: {
            datasets: [{
              label: '英語の理解度',
              data: [],
              borderColor: 'rgb(75, 192, 192)',
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              tension: 0.4,
              fill: true,
              borderWidth: 3,
              pointRadius: 5,
              pointBackgroundColor: 'rgb(75, 192, 192)',
              pointBorderColor: '#fff',
              pointBorderWidth: 2,
              pointHoverRadius: 7
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: true,
            animation: {
              duration: 800,
              easing: 'easeInOutQuart'
            },
            plugins: {
              legend: {
                display: true,
                position: 'top',
                labels: {
                  color: '#333',
                  font: {
                    size: 14
                  }
                }
              },
              title: {
                display: false
              }
            },
            scales: {
              y: {
                beginAtZero: true,
                max: 100,
                ticks: {
                  callback: function(value) {
                    return value + '%'
                  },
                  color: '#666'
                },
                title: {
                  display: true,
                  text: '英語の理解度',
                  color: '#333',
                  font: {
                    size: 14
                  }
                },
                grid: {
                  color: 'rgba(0, 0, 0, 0.1)'
                }
              },
              x: {
                type: 'time',
                time: {
                  unit: 'year',
                  displayFormats: {
                    year: 'yyyy',
                    month: 'yyyy/MM'
                  },
                  tooltipFormat: 'yyyy年MM月'
                },
                ticks: {
                  color: '#666',
                  maxRotation: 45,
                  minRotation: 0,
                  source: 'auto'
                },
                title: {
                  display: true,
                  text: '時期',
                  color: '#333',
                  font: {
                    size: 14
                  }
                },
                grid: {
                  color: 'rgba(0, 0, 0, 0.1)'
                }
              }
            }
          }
        })
      }
    }
    document.head.appendChild(adapterScript)
  }
  document.head.appendChild(chartScript)
})

// Watch for clicks and update chart
watchEffect(() => {
  if (chartInstance.value && typeof $clicks !== 'undefined') {
    const clicks = $clicks.value || 0
    const pointsToShow = Math.min(clicks, allData.length)
    chartInstance.value.data.datasets[0].data = allData.slice(0, pointsToShow)
    chartInstance.value.update()
  }
})
</script>

<style scoped>
.chart-container {
  width: 80%;
  max-width: 800px;
  height: 400px;
  margin: 2rem auto;
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>

---
transition: fade-out
---

# 学習の目標

継続的な英語力向上のための体系的アプローチ

<v-clicks>

- 🎯 **毎日3時間** - 6セッション × 30分の集中学習
- 📈 **段階的成長** - 発音、文法、語彙、実践の順序立てた習得
- 🔄 **反復練習** - 音読、暗唱、瞬間英作文による定着
- 💪 **継続は力なり** - Consistency is key to success

</v-clicks>

<br>
<br>

<v-click>

> 言語学習は短距離走ではなく、マラソンです

</v-click>

---
layout: two-cols
---

# 📅 毎日の学習計画

## 朝のセッション

<v-clicks>

### 🎵 ハノン (30分)
発音とリズムの基礎練習

### 📖 音読&暗唱 (30分)
文章の音読と暗記練習

</v-clicks>

::right::

<div class="mt-10">

## 日中・夜のセッション

<v-clicks>

### 📝 単語学習 (30分)
80単語を目標に学習

### ⚡ 瞬間英作文 (30分)
素早い英作文トレーニング

### 🎧 リスニング (30分)
英語音声の聞き取り練習

### 🗣️ 自由練習 (30分)
スクール、英会話など

</v-clicks>

</div>

---
layout: section
---

# 📖 理論と文法

発音と文法の基礎を固める

---

# 🗣️ 発音の重要性

正しい発音は理解と自信の基盤

<v-clicks>

## 重点項目

- **音素** - 英語特有の音を正確に発音
- **リズム** - 英語のストレスとイントネーション
- **リエゾン** - 音の連結とリダクション
- **イントネーション** - 文脈に応じた音調変化

</v-clicks>

<br>

<v-click>

```markdown
Practice makes perfect!
/ˈpræktɪs meɪks ˈpɜːrfɪkt/
```

</v-click>

---

# 📝 文法の体系

文法は言語の骨格

<div class="grid grid-cols-2 gap-4 mt-8">

<v-clicks>

<div>

## 基本文型
- SV（第1文型）
- SVC（第2文型）
- SVO（第3文型）
- SVOO（第4文型）
- SVOC（第5文型）

</div>

<div>

## 重要文法項目
- 時制（現在・過去・未来）
- 完了形
- 仮定法
- 受動態
- 関係代名詞

</div>

</v-clicks>

</div>

---
layout: section
---

# 📚 単語集の構成

品詞別・トピック別の体系的学習

---

# 🔤 動詞 (Verbs)

文型別とビジネス用途で分類

<div class="grid grid-cols-2 gap-4 mt-6">

<v-clicks>

<div>

## 文型別
- **助動詞 (AUX)**
  - can, will, must, should...
- **SVC構文**
  - be, become, seem...
- **SVOC構文**
  - make, let, have...
- **SVOO構文**
  - give, tell, show...

</div>

<div>

## 用途別
- **ビジネス動詞**
  - negotiate, implement, analyze...
- **一般動詞**
  - 日常で頻繁に使う動詞

</div>

</v-clicks>

</div>

---

# 📋 形容詞・名詞

トピック別に整理された語彙

<div class="grid grid-cols-3 gap-3 mt-4">

<v-clicks>

<div class="bg-blue-500/10 p-3 rounded">

### 💼 ビジネス
corporate, revenue, strategy, stakeholder...

</div>

<div class="bg-purple-500/10 p-3 rounded">

### ⚖️ 政治・宗教
democracy, legislation, faith, doctrine...

</div>

<div class="bg-red-500/10 p-3 rounded">

### 🔒 法律・犯罪
lawsuit, defendant, evidence, verdict...

</div>

<div class="bg-green-500/10 p-3 rounded">

### 🎓 教育
curriculum, pedagogy, scholarship...

</div>

<div class="bg-teal-500/10 p-3 rounded">

### 🔬 科学
hypothesis, experiment, molecule...

</div>

<div class="bg-orange-500/10 p-3 rounded">

### 🏥 健康
symptom, diagnosis, treatment...

</div>

</v-clicks>

</div>

---

# ⚡ 副詞 (Adverbs)

位置による分類で使い分けをマスター

<v-clicks>

<div class="mt-6">

## 📍 文頭の副詞
- **However**, I disagree with that opinion.
- **Moreover**, this approach has several benefits.
- **Consequently**, we need to revise our plan.

</div>

<div class="mt-6">

## 📍 文中の副詞
- She **always** arrives on time.
- They are **probably** going to attend.
- I **completely** understand your concern.

</div>

<div class="mt-6">

## 📍 文末の副詞
- She speaks English **fluently**.
- They worked **hard** on the project.
- He answered the question **correctly**.

</div>

</v-clicks>

---
layout: section
---

# ✏️ 実践練習

知識を実践に移す

---

# 練習エリアの活用

<div class="grid grid-cols-2 gap-6 mt-8">

<v-clicks>

<div>

## 📰 Sandbox
実践的な練習エリア

- **トピック練習**
  - Future of Food
  - 様々なテーマで表現練習

- **日常会話 (Today)**
  - 日々の出来事を英語で表現

</div>

<div>

## 🎯 フォーカス項目

- **Opening練習**
  - 会話の始め方

- **YouTube学習**
  - 動画コンテンツの活用

- **スクリプト練習**
  - Clarification
  - Format
  - Order

</div>

</v-clicks>

</div>

---
layout: center
class: text-center
---

# 学習の成果

<div class="grid grid-cols-3 gap-8 mt-12">

<v-clicks>

<div>
<div class="text-5xl font-bold text-blue-500 mb-2">3hrs</div>
<div class="text-xl">毎日の学習時間</div>
</div>

<div>
<div class="text-5xl font-bold text-green-500 mb-2">80+</div>
<div class="text-xl">1日の単語目標</div>
</div>

<div>
<div class="text-5xl font-bold text-purple-500 mb-2">6</div>
<div class="text-xl">学習セッション</div>
</div>

</v-clicks>

</div>

---

# リポジトリ構造

```
English/
├── README.md              # 学習プラン
├── sandbox/               # 練習用エリア
│   ├── future_of_food.md
│   ├── today.md
│   └── youtube.md
├── thesis/                # 理論・文法
│   ├── 0_pronunciation.md
│   └── 1_grammer.md
└── words/                 # 単語・表現集
    ├── 02_verb/          # 動詞
    ├── 03_adjective_noun/ # 形容詞・名詞
    ├── 04_adverb/        # 副詞
    ├── script/           # スクリプト
    └── temp/             # 一時ファイル
```

---
layout: center
class: text-center
---

# Key Takeaways

<v-clicks>

## 🎯 体系的アプローチ
発音→文法→語彙→実践の順序立てた学習

## 🔄 反復と継続
毎日3時間、6セッションの習慣化

## 📚 カテゴリ別整理
品詞別・トピック別の効率的な語彙習得

## 💪 実践重視
Sandboxでの実践的な練習とアウトプット

</v-clicks>

---
layout: center
class: text-center
---

# ありがとうございました

### 継続は力なり
**Consistency is key to success**

<div class="mt-12">
  <a href="https://github.com/namtoki/English" target="_blank" class="text-xl">
    📚 GitHub Repository
  </a>
</div>

<div class="abs-br m-6 text-sm opacity-50">
  English Learning Journey 2025
</div>
