<template>
  <div class="my-12">
    <h2 class="text-3xl font-bold text-gray-800 mb-8 text-center">
      📊 SFT数据集详细示例与可视化
    </h2>

    <!-- 6种任务类型的数据示例 -->
    <div class="grid md:grid-cols-2 gap-6 mb-8">
      <div 
        v-for="(task, index) in tasks" 
        :key="index"
        class="card hover:shadow-xl transition-shadow cursor-pointer"
        :class="getBgClass(index)"
        @click="selectedTask = task"
      >
        <div class="flex items-start space-x-4">
          <div class="text-5xl">{{ task.icon }}</div>
          <div class="flex-1">
            <h3 class="text-xl font-bold mb-2" :class="getTitleClass(index)">
              {{ task.name }}
            </h3>
            <p class="text-sm text-gray-600 mb-3">{{ task.description }}</p>
            <div class="flex items-center space-x-2 text-xs text-gray-500">
              <span class="bg-gray-100 px-2 py-1 rounded">{{ task.sampleCount }} 样本示例</span>
              <span class="bg-gray-100 px-2 py-1 rounded">{{ task.difficulty }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 选中任务的详细示例 -->
    <div v-if="selectedTask" class="card bg-gradient-to-br from-indigo-50 to-purple-50 mb-8">
      <div class="flex items-center justify-between mb-6">
        <h3 class="text-2xl font-bold text-indigo-800 flex items-center">
          <span class="text-4xl mr-3">{{ selectedTask.icon }}</span>
          {{ selectedTask.name }} - 数据示例
        </h3>
        <button 
          @click="selectedTask = null"
          class="text-gray-500 hover:text-gray-700 text-2xl"
        >
          ×
        </button>
      </div>

      <div 
        v-for="(example, idx) in selectedTask.examples" 
        :key="idx"
        class="bg-white p-6 rounded-xl shadow-sm mb-4"
      >
        <div class="flex items-center justify-between mb-4">
          <span class="text-sm font-bold text-purple-600">示例 {{ idx + 1 }}</span>
          <span class="text-xs bg-purple-100 text-purple-700 px-2 py-1 rounded">完整三元组</span>
        </div>

        <!-- Instruction -->
        <div class="mb-4">
          <div class="flex items-center space-x-2 mb-2">
            <span class="bg-blue-500 text-white text-xs px-2 py-1 rounded font-bold">Instruction</span>
            <span class="text-xs text-gray-500">任务描述</span>
          </div>
          <div class="bg-blue-50 p-4 rounded-lg">
            <p class="text-sm text-gray-800">{{ example.instruction }}</p>
          </div>
        </div>

        <!-- Input -->
        <div class="mb-4">
          <div class="flex items-center space-x-2 mb-2">
            <span class="bg-green-500 text-white text-xs px-2 py-1 rounded font-bold">Input</span>
            <span class="text-xs text-gray-500">用户输入</span>
          </div>
          <div class="bg-green-50 p-4 rounded-lg">
            <p class="text-sm text-gray-800 whitespace-pre-wrap">{{ example.input }}</p>
          </div>
        </div>

        <!-- Output -->
        <div>
          <div class="flex items-center space-x-2 mb-2">
            <span class="bg-purple-500 text-white text-xs px-2 py-1 rounded font-bold">Output</span>
            <span class="text-xs text-gray-500">期望响应</span>
          </div>
          <div class="bg-purple-50 p-4 rounded-lg">
            <p class="text-sm text-gray-800 whitespace-pre-wrap">{{ example.output }}</p>
          </div>
        </div>

        <!-- 数据特征 -->
        <div class="mt-4 bg-gradient-to-r from-gray-50 to-gray-100 p-3 rounded-lg">
          <p class="text-xs text-gray-600 flex items-center space-x-4">
            <span>📏 长度：Inst={{ example.instruction.length }} | In={{ example.input.length }} | Out={{ example.output.length }}</span>
          </p>
        </div>
      </div>
    </div>

    <!-- 数据质量对比：好的 vs 坏的 -->
    <div class="card mb-8 bg-gradient-to-br from-orange-50 to-yellow-50">
      <h3 class="text-2xl font-bold text-orange-800 mb-6 flex items-center">
        <span class="text-4xl mr-3">⚖️</span>
        好数据 vs 坏数据对比
      </h3>

      <div class="grid md:grid-cols-2 gap-6">
        <!-- 坏数据示例 -->
        <div>
          <div class="flex items-center space-x-2 mb-4">
            <span class="text-2xl">❌</span>
            <h4 class="font-bold text-red-700">坏数据示例</h4>
          </div>

          <div class="space-y-4">
            <div class="bg-white p-4 rounded-lg border-2 border-red-200">
              <p class="text-xs text-gray-500 mb-2">示例 1 - Instruction不清晰</p>
              <div class="space-y-2 text-sm">
                <div class="bg-red-50 p-2 rounded">
                  <strong>Instruction:</strong> "回答"
                </div>
                <div class="bg-red-50 p-2 rounded">
                  <strong>Input:</strong> "AI"
                </div>
                <div class="bg-red-50 p-2 rounded">
                  <strong>Output:</strong> "是的"
                </div>
              </div>
              <div class="mt-2 bg-red-100 p-2 rounded text-xs text-red-800">
                <strong>问题：</strong>instruction太简单，output没有信息价值
              </div>
            </div>

            <div class="bg-white p-4 rounded-lg border-2 border-red-200">
              <p class="text-xs text-gray-500 mb-2">示例 2 - Output过短</p>
              <div class="space-y-2 text-sm">
                <div class="bg-red-50 p-2 rounded">
                  <strong>Instruction:</strong> "解释什么是深度学习"
                </div>
                <div class="bg-red-50 p-2 rounded">
                  <strong>Output:</strong> "就是神经网络"
                </div>
              </div>
              <div class="mt-2 bg-red-100 p-2 rounded text-xs text-red-800">
                <strong>问题：</strong>回答过于简短，缺乏细节
              </div>
            </div>
          </div>
        </div>

        <!-- 好数据示例 -->
        <div>
          <div class="flex items-center space-x-2 mb-4">
            <span class="text-2xl">✅</span>
            <h4 class="font-bold text-green-700">好数据示例</h4>
          </div>

          <div class="space-y-4">
            <div class="bg-white p-4 rounded-lg border-2 border-green-200">
              <p class="text-xs text-gray-500 mb-2">示例 1 - 清晰且详细</p>
              <div class="space-y-2 text-sm">
                <div class="bg-green-50 p-2 rounded">
                  <strong>Instruction:</strong> "作为AI助手，用通俗易懂的语言解释技术概念"
                </div>
                <div class="bg-green-50 p-2 rounded">
                  <strong>Input:</strong> "什么是人工智能？"
                </div>
                <div class="bg-green-50 p-2 rounded">
                  <strong>Output:</strong> "人工智能(AI)是让计算机模拟人类智能的技术。就像人类能够学习、推理和解决问题..."
                </div>
              </div>
              <div class="mt-2 bg-green-100 p-2 rounded text-xs text-green-800">
                <strong>优点：</strong>instruction明确角色，output详细且易懂
              </div>
            </div>

            <div class="bg-white p-4 rounded-lg border-2 border-green-200">
              <p class="text-xs text-gray-500 mb-2">示例 2 - 结构完整</p>
              <div class="space-y-2 text-sm">
                <div class="bg-green-50 p-2 rounded">
                  <strong>Instruction:</strong> "编写Python函数并提供使用示例"
                </div>
                <div class="bg-green-50 p-2 rounded">
                  <strong>Output:</strong> 包含文档字符串、类型注释、使用示例
                </div>
              </div>
              <div class="mt-2 bg-green-100 p-2 rounded text-xs text-green-800">
                <strong>优点：</strong>格式规范，信息完整，可直接使用
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 数据质量的6个维度 -->
    <div class="card mb-8 bg-gradient-to-br from-cyan-50 to-blue-50">
      <h3 class="text-2xl font-bold text-cyan-800 mb-6 flex items-center">
        <span class="text-4xl mr-3">🎯</span>
        数据质量的6个维度
      </h3>

      <div class="grid md:grid-cols-3 gap-4">
        <div 
          v-for="(dimension, idx) in qualityDimensions" 
          :key="idx"
          class="bg-white p-5 rounded-xl shadow-sm hover:shadow-md transition-shadow"
        >
          <div class="text-3xl mb-3">{{ dimension.icon }}</div>
          <h4 class="font-bold text-gray-800 mb-2">{{ dimension.name }}</h4>
          <p class="text-sm text-gray-600 mb-3">{{ dimension.description }}</p>
          <div class="bg-cyan-50 p-3 rounded">
            <p class="text-xs text-cyan-800 font-semibold mb-1">检查方法：</p>
            <p class="text-xs text-gray-700">{{ dimension.check }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 数据增强技术 -->
    <div class="card bg-gradient-to-br from-purple-50 to-pink-50">
      <h3 class="text-2xl font-bold text-purple-800 mb-6 flex items-center">
        <span class="text-4xl mr-3">🔄</span>
        5种数据增强技术
      </h3>

      <div class="space-y-4">
        <div 
          v-for="(method, idx) in augmentationMethods" 
          :key="idx"
          class="bg-white p-5 rounded-xl shadow-sm"
        >
          <div class="flex items-start space-x-4">
            <div class="text-3xl">{{ method.icon }}</div>
            <div class="flex-1">
              <h4 class="font-bold text-gray-800 mb-2">{{ method.name }}</h4>
              <p class="text-sm text-gray-600 mb-3">{{ method.description }}</p>
              
              <div class="bg-gray-50 p-4 rounded-lg">
                <p class="text-xs text-gray-500 mb-1">示例：</p>
                <div class="space-y-1">
                  <p class="text-sm text-blue-700">原始: {{ method.example.original }}</p>
                  <p class="text-sm text-green-700">增强后: {{ method.example.augmented }}</p>
                </div>
              </div>

              <div class="mt-3 flex items-center space-x-2">
                <span class="text-xs bg-purple-100 text-purple-700 px-2 py-1 rounded">
                  扩充比例: {{ method.ratio }}
                </span>
                <span class="text-xs bg-purple-100 text-purple-700 px-2 py-1 rounded">
                  {{ method.difficulty }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const selectedTask = ref(null)

const tasks = ref([
  {
    name: '问答任务',
    icon: '💬',
    description: '回答用户的各类问题',
    sampleCount: 3,
    difficulty: '简单',
    examples: [
      {
        instruction: '回答用户的问题',
        input: '什么是人工智能？',
        output: '人工智能(AI)是计算机科学的一个分支，致力于创建能够模拟人类智能行为的系统。它包括机器学习、深度学习、自然语言处理、计算机视觉等多个子领域。AI系统可以学习、推理、解决问题，并在没有明确编程的情况下改进自己的性能。'
      },
      {
        instruction: '回答用户的问题',
        input: '机器学习和深度学习有什么区别？',
        output: '机器学习是一种让计算机从数据中学习的方法，包括决策树、支持向量机等算法。深度学习是机器学习的一个子集，专门使用多层神经网络来学习数据的复杂模式。深度学习在图像识别、语音识别等任务上表现出色，但通常需要更多的数据和计算资源。'
      }
    ]
  },
  {
    name: '文本摘要',
    icon: '📝',
    description: '将长文本总结成简短摘要',
    sampleCount: 2,
    difficulty: '中等',
    examples: [
      {
        instruction: '将下面的文章总结成三句话',
        input: 'OpenAI最近发布了GPT-4，这是其大型语言模型系列的最新版本。GPT-4在多个基准测试中展现出了显著的性能提升，特别是在推理能力、代码生成和多语言理解方面。该模型经过大规模预训练，并通过人类反馈强化学习(RLHF)进行了精细调优，使其能够更好地理解和执行复杂指令。',
        output: 'OpenAI发布了GPT-4，在推理、代码和多语言能力上有显著提升。模型通过预训练和RLHF调优，能更好地执行复杂指令。GPT-4在安全性和准确性方面也有重大改进。'
      }
    ]
  },
  {
    name: '代码生成',
    icon: '💻',
    description: '根据需求编写代码',
    sampleCount: 2,
    difficulty: '中等',
    examples: [
      {
        instruction: '编写一个Python函数来计算斐波那契数列',
        input: '要求：使用递归方法，输入n返回第n个斐波那契数',
        output: '```python\ndef fibonacci(n):\n    """\n    计算第n个斐波那契数（递归方法）\n    \n    Args:\n        n: 整数，要计算的斐波那契数的位置\n    \n    Returns:\n        第n个斐波那契数\n    """\n    if n <= 0:\n        return 0\n    elif n == 1:\n        return 1\n    else:\n        return fibonacci(n-1) + fibonacci(n-2)\n```'
      }
    ]
  },
  {
    name: '对话任务',
    icon: '🗨️',
    description: '多轮对话和角色扮演',
    sampleCount: 2,
    difficulty: '困难',
    examples: [
      {
        instruction: '你是一个友好的客服助手，请专业且礼貌地回答用户的问题',
        input: '我的订单已经三天了还没发货，怎么回事？',
        output: '非常抱歉给您带来了不便！我立即为您查询订单状态。请问您能提供一下订单号吗？这样我可以更快地帮您追踪物流信息。同时，如果订单确实延误，我们会为您申请加急处理或提供相应的补偿。感谢您的耐心等待！'
      }
    ]
  },
  {
    name: '翻译任务',
    icon: '🌐',
    description: '中英文互译',
    sampleCount: 3,
    difficulty: '简单',
    examples: [
      {
        instruction: '将下面的中文翻译成英文',
        input: '人工智能正在改变我们的生活方式。',
        output: 'Artificial intelligence is changing the way we live.'
      },
      {
        instruction: '将下面的英文翻译成中文',
        input: 'Machine learning is a subset of artificial intelligence.',
        output: '机器学习是人工智能的一个子集。'
      }
    ]
  },
  {
    name: '文本分类',
    icon: '🏷️',
    description: '判断文本所属类别',
    sampleCount: 3,
    difficulty: '简单',
    examples: [
      {
        instruction: '判断下面的评论是正面还是负面',
        input: '这部电影太精彩了！演员演技出色，剧情引人入胜，强烈推荐！',
        output: '正面'
      },
      {
        instruction: '判断下面的新闻属于哪个类别（科技/娱乐/体育/财经）',
        input: '苹果公司今日发布最新款iPhone，搭载全新A17芯片，性能提升显著。',
        output: '科技'
      }
    ]
  }
])

const qualityDimensions = ref([
  {
    name: '完整性',
    icon: '✅',
    description: '所有必要字段都存在且非空',
    check: '检查instruction、input、output是否都存在'
  },
  {
    name: '准确性',
    icon: '🎯',
    description: 'Output正确回答了Input',
    check: '人工审核或使用评估模型'
  },
  {
    name: '相关性',
    icon: '🔗',
    description: 'Output与Instruction要求对应',
    check: '检查output是否遵循instruction'
  },
  {
    name: '多样性',
    icon: '🎨',
    description: 'Instruction多样化，避免重复',
    check: '统计unique instructions数量'
  },
  {
    name: '长度',
    icon: '📏',
    description: '不过长也不过短，合理适中',
    check: '统计字符数，设定合理范围'
  },
  {
    name: '格式',
    icon: '📋',
    description: '遵循统一的数据格式',
    check: 'JSON schema验证'
  }
])

const augmentationMethods = ref([
  {
    name: 'Instruction改写',
    icon: '✏️',
    description: '用同义词或不同表达方式改写instruction',
    example: {
      original: '回答用户的问题',
      augmented: '请回答以下问题 / 针对用户提问，给出答案'
    },
    ratio: '2-3x',
    difficulty: '简单'
  },
  {
    name: '回译增强',
    icon: '🔄',
    description: '翻译成其他语言再翻译回来',
    example: {
      original: '人工智能正在改变世界',
      augmented: 'AI技术正在改变世界 (中→英→中)'
    },
    ratio: '2x',
    difficulty: '中等'
  },
  {
    name: '角色设定',
    icon: '🎭',
    description: '为instruction添加角色persona',
    example: {
      original: '回答问题',
      augmented: '作为一个专业的AI助手，回答问题'
    },
    ratio: '3-5x',
    difficulty: '简单'
  },
  {
    name: '负例生成',
    icon: '❌',
    description: '创建不好的回答作为对比',
    example: {
      original: '(正常回答)',
      augmented: '"不知道" (展示不好的回答)'
    },
    ratio: '1.2x',
    difficulty: '简单'
  },
  {
    name: '模板填充',
    icon: '📝',
    description: '使用模板批量生成数据',
    example: {
      original: '1个模板',
      augmented: '填充不同参数生成100+样本'
    },
    ratio: '10-100x',
    difficulty: '中等'
  }
])

const getBgClass = (index) => {
  const classes = [
    'bg-gradient-to-br from-blue-50 to-cyan-50',
    'bg-gradient-to-br from-green-50 to-emerald-50',
    'bg-gradient-to-br from-purple-50 to-pink-50',
    'bg-gradient-to-br from-orange-50 to-yellow-50',
    'bg-gradient-to-br from-red-50 to-rose-50',
    'bg-gradient-to-br from-indigo-50 to-purple-50'
  ]
  return classes[index % classes.length]
}

const getTitleClass = (index) => {
  const classes = [
    'text-blue-800',
    'text-green-800',
    'text-purple-800',
    'text-orange-800',
    'text-red-800',
    'text-indigo-800'
  ]
  return classes[index % classes.length]
}
</script>

<style scoped>
.card {
  @apply p-6 rounded-xl shadow-md;
}
</style>

