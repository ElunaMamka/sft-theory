<template>
  <div class="card my-8" :class="bgClass">
    <div class="flex items-start space-x-4">
      <div class="text-5xl">{{ icon }}</div>
      <div class="flex-1">
        <h3 class="text-2xl font-bold mb-4" :class="titleClass">{{ title }}</h3>
        <div class="bg-white rounded-lg p-5 shadow-sm">
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
    default: '📝'
  },
  title: {
    type: String,
    required: true
  },
  variant: {
    type: String,
    default: 'blue',
    validator: (value) => ['blue', 'purple', 'green', 'orange'].includes(value)
  }
})

const bgClass = computed(() => {
  const classes = {
    blue: 'bg-gradient-to-br from-blue-50 to-cyan-50',
    purple: 'bg-gradient-to-br from-purple-50 to-pink-50',
    green: 'bg-gradient-to-br from-green-50 to-emerald-50',
    orange: 'bg-gradient-to-br from-orange-50 to-amber-50'
  }
  return classes[props.variant]
})

const titleClass = computed(() => {
  const classes = {
    blue: 'text-blue-800',
    purple: 'text-purple-800',
    green: 'text-green-800',
    orange: 'text-orange-800'
  }
  return classes[props.variant]
})
</script>

