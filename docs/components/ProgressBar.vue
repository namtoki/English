<template>
  <div v-if="currentPage > 1" class="progress-bar">
    <div class="progress-bar-fill" :style="{ width: progressWidth }"></div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const { $slidev } = useSlideContext()

const currentPage = computed(() => $slidev.nav.currentPage)
const progressWidth = computed(() => {
  const total = $slidev.nav.total
  const current = $slidev.nav.currentPage
  return `${(current / total) * 100}%`
})
</script>

<style scoped>
.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 6px;
  background: rgba(0, 0, 0, 0.1);
  z-index: 1000;
}

.progress-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899);
  transition: width 0.3s ease;
  box-shadow: 0 0 10px rgba(59, 130, 246, 0.5);
}
</style>
