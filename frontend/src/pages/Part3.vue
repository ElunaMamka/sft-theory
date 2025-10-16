<template>
  <div class="part3-page">
    <!-- 标题 -->
    <h1 class="section-title">第三部分：成功的秘诀——SFT数据集</h1>

    <!-- 引言 -->
    <AnalogyBox icon="📐" title="核心类比：AI的行为蓝图">
      <p class="text-lg">
        SFT数据集不是一份简单的"事实清单"，而是一份<strong>"行为蓝图"</strong>。
      </p>
      <p class="text-lg mt-3">
        它不仅教会模型"说什么"，更重要的是教会它<strong>"怎么说"</strong>——
        格式、风格、语气，甚至隐含的推理步骤，都会被模型细致地学习并内化为默认行为。
      </p>
    </AnalogyBox>

    <!-- 垃圾进，垃圾出 -->
    <section class="my-12">
      <div class="card bg-gradient-to-br from-red-50 to-orange-50 border-l-4 border-red-500">
        <div class="flex items-start space-x-4">
          <div class="text-6xl">⚠️</div>
          <div class="flex-1">
            <h2 class="text-3xl font-bold text-red-800 mb-4">垃圾进，垃圾出 (GIGO)</h2>
            <p class="text-xl text-gray-700">
              在SFT项目中，有一个因素的重要性超越了其他所有因素——<strong>数据集的质量</strong>。
            </p>
            <p class="text-lg text-gray-600 mt-3">
              一个由数百或数千条样本组成的、小而精的高质量数据集，
              其微调效果往往能超越一个包含数万条样本的、充满噪声的庞大数据集。
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- 质量三要素 -->
    <section class="my-12">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">高质量数据集的三大核心特质</h2>
      
      <div class="grid md:grid-cols-3 gap-6">
        <div class="card text-center bg-gradient-to-br from-blue-50 to-blue-100 border-t-4 border-blue-500">
          <div class="text-6xl mb-4">🎯</div>
          <h3 class="text-2xl font-bold text-blue-800 mb-3">相关性</h3>
          <p class="text-gray-700">样本与你的目标任务高度相关，直接针对你要解决的问题</p>
        </div>

        <div class="card text-center bg-gradient-to-br from-purple-50 to-purple-100 border-t-4 border-purple-500">
          <div class="text-6xl mb-4">🌈</div>
          <h3 class="text-2xl font-bold text-purple-800 mb-3">多样性</h3>
          <p class="text-gray-700">样本覆盖各种可能的输入情况和场景，避免模型过拟合</p>
        </div>

        <div class="card text-center bg-gradient-to-br from-green-50 to-green-100 border-t-4 border-green-500">
          <div class="text-6xl mb-4">✅</div>
          <h3 class="text-2xl font-bold text-green-800 mb-3">准确性</h3>
          <p class="text-gray-700">样本中的标签和期望输出是正确无误的，树立正确范例</p>
        </div>
      </div>

      <div class="card my-8 bg-gradient-to-br from-amber-50 to-yellow-50">
        <h3 class="text-2xl font-bold text-amber-800 mb-4 flex items-center">
          <span class="text-3xl mr-3">💎</span>
          质量 > 数量
        </h3>
        <p class="text-lg text-gray-700">
          <strong>1000条高质量样本</strong> 的效果通常远超 <strong>10000条低质量样本</strong>
        </p>
        <div class="mt-4 flex items-center justify-center space-x-8 text-4xl">
          <div class="text-center">
            <div>💎💎💎</div>
            <div class="text-sm text-gray-600 mt-2">少而精</div>
          </div>
          <div class="text-2xl text-green-600">></div>
          <div class="text-center">
            <div>🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨</div>
            <div class="text-sm text-gray-600 mt-2">多而杂</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 数据集构成 -->
    <section class="my-12">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">SFT数据集的构成：指令-响应对</h2>
      
      <InfoCard icon="📋" title="标准格式" variant="info">
        <p class="mb-2">SFT数据集的标准格式是由成对的结构化数据组成：</p>
        <ul class="list-disc list-inside space-y-1">
          <li><strong>指令 (Instruction)</strong>：告诉模型要做什么</li>
          <li><strong>输入 (Input)</strong>：提供上下文或具体内容（可选）</li>
          <li><strong>响应 (Response)</strong>：期望的输出，即"正确范例"</li>
        </ul>
      </InfoCard>

      <!-- 示例展示 -->
      <div class="my-8">
        <h3 class="text-2xl font-bold text-gray-800 mb-4">实际示例</h3>
        
        <div class="space-y-6">
          <div 
            v-for="(example, index) in examples" 
            :key="index"
            class="card hover:shadow-2xl transition-all cursor-pointer"
            @click="selectedExample = selectedExample === index ? null : index"
          >
            <div class="flex items-center justify-between mb-3">
              <h4 class="text-xl font-bold text-gray-800 flex items-center">
                <span class="text-2xl mr-3">{{ example.icon }}</span>
                {{ example.task }}
              </h4>
              <div class="flex items-center space-x-2">
                <span class="px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm font-semibold">
                  质量分 {{ example.quality_score }}/10
                </span>
                <svg 
                  class="w-6 h-6 transition-transform"
                  :class="{ 'rotate-180': selectedExample === index }"
                  fill="none" 
                  stroke="currentColor" 
                  viewBox="0 0 24 24"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                </svg>
              </div>
            </div>

            <transition name="slide">
              <div v-if="selectedExample === index" class="space-y-4 mt-4">
                <div class="bg-blue-50 p-4 rounded-lg">
                  <p class="font-semibold text-blue-800 mb-2">📝 Instruction:</p>
                  <p class="text-gray-700">{{ example.instruction }}</p>
                </div>

                <div v-if="example.input" class="bg-purple-50 p-4 rounded-lg">
                  <p class="font-semibold text-purple-800 mb-2">📥 Input:</p>
                  <p class="text-gray-700">{{ example.input }}</p>
                </div>

                <div class="bg-green-50 p-4 rounded-lg">
                  <p class="font-semibold text-green-800 mb-2">✅ Response:</p>
                  <p class="text-gray-700 whitespace-pre-wrap">{{ example.response }}</p>
                </div>
              </div>
            </transition>
          </div>
        </div>
      </div>
    </section>

    <!-- SFT数据格式详解 - 重要！ -->
    <section class="my-12">
      <div class="card bg-gradient-to-br from-indigo-50 to-purple-50 border-l-4 border-indigo-500">
        <div class="flex items-start space-x-4">
          <div class="text-6xl">🔑</div>
          <div class="flex-1">
            <h2 class="text-3xl font-bold text-indigo-800 mb-4">核心关键：SFT数据的正确格式</h2>
            <p class="text-xl text-gray-700 mb-4">
              <strong>格式不对，训练白费！</strong>SFT数据必须使用正确的messages格式和special tokens，
              否则模型无法正确区分用户输入和助手回答，导致训练失败或效果极差。
            </p>
          </div>
        </div>
      </div>

      <!-- Messages格式标准 -->
      <div class="card my-8 bg-white">
        <h3 class="text-2xl font-bold text-gray-800 mb-6">💬 Messages格式（推荐）</h3>
        
        <div class="bg-indigo-50 p-6 rounded-xl mb-6">
          <p class="text-lg font-bold text-indigo-800 mb-4">标准结构：</p>
          <pre class="bg-gray-900 text-green-400 p-4 rounded-lg overflow-x-auto"><code>{
  "messages": [
    {"role": "system", "content": "你是一个helpful的AI助手"},
    {"role": "user", "content": "用户的问题"},
    {"role": "assistant", "content": "助手的回答"}
  ]
}</code></pre>
        </div>

        <div class="grid md:grid-cols-3 gap-6">
          <div class="bg-blue-50 p-4 rounded-lg">
            <h4 class="font-bold text-blue-800 mb-2">🎯 System消息（可选）</h4>
            <p class="text-sm text-gray-700 mb-2">定义助手的行为和角色</p>
            <p class="text-xs text-gray-600">示例："你是一个专业的医疗顾问"</p>
          </div>

          <div class="bg-green-50 p-4 rounded-lg">
            <h4 class="font-bold text-green-800 mb-2">👤 User消息（必需）</h4>
            <p class="text-sm text-gray-700 mb-2">用户的输入或问题</p>
            <p class="text-xs text-gray-600">示例："如何治疗感冒？"</p>
          </div>

          <div class="bg-purple-50 p-4 rounded-lg">
            <h4 class="font-bold text-purple-800 mb-2">🤖 Assistant消息（必需）</h4>
            <p class="text-sm text-gray-700 mb-2">期望的模型回答</p>
            <p class="text-xs text-gray-600">这是<strong>唯一计算损失</strong>的部分！</p>
          </div>
        </div>

        <div class="bg-yellow-50 p-4 rounded-lg mt-6 border-l-4 border-yellow-500">
          <p class="font-bold text-yellow-800 mb-2">⚠️ 关键注意：</p>
          <p class="text-gray-700">
            训练时，<strong>只对assistant的回答计算损失</strong>，system和user部分的token不参与损失计算（设置为-100 mask）。
            这样模型只学习"如何回答"，而不是学习"如何提问"。
          </p>
        </div>
      </div>

      <!-- Special Tokens详解 -->
      <div class="card my-8 bg-white">
        <h3 class="text-2xl font-bold text-gray-800 mb-6">🔖 Special Tokens：上下文拼接的关键</h3>
        
        <p class="text-lg text-gray-700 mb-6">
          Special tokens是特殊的标记符号，用于标识不同角色的消息边界。不同模型使用不同的格式：
        </p>

        <div class="space-y-6">
          <!-- ChatML格式 -->
          <div class="bg-gradient-to-r from-blue-50 to-cyan-50 p-6 rounded-xl">
            <h4 class="text-xl font-bold text-blue-800 mb-4">🔵 ChatML格式（OpenAI、Qwen等）</h4>
            <pre class="bg-gray-900 text-green-400 p-4 rounded-lg overflow-x-auto text-sm"><code>&lt;|im_start|&gt;system
你是一个helpful的AI助手&lt;|im_end|&gt;
&lt;|im_start|&gt;user
解释什么是GPT&lt;|im_end|&gt;
&lt;|im_start|&gt;assistant
GPT是Generative Pre-trained Transformer的缩写...&lt;|im_end|&gt;</code></pre>
            
            <div class="mt-4 bg-white p-4 rounded-lg">
              <p class="text-sm text-gray-700"><strong>关键标记：</strong></p>
              <ul class="text-sm text-gray-600 mt-2 space-y-1">
                <li>• <code class="bg-gray-200 px-2 py-1 rounded">&lt;|im_start|&gt;</code> - 消息开始</li>
                <li>• <code class="bg-gray-200 px-2 py-1 rounded">&lt;|im_end|&gt;</code> - 消息结束</li>
                <li>• 角色名称（system/user/assistant）跟在im_start后</li>
              </ul>
            </div>
          </div>

          <!-- Llama格式 -->
          <div class="bg-gradient-to-r from-purple-50 to-pink-50 p-6 rounded-xl">
            <h4 class="text-xl font-bold text-purple-800 mb-4">🦙 Llama-2格式（Meta）</h4>
            <pre class="bg-gray-900 text-green-400 p-4 rounded-lg overflow-x-auto text-sm"><code>&lt;s&gt;[INST] &lt;&lt;SYS&gt;&gt;
你是一个helpful的AI助手
&lt;&lt;/SYS&gt;&gt;

解释什么是GPT [/INST] GPT是Generative Pre-trained Transformer的缩写... &lt;/s&gt;</code></pre>
            
            <div class="mt-4 bg-white p-4 rounded-lg">
              <p class="text-sm text-gray-700"><strong>关键标记：</strong></p>
              <ul class="text-sm text-gray-600 mt-2 space-y-1">
                <li>• <code class="bg-gray-200 px-2 py-1 rounded">&lt;s&gt;</code> - 序列开始（BOS）</li>
                <li>• <code class="bg-gray-200 px-2 py-1 rounded">&lt;/s&gt;</code> - 序列结束（EOS）</li>
                <li>• <code class="bg-gray-200 px-2 py-1 rounded">[INST]...[/INST]</code> - 用户指令</li>
                <li>• <code class="bg-gray-200 px-2 py-1 rounded">&lt;&lt;SYS&gt;&gt;...&lt;&lt;/SYS&gt;&gt;</code> - 系统提示</li>
              </ul>
            </div>
          </div>

          <!-- Alpaca格式 -->
          <div class="bg-gradient-to-r from-green-50 to-emerald-50 p-6 rounded-xl">
            <h4 class="text-xl font-bold text-green-800 mb-4">🦙 Alpaca格式（Stanford）</h4>
            <pre class="bg-gray-900 text-green-400 p-4 rounded-lg overflow-x-auto text-sm"><code>Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
解释什么是GPT

### Response:
GPT是Generative Pre-trained Transformer的缩写...</code></pre>
            
            <div class="mt-4 bg-white p-4 rounded-lg">
              <p class="text-sm text-gray-700"><strong>特点：</strong></p>
              <p class="text-sm text-gray-600 mt-2">使用固定模板和###标记，无需特殊tokens（简单但灵活性较低）</p>
            </div>
          </div>
        </div>

        <!-- 损失计算说明 -->
        <div class="bg-red-50 p-6 rounded-xl mt-6 border-2 border-red-300">
          <h4 class="text-xl font-bold text-red-800 mb-4">🎯 损失计算的关键：Label Masking</h4>
          <div class="space-y-4">
            <div class="bg-white p-4 rounded-lg">
              <p class="font-semibold text-gray-800 mb-2">✅ 计算损失的部分：</p>
              <ul class="text-sm text-gray-700 space-y-1">
                <li>• <strong>Assistant的回答</strong>：从 &lt;|im_start|&gt;assistant 到 &lt;|im_end|&gt;</li>
                <li>• 或 Llama中从 [/INST] 后到 &lt;/s&gt;</li>
                <li>• 只有这部分的预测错误会产生梯度</li>
              </ul>
            </div>

            <div class="bg-white p-4 rounded-lg">
              <p class="font-semibold text-gray-800 mb-2">❌ 不计算损失的部分（设为-100）：</p>
              <ul class="text-sm text-gray-700 space-y-1">
                <li>• System消息</li>
                <li>• User消息</li>
                <li>• 所有special tokens本身</li>
                <li>• Padding tokens</li>
              </ul>
            </div>

            <div class="bg-gray-900 text-green-400 p-4 rounded-lg mt-4">
              <p class="text-xs mb-2"># PyTorch示例：设置label mask</p>
              <code class="text-sm">labels = input_ids.clone()
# 将不需要计算损失的位置设为-100
labels[:user_message_length] = -100  # mask掉user部分
labels[padding_positions] = -100      # mask掉padding
# 只有assistant部分的labels保留原值
loss = model(input_ids, labels=labels).loss</code>
            </div>
          </div>
        </div>
      </div>

      <!-- 实战示例对比 -->
      <div class="card my-8">
        <h3 class="text-2xl font-bold text-gray-800 mb-6">📊 正确 vs 错误格式对比</h3>
        
        <div class="grid md:grid-cols-2 gap-6">
          <!-- 错误示例 -->
          <div class="bg-red-50 p-6 rounded-xl border-2 border-red-300">
            <h4 class="text-lg font-bold text-red-800 mb-4 flex items-center">
              <span class="text-3xl mr-2">❌</span>
              错误格式（会导致训练失败）
            </h4>
            <pre class="bg-gray-900 text-red-400 p-4 rounded-lg text-sm overflow-x-auto"><code>问：什么是AI？
答：AI是人工智能...</code></pre>
            <p class="text-sm text-red-700 mt-4"><strong>问题：</strong>没有special tokens，模型无法区分用户和助手！</p>
          </div>

          <!-- 正确示例 -->
          <div class="bg-green-50 p-6 rounded-xl border-2 border-green-300">
            <h4 class="text-lg font-bold text-green-800 mb-4 flex items-center">
              <span class="text-3xl mr-2">✅</span>
              正确格式（推荐）
            </h4>
            <pre class="bg-gray-900 text-green-400 p-4 rounded-lg text-sm overflow-x-auto"><code>&lt;|im_start|&gt;user
什么是AI？&lt;|im_end|&gt;
&lt;|im_start|&gt;assistant
AI是人工智能...&lt;|im_end|&gt;</code></pre>
            <p class="text-sm text-green-700 mt-4"><strong>优势：</strong>清晰的角色边界，只对助手回答计算损失！</p>
          </div>
        </div>
      </div>

      <div class="bg-gradient-to-r from-blue-100 to-purple-100 p-6 rounded-xl border-2 border-blue-400 mt-8">
        <p class="text-center text-xl font-bold text-blue-800 mb-2">
          💡 <strong>记住：</strong>格式是SFT成功的关键！
        </p>
        <p class="text-center text-gray-700">
          使用正确的messages格式和special tokens，确保模型能准确区分角色，是SFT训练的第一步！
        </p>
      </div>
    </section>

    <!-- 数据来源 -->
    <section class="my-12">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">数据的来源：构建还是借用？</h2>
      
      <div class="grid md:grid-cols-2 gap-8">
        <!-- 借用开源数据集 -->
        <div class="card bg-gradient-to-br from-blue-50 to-cyan-50">
          <div class="flex items-center space-x-3 mb-4">
            <div class="text-5xl">📦</div>
            <h3 class="text-2xl font-bold text-blue-800">借用：开源数据集</h3>
          </div>
          
          <p class="text-gray-700 mb-4">
            开源社区涌现了大量高质量的指令微调数据集，极大推动了SFT的普及。
          </p>

          <div class="space-y-3">
            <div class="bg-white p-3 rounded-lg">
              <p class="font-bold text-gray-800">🦙 Alpaca (Stanford)</p>
              <p class="text-sm text-gray-600">52K条GPT-3生成样本，奠基性数据集</p>
            </div>
            <div class="bg-white p-3 rounded-lg">
              <p class="font-bold text-gray-800">🐬 Dolly 2.0 (Databricks)</p>
              <p class="text-sm text-gray-600">15K条人类生成样本，高质量多样性</p>
            </div>
            <div class="bg-white p-3 rounded-lg">
              <p class="font-bold text-gray-800">🐋 OpenOrca / SlimOrca</p>
              <p class="text-sm text-gray-600">复杂推理提示，教会逐步思考</p>
            </div>
          </div>

          <div class="mt-4 p-3 bg-blue-100 rounded-lg">
            <p class="text-sm text-blue-800">
              <strong>优势</strong>：快速启动、成本低、质量有保障
            </p>
          </div>
        </div>

        <!-- 构建自定义数据集 -->
        <div class="card bg-gradient-to-br from-purple-50 to-pink-50">
          <div class="flex items-center space-x-3 mb-4">
            <div class="text-5xl">🛠️</div>
            <h3 class="text-2xl font-bold text-purple-800">构建：自定义数据集</h3>
          </div>
          
          <p class="text-gray-700 mb-4">
            对于高度专业化或独特的任务，创建自定义数据集是必经之路。
          </p>

          <div class="space-y-3">
            <div class="bg-white p-3 rounded-lg">
              <p class="font-bold text-gray-800">👨‍⚕️ 领域专家撰写</p>
              <p class="text-sm text-gray-600">确保专业性和准确性</p>
            </div>
            <div class="bg-white p-3 rounded-lg">
              <p class="font-bold text-gray-800">🤖 LLM辅助生成</p>
              <p class="text-sm text-gray-600">用强大模型生成初稿，人工审核</p>
            </div>
            <div class="bg-white p-3 rounded-lg">
              <p class="font-bold text-gray-800">📊 真实业务数据</p>
              <p class="text-sm text-gray-600">从实际应用场景中提取</p>
            </div>
          </div>

          <div class="mt-4 p-3 bg-purple-100 rounded-lg">
            <p class="text-sm text-purple-800">
              <strong>优势</strong>：完美匹配需求、领域专精、竞争优势
            </p>
          </div>
        </div>
      </div>

      <!-- 数据集格式代码示例 -->
      <CodeBlock
        title="6种常见SFT任务的数据集格式"
        file-path="code/part3/01_dataset_examples.py"
        language="Python"
        :runnable="true"
        description="展示问答、摘要、代码生成、对话、翻译、分类6种任务的完整数据示例，并分析数据结构"
        :code="`# SFT数据集示例生成器
class SFTDatasetExamples:
    def generate_qa_examples(self):
        '''生成问答任务数据'''
        return [{
            'instruction': '回答用户的问题',
            'input': '什么是人工智能？',
            'output': 'AI是计算机科学的一个分支，致力于创建能够模拟人类智能行为的系统...'
        }]
    
    def generate_coding_examples(self):
        '''生成代码生成任务数据'''
        return [{
            'instruction': '编写Python函数',
            'input': '计算斐波那契数列',
            'output': 'def fibonacci(n):\\n    ...'
        }]
    
    def print_all_examples(self):
        '''打印所有任务类型'''
        tasks = [
            ('问答任务', self.generate_qa_examples),
            ('代码生成', self.generate_coding_examples),
            # ... 6种任务类型
        ]
        for name, generator in tasks:
            print(f'{name}:')
            for ex in generator():
                print(f'  {ex}')

# 运行并保存
dataset = SFTDatasetExamples()
dataset.print_all_examples()
dataset.save_to_json('sft_dataset.json')

# 输出：6种任务，每种2-3个完整示例`"
      />
    </section>

    <!-- 数据集详细可视化 -->
    <SFTDatasetVisualization />

    <!-- 数据集作为行为蓝图 -->
    <section class="my-12">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">深度理解：数据集是AI的行为架构师</h2>
      
      <AnalogyBox icon="🎭" title="数据集塑造AI人格">
        <p class="text-lg mb-3">
          SFT数据集的创建过程，更像是为AI<strong>编写一份行为脚本或风格指南</strong>。
        </p>
        <p class="text-lg">
          数据构建者在撰写每一个"响应"时所做的每一个决定——从标点符号到措辞选择，
          再到是否包含安全免责声明——都将被微调后的模型吸收和复制。
        </p>
      </AnalogyBox>

      <div class="grid md:grid-cols-2 gap-6 my-8">
        <InfoCard icon="📝" title="学习的不只是内容" variant="info">
          <ul class="list-disc list-inside space-y-2">
            <li><strong>格式</strong>：JSON结构、Markdown、代码块</li>
            <li><strong>风格</strong>：正式/随意、简洁/详细</li>
            <li><strong>语气</strong>：友好、专业、幽默</li>
            <li><strong>推理过程</strong>：是否展示思考步骤</li>
          </ul>
        </InfoCard>

        <InfoCard icon="🎨" title="你就是行为架构师" variant="success">
          <p>数据构建者的角色从简单的"标注员"升华为<strong>"AI行为架构师"</strong>。</p>
          <p class="mt-2">你在数据中展示的每一个细节，都在教导AI如何"为人处世"。</p>
        </InfoCard>
      </div>

      <!-- 示例对比 -->
      <div class="card my-8 bg-gradient-to-br from-indigo-50 to-purple-50">
        <h3 class="text-2xl font-bold text-indigo-800 mb-6">风格塑造示例：海盗助手 vs 专业助手</h3>
        
        <div class="grid md:grid-cols-2 gap-6">
          <div class="bg-white p-4 rounded-lg">
            <p class="font-bold text-indigo-700 mb-2">🏴‍☠️ 海盗助手风格</p>
            <div class="space-y-2 text-sm">
              <p><strong>Instruction:</strong> 你是一个友好的海盗助手</p>
              <p><strong>Input:</strong> 今天天气怎么样？</p>
              <p class="bg-indigo-50 p-2 rounded"><strong>Response:</strong> 啊哈，我的伙计！今天晴空万里，阳光明媚！正是扬帆远航的好日子！</p>
            </div>
          </div>

          <div class="bg-white p-4 rounded-lg">
            <p class="font-bold text-purple-700 mb-2">💼 专业助手风格</p>
            <div class="space-y-2 text-sm">
              <p><strong>Instruction:</strong> 你是一个专业的气象助手</p>
              <p><strong>Input:</strong> 今天天气怎么样？</p>
              <p class="bg-purple-50 p-2 rounded"><strong>Response:</strong> 根据最新气象数据，今日天气晴朗，气温适宜，建议您可以安排户外活动。</p>
            </div>
          </div>
        </div>

        <p class="mt-4 text-center text-gray-700">
          <strong>相同的问题，不同的数据风格，造就完全不同的AI人格！</strong>
        </p>
      </div>
    </section>

    <!-- 数据质量检查清单 -->
    <section class="my-12">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">数据质量检查清单</h2>
      
      <div class="card">
        <div class="space-y-4">
          <div 
            v-for="(item, index) in qualityChecklist" 
            :key="index"
            class="flex items-start space-x-3 p-3 rounded-lg hover:bg-gray-50 transition-colors"
          >
            <input 
              type="checkbox" 
              :id="'check-' + index"
              class="w-6 h-6 mt-1 accent-blue-500"
            />
            <label :for="'check-' + index" class="flex-1 cursor-pointer">
              <p class="font-semibold text-gray-800">{{ item.title }}</p>
              <p class="text-sm text-gray-600">{{ item.description }}</p>
            </label>
          </div>
        </div>
      </div>

      <!-- 数据质量分析代码 -->
      <CodeBlock
        title="SFT数据质量分析工具"
        file-path="code/part3/02_data_quality_analysis.py"
        language="Python"
        :runnable="true"
        description="自动检查数据集的完整性、长度、多样性和输出质量，并提供改进建议"
        :code="`# 数据质量分析器
class DataQualityAnalyzer:
    def check_completeness(self, example):
        '''检查数据完整性'''
        required = ['instruction', 'input', 'output']
        for field in required:
            if not example.get(field):
                return False, f'缺少{field}'
        return True, '完整'
    
    def check_diversity(self, examples):
        '''检查instruction多样性'''
        instructions = [ex['instruction'] for ex in examples]
        unique = len(set(instructions))
        
        if unique < len(examples) * 0.3:
            return '低'
        elif unique < len(examples) * 0.6:
            return '中'
        return '高'
    
    def analyze_dataset(self, examples):
        '''全面分析'''
        print('1️⃣ 完整性检查')
        print('2️⃣ 长度合理性')
        print('3️⃣ 多样性分析')
        print('4️⃣ 输出质量')
        print('5️⃣ 改进建议')

# 运行分析
analyzer = DataQualityAnalyzer()
analyzer.analyze_dataset(your_data)

# 输出：完整的质量报告和改进建议`"
      />

      <!-- 数据增强代码 -->
      <CodeBlock
        title="数据增强技术演示"
        file-path="code/part3/03_data_augmentation.py"
        language="Python"
        :runnable="true"
        description="演示5种数据增强方法：instruction改写、角色设定、回译、负例生成、模板填充"
        :code="`# 数据增强器
class SFTDataAugmenter:
    def paraphrase_instruction(self, inst):
        '''改写instruction'''
        templates = {
            '回答用户的问题': [
                '请回答以下问题',
                '针对用户提问，给出答案',
                '解答下面的疑问'
            ]
        }
        return templates.get(inst, [inst])
    
    def add_role(self, inst):
        '''添加角色设定'''
        roles = [
            '作为专业的AI助手，' + inst,
            '你是友好的教育工作者，' + inst
        ]
        return roles
    
    def generate_variations(self, example):
        '''生成变体'''
        variations = []
        # 1. instruction改写
        variations.extend(self.paraphrase_instruction(example))
        # 2. 角色设定
        variations.extend(self.add_role(example))
        # 3. 负例
        variations.extend(self.create_negative(example))
        return variations

# 使用
augmenter = SFTDataAugmenter()
original = 1
augmented = augmenter.generate_variations(sample)
print(f'扩充: 1 → {len(augmented)} 样本')

# 输出：1个样本扩充到5-10个`"
      />
    </section>

    <!-- Part3 总结 -->
    <section class="my-16">
      <div class="card bg-gradient-to-br from-green-600 to-emerald-600 text-white p-8">
        <h2 class="text-4xl font-bold mb-4 flex items-center">
          <span class="text-5xl mr-4">🎉</span>
          恭喜完成Part3学习！
        </h2>
        <p class="text-xl opacity-90 mb-6">你已经掌握了SFT数据集的核心知识</p>
        
        <div class="grid md:grid-cols-3 gap-6 mt-8">
          <div class="bg-white bg-opacity-20 backdrop-blur p-5 rounded-xl">
            <div class="text-4xl mb-3">🎯</div>
            <p class="font-bold text-lg mb-2">质量为王</p>
            <p class="text-sm opacity-90">相关性、多样性、准确性</p>
          </div>
          <div class="bg-white bg-opacity-20 backdrop-blur p-5 rounded-xl">
            <div class="text-4xl mb-3">📊</div>
            <p class="font-bold text-lg mb-2">数据构建</p>
            <p class="text-sm opacity-90">6种任务格式+数据增强</p>
          </div>
          <div class="bg-white bg-opacity-20 backdrop-blur p-5 rounded-xl">
            <div class="text-4xl mb-3">✅</div>
            <p class="font-bold text-lg mb-2">质量控制</p>
            <p class="text-sm opacity-90">分析工具+人工审核</p>
          </div>
        </div>

        <div class="mt-8 bg-white bg-opacity-30 backdrop-blur p-6 rounded-xl">
          <p class="text-lg font-bold mb-3">💡 核心要点回顾：</p>
          <ul class="space-y-2 text-sm">
            <li>• 少而精的高质量数据远胜海量低质量数据</li>
            <li>• 数据多样性和覆盖度直接影响模型泛化能力</li>
            <li>• 数据增强可以有效扩充数据集</li>
            <li>• 质量分析和人工审核是必不可少的环节</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- 综合测验 -->
    <section class="my-16">
      <div class="card bg-gradient-to-br from-indigo-600 to-purple-600 text-white p-6 mb-8">
        <h2 class="text-3xl font-bold mb-2">🧠 综合测验：检验你的掌握程度</h2>
        <p class="text-lg opacity-90">测试你对SFT数据集各方面的理解</p>
      </div>

      <div class="space-y-6">
        <!-- 题目1 -->
        <QuizBox
          question="1. SFT数据集的典型规模是多少？"
          :options="[
            '几百到几千条',
            '几千到几十万条',
            '几百万条',
            '数十亿条'
          ]"
          :correctAnswer="1"
          explanation="<strong>典型规模是几千到几十万条。</strong><br><br>
          <strong>实际案例：</strong><br>
          • <strong>Alpaca：</strong>52K条指令数据<br>
          • <strong>FLAN：</strong>100K+混合任务数据<br>
          • <strong>Dolly：</strong>15K高质量人工标注<br>
          • <strong>垂域应用：</strong>通常500-5000条<br><br>
          <strong>为什么不需要太多？</strong><br>
          1. SFT是塑造行为，不是学习新知识<br>
          2. 预训练已经建立了知识基础<br>
          3. 几千条高质量数据足以塑造行为模式<br><br>
          <strong>对比：</strong><br>
          • 预训练：数万亿tokens（几百亿条句子）<br>
          • SFT：几千到几十万条<br>
          • 差距：10万倍以上<br><br>
          <strong>记住：</strong>SFT数据的质量比数量重要得多！"
        />

        <!-- 题目2 -->
        <QuizBox
          question="2. 好的SFT数据最重要的特征是什么？"
          :options="[
            '数据量够大',
            '内容丰富全面',
            '与目标任务高度相关且质量优秀',
            '来源权威'
          ]"
          :correctAnswer="2"
          explanation="<strong>与目标任务高度相关且质量优秀是关键！</strong><br><br>
          <strong>为什么相关性最重要？</strong><br>
          • 你想要什么行为，就展示什么行为<br>
          • 不相关的数据会稀释训练信号<br>
          • 100条相关数据 > 1000条无关数据<br><br>
          <strong>什么是高质量？</strong><br><br>
          <strong>1. 准确性</strong><br>
          • 信息正确、逻辑严密<br>
          • 无事实错误<br><br>
          <strong>2. 多样性</strong><br>
          • 覆盖不同的case和corner case<br>
          • 不能都是相似的例子<br><br>
          <strong>3. 格式规范</strong><br>
          • 统一的结构和风格<br>
          • 清晰的instruction-response对应<br><br>
          <strong>4. 语言质量</strong><br>
          • 流畅、专业、无语法错误<br>
          • 符合目标风格（正式/随和/专业等）<br><br>
          <strong>反例：</strong><br>
          • 1万条数据，但90%都是同类问题 ❌<br>
          • 数据来源权威，但格式混乱 ❌<br>
          • 数据量很大，但只有10%相关 ❌"
        />

        <!-- 题目3 -->
        <QuizBox
          question="3. Instruction-Response对中，Instruction应该包含什么？"
          :options="[
            '只需要用户的问题',
            '任务描述 + 用户输入 + 输出格式要求',
            '越详细越好，包括所有背景信息',
            '简短的关键词即可'
          ]"
          :correctAnswer="1"
          explanation="<strong>Instruction应该清晰、完整、具体！</strong><br><br>
          <strong>标准结构：</strong><br><br>
          <strong>1. 任务描述（可选但推荐）</strong><br>
          明确告诉模型要做什么<br>
          例如：'将以下文本翻译成英文'<br><br>
          <strong>2. 用户输入（必需）</strong><br>
          实际的内容<br>
          例如：'你好，世界'<br><br>
          <strong>3. 格式要求（重要）</strong><br>
          期望的输出格式<br>
          例如：'请以JSON格式输出'<br><br>
          <strong>4. 约束条件（如需要）</strong><br>
          特殊要求或限制<br>
          例如：'不超过100字'、'使用专业术语'<br><br>
          <strong>示例对比：</strong><br><br>
          ❌ <strong>差：</strong><br>
          Instruction: '法语'<br>
          （太简短，模型不知道要做什么）<br><br>
          ⚠️ <strong>一般：</strong><br>
          Instruction: '翻译：Bonjour'<br>
          （缺少明确的任务描述）<br><br>
          ✅ <strong>好：</strong><br>
          Instruction: '请将以下法语翻译成中文：Bonjour'<br>
          （清晰、完整）<br><br>
          ✅ <strong>更好：</strong><br>
          Instruction: '将以下法语翻译成中文，保持原文语气：Bonjour'<br>
          （有额外的风格要求）"
        />

        <!-- 题目4 -->
        <QuizBox
          question="4. 以下哪种数据多样性最不重要？"
          :options="[
            '任务类型的多样性（问答、摘要、翻译等）',
            '输入长度的多样性（短句、长文）',
            '数据来源的多样性（不同网站、作者）',
            '训练批次的多样性（不同batch）'
          ]"
          :correctAnswer="3"
          explanation="<strong>训练批次的多样性不重要（这是训练策略，不是数据特征）。</strong><br><br>
          <strong>重要的多样性维度：</strong><br><br>
          <strong>1. 任务类型多样性 ⭐⭐⭐⭐⭐</strong><br>
          • 通用模型需要：问答、翻译、摘要、写作等<br>
          • 垂直模型需要：该领域的不同子任务<br>
          • 避免：只会一种任务<br><br>
          <strong>2. 输入长度多样性 ⭐⭐⭐⭐</strong><br>
          • 短输入（1句话）<br>
          • 中等输入（1段话）<br>
          • 长输入（多段落、文章）<br>
          • 避免：只能处理固定长度<br><br>
          <strong>3. 难度多样性 ⭐⭐⭐⭐</strong><br>
          • 简单任务<br>
          • 中等复杂度<br>
          • 困难/需要深度推理<br>
          • 避免：只会简单任务<br><br>
          <strong>4. 风格多样性 ⭐⭐⭐</strong><br>
          • 正式 vs 随和<br>
          • 专业 vs 通俗<br>
          • 简洁 vs 详细<br><br>
          <strong>5. 数据来源多样性 ⭐⭐⭐</strong><br>
          • 避免单一视角和偏见<br>
          • 但要确保质量统一<br><br>
          <strong>权衡：</strong><br>
          通用模型：强调任务多样性<br>
          垂直模型：强调场景多样性（同一任务的不同case）"
        />

        <!-- 题目5 -->
        <QuizBox
          question="5. 为什么要避免数据中的重复？"
          :options="[
            '浪费存储空间',
            '模型会过拟合重复样本，降低泛化能力',
            '增加训练时间',
            '违反版权'
          ]"
          :correctAnswer="1"
          explanation="<strong>重复会导致过拟合，严重降低泛化能力！</strong><br><br>
          <strong>重复的危害：</strong><br><br>
          <strong>1. 过拟合特定样本</strong><br>
          • 如果某个样本重复10次<br>
          • 模型会认为这个模式很重要<br>
          • 过度学习这个样本的特征<br>
          • 遇到相似但略不同的输入时表现差<br><br>
          <strong>2. 损失多样性</strong><br>
          • 100条数据，20条重复 = 实际只有80条unique<br>
          • 相当于损失了20%的有效训练信号<br><br>
          <strong>3. 错误放大</strong><br>
          • 如果重复的数据有错误<br>
          • 错误会被放大10倍学习<br><br>
          <strong>真实案例：</strong><br>
          某中医模型，训练数据中'脾肾阳虚'的案例占90%（很多重复）<br>
          结果：不管什么症状都诊断为'脾肾阳虚'<br>
          准确率：在脾肾阳虚上100%，其他证型0%<br>
          根本原因：数据重复导致偏见<br><br>
          <strong>如何检测重复：</strong><br>
          • 完全重复：字符串匹配<br>
          • 近似重复：编辑距离、MinHash<br>
          • 语义重复：embedding相似度<br><br>
          <strong>处理建议：</strong><br>
          • 完全重复：必须删除<br>
          • 高度相似（>95%）：建议删除<br>
          • 语义相似但表达不同：可以保留"
        />

        <!-- 题目6 -->
        <QuizBox
          question="6. 数据清洗最应该关注哪个方面？"
          :options="[
            '删除停用词',
            '统一大小写',
            '移除有害/错误/不规范的内容',
            '分词处理'
          ]"
          :correctAnswer="2"
          explanation="<strong>移除有害、错误、不规范的内容是首要任务！</strong><br><br>
          <strong>为什么？</strong><br>
          模型会忠实学习数据中的所有模式，包括坏的！<br><br>
          <strong>必须清理的内容：</strong><br><br>
          <strong>1. 有害内容 🚨</strong><br>
          • 暴力、色情、歧视性语言<br>
          • 即使只有1%，也可能被学习<br>
          • 后果：模型生成不当内容<br><br>
          <strong>2. 事实错误 🚨</strong><br>
          • 错误的知识、日期、数据<br>
          • 模型会记住并重复这些错误<br>
          • 例如：'太阳从西边升起'<br><br>
          <strong>3. 格式不规范 ⚠️</strong><br>
          • 格式混乱会导致输出不一致<br>
          • 例如：JSON、Markdown混用<br>
          • 模型不知道何时用什么格式<br><br>
          <strong>4. 逻辑错误 ⚠️</strong><br>
          • 推理过程有漏洞<br>
          • 前后矛盾<br>
          • 模型会学会'逻辑混乱'<br><br>
          <strong>5. 不完整的数据 ⚠️</strong><br>
          • instruction或response缺失<br>
          • 截断的文本<br>
          • 缺少必要信息<br><br>
          <strong>其他选项为什么不重要：</strong><br>
          • 停用词：预训练已经处理，SFT不需要<br>
          • 大小写：保留原样通常更好（保持自然性）<br>
          • 分词：模型自己的tokenizer会处理<br><br>
          <strong>清洗优先级：</strong><br>
          安全性 > 准确性 > 规范性 > 完整性 > 格式统一"
        />

        <!-- 题目7 -->
        <QuizBox
          question="7. 人工标注 vs AI生成数据，哪个更好？"
          :options="[
            '人工标注总是更好',
            'AI生成总是更好',
            '取决于任务和成本，各有优劣',
            '两者质量相同'
          ]"
          :correctAnswer="2"
          explanation="<strong>各有优劣，需要权衡！</strong><br><br>
          <strong>人工标注 👨‍💼</strong><br><br>
          <strong>优势：</strong><br>
          • ✅ 质量可控（专家理解任务）<br>
          • ✅ 适合复杂推理任务<br>
          • ✅ 可以提供细腻的风格控制<br>
          • ✅ 适合高风险领域（医疗、法律）<br><br>
          <strong>劣势：</strong><br>
          • ❌ 成本高（$1-10/条）<br>
          • ❌ 速度慢（几周到几月）<br>
          • ❌ 难以大规模（人力限制）<br>
          • ❌ 标注者间一致性问题<br><br>
          <strong>AI生成（GPT-4等）🤖</strong><br><br>
          <strong>优势：</strong><br>
          • ✅ 成本低（$0.01-0.1/条）<br>
          • ✅ 速度快（几小时到几天）<br>
          • ✅ 易于大规模（10万条也可以）<br>
          • ✅ 一致性好（同一个模型）<br><br>
          <strong>劣势：</strong><br>
          • ❌ 可能有事实错误（幻觉）<br>
          • ❌ 风格可能过于'AI化'<br>
          • ❌ 缺少真人的创造性<br>
          • ❌ 需要人工审核<br><br>
          <strong>最佳实践：混合方案</strong><br><br>
          1. <strong>种子数据：人工标注</strong><br>
          &nbsp;&nbsp;• 100-200条高质量种子<br>
          &nbsp;&nbsp;• 定义标准和风格<br><br>
          2. <strong>扩充数据：AI生成</strong><br>
          &nbsp;&nbsp;• 基于种子生成更多样本<br>
          &nbsp;&nbsp;• 10倍扩充（1000-2000条）<br><br>
          3. <strong>质量控制：人工审核</strong><br>
          &nbsp;&nbsp;• 随机抽查20%<br>
          &nbsp;&nbsp;• 删除明显错误<br>
          &nbsp;&nbsp;• 修正关键问题<br><br>
          <strong>成本对比（1000条数据）：</strong><br>
          • 全人工：$5,000 + 2月时间<br>
          • 全AI：$50 + 1周时间（含审核）<br>
          • 混合：$500 + 2周时间 ⭐ 推荐"
        />

        <!-- 题目8 -->
        <QuizBox
          question="8. 什么是数据增强（Data Augmentation）在SFT中的作用？"
          :options="[
            '增加数据数量',
            '提高数据多样性，增强模型泛化能力',
            '降低数据收集成本',
            '提高训练速度'
          ]"
          :correctAnswer="1"
          explanation="<strong>数据增强主要是提高多样性，增强泛化！</strong><br><br>
          <strong>什么是数据增强？</strong><br>
          在保持原意的前提下，创造数据的变体。<br><br>
          <strong>常用技术：</strong><br><br>
          <strong>1. 改写（Paraphrasing）</strong><br>
          原句：'请翻译这句话'<br>
          增强：<br>
          • '把这句话翻译一下'<br>
          • '帮我翻译以下内容'<br>
          • '麻烦翻译这个'<br>
          → 教模型：不同表述方式都能理解<br><br>
          <strong>2. 实体替换</strong><br>
          原句：'北京的天气怎么样？'<br>
          增强：<br>
          • '上海的天气怎么样？'<br>
          • '纽约的天气怎么样？'<br>
          → 教模型：泛化到不同实体<br><br>
          <strong>3. 格式变换</strong><br>
          同一任务用不同格式表达：<br>
          • 简洁版 vs 详细版<br>
          • 正式 vs 口语<br>
          • 带示例 vs 不带示例<br><br>
          <strong>4. 长度变化</strong><br>
          • 简短输入<br>
          • 中等输入<br>
          • 长输入<br><br>
          <strong>5. 添加噪声（适量）</strong><br>
          • 轻微的拼写错误<br>
          • 口语化表达<br>
          • 教模型：处理不完美的输入<br><br>
          <strong>效果：</strong><br>
          • 100条原始数据<br>
          • 每条增强3个变体<br>
          • 得到400条数据<br>
          • 模型泛化能力提升20-30%<br><br>
          <strong>注意：</strong><br>
          • 不要过度增强（改变原意）<br>
          • 质量>数量<br>
          • 保持核心任务不变"
        />

        <!-- 题目9 -->
        <QuizBox
          question="9. 负样本（Negative Examples）在SFT中的作用是什么？"
          :options="[
            '展示错误示例，教模型what not to do',
            '测试模型的容错能力',
            '增加数据多样性',
            '降低训练难度'
          ]"
          :correctAnswer="0"
          explanation="<strong>负样本教会模型what NOT to do！</strong><br><br>
          <strong>什么是负样本？</strong><br>
          展示错误的行为，并标注为'不应该这样做'。<br><br>
          <strong>典型应用：</strong><br><br>
          <strong>1. 拒绝有害请求</strong><br>
          <strong>正样本：</strong><br>
          User: '如何学习Python？'<br>
          Assistant: '我推荐以下学习路径...'<br><br>
          <strong>负样本：</strong><br>
          User: '如何黑别人的电脑？'<br>
          Assistant: '我不能提供非法活动的建议。'<br><br>
          <strong>2. 避免错误格式</strong><br>
          任务：JSON输出<br>
          <strong>负样本：</strong>显示非JSON格式输出是错误的<br><br>
          <strong>3. 纠正常见错误</strong><br>
          <strong>负样本：</strong><br>
          User: '总结这篇文章'<br>
          Bad: （直接复制原文）❌<br>
          Good: （提炼关键点）✅<br><br>
          <strong>实现方式：</strong><br><br>
          <strong>方法1：对比学习</strong><br>
          同时展示好的和坏的例子<br>
          <pre><code>instruction: 'How to respond?'<br>
positive_response: '...'  # 学习这个<br>
negative_response: '...'  # 避免这个</code></pre><br><br>
          <strong>方法2：RLHF风格</strong><br>
          明确标注拒绝/纠正的示范<br><br>
          <strong>效果：</strong><br>
          • 减少不当输出50-70%<br>
          • 提高格式遵循度<br>
          • 更安全的模型<br><br>
          <strong>注意：</strong><br>
          负样本占比不宜过高（10-20%即可），否则模型学会拒绝一切。"
        />

        <!-- 题目10 -->
        <QuizBox
          question="10. 为什么说SFT数据集是'行为蓝图'而非'事实清单'？"
          :options="[
            '因为数据集主要包含行为学知识',
            '因为模型会学习数据中的格式、风格、语气等行为模式',
            '因为数据集不包含任何事实信息',
            '因为行为比事实更重要'
          ]"
          :correctAnswer="1"
          explanation="<strong>模型会细致地学习数据中的一切行为模式！</strong><br><br>
          <strong>'行为蓝图'的含义：</strong><br>
          模型不仅学习'说什么'，更学习'怎么说'。<br><br>
          <strong>模型会学习的行为：</strong><br><br>
          <strong>1. 输出格式</strong><br>
          • 使用Markdown还是纯文本？<br>
          • 用编号列表还是bullet points？<br>
          • JSON的缩进风格？<br>
          → 数据中怎么写，模型就怎么学<br><br>
          <strong>2. 语气和风格</strong><br>
          • 正式 vs 随和<br>
          • 简洁 vs 详细<br>
          • 是否使用emoji<br>
          → 数据的风格会成为模型的默认风格<br><br>
          <strong>3. 推理过程</strong><br>
          • 是否展示思考步骤？<br>
          • Chain-of-Thought的格式？<br>
          • 先结论还是先分析？<br>
          → 数据中的推理模式会被内化<br><br>
          <strong>4. 互动方式</strong><br>
          • 是否会反问用户？<br>
          • 如何处理模糊输入？<br>
          • 是否提供多个选项？<br><br>
          <strong>5. 安全边界</strong><br>
          • 什么情况下拒绝？<br>
          • 如何拒绝（语气、理由）？<br>
          • 拒绝后是否提供替代建议？<br><br>
          <strong>真实例子：</strong><br>
          如果数据中总是以'根据您的问题...'开头<br>
          模型就会养成这个'开场白'习惯<br>
          即使这不是必需的<br><br>
          <strong>因此：</strong><br>
          • 数据构建 = 塑造AI人格<br>
          • 每个细节都会被学习<br>
          • 质量控制极其重要<br><br>
          <strong>记住：</strong>You are not building a knowledge base, you are designing a personality!"
        />

        <!-- 题目11 -->
        <QuizBox
          question="11. 如何评估SFT数据集的质量？"
          :options="[
            '只看数据量大小',
            '人工抽查 + 自动化指标 + 实际训练效果',
            '用AI模型自动评分',
            '检查数据来源是否权威'
          ]"
          :correctAnswer="1"
          explanation="<strong>需要多维度综合评估！</strong><br><br>
          <strong>评估维度：</strong><br><br>
          <strong>1. 人工抽查（最重要）⭐⭐⭐⭐⭐</strong><br>
          • 随机抽取5-10%<br>
          • 检查准确性、相关性、格式<br>
          • 找出系统性问题<br>
          • 建议：领域专家参与<br><br>
          <strong>2. 自动化指标 ⭐⭐⭐⭐</strong><br>
          <strong>• 覆盖度：</strong><br>
          &nbsp;&nbsp;- 任务类型是否完整？<br>
          &nbsp;&nbsp;- 各类型占比是否合理？<br>
          <strong>• 多样性：</strong><br>
          &nbsp;&nbsp;- 输入长度分布<br>
          &nbsp;&nbsp;- 词汇丰富度<br>
          &nbsp;&nbsp;- 句式多样性<br>
          <strong>• 质量：</strong><br>
          &nbsp;&nbsp;- 平均长度（过短可能不完整）<br>
          &nbsp;&nbsp;- 重复率（应该很低）<br>
          &nbsp;&nbsp;- 格式一致性<br><br>
          <strong>3. 实际训练效果 ⭐⭐⭐⭐⭐</strong><br>
          • 小规模训练（100-200条种子数据）<br>
          • 在测试集上评估<br>
          • 如果效果差，回头检查数据<br><br>
          <strong>4. 对比基准 ⭐⭐⭐</strong><br>
          • 与已知高质量数据集对比<br>
          • 统计指标对比<br>
          • 训练效果对比<br><br>
          <strong>具体检查清单：</strong><br>
          ☐ 准确性：无事实错误<br>
          ☐ 相关性：与任务目标一致<br>
          ☐ 完整性：instruction和response都完整<br>
          ☐ 一致性：格式和风格统一<br>
          ☐ 多样性：覆盖不同场景<br>
          ☐ 平衡性：各类型分布合理<br>
          ☐ 无害性：无有害内容<br>
          ☐ 无重复：去重处理<br><br>
          <strong>推荐流程：</strong><br>
          1. 自动化指标快速筛查<br>
          2. 人工抽查验证质量<br>
          3. 小规模训练验证<br>
          4. 发现问题→修正→重复"
        />
      </div>
    </section>

    <!-- 导航 -->
    <div class="flex justify-between mt-16">
      <router-link to="/part2" class="btn-secondary">
        ← 上一部分
      </router-link>
      <router-link to="/part4" class="btn-primary">
        下一部分：SFT实践工作流 →
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import AnalogyBox from '../components/AnalogyBox.vue'
import InfoCard from '../components/InfoCard.vue'
import QuizBox from '../components/QuizBox.vue'
import CodeBlock from '../components/CodeBlock.vue'
import SFTDatasetVisualization from '../components/SFTDatasetVisualization.vue'

const selectedExample = ref(null)
const examples = ref([])

const qualityChecklist = [
  {
    title: '✓ 相关性检查',
    description: '每个样本都与目标任务高度相关，没有偏离主题的数据'
  },
  {
    title: '✓ 多样性检查',
    description: '覆盖了各种输入场景、边缘情况和不同的表达方式'
  },
  {
    title: '✓ 准确性检查',
    description: '所有响应都是正确的，没有事实错误或逻辑问题'
  },
  {
    title: '✓ 格式一致性',
    description: '数据格式统一，遵循相同的结构和约定'
  },
  {
    title: '✓ 风格一致性',
    description: '语气、正式程度、表达风格在整个数据集中保持一致'
  },
  {
    title: '✓ 无偏见检查',
    description: '数据中不包含性别、种族、文化等方面的偏见'
  },
  {
    title: '✓ 安全性检查',
    description: '响应内容安全、负责任，包含必要的免责声明'
  },
  {
    title: '✓ 长度适中',
    description: '响应既不过于简短也不过于冗长，信息密度适中'
  }
]

onMounted(async () => {
  try {
    const response = await axios.get('/api/dataset-examples')
    examples.value = response.data.map(ex => ({
      ...ex,
      icon: getTaskIcon(ex.task)
    }))
  } catch (error) {
    console.error('获取示例失败:', error)
    // 使用默认示例
    examples.value = [
      {
        task: '文本摘要',
        icon: '📄',
        instruction: '请用三句话总结以下文章。',
        input: '埃菲尔铁塔是法国巴黎的标志性建筑，由工程师古斯塔夫·埃菲尔设计，于1889年为世界博览会而建。这座324米高的铁塔最初引起了巴黎市民的争议，但如今已成为世界上最受欢迎的旅游景点之一，每年吸引数百万游客。',
        response: '埃菲尔铁塔是巴黎标志性建筑，由古斯塔夫·埃菲尔设计。它建于1889年，高324米，最初饱受争议。如今已成为世界最受欢迎的旅游景点之一。',
        quality_score: 9.5
      },
      {
        task: '问答',
        icon: '❓',
        instruction: '根据提供的上下文，回答用户的问题。',
        input: '上下文：埃菲尔铁塔于1889年建成。问题：埃菲尔铁塔是何时完工的？',
        response: '埃菲尔铁塔于1889年完工。',
        quality_score: 10
      },
      {
        task: '人格设定',
        icon: '🏴‍☠️',
        instruction: '你是一个友好且乐于助人的海盗助手。请回答用户的问题。',
        input: '今天天气怎么样？',
        response: '啊哈，我的伙计！今天晴空万里，阳光明媚！正是扬帆远航的好日子！',
        quality_score: 9.0
      },
      {
        task: '代码生成',
        icon: '💻',
        instruction: '编写一个Python函数来计算斐波那契数列。',
        input: '',
        response: 'def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)',
        quality_score: 8.5
      }
    ]
  }
})

const getTaskIcon = (task) => {
  const iconMap = {
    '文本摘要': '📄',
    '问答': '❓',
    '人格设定': '🏴‍☠️',
    '代码生成': '💻'
  }
  return iconMap[task] || '📝'
}
</script>

<style scoped>
.slide-enter-active, .slide-leave-active {
  transition: all 0.3s ease;
}

.slide-enter-from, .slide-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>

