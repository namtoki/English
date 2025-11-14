---
theme: default
background: /mario.gif
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
  position: absolute;
  left: 0;
}

.new-text.slidev-vclick-current {
  animation: fade-in-up 1.2s ease-out forwards;
  animation-delay: 0.8s;
}

@keyframes fade-in-up {
  0% {
    transform: translateY(0) scale(0.9);
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
    英語学習<span style="position: relative; display: inline-block;"><span v-click.hide="1" class="crumble-text"><span class="crumble-char" style="--delay: 0">教</span><span class="crumble-char" style="--delay: 1">え</span><span class="crumble-char" style="--delay: 2">ま</span><span class="crumble-char" style="--delay: 3">す</span><span class="crumble-char" style="--delay: 4">！</span></span><span v-click="1" class="new-text">仲間募集中</span></span>
  </div>
</div>

<div v-click="1" class="subtitle">
  📚 継続的な学習で英語力を向上させる旅
</div>

---
transition: fade-out
---

# 英語遍歴

<div class="chart-container">
  <canvas id="englishJourneyChart"></canvas>
</div>

<div v-click="1" style="height: 0; overflow: hidden;"></div>
<div v-click="2" style="height: 0; overflow: hidden;"></div>
<div v-click="3" style="height: 0; overflow: hidden;"></div>
<div v-click="4" style="height: 0; overflow: hidden;"></div>
<div v-click="5" style="height: 0; overflow: hidden;"></div>
<div v-click="6" style="height: 0; overflow: hidden;"></div>
<div v-click="7" style="height: 0; overflow: hidden;"></div>
<div v-click="8" style="height: 0; overflow: hidden;"></div>
<div v-click="9" style="height: 0; overflow: hidden;"></div>
<div v-click="10" style="height: 0; overflow: hidden;"></div>
<div v-click="11" style="height: 0; overflow: hidden;"></div>

<script setup>
import { onMounted, watch, ref } from 'vue'

const allDataPoints = [
  { x: '2008-01-01', y: 30 },
  { x: '2015-01-01', y: 20 },
  { x: '2022-01-01', y: 10 },
  { x: '2024-05-01', y: 30 },
  { x: '2024-11-01', y: 30 },
  { x: '2025-06-01', y: 50 }
]

let chart = null
let showImage = false
let showSatoriImage = false
let showToeic2022Image = false
let showToeic202405Image = false
let showToeic202411Image = false
let showEiken202506Image = false

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
        // Load images with base path
        const basePath = import.meta.env.BASE_URL || '/'

        const kikutanImg = new Image()
        kikutanImg.src = basePath + 'kikutan.png'

        const satoriImg = new Image()
        satoriImg.src = basePath + 'satori.png'

        const toeic2022Img = new Image()
        toeic2022Img.src = basePath + 'toeic-2022.png'

        const toeic202405Img = new Image()
        toeic202405Img.src = basePath + 'toeic-202406.png'

        const toeic202411Img = new Image()
        toeic202411Img.src = basePath + 'toeic-202411.png'

        const eiken202506Img = new Image()
        eiken202506Img.src = basePath + 'toeic-eiken-202506.png'

        // Helper function to draw image at data point
        const drawImageAtPoint = (ctx, img, baseX, baseY, width, height, offsetX = 0, offsetY = null) => {
          const finalOffsetY = offsetY !== null ? offsetY : -height - 10
          ctx.drawImage(img, baseX + offsetX - width/2, baseY + finalOffsetY, width, height)
        }

        const imagePlugin = {
          id: 'imagePlugin',
          afterDatasetsDraw(chart) {
            if (!showImage) return

            const { ctx, chartArea: { top, bottom, left, right }, scales: { x, y } } = chart
            const meta = chart.getDatasetMeta(0)

            meta.data.forEach((dataPoint, index) => {
              const baseX = dataPoint.x
              const baseY = dataPoint.y

              if (index === 0 && kikutanImg.complete) {
                drawImageAtPoint(ctx, kikutanImg, baseX+60, baseY, 120, 120)
              }

              if (index === 1 && satoriImg.complete && showSatoriImage) {
                drawImageAtPoint(ctx, satoriImg, baseX, baseY, 100, 120)
              }

              if (index === 2 && toeic2022Img.complete && showToeic2022Image) {
                drawImageAtPoint(ctx, toeic2022Img, baseX-60, baseY, 90, 65)
              }

              if (index === 3 && toeic202405Img.complete && showToeic202405Image) {
                drawImageAtPoint(ctx, toeic202405Img, baseX-80, baseY, 90, 65)
              }

              if (index === 4 && toeic202411Img.complete && showToeic202411Image) {
                drawImageAtPoint(ctx, toeic202411Img, baseX-50, baseY-30, 90, 65)
              }

              if (index === 5 && eiken202506Img.complete && showEiken202506Image) {
                drawImageAtPoint(ctx, eiken202506Img, baseX-80, baseY-10, 180, 110)
              }
            })
          }
        }

        chart = new Chart(ctx, {
          type: 'line',
          data: {
            datasets: [{
              label: '英語の理解度',
              data: [allDataPoints[0]],
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
          plugins: [imagePlugin],
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
                min: '2008-01-01',
                max: '2025-06-01',
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

watch($clicks, (clicks) => {
  if (!chart) return

  // Reset all image flags
  showImage = false
  showSatoriImage = false
  showToeic2022Image = false
  showToeic202405Image = false
  showToeic202411Image = false
  showEiken202506Image = false

  if (clicks === 0) {
    // Initial state: first data point only, no image
    chart.data.datasets[0].data = allDataPoints.slice(0, 1)
  } else if (clicks === 1) {
    // First click: show kikutan image on 2008 point
    chart.data.datasets[0].data = allDataPoints.slice(0, 1)
    showImage = true
  } else if (clicks === 2) {
    // Second click: extend to 2015
    chart.data.datasets[0].data = allDataPoints.slice(0, 2)
    showImage = true
  } else if (clicks === 3) {
    // Third click: show satori image on 2015 point
    chart.data.datasets[0].data = allDataPoints.slice(0, 2)
    showImage = true
    showSatoriImage = true
  } else if (clicks === 4) {
    // Fourth click: extend to 2022
    chart.data.datasets[0].data = allDataPoints.slice(0, 3)
    showImage = true
    showSatoriImage = true
  } else if (clicks === 5) {
    // Fifth click: show toeic-2022 image on 2022 point
    chart.data.datasets[0].data = allDataPoints.slice(0, 3)
    showImage = true
    showSatoriImage = true
    showToeic2022Image = true
  } else if (clicks === 6) {
    // Sixth click: extend to 2024/5
    chart.data.datasets[0].data = allDataPoints.slice(0, 4)
    showImage = true
    showSatoriImage = true
    showToeic2022Image = true
  } else if (clicks === 7) {
    // Seventh click: show toeic-202405 image on 2024/5 point
    chart.data.datasets[0].data = allDataPoints.slice(0, 4)
    showImage = true
    showSatoriImage = true
    showToeic2022Image = true
    showToeic202405Image = true
  } else if (clicks === 8) {
    // Eighth click: extend to 2024/11
    chart.data.datasets[0].data = allDataPoints.slice(0, 5)
    showImage = true
    showSatoriImage = true
    showToeic2022Image = true
    showToeic202405Image = true
  } else if (clicks === 9) {
    // Ninth click: show toeic-202411 image on 2024/11 point
    chart.data.datasets[0].data = allDataPoints.slice(0, 5)
    showImage = true
    showSatoriImage = true
    showToeic2022Image = true
    showToeic202405Image = true
    showToeic202411Image = true
  } else if (clicks === 10) {
    // Tenth click: extend to 2025/6
    chart.data.datasets[0].data = allDataPoints.slice(0, 6)
    showImage = true
    showSatoriImage = true
    showToeic2022Image = true
    showToeic202405Image = true
    showToeic202411Image = true
  } else if (clicks >= 11) {
    // Eleventh click: show eiken-202506 image on 2025/6 point
    chart.data.datasets[0].data = allDataPoints.slice(0, 6)
    showImage = true
    showSatoriImage = true
    showToeic2022Image = true
    showToeic202405Image = true
    showToeic202411Image = true
    showEiken202506Image = true
  }

  chart.update()
})
</script>

<style scoped>
.chart-container {
  width: 85%;
  max-width: 900px;
  height: 450px;
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

# 目標設定と学習時間

<v-clicks>

<div class="grid grid-cols-2 gap-6 mt-6">

<div class="bg-green-500/10 p-4 rounded">

### ビジネス英語
**1,500〜2,000時間**

ビジネスの場で最低限の会話が成立する

<div class="mt-3 text-sm">
毎日2時間：2〜3年<br>
毎日3時間：1.5〜2年
</div>

</div>

<div class="bg-purple-500/10 p-4 rounded">

### 日常英会話
**3,000〜5,000時間**

ネイティブ並みの日常会話

<div class="mt-3 text-sm">
毎日2時間：4〜7年<br>
毎日3時間：3〜5年
</div>

</div>

</div>

## 📚 難関資格との比較

- **公認会計士**：3,000〜5,000時間
- **司法試験**：5,000〜8,000時間以上
- **医師国家試験**（医学部6年間）：10,000時間以上

<div class="mt-4 text-sm opacity-80">
💡 ネイティブ並みの日常英会話は公認会計士や司法試験と同等かそれ以上の学習時間が必要
</div>

</v-clicks>

---
layout: center
class: text-center
---

<div class="video-container">
  <iframe
    id="youtube-video"
    <!-- src="https://www.youtube.com/embed/X2MNJVPcX3Q?si=MqmBrKx-p_2mHo48?autoplay=1&start=0&end=10&mute=0&controls=0&modestbranding=1&rel=0" -->
    src="https://www.youtube.com/embed/VIDEO_ID?autoplay=1&start=0&end=10&mute=0&controls=0&modestbranding=1&rel=0"
    frameborder="0"
    allow="autoplay; encrypted-media"
    allowfullscreen
  ></iframe>
</div>

<style scoped>
.video-container {
  position: relative;
  width: 100vw;
  height: 100vh;
  margin: -2rem -2rem;
}

.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>

---
layout: center
class: text-center
---

<div class="transition-message">
  <h1 class="text-6xl font-bold mb-8" v-click>
    英語学習には<br>時間がかかる
  </h1>

  <div v-click class="text-5xl font-bold text-blue-400 mt-12 mb-8">
    だからこそ
  </div>

  <h2 v-click class="text-7xl font-bold text-gradient">
    効率的な学習が必要！
  </h2>
</div>

<style scoped>
.transition-message {
  padding: 2rem;
}

.text-gradient {
  background: linear-gradient(45deg, #12c2e9, #c471ed, #f64f59);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: gradient-shift 3s ease infinite;
}

@keyframes gradient-shift {
  0%, 100% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
}
</style>

---
transition: fade-out
---

# ラフな目標設定と計画

<div class="compact-layout">

<v-clicks>

## 🎯 目標：ビジネス英語レベル（2,000時間）

**1日2.5時間** × 週5日 = 週12.5時間 → **3年で1,950時間** ✨

## ⏰ 1日2.5時間をどう捻出するか？

| 時間帯 | 内容 | 時間 |
|--------|------|------|
| 🌅 朝 | 朝の学習 | 30分 |
| 🚃 通勤時間 | 家→駅 | 20分 |
| 🍱 12:00-12:40 | 昼休み | 40分 |
| 🌙 就寝前 | リラックス学習 | 60分 |

<div class="total-box">
合計：<strong>2.5時間</strong>/日
</div>

</v-clicks>

<div v-click class="stamp-overlay">
  <div class="stamp-inner">
    <div class="stamp-label">現在</div>
    <div class="stamp-hours">1,250時間</div>
    <div class="stamp-sublabel">達成済み</div>
  </div>
</div>

</div>

<style scoped>
.compact-layout {
  font-size: 0.9rem;
  position: relative;
}

.compact-layout h2 {
  font-size: 1.3rem;
  margin: 0.8rem 0;
}

.stamp-overlay {
  position: absolute;
  top: 50%;
  right: 10%;
  background: rgba(239, 68, 68, 0.15);
  border: 3px solid rgba(239, 68, 68, 0.6);
  border-radius: 50%;
  width: 140px;
  height: 140px;
  display: flex;
  align-items: center;
  justify-content: center;
  transform: translate(0, -50%) rotate(-12deg);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 10;
}

.stamp-inner {
  text-align: center;
  color: rgba(239, 68, 68, 0.9);
  font-weight: bold;
}

.stamp-label {
  font-size: 0.7rem;
  margin-bottom: 0.2rem;
}

.stamp-hours {
  font-size: 1.3rem;
  line-height: 1.2;
  margin: 0.2rem 0;
}

.stamp-sublabel {
  font-size: 0.65rem;
  margin-top: 0.2rem;
}

.compact-layout table {
  width: 100%;
  border-collapse: collapse;
  background: white;
  border-radius: 8px;
  overflow: hidden;
  font-size: 0.85rem;
  margin: 0.5rem 0;
}

.compact-layout th,
.compact-layout td {
  padding: 0.5rem;
  text-align: left;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}

.compact-layout th {
  background: rgba(59, 130, 246, 0.1);
  font-weight: bold;
}

.total-box {
  background: rgba(147, 51, 234, 0.1);
  padding: 0.8rem;
  border-radius: 8px;
  text-align: center;
  font-size: 1.1rem;
  margin-top: 0.8rem;
}
</style>

---
transition: fade-out
---

