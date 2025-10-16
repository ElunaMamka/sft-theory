<template>
  <div class="home-page">
    <!-- 英雄区域 -->
    <section class="text-center py-16 animate-fade-in">
      <h1 class="text-5xl md:text-6xl font-bold mb-6">
        <span class="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
          从通才到专才
        </span>
      </h1>
      <h2 class="text-3xl md:text-4xl text-gray-700 mb-8">
        监督式微调（SFT）入门指南
      </h2>
      <p class="text-xl text-gray-600 max-w-3xl mx-auto mb-12">
        通过丰富的可视化和形象的比喻，轻松掌握SFT的核心原理
      </p>
      
      <!-- 核心类比 -->
      <div class="analogy-box max-w-4xl mx-auto mb-12 animate-slide-up">
        <div class="flex items-start space-x-4">
          <div class="text-4xl">🎓</div>
          <div class="flex-1 text-left">
            <h3 class="text-2xl font-bold text-orange-700 mb-3">核心类比：AI的岗位培训</h3>
            <p class="text-lg text-gray-700 leading-relaxed">
              想象一下，一个大型语言模型（LLM）就像一位<strong>才华横溢的大学毕业生</strong>。
              这位毕业生博览群书，通晓古今，几乎阅读了图书馆里的每一本书，掌握了海量的通用知识。
              然而，尽管他知识渊博，却没有丝毫实际工作经验。
            </p>
            <p class="text-lg text-gray-700 leading-relaxed mt-3">
              <strong>监督式微调（SFT）</strong>正是将这位"通才毕业生"转变为"领域专家"的桥梁 —— 
              相当于一套专门的<strong>在职培训体系</strong>！
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- 课程概览 -->
    <section class="mb-16">
      <h2 class="section-title text-center mb-12">课程内容</h2>
      <div class="grid md:grid-cols-2 gap-8">
        <router-link 
          v-for="part in courseParts" 
          :key="part.id"
          :to="part.path"
          class="card hover:scale-105 transition-transform cursor-pointer group"
        >
          <div class="flex items-start space-x-4">
            <div class="text-5xl group-hover:scale-110 transition-transform">
              {{ part.icon }}
            </div>
            <div class="flex-1">
              <h3 class="text-2xl font-bold text-gray-800 mb-2 group-hover:text-blue-600 transition-colors">
                {{ part.title }}
              </h3>
              <p class="text-gray-600 mb-3">{{ part.description }}</p>
              <div class="flex flex-wrap gap-2">
                <span 
                  v-for="tag in part.tags" 
                  :key="tag"
                  class="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm"
                >
                  {{ tag }}
                </span>
              </div>
            </div>
          </div>
        </router-link>
      </div>
    </section>

    <!-- 核心要点 -->
    <section class="mb-16">
      <h2 class="section-title text-center mb-12">核心要点</h2>
      <div class="grid md:grid-cols-3 gap-6">
        <div class="card text-center">
          <div class="text-5xl mb-4">📚 → 💼</div>
          <h3 class="text-xl font-bold text-gray-800 mb-2">预训练 vs SFT</h3>
          <p class="text-gray-600">预训练构建知识大脑<br/>SFT教会如何工作</p>
        </div>
        <div class="card text-center">
          <div class="text-5xl mb-4">🔌</div>
          <h3 class="text-xl font-bold text-gray-800 mb-2">LoRA：智能适配器</h3>
          <p class="text-gray-600">像电源转换插头<br/>高效、安全、可插拔</p>
        </div>
        <div class="card text-center">
          <div class="text-5xl mb-4">🎯</div>
          <h3 class="text-xl font-bold text-gray-800 mb-2">数据质量为王</h3>
          <p class="text-gray-600">数据是AI的行为蓝图<br/>质量决定成败</p>
        </div>
      </div>
    </section>

    <!-- 学习目标 -->
    <section class="mb-16">
      <div class="card bg-gradient-to-br from-blue-50 to-purple-50">
        <h2 class="text-3xl font-bold text-gray-800 mb-6">完成本课程后，你将能够：</h2>
        <ul class="space-y-4">
          <li v-for="goal in learningGoals" :key="goal" class="flex items-start space-x-3">
            <svg class="w-6 h-6 text-green-500 mt-1 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
            </svg>
            <span class="text-lg text-gray-700">{{ goal }}</span>
          </li>
        </ul>
      </div>
    </section>

    <!-- 开始学习按钮 -->
    <section class="text-center py-12">
      <router-link to="/part1" class="btn-primary text-xl px-12 py-4 inline-block">
        开始学习 →
      </router-link>
    </section>
  </div>
</template>

<script setup>
const courseParts = [
  {
    id: 1,
    path: '/part1',
    icon: '🎓',
    title: '第一部分：预训练 vs SFT',
    description: '理解LLM的两阶段成长之旅：通识教育与专业实习',
    tags: ['基座模型', '指令模型', '两阶段训练']
  },
  {
    id: 2,
    path: '/part2',
    icon: '🔌',
    title: '第二部分：LoRA高效微调',
    description: '像电源适配器一样的智能微调技术',
    tags: ['参数高效', '防止遗忘', '可插拔技能']
  },
  {
    id: 3,
    path: '/part3',
    icon: '📊',
    title: '第三部分：SFT数据集',
    description: 'AI的行为蓝图：质量远胜于数量',
    tags: ['指令-响应对', '数据质量', '行为塑造']
  },
  {
    id: 4,
    path: '/part4',
    icon: '🔄',
    title: '第四部分：SFT实践工作流',
    description: '以数据为中心的迭代优化过程',
    tags: ['模型选择', '数据准备', '训练评估']
  }
]

const learningGoals = [
  '深刻理解预训练和SFT的区别与联系',
  '掌握LoRA等参数高效微调技术的原理',
  '了解如何构建高质量的SFT数据集',
  '熟悉完整的SFT实践工作流程',
  '能够为自己的任务选择合适的微调策略',
  '具备打造专属AI助手的基础知识'
]
</script>

<style scoped>
.home-page {
  animation: fadeIn 0.5s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
</style>

