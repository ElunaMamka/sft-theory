<template>
  <div class="my-8">
    <div class="flex justify-between items-center relative">
      <!-- 连接线 -->
      <div class="absolute top-6 left-0 right-0 h-1 bg-gray-200 -z-10">
        <div 
          class="h-full bg-gradient-to-r from-blue-500 to-purple-500 transition-all duration-500"
          :style="{ width: `${progress}%` }"
        ></div>
      </div>

      <!-- 步骤节点 -->
      <div 
        v-for="(step, index) in steps" 
        :key="index"
        class="flex flex-col items-center flex-1"
      >
        <div 
          class="w-12 h-12 rounded-full flex items-center justify-center font-bold text-lg transition-all duration-300 z-10"
          :class="getStepClass(index)"
        >
          <span v-if="index < currentStep">✓</span>
          <span v-else>{{ index + 1 }}</span>
        </div>
        <div class="mt-3 text-center max-w-[120px]">
          <p class="font-semibold text-sm" :class="index <= currentStep ? 'text-gray-800' : 'text-gray-400'">
            {{ step.title }}
          </p>
          <p v-if="step.description" class="text-xs text-gray-500 mt-1">
            {{ step.description }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  steps: {
    type: Array,
    required: true
  },
  currentStep: {
    type: Number,
    default: 0
  }
})

const progress = computed(() => {
  if (props.steps.length <= 1) return 0
  return (props.currentStep / (props.steps.length - 1)) * 100
})

const getStepClass = (index) => {
  if (index < props.currentStep) {
    return 'bg-gradient-to-br from-green-400 to-green-600 text-white'
  } else if (index === props.currentStep) {
    return 'bg-gradient-to-br from-blue-500 to-purple-500 text-white animate-pulse'
  } else {
    return 'bg-gray-200 text-gray-500'
  }
}
</script>

