---
theme: default
background: /robot.gif
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
  font-size: 4.5rem;
}

.subtitle {
  font-size: 1.5rem;
}

.author-info {
  position: absolute;
  bottom: 2rem;
  right: 1rem;
  text-align: right;
  color: white;
  font-size: 1rem;
}

.author-name {
  font-weight: bold;
  margin-bottom: 0.3rem;
}

.author-department {
  font-size: 0.9rem;
  opacity: 0.9;
}
</style>

<div class="title-container">
  <div class="title-text">
    コツコツ続ける英語学習
  </div>
</div>

<div class="subtitle">
  📚 天才ではない人のための地道な足掻き
</div>

<div class="author-info">
  <div class="author-name">棚村俊之</div>
  <div class="author-department">Product Software Headphone team</div>
</div>

---

# 自己紹介

<div class="profile-layout">

<v-clicks>

<div class="profile-header">
  <h2>棚村俊之</h2>
  <p class="join-date">2023年10月 中途入社</p>
  <p class="department">Product Software Headphone team</p>
</div>

<div class="career-timeline">
  <div class="career-item">
    <img src="/pioneer.png" alt="Pioneer" class="company-logo logo-pioneer" />
    <div class="duration">3年弱</div>
  </div>
  <div class="career-item fixstars-container">
    <img src="/fixstars.png" alt="Fixstars" class="company-logo logo-fixstars" />
    <div class="duration">6年弱</div>
  </div>
  <div class="career-item">
    <img src="/optim.png" alt="OPTiM" class="company-logo logo-optim" />
    <div class="duration">3年弱</div>
  </div>
  <div class="career-item current">
    <img src="/dandm.png" alt="D&M" class="company-logo logo-dandm" />
    <div class="duration">現在</div>
  </div>
</div>

<img v-click src="/fixstars-okinawa.jpg" alt="Fixstars Okinawa" class="fixstars-okinawa" />

<div class="info-section">
  <p><strong>Like:</strong> Vim, Claude, Swift, Flutter, ROS,,,</p>
  <p><strong>最近は AWS, Terraform など Cloud 関連勉強中</strong></p>
</div>

<div v-click class="flutterkaigi-images">
  <img src="/flutterkaigi1.jpg" alt="FlutterKaigi 1" class="flutterkaigi-img" />
  <img src="/flutterkaigi2.jpg" alt="FlutterKaigi 2" class="flutterkaigi-img" />
</div>

<div class="hometown">
  <p>名古屋出身でベイスターズファン</p>
</div>

</v-clicks>

</div>

<style scoped>
.profile-layout {
  padding: 1rem 2rem;
  background: linear-gradient(135deg, rgba(245, 222, 179, 0.3), rgba(255, 248, 220, 0.3));
  position: relative;
}

.profile-header {
  text-align: center;
  margin-bottom: 1rem;
}

.profile-header h2 {
  font-size: 1.6rem;
  color: #5d4037;
  margin-bottom: 0.3rem;
}

.join-date {
  font-size: 1rem;
  color: #333;
  font-weight: 500;
}

.department {
  font-size: 0.9rem;
  color: #666;
  font-weight: 400;
  margin-top: 0.3rem;
}

.career-timeline {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 0.8rem;
  margin-bottom: 1rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.6);
  border-radius: 12px;
}

.career-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.3rem;
}

.fixstars-container {
  position: relative;
}

.company-logo {
  width: auto;
  object-fit: contain;
}

.logo-pioneer {
  height: 30px;  /* 3年 ≈ 50% */
}

.logo-fixstars {
  height: 50px;  /* 6年 = 100% (最大) */
}

.logo-optim {
  height: 30px;  /* 3年 ≈ 50% */
}

.logo-dandm {
  height: 25px;  /* 2年 ≈ 33% */
}

.fixstars-okinawa {
  position: absolute;
  top: 200px;
  left: 53%;
  transform: translateX(-50px);
  width: 150px;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  z-index: 10;
}

.flutterkaigi-images {
  position: absolute;
  top: 275px;
  left: 72%;
  transform: translateX(-50px);
  display: flex;
  gap: 0.5rem;
  z-index: 10;
}

.flutterkaigi-img {
  width: 140px;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}

.duration {
  font-size: 0.8rem;
  color: #666;
  font-weight: 500;
}

.career-item.current .duration {
  color: rgba(16, 185, 129, 1);
  font-weight: bold;
}

.info-section {
  background: rgba(255, 255, 255, 0.7);
  border-radius: 12px;
  padding: 1rem;
  margin-bottom: 0.8rem;
}

.info-section p {
  font-size: 0.95rem;
  color: #333;
  margin: 0.5rem 0;
}

.info-section strong {
  color: #5d4037;
}

.hometown {
  text-align: center;
  padding: 0.8rem;
  background: rgba(255, 255, 255, 0.5);
  border-radius: 12px;
  border: 2px dashed rgba(239, 68, 68, 0.4);
}

.hometown p {
  font-size: 1rem;
  color: #333;
  margin: 0;
  font-weight: 500;
}
</style>

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
  { x: '2008-01-01', y: 40 },
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
        // Set high resolution for canvas
        const dpr = window.devicePixelRatio || 2
        const rect = ctx.getBoundingClientRect()
        ctx.width = rect.width * dpr
        ctx.height = rect.height * dpr
        ctx.style.width = rect.width + 'px'
        ctx.style.height = rect.height + 'px'

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
              borderWidth: 4,
              pointRadius: 6,
              pointBackgroundColor: 'rgb(75, 192, 192)',
              pointBorderColor: '#fff',
              pointBorderWidth: 3,
              pointHoverRadius: 8
            }]
          },
          plugins: [imagePlugin],
          options: {
            responsive: true,
            maintainAspectRatio: true,
            devicePixelRatio: Math.max(window.devicePixelRatio || 2, 3),
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
                    size: 16,
                    weight: '500'
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
                    size: 16,
                    weight: '500'
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
                    size: 16,
                    weight: '500'
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

.chart-container canvas {
  image-rendering: -webkit-optimize-contrast;
  image-rendering: crisp-edges;
}
</style>

---
transition: fade-out
---

# 何故英語を勉強し始めたのか

<div class="simple-reason-layout">

<div v-click>
  <div class="reason-text">
    入社したら隣に外国人がいたから
  </div>
</div>

<div class="image-container">
  <div v-click="1" class="image-placeholder image-main">
    <img src="/foreigner.gif" alt="外国人の同僚" class="reason-image" />
  </div>
  <div v-click="2" class="image-placeholder image-small">
    <img src="/kaonashi.jpg" alt="カオナシ" class="reason-image reason-image-small" />
  </div>
</div>

</div>

<style scoped>
.simple-reason-layout {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  padding: 1rem 2rem;
  gap: 1.5rem;
}

.reason-text {
  font-size: 1.5rem;
  font-weight: bold;
  text-align: center;
  color: #333;
  margin-bottom: 1rem;
}

.image-container {
  display: flex;
  gap: 1rem;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 100%;
  min-height: 300px;
}

.image-placeholder {
  display: flex;
  justify-content: center;
  align-items: center;
}

.image-main {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}

.image-small {
  position: absolute;
  left: 50%;
  transform: translateX(calc(150px + 0.5rem));
}

.reason-image {
  max-width: 100%;
  max-height: 300px;
  object-fit: contain;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.reason-image-small {
  max-height: 150px;
}
</style>

---
transition: fade-out
---

# 素数を数えて落ち着くんだ...

<v-clicks>

<div class="grid grid-cols-2 gap-6 mt-6">

<div class="bg-green-500/10 p-4 rounded goal-box">

### ビジネス英語
**1,500〜2,000時間**

ビジネスの場で最低限の会話が成立する

<div class="mt-3 text-sm">
毎日2時間：2〜3年<br>
毎日3時間：1.5〜2年
</div>

</div>

<div class="bg-purple-500/10 p-4 rounded goal-box">

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

<div v-click class="pc-overlay">
  <img src="/pc.gif" alt="PC" class="pc-image" />
</div>

<style scoped>
.goal-box {
  transition: transform 0.3s ease;
}

.goal-box:hover {
  transform: translateY(-5px);
}

.pc-overlay {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 100;
  display: flex;
  justify-content: center;
  align-items: center;
}

.pc-image {
  max-width: 600px;
  max-height: 500px;
  object-fit: contain;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}
</style>

---
layout: center
class: text-center
---

<div class="transition-message">
  <h1 class="text-6xl font-bold mb-8" v-click>
    英語学習には時間がかかる...
  </h1>

  <div v-click class="text-5xl font-bold text-blue-400 mt-12 mb-8">
    だからこそ
  </div>

  <h1 v-click class="text-7xl font-bold text-gradient">
    計画的な学習とモチベーション管理が必要！
  </h1>
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

# どれくらいで終わるかな...

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
    <div class="stamp-hours">約1,200時間</div>
    <div class="stamp-sublabel">達成済み(たぶん)</div>
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

# どんな学習をすればいいんだ？

<div class="learning-method-layout">

<v-clicks>

<div class="thought-box">
  <p>「幼少期以降に勉強して英語がネイティブのように話せるようになった日本人」がやっていたことを真似よう</p>
</div>

<div class="thought-box doubt">
  <p>いや、ていうかその人がネイティブのように話せているのか判断がつかない</p>
</div>

<div class="thought-box idea">
  <p>逆に「幼少期以降に日本語を勉強してネイティブのように話せるようになった英語話者」を参考にした方が良いのでは？と思い当たる</p>
</div>

<div class="discovery-section">
  <h3>📚 2名の該当者を見つけ、超インプット学習が大事であることを知る</h3>

  <div class="video-container">
    <div class="video-wrapper">
      <iframe
        src="https://www.youtube.com/embed/NS97LNh-fQQ?start=132&end=175"
        title="YouTube video 1"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
      </iframe>
    </div>
    <div class="video-wrapper">
      <iframe
        src="https://www.youtube.com/embed/_l0mg-K3JlU?start=176&end=200"
        title="YouTube video 2"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
      </iframe>
    </div>
  </div>
</div>

</v-clicks>

</div>

<style scoped>
.learning-method-layout {
  padding: 0.5rem 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.thought-box {
  background: rgba(59, 130, 246, 0.1);
  border-left: 4px solid rgba(59, 130, 246, 0.6);
  padding: 0.6rem 1rem;
  border-radius: 8px;
  font-size: 0.8rem;
  line-height: 1.4;
}

.thought-box.doubt {
  background: rgba(245, 158, 11, 0.1);
  border-left-color: rgba(245, 158, 11, 0.6);
}

.thought-box.idea {
  background: rgba(16, 185, 129, 0.1);
  border-left-color: rgba(16, 185, 129, 0.6);
}

.thought-box p {
  margin: 0;
  color: #333;
}

.discovery-section {
  margin-top: 0.5rem;
}

.discovery-section h3 {
  font-size: 0.95rem;
  color: rgba(16, 185, 129, 1);
  margin-bottom: 0.5rem;
  text-align: center;
}

.video-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-top: 0.5rem;
}

.video-wrapper {
  position: relative;
  padding-bottom: 40%;
  height: 0;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.video-wrapper iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>

---
transition: fade-out
---

# 何からやろうか...

<div class="skill-image-container">
  <img src="/skill.png" alt="4技能と学習領域" class="skill-chart" />

  <div v-click="1" class="focus-box">
    <div class="focus-label">とりあえずここやろう</div>
  </div>

  <div v-click="2" class="book-images">
    <img src="/duo.jpg" alt="DUO" class="book-img" />
    <img src="/ichiokunin.jpg" alt="一億人の英文法" class="book-img" />
    <img src="/shineibunpo.jpg" alt="真・英文法大全" class="book-img" />
    <img src="/toshizu.jpg" alt="トシズ" class="book-img" />
    <img src="/porepore.jpg" alt="ポレポレ" class="book-img" />
  </div>
</div>

<style scoped>
.skill-image-container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 4rem;
  height: 100%;
}

.skill-chart {
  max-width: 90%;
  max-height: 80vh;
  width: auto;
  height: auto;
  object-fit: contain;
}

.focus-box {
  position: absolute;
  top: 79%;
  left: 51.5%;
  width: 600px;
  height: 100px;
  border: 4px solid red;
  background: transparent;
  transform: translate(-50%, -50%);
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding-top: 0.5rem;
}

.focus-label {
  background: rgba(255, 0, 0, 0.9);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-weight: bold;
  font-size: 1rem;
  white-space: nowrap;
}

.book-images {
  position: absolute;
  top: 55%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  gap: 1rem;
  z-index: 10;
  align-items: flex-end;
  flex-wrap: wrap;
  justify-content: center;
  max-width: 90%;
}

.book-img {
  height: 180px;
  width: auto;
  object-fit: contain;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  border-radius: 4px;
}
</style>

---
---

# モチベーションが続かない...

<div class="motivation-page">
  <div v-click class="solution-content">
    <h2 class="solution-title">YouTube で楽しく発音勉強</h2>
    <div class="solution-items">
      <div class="solution-item">
        <img src="/atsuhatuon.png" alt="Atsu発音講座" class="solution-img" />
        <p class="solution-text">Atsuさんの発音講座で<br>発音の基礎を学習</p>
      </div>
      <div class="solution-item">
        <img src="/youtube.png" alt="YouTube" class="solution-img" />
        <p class="solution-text">YouTubeでネイティブの<br>発音にたくさん触れた</p>
      </div>
    </div>
  </div>
</div>

<style scoped>
.motivation-page {
  padding: 1rem 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
}

.solution-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
}

.solution-title {
  font-size: 2rem;
  font-weight: bold;
  color: #10b981;
  margin: 0;
}

.solution-items {
  display: flex;
  gap: 2rem;
  align-items: flex-start;
  justify-content: center;
}

.solution-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.8rem;
}

.solution-img {
  width: 180px;
  height: auto;
  object-fit: contain;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  border-radius: 8px;
}

.solution-item:nth-child(2) .solution-img {
  width: 370px;
}

.solution-text {
  font-size: 1rem;
  font-weight: 600;
  text-align: center;
  line-height: 1.5;
  color: #333;
}
</style>

---
transition: fade-out
---

# まずは基礎固め：文法と単語とちょびっと発音

<div class="foundation-layout">

<v-clicks>

## 📚 取り組んだこと（2023年10月〜2024年5月：半年間）

<div class="approach-box">
  <div class="approach-item foundation-approach">
    <h3>📖 文法</h3>
    <p>基礎文法を一から学び直し</p>
  </div>

  <div class="approach-item foundation-approach">
    <h3>📝 単語</h3>
    <p>頻出単語を集中的に学習</p>
  </div>
</div>

## 🎯 成果

<div class="result-box">
  <div class="result-year">2024年5月</div>
  <div class="result-score">TOEIC <span class="score-number">755</span>点 取得</div>
  <div class="result-comment">半年間の基礎固めで着実にスコアアップ！</div>

  <div v-click class="timeline-container">
    <img src="/timeline.png" alt="Timeline" class="timeline-img" />
    <div class="timeline-focus-box"></div>
  </div>
</div>

</v-clicks>

</div>

<style scoped>
.foundation-layout {
  padding: 1rem 2rem;
}

.foundation-layout h2 {
  margin-bottom: 1rem;
  font-size: 1.3rem;
}

.approach-box {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.approach-item {
  background: rgba(59, 130, 246, 0.1);
  border: 2px solid rgba(59, 130, 246, 0.3);
  border-radius: 12px;
  padding: 1rem;
  text-align: center;
  transition: transform 0.3s ease;
}

.foundation-approach:hover {
  transform: translateY(-5px);
}

.approach-item h3 {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

.approach-item p {
  font-size: 0.9rem;
  margin: 0.3rem 0;
  color: #333;
}

.result-box {
  position: relative;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(59, 130, 246, 0.2));
  border: 3px solid rgba(16, 185, 129, 0.5);
  border-radius: 16px;
  padding: 1.5rem;
  text-align: center;
  max-width: 600px;
  margin: 0 auto;
}

.result-year {
  font-size: 1.1rem;
  font-weight: bold;
  color: rgba(16, 185, 129, 1);
  margin-bottom: 0.8rem;
}

.result-score {
  font-size: 1.8rem;
  font-weight: bold;
  margin-bottom: 0.8rem;
  color: #333;
}

.score-number {
  font-size: 2.5rem;
  color: rgba(16, 185, 129, 1);
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.result-comment {
  font-size: 1rem;
  color: #444;
  font-style: italic;
}

.timeline-container {
  position: absolute;
  top: -20px;
  right: -60px;
  width: 200px;
  height: 150px;
}

.timeline-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.timeline-focus-box {
  position: absolute;
  top: 50%;
  left: 89%;
  width: 15px;
  height: 80px;
  border: 2px solid red;
  background: transparent;
  transform: translate(-50%, -50%);
}
</style>

---
transition: fade-out
---

# 次の挑戦：英会話

<div class="foundation-layout conversation">

<v-clicks>

## 🗣️ 取り組んだこと（2024年6月〜11月：半年間）

<div class="approach-box">
  <div class="approach-item failure conversation-approach">
    <h3>💬 英会話</h3>
    <p>オンライン英会話に挑戦</p>
  </div>

  <div class="approach-item failure conversation-approach">
    <h3>🤔 結果</h3>
    <p>何も口から出ない...</p>
  </div>
</div>

## 😰 課題発見

<div class="result-box failure">
  <div class="result-year failure">2024年11月</div>
  <div class="result-score">TOEIC <span class="score-number">750</span>点（変化なし）</div>
  <div class="result-comment failure">
    <strong>英語のリズム</strong>と<strong>語法の知見</strong>が無いと何も話せない...
  </div>

  <div v-click class="timeline-container">
    <img src="/timeline.png" alt="Timeline" class="timeline-img" />
    <div class="timeline-focus-box-2"></div>
  </div>
</div>

</v-clicks>

</div>

<style scoped>
.foundation-layout {
  padding: 1rem 2rem;
}

.foundation-layout h2 {
  margin-bottom: 1rem;
  font-size: 1.3rem;
}

.approach-box {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.approach-item {
  background: rgba(59, 130, 246, 0.1);
  border: 2px solid rgba(59, 130, 246, 0.3);
  border-radius: 12px;
  padding: 1rem;
  text-align: center;
}

.approach-item.failure {
  background: rgba(239, 68, 68, 0.05);
  border: 2px solid rgba(239, 68, 68, 0.3);
}

.conversation-approach:hover {
  transform: translateY(-5px);
}

.approach-item h3 {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

.approach-item p {
  font-size: 0.9rem;
  margin: 0.3rem 0;
  color: #333;
}

.result-box {
  position: relative;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(59, 130, 246, 0.2));
  border: 3px solid rgba(16, 185, 129, 0.5);
  border-radius: 16px;
  padding: 1.5rem;
  text-align: center;
  max-width: 600px;
  margin: 0 auto;
}

.result-box.failure {
  background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(245, 158, 11, 0.1));
  border: 3px solid rgba(239, 68, 68, 0.5);
}

.result-year {
  font-size: 1.1rem;
  font-weight: bold;
  color: rgba(16, 185, 129, 1);
  margin-bottom: 0.8rem;
}

.result-year.failure {
  color: rgba(239, 68, 68, 1);
}

.result-score {
  font-size: 1.8rem;
  font-weight: bold;
  margin-bottom: 0.8rem;
  color: #333;
}

.score-number {
  font-size: 2.5rem;
  color: rgba(16, 185, 129, 1);
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.result-comment {
  font-size: 1rem;
  color: #444;
  font-style: italic;
}

.result-comment.failure {
  font-size: 1rem;
  color: #333;
  font-style: normal;
  line-height: 1.5;
}

.result-comment.failure strong {
  color: rgba(239, 68, 68, 1);
  font-weight: bold;
}

.foundation-layout.conversation .approach-box {
  gap: 1rem;
  margin-bottom: 1rem;
}

.foundation-layout.conversation h2 {
  margin-bottom: 0.8rem;
  font-size: 1.2rem;
}

.foundation-layout.conversation {
  padding: 0.5rem 2rem;
}

.foundation-layout.conversation .result-box {
  padding: 1.2rem;
}

.foundation-layout.conversation .result-comment.failure {
  font-size: 0.95rem;
}

.timeline-container {
  position: absolute;
  top: -20px;
  right: -60px;
  width: 200px;
  height: 150px;
}

.timeline-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.timeline-focus-box-2 {
  position: absolute;
  top: 50%;
  left: 94%;
  width: 8px;
  height: 80px;
  border: 2px solid red;
  background: transparent;
  transform: translate(-50%, -50%);
}
</style>

---
transition: fade-out
---

# 再挑戦：英文のリズムと語法

<div class="foundation-layout conversation">

<v-clicks>

## 📚 取り組んだこと（2024年11月〜2025年5月）

<div class="approach-box">
  <div class="approach-item rechallenge-approach">
    <h3>🗣️ 発音</h3>
    <p>発音の応用知識を学習</p>
    <img src="/doctord.png" alt="ドクターD" class="approach-book-img" />
  </div>
  <div class="approach-item rechallenge-approach">
    <h3>📖 語法</h3>
    <p>表現パターンを習得</p>
  </div>
  <div class="approach-item rechallenge-approach">
    <h3>💭 英語の気持ち</h3>
    <p>新書が結構面白い</p>
    <img src="/nihonjin.jpg" alt="一億人の英文法" class="approach-book-img" />
  </div>
</div>

## 🎯 成果

<div class="result-box">
  <div class="result-year">2025年6月</div>
  <div class="result-score">TOEIC <span class="score-number">840</span>点</div>
  <div class="result-comment">
    <strong>発音</strong>と<strong>語法</strong>の学習でスコアアップ！
  </div>

  <div v-click class="timeline-container">
    <img src="/timeline.png" alt="Timeline" class="timeline-img" />
    <div class="timeline-focus-box-3"></div>
  </div>
</div>

</v-clicks>

</div>

<style scoped>
.foundation-layout {
  padding: 1rem 2rem;
}

.foundation-layout.conversation {
  padding: 0.2rem 1.5rem;
}

.foundation-layout h2 {
  margin-bottom: 1rem;
  font-size: 1.3rem;
}

.foundation-layout.conversation h2 {
  margin-bottom: 0.3rem;
  font-size: 1rem;
}

.approach-box {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.foundation-layout.conversation .approach-box {
  grid-template-columns: 1fr 1fr 1fr;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.approach-item {
  background: rgba(59, 130, 246, 0.1);
  border: 2px solid rgba(59, 130, 246, 0.3);
  border-radius: 12px;
  padding: 0.8rem;
  text-align: center;
}

.rechallenge-approach:hover {
  transform: translateY(-5px);
}

.foundation-layout.conversation .approach-item {
  padding: 0.5rem;
}

.approach-book-img {
  width: 80px;
  height: auto;
  margin-top: 0.3rem;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.foundation-layout.conversation .approach-book-img {
  width: 60px;
  margin-top: 0.2rem;
}

.foundation-layout.conversation .approach-item h3 {
  font-size: 0.95rem;
  margin-bottom: 0.2rem;
}

.foundation-layout.conversation .approach-item p {
  font-size: 0.75rem;
  margin: 0.1rem 0;
}

.approach-item h3 {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

.approach-item p {
  font-size: 0.9rem;
  margin: 0.3rem 0;
  color: #333;
}

.result-box {
  position: relative;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(59, 130, 246, 0.2));
  border: 3px solid rgba(16, 185, 129, 0.5);
  border-radius: 16px;
  padding: 1.5rem;
  text-align: center;
  max-width: 600px;
  margin: 0 auto;
}

.foundation-layout.conversation .result-box {
  padding: 0.8rem;
  max-width: 500px;
}

.foundation-layout.conversation .result-comment {
  font-size: 0.85rem;
}

.foundation-layout.conversation .result-score {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.foundation-layout.conversation .score-number {
  font-size: 2rem;
}

.result-year {
  font-size: 1.1rem;
  font-weight: bold;
  color: rgba(16, 185, 129, 1);
  margin-bottom: 0.8rem;
}

.result-score {
  font-size: 1.8rem;
  font-weight: bold;
  margin-bottom: 0.8rem;
  color: #333;
}

.score-number {
  font-size: 2.5rem;
  color: rgba(16, 185, 129, 1);
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.result-comment {
  font-size: 1rem;
  color: #444;
  font-style: italic;
}

.foundation-layout.conversation .result-comment {
  font-size: 0.95rem;
}

.result-comment strong {
  color: rgba(16, 185, 129, 1);
  font-weight: bold;
}

.timeline-container {
  position: absolute;
  top: -20px;
  right: -60px;
  width: 200px;
  height: 150px;
}

.foundation-layout.conversation .timeline-container {
  width: 150px;
  height: 110px;
  top: -15px;
  right: -40px;
}

.timeline-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.timeline-focus-box-3 {
  position: absolute;
  top: 50%;
  left: 96%;
  width: 6px;
  height: 80px;
  border: 1px solid red;
  background: transparent;
  transform: translate(-50%, -50%);
}
</style>

---
transition: fade-out
---

# 今取り組んでいること

<div class="current-work-layout">

<v-clicks>

<div class="work-grid">
  <div class="work-item">
    <div class="work-icon">📚</div>
    <h3>構文解析本の学習</h3>
    <p>英文の構造を深く理解</p>
  </div>

  <div class="work-item">
    <div class="work-icon">📝</div>
    <h3>単語学習の継続</h3>
    <p>語彙力を着実に強化</p>
  </div>

  <div class="work-item">
    <div class="work-icon">🎧</div>
    <h3>YouTube動画の多聴/精聴</h3>
    <p>ネイティブの生の英語に触れる</p>
  </div>

  <div class="work-item">
    <div class="work-icon">🗣️</div>
    <h3>発話基礎練習</h3>
    <p>実際に口を動かして練習</p>
  </div>
</div>

<div class="goal-message">
  <strong>目標：2026年中にTOEIC 900点突破！</strong>
</div>

</v-clicks>

</div>

<style scoped>
.current-work-layout {
  padding: 1rem 2rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
}

.work-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.work-item {
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(147, 51, 234, 0.1));
  border: 2px solid rgba(59, 130, 246, 0.4);
  border-radius: 12px;
  padding: 1rem;
  text-align: center;
  transition: transform 0.3s ease;
}

.work-item:hover {
  transform: translateY(-5px);
}

.work-icon {
  font-size: 2.5rem;
  margin-bottom: 0.3rem;
}

.work-item h3 {
  font-size: 1rem;
  margin-bottom: 0.3rem;
  color: rgba(59, 130, 246, 1);
}

.work-item p {
  font-size: 0.85rem;
  color: #555;
  margin: 0;
}

.goal-message {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(59, 130, 246, 0.2));
  border: 3px solid rgba(16, 185, 129, 0.6);
  border-radius: 12px;
  padding: 1rem;
  text-align: center;
  font-size: 1.1rem;
  color: #333;
}

.goal-message strong {
  color: rgba(16, 185, 129, 1);
}
</style>

---
transition: fade-out
---

# これからやりたいこと

<div class="future-layout">

<v-clicks>

<div class="future-content">
  <div class="future-icon">🌟</div>
  <h2>英会話への再挑戦</h2>

  <div class="reason-box">
    <p>発音と語法をもうちょい学んだら、きっとためになるはず</p>
  </div>

  <div class="service-highlight">
    <div class="service-icon">💬</div>
    <h3>Cambly が気になっている</h3>
    <ul>
      <li>AI フィードバック機能がすごい</li>
      <li>発語スピードも表示される</li>
      <li>24時間いつでも予約なしでレッスン可能</li>
    </ul>
  </div>

  <div class="message-box">
    <strong>基礎を固めたら、実践の時！</strong>
  </div>
</div>

</v-clicks>

</div>

<style scoped>
.future-layout {
  padding: 0.5rem 2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.future-content {
  text-align: center;
  max-width: 700px;
}

.future-icon {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.future-content h2 {
  font-size: 1.5rem;
  margin-bottom: 0.6rem;
  color: rgba(59, 130, 246, 1);
}

.reason-box {
  background: rgba(245, 158, 11, 0.1);
  border: 2px solid rgba(245, 158, 11, 0.4);
  border-radius: 12px;
  padding: 0.7rem;
  margin-bottom: 0.8rem;
  transition: transform 0.3s ease;
}

.reason-box:hover {
  transform: translateY(-5px);
}

.reason-box p {
  font-size: 0.95rem;
  color: #333;
  margin: 0;
  font-weight: 500;
}

.service-highlight {
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(147, 51, 234, 0.1));
  border: 3px solid rgba(59, 130, 246, 0.5);
  border-radius: 16px;
  padding: 1rem;
  margin-bottom: 0.8rem;
  transition: transform 0.3s ease;
}

.service-highlight:hover {
  transform: translateY(-5px);
}

.service-icon {
  font-size: 2rem;
  margin-bottom: 0.3rem;
}

.service-highlight h3 {
  font-size: 1.1rem;
  color: rgba(59, 130, 246, 1);
  margin-bottom: 0.6rem;
}

.service-highlight ul {
  text-align: left;
  display: inline-block;
  margin: 0;
  padding-left: 1.5rem;
}

.service-highlight li {
  font-size: 0.85rem;
  color: #444;
  margin: 0.3rem 0;
}

.message-box {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(59, 130, 246, 0.2));
  border: 3px solid rgba(16, 185, 129, 0.6);
  border-radius: 12px;
  padding: 0.8rem;
  font-size: 1rem;
  color: #333;
}

.message-box strong {
  color: rgba(16, 185, 129, 1);
}
</style>
