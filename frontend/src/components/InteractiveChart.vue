<template>
  <div class="card my-8">
    <h3 v-if="title" class="text-2xl font-bold text-gray-800 mb-6">{{ title }}</h3>
    <div class="relative">
      <canvas ref="chartCanvas"></canvas>
    </div>
    <p v-if="description" class="text-gray-600 mt-4 text-center">{{ description }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { Chart, registerables } from 'chart.js'

Chart.register(...registerables)

const props = defineProps({
  title: String,
  description: String,
  type: {
    type: String,
    default: 'line'
  },
  data: {
    type: Object,
    required: true
  },
  options: {
    type: Object,
    default: () => ({})
  }
})

const chartCanvas = ref(null)
let chartInstance = null

const defaultOptions = {
  responsive: true,
  maintainAspectRatio: true,
  plugins: {
    legend: {
      position: 'top',
      labels: {
        font: { size: 14 },
        padding: 15
      }
    },
    tooltip: {
      backgroundColor: 'rgba(0, 0, 0, 0.8)',
      padding: 12,
      titleFont: { size: 14 },
      bodyFont: { size: 13 }
    }
  },
  scales: props.type === 'radar' ? {} : {
    y: {
      beginAtZero: true,
      grid: {
        color: 'rgba(0, 0, 0, 0.05)'
      }
    },
    x: {
      grid: {
        color: 'rgba(0, 0, 0, 0.05)'
      }
    }
  }
}

const createChart = () => {
  if (chartInstance) {
    chartInstance.destroy()
  }

  chartInstance = new Chart(chartCanvas.value, {
    type: props.type,
    data: props.data,
    options: { ...defaultOptions, ...props.options }
  })
}

onMounted(() => {
  createChart()
})

watch(() => props.data, () => {
  createChart()
}, { deep: true })
</script>

