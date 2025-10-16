<template>
  <div 
    class="card border-l-4 transition-all duration-300 hover:shadow-2xl"
    :class="borderColorClass"
  >
    <div class="flex items-start space-x-4">
      <div class="text-3xl">{{ icon }}</div>
      <div class="flex-1">
        <h4 class="text-xl font-bold mb-2" :class="titleColorClass">{{ title }}</h4>
        <div class="text-gray-700">
          <slot></slot>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  icon: {
    type: String,
    default: 'ℹ️'
  },
  title: {
    type: String,
    required: true
  },
  variant: {
    type: String,
    default: 'info', // info, success, warning, error
    validator: (value) => ['info', 'success', 'warning', 'error'].includes(value)
  }
})

const borderColorClass = computed(() => {
  const colors = {
    info: 'border-blue-500',
    success: 'border-green-500',
    warning: 'border-yellow-500',
    error: 'border-red-500'
  }
  return colors[props.variant]
})

const titleColorClass = computed(() => {
  const colors = {
    info: 'text-blue-700',
    success: 'text-green-700',
    warning: 'text-yellow-700',
    error: 'text-red-700'
  }
  return colors[props.variant]
})
</script>

