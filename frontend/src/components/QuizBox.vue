<template>
  <div class="card my-8 bg-gradient-to-br from-purple-50 to-pink-50">
    <h3 class="text-2xl font-bold text-purple-700 mb-4 flex items-center">
      <span class="text-3xl mr-3">🤔</span>
      {{ question }}
    </h3>
    
    <div class="space-y-3 mb-6">
      <button
        v-for="(option, index) in options"
        :key="index"
        @click="selectAnswer(index)"
        :disabled="answered"
        class="w-full text-left p-4 rounded-lg border-2 transition-all duration-300"
        :class="getOptionClass(index)"
      >
        <span class="font-semibold mr-2">{{ String.fromCharCode(65 + index) }}.</span>
        {{ option }}
      </button>
    </div>

    <div v-if="answered" class="p-4 rounded-lg" :class="isCorrect ? 'bg-green-100' : 'bg-red-100'">
      <p class="font-bold mb-2" :class="isCorrect ? 'text-green-700' : 'text-red-700'">
        {{ isCorrect ? '✓ 回答正确！' : '✗ 回答错误' }}
      </p>
      <p class="text-gray-700">{{ explanation }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  question: {
    type: String,
    required: true
  },
  options: {
    type: Array,
    required: true
  },
  correctAnswer: {
    type: Number,
    required: true
  },
  explanation: {
    type: String,
    required: true
  }
})

const selectedAnswer = ref(null)
const answered = ref(false)

const isCorrect = computed(() => selectedAnswer.value === props.correctAnswer)

const selectAnswer = (index) => {
  if (answered.value) return
  selectedAnswer.value = index
  answered.value = true
}

const getOptionClass = (index) => {
  if (!answered.value) {
    return 'border-gray-300 hover:border-purple-400 hover:bg-purple-50 cursor-pointer'
  }
  
  if (index === props.correctAnswer) {
    return 'border-green-500 bg-green-50'
  }
  
  if (index === selectedAnswer.value && index !== props.correctAnswer) {
    return 'border-red-500 bg-red-50'
  }
  
  return 'border-gray-300 opacity-50'
}
</script>

