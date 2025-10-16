<template>
  <div class="my-6">
    <!-- 文件路径显示 -->
    <div v-if="filePath" class="bg-gradient-to-r from-indigo-600 to-purple-600 text-white px-4 py-2 rounded-t-lg flex items-center space-x-2">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"></path>
      </svg>
      <span class="font-mono text-sm">📁 {{ filePath }}</span>
      <a 
        v-if="githubUrl" 
        :href="githubUrl" 
        target="_blank"
        class="ml-auto text-xs bg-white/20 hover:bg-white/30 px-2 py-1 rounded transition-colors"
      >
        在GitHub查看 →
      </a>
    </div>
    
    <!-- 标题栏 -->
    <div v-if="title" class="bg-gray-800 text-gray-200 px-4 py-2 flex items-center justify-between" :class="{ 'rounded-t-lg': !filePath }">
      <span class="font-semibold">{{ title }}</span>
      <div class="flex items-center space-x-2">
        <span v-if="language" class="text-xs bg-gray-700 px-2 py-1 rounded">{{ language }}</span>
        <button 
          @click="copyCode"
          class="text-sm bg-gray-700 hover:bg-gray-600 px-3 py-1 rounded transition-colors"
        >
          {{ copied ? '✓ 已复制!' : '📋 复制代码' }}
        </button>
      </div>
    </div>
    
    <!-- 代码块 -->
    <pre :class="{ 
      'rounded-t-lg': !title && !filePath, 
      'rounded-b-lg': true 
    }" class="code-block relative group"><code>{{ code }}</code>
      <!-- 运行提示 -->
      <div v-if="runnable" class="absolute top-2 right-2 bg-green-500 text-white text-xs px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity">
        ▶️ 可运行
      </div>
    </pre>
    
    <!-- 代码说明 -->
    <div v-if="description" class="bg-blue-50 border-l-4 border-blue-500 p-3 text-sm text-gray-700">
      <strong class="text-blue-700">💡 说明：</strong>{{ description }}
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  code: {
    type: String,
    required: true
  },
  title: String,
  filePath: String,  // 文件路径，如 "code/part1/01_example.py"
  language: String,  // 编程语言，如 "Python", "JavaScript"
  description: String,  // 代码说明
  runnable: {  // 是否可运行
    type: Boolean,
    default: false
  },
  githubUrl: String  // GitHub链接（可选）
})

const copied = ref(false)

const copyCode = async () => {
  try {
    await navigator.clipboard.writeText(props.code)
    copied.value = true
    setTimeout(() => {
      copied.value = false
    }, 2000)
  } catch (err) {
    console.error('复制失败:', err)
  }
}
</script>

