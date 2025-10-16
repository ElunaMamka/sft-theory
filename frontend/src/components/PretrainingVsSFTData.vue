<template>
  <div class="my-12">
    <h2 class="text-3xl font-bold text-gray-800 mb-8 text-center">
      📊 预训练数据 vs SFT数据：具体示例对比
    </h2>

    <!-- 预训练数据示例 -->
    <div class="card mb-8 bg-gradient-to-br from-blue-50 to-cyan-50">
      <h3 class="text-2xl font-bold text-blue-800 mb-6 flex items-center">
        <span class="text-4xl mr-3">📚</span>
        预训练数据示例
      </h3>
      
      <div class="space-y-6">
        <!-- 示例1 -->
        <div class="bg-white p-6 rounded-xl shadow-sm">
          <div class="flex items-center justify-between mb-3">
            <h4 class="font-bold text-lg text-gray-800">示例1：维基百科文章</h4>
            <span class="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm">未标注文本</span>
          </div>
          <div class="bg-gray-50 p-4 rounded-lg font-mono text-sm mb-3">
            <p class="text-gray-800 leading-relaxed">
              人工智能（Artificial Intelligence，缩写为AI）是计算机科学的一个分支，
              它企图了解智能的实质，并生产出一种新的能以人类智能相似的方式做出反应的智能机器。
              该领域的研究包括机器人、语言识别、图像识别、自然语言处理和专家系统等。
            </p>
          </div>
          <div class="bg-blue-100 p-4 rounded-lg">
            <p class="font-bold text-blue-900 mb-2">🎯 训练任务</p>
            <div class="space-y-2 text-sm">
              <div class="flex items-start space-x-2">
                <span class="text-blue-600">输入:</span>
                <span class="flex-1 bg-white px-2 py-1 rounded">"人工智能是计算机科学的一个"</span>
              </div>
              <div class="flex items-start space-x-2">
                <span class="text-blue-600">目标:</span>
                <span class="flex-1 bg-white px-2 py-1 rounded font-bold">"分支"</span>
              </div>
              <div class="flex items-start space-x-2">
                <span class="text-blue-600">损失:</span>
                <span class="flex-1">交叉熵损失 = -log P(分支 | context)</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 示例2 -->
        <div class="bg-white p-6 rounded-xl shadow-sm">
          <div class="flex items-center justify-between mb-3">
            <h4 class="font-bold text-lg text-gray-800">示例2：GitHub代码</h4>
            <span class="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm">代码语料</span>
          </div>
          <div class="bg-gray-900 p-4 rounded-lg mb-3">
            <pre class="text-green-400 text-sm font-mono">def calculate_sum(a, b):
    """计算两数之和"""
    result = a + b
    return result</pre>
          </div>
          <div class="bg-blue-100 p-4 rounded-lg">
            <p class="font-bold text-blue-900 mb-2">🎯 训练任务</p>
            <div class="space-y-2 text-sm">
              <div class="flex items-start space-x-2">
                <span class="text-blue-600">输入:</span>
                <span class="flex-1 bg-white px-2 py-1 rounded font-mono">def calculate_sum(a, b):</span>
              </div>
              <div class="flex items-start space-x-2">
                <span class="text-blue-600">目标:</span>
                <span class="flex-1 bg-white px-2 py-1 rounded font-bold font-mono">"""计算...</span>
              </div>
              <div class="flex items-start space-x-2">
                <span class="text-blue-600">学习:</span>
                <span class="flex-1">代码结构、文档字符串格式、编程模式</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 示例3 -->
        <div class="bg-white p-6 rounded-xl shadow-sm">
          <div class="flex items-center justify-between mb-3">
            <h4 class="font-bold text-lg text-gray-800">示例3：新闻文章</h4>
            <span class="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm">新闻语料</span>
          </div>
          <div class="bg-gray-50 p-4 rounded-lg font-mono text-sm mb-3">
            <p class="text-gray-800 leading-relaxed">
              【科技新闻】OpenAI今日发布最新大语言模型GPT-4，相比前代版本，
              新模型在推理能力、代码生成和多语言理解方面都有显著提升。
            </p>
          </div>
          <div class="bg-blue-100 p-4 rounded-lg">
            <p class="font-bold text-blue-900 mb-2">🎯 训练任务</p>
            <div class="space-y-2 text-sm">
              <div class="flex items-start space-x-2">
                <span class="text-blue-600">输入:</span>
                <span class="flex-1 bg-white px-2 py-1 rounded">"新模型在推理能力、代码生成和多语言理解方面都有显著"</span>
              </div>
              <div class="flex items-start space-x-2">
                <span class="text-blue-600">目标:</span>
                <span class="flex-1 bg-white px-2 py-1 rounded font-bold">"提升"</span>
              </div>
              <div class="flex items-start space-x-2">
                <span class="text-blue-600">学习:</span>
                <span class="flex-1">新闻写作风格、技术术语、上下文理解</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mt-6 bg-gradient-to-r from-blue-100 to-cyan-100 p-5 rounded-xl">
        <p class="font-bold text-blue-900 mb-3">📌 预训练数据特点总结</p>
        <div class="grid md:grid-cols-2 gap-4">
          <div class="space-y-2">
            <p class="text-sm text-blue-800">✓ 来源多样（网页、书籍、代码...）</p>
            <p class="text-sm text-blue-800">✓ 海量规模（万亿tokens）</p>
            <p class="text-sm text-blue-800">✓ 无人工标注</p>
          </div>
          <div class="space-y-2">
            <p class="text-sm text-blue-800">✓ 任务统一（预测下一个词）</p>
            <p class="text-sm text-blue-800">✓ 自监督学习</p>
            <p class="text-sm text-blue-800">✓ 学习通用语言规律</p>
          </div>
        </div>
      </div>
    </div>

    <!-- SFT数据示例 -->
    <div class="card mb-8 bg-gradient-to-br from-purple-50 to-pink-50">
      <h3 class="text-2xl font-bold text-purple-800 mb-6 flex items-center">
        <span class="text-4xl mr-3">🎯</span>
        SFT数据示例
      </h3>
      
      <div class="space-y-6">
        <!-- 示例1 -->
        <div class="bg-white p-6 rounded-xl shadow-sm">
          <div class="flex items-center justify-between mb-3">
            <h4 class="font-bold text-lg text-gray-800">示例1：问答任务</h4>
            <span class="px-3 py-1 bg-purple-100 text-purple-700 rounded-full text-sm">指令-响应对</span>
          </div>
          <div class="space-y-3">
            <div class="bg-purple-50 p-4 rounded-lg">
              <p class="font-bold text-purple-800 mb-2">📝 Instruction</p>
              <p class="text-gray-700 bg-white p-3 rounded">回答用户关于人工智能的问题</p>
            </div>
            <div class="bg-blue-50 p-4 rounded-lg">
              <p class="font-bold text-blue-800 mb-2">📥 Input</p>
              <p class="text-gray-700 bg-white p-3 rounded">什么是人工智能？请用一句话解释。</p>
            </div>
            <div class="bg-green-50 p-4 rounded-lg">
              <p class="font-bold text-green-800 mb-2">✅ Response (标准答案)</p>
              <p class="text-gray-700 bg-white p-3 rounded">
                人工智能是让计算机系统模拟人类智能行为的技术，包括学习、推理、问题解决、感知和语言理解等能力。
              </p>
            </div>
          </div>
          <div class="bg-purple-100 p-4 rounded-lg mt-3">
            <p class="font-bold text-purple-900 mb-2">🎯 训练目标</p>
            <div class="text-sm space-y-1">
              <p>• 模型学习：给定instruction和input，生成response</p>
              <p>• 损失计算：最小化生成文本与标准答案的差异</p>
              <p>• 学会的能力：遵循指令、简洁回答、使用定义句式</p>
            </div>
          </div>
        </div>

        <!-- 示例2 -->
        <div class="bg-white p-6 rounded-xl shadow-sm">
          <div class="flex items-center justify-between mb-3">
            <h4 class="font-bold text-lg text-gray-800">示例2：文本摘要</h4>
            <span class="px-3 py-1 bg-purple-100 text-purple-700 rounded-full text-sm">专业任务</span>
          </div>
          <div class="space-y-3">
            <div class="bg-purple-50 p-4 rounded-lg">
              <p class="font-bold text-purple-800 mb-2">📝 Instruction</p>
              <p class="text-gray-700 bg-white p-3 rounded">将下面的新闻文章总结成三句话</p>
            </div>
            <div class="bg-blue-50 p-4 rounded-lg">
              <p class="font-bold text-blue-800 mb-2">📥 Input</p>
              <p class="text-gray-700 bg-white p-3 rounded text-sm">
                【科技新闻】OpenAI今日发布最新大语言模型GPT-4，相比前代版本，
                新模型在推理能力、代码生成和多语言理解方面都有显著提升。
                研究团队表示，GPT-4经过大规模预训练和精细的人类反馈对齐，
                能够更好地理解复杂指令并生成高质量回答...
              </p>
            </div>
            <div class="bg-green-50 p-4 rounded-lg">
              <p class="font-bold text-green-800 mb-2">✅ Response (期望输出)</p>
              <p class="text-gray-700 bg-white p-3 rounded text-sm">
                OpenAI发布了GPT-4大语言模型，在推理、代码和多语言能力上有显著提升。
                模型经过预训练和人类反馈对齐优化。
                能够更好地理解指令并生成高质量回答。
              </p>
            </div>
          </div>
          <div class="bg-purple-100 p-4 rounded-lg mt-3">
            <p class="font-bold text-purple-900 mb-2">🎯 训练目标</p>
            <div class="text-sm space-y-1">
              <p>• 学会提取关键信息</p>
              <p>• 遵守"三句话"的格式要求</p>
              <p>• 保持客观中立的新闻语气</p>
            </div>
          </div>
        </div>

        <!-- 示例3 -->
        <div class="bg-white p-6 rounded-xl shadow-sm">
          <div class="flex items-center justify-between mb-3">
            <h4 class="font-bold text-lg text-gray-800">示例3：风格控制</h4>
            <span class="px-3 py-1 bg-purple-100 text-purple-700 rounded-full text-sm">行为塑造</span>
          </div>
          <div class="space-y-3">
            <div class="bg-purple-50 p-4 rounded-lg">
              <p class="font-bold text-purple-800 mb-2">📝 Instruction</p>
              <p class="text-gray-700 bg-white p-3 rounded">你是一个友好且专业的客服助手，请回答用户的问题</p>
            </div>
            <div class="bg-blue-50 p-4 rounded-lg">
              <p class="font-bold text-blue-800 mb-2">📥 Input</p>
              <p class="text-gray-700 bg-white p-3 rounded">我的订单还没发货，怎么回事？</p>
            </div>
            <div class="bg-green-50 p-4 rounded-lg">
              <p class="font-bold text-green-800 mb-2">✅ Response (期望风格)</p>
              <p class="text-gray-700 bg-white p-3 rounded">
                您好！非常抱歉让您久等了。我查询到您的订单目前还在仓库准备中，
                预计今天下午发货。我们会第一时间为您更新物流信息，
                感谢您的耐心等待！如有其他问题，随时联系我。😊
              </p>
            </div>
          </div>
          <div class="bg-purple-100 p-4 rounded-lg mt-3">
            <p class="font-bold text-purple-900 mb-2">🎯 学习的行为模式</p>
            <div class="text-sm space-y-1">
              <p>• 礼貌用语（"您好"、"抱歉"、"感谢"）</p>
              <p>• 同理心表达（"让您久等了"）</p>
              <p>• 具体信息（"今天下午发货"）</p>
              <p>• 友好语气（emoji使用）</p>
            </div>
          </div>
        </div>

        <!-- 示例4：多轮对话（最能体现SFT与预训练的差异） -->
        <div class="bg-white p-6 rounded-xl shadow-sm border-4 border-purple-300">
          <div class="flex items-center justify-between mb-3">
            <h4 class="font-bold text-lg text-gray-800 flex items-center">
              <span class="text-2xl mr-2">🔥</span>
              示例4：多轮对话（核心差异体现）
            </h4>
            <span class="px-3 py-1 bg-red-100 text-red-700 rounded-full text-sm font-bold">Messages格式</span>
          </div>
          
          <div class="bg-gradient-to-r from-purple-100 to-pink-100 p-4 rounded-lg mb-4">
            <p class="font-bold text-purple-900 mb-2">💡 为什么多轮对话最能体现差异？</p>
            <p class="text-sm text-purple-800">
              预训练数据是<strong>连续的原始文本</strong>，而SFT数据必须使用<strong>messages格式+special tokens</strong>
              来清晰区分<strong>系统提示、用户输入、助手回答</strong>。这是SFT的核心特征！
            </p>
          </div>

          <div class="space-y-4">
            <!-- Messages格式展示 -->
            <div class="bg-gradient-to-br from-indigo-50 to-blue-50 p-4 rounded-lg">
              <p class="font-bold text-indigo-900 mb-3">📋 Messages格式数据结构</p>
              <div class="bg-gray-900 p-4 rounded-lg font-mono text-sm overflow-x-auto">
<pre class="text-green-400">{
  "messages": [
    {
      "role": "system",
      "content": "你是一个专业的Python编程助手，擅长解释代码和调试问题。"
    },
    {
      "role": "user", 
      "content": "这段代码为什么报错？\nfor i in range(10)\n    print(i)"
    },
    {
      "role": "assistant",
      "content": "这段代码缺少冒号！for循环语句末尾需要冒号。正确写法：\nfor i in range(10):\n    print(i)"
    },
    {
      "role": "user",
      "content": "谢谢！那range(10)会输出什么？"
    },
    {
      "role": "assistant",
      "content": "range(10)会生成0到9的整数序列（不包括10）。所以这段代码会依次打印：\n0\n1\n2\n...\n9"
    }
  ]
}</pre>
              </div>
            </div>

            <!-- 转换为训练格式（带special tokens） -->
            <div class="bg-gradient-to-br from-orange-50 to-amber-50 p-4 rounded-lg">
              <p class="font-bold text-orange-900 mb-3">🔧 转换为训练文本（ChatML格式 + Special Tokens）</p>
              <div class="bg-gray-900 p-4 rounded-lg font-mono text-xs overflow-x-auto">
<pre class="text-cyan-400"><span class="text-yellow-400">&lt;|im_start|&gt;</span>system
你是一个专业的Python编程助手，擅长解释代码和调试问题。<span class="text-yellow-400">&lt;|im_end|&gt;</span>
<span class="text-yellow-400">&lt;|im_start|&gt;</span>user
这段代码为什么报错？
for i in range(10)
    print(i)<span class="text-yellow-400">&lt;|im_end|&gt;</span>
<span class="text-yellow-400">&lt;|im_start|&gt;</span>assistant
这段代码缺少冒号！for循环语句末尾需要冒号。正确写法：
for i in range(10):
    print(i)<span class="text-yellow-400">&lt;|im_end|&gt;</span>
<span class="text-yellow-400">&lt;|im_start|&gt;</span>user
谢谢！那range(10)会输出什么？<span class="text-yellow-400">&lt;|im_end|&gt;</span>
<span class="text-yellow-400">&lt;|im_start|&gt;</span>assistant
range(10)会生成0到9的整数序列（不包括10）。所以这段代码会依次打印：
0
1
2
...
9<span class="text-yellow-400">&lt;|im_end|&gt;</span></pre>
              </div>
              <p class="text-xs text-orange-700 mt-2">
                <strong>特殊标记说明：</strong>
                <code class="bg-yellow-100 px-1 rounded">&lt;|im_start|&gt;</code> 和 
                <code class="bg-yellow-100 px-1 rounded">&lt;|im_end|&gt;</code> 
                是ChatML格式的special tokens，用于标记每条消息的开始和结束
              </p>
            </div>

            <!-- 损失计算的关键差异 -->
            <div class="bg-gradient-to-br from-rose-50 to-red-50 p-4 rounded-lg">
              <p class="font-bold text-red-900 mb-3">🎯 损失计算：只对assistant回答计算loss</p>
              <div class="space-y-2 text-sm">
                <div class="bg-white p-3 rounded border-l-4 border-green-500">
                  <p class="font-semibold text-green-800 mb-1">✅ 计算损失的部分：</p>
                  <p class="text-gray-700">• <code>assistant</code> 角色的所有内容（两次回答）</p>
                  <p class="text-xs text-gray-600 mt-1">模型学习如何像助手一样回答问题</p>
                </div>
                <div class="bg-white p-3 rounded border-l-4 border-red-500">
                  <p class="font-semibold text-red-800 mb-1">❌ 不计算损失的部分（label = -100）：</p>
                  <p class="text-gray-700">
                    • <code>system</code> 消息内容<br/>
                    • <code>user</code> 消息内容<br/>
                    • 所有 special tokens (<code>&lt;|im_start|&gt;</code>, <code>&lt;|im_end|&gt;</code>)
                  </p>
                  <p class="text-xs text-gray-600 mt-1">这些是输入上下文，不是模型要学习生成的内容</p>
                </div>
              </div>
            </div>

            <!-- 其他格式对比 -->
            <div class="bg-gradient-to-br from-slate-50 to-gray-50 p-4 rounded-lg">
              <p class="font-bold text-gray-900 mb-3">📚 不同模型的Special Tokens格式</p>
              <div class="space-y-3 text-xs">
                <div class="bg-white p-3 rounded">
                  <p class="font-semibold text-blue-800 mb-1">ChatML (OpenAI):</p>
                  <code class="text-gray-700">&lt;|im_start|&gt;user\n内容&lt;|im_end|&gt;</code>
                </div>
                <div class="bg-white p-3 rounded">
                  <p class="font-semibold text-blue-800 mb-1">Llama-2 格式:</p>
                  <code class="text-gray-700">&lt;s&gt;[INST] 用户输入 [/INST] 助手回答 &lt;/s&gt;</code>
                </div>
                <div class="bg-white p-3 rounded">
                  <p class="font-semibold text-blue-800 mb-1">Alpaca 格式:</p>
                  <code class="text-gray-700">### Instruction:\n...\n### Response:\n...</code>
                </div>
              </div>
              <p class="text-xs text-gray-600 mt-2 bg-yellow-100 p-2 rounded">
                ⚠️ <strong>格式必须与模型预训练时一致！</strong>用错格式会导致SFT失败！
              </p>
            </div>
          </div>

          <div class="bg-gradient-to-r from-purple-100 to-pink-100 p-4 rounded-lg mt-4">
            <p class="font-bold text-purple-900 mb-2">🔑 多轮对话SFT的核心要点</p>
            <div class="grid md:grid-cols-2 gap-3 text-sm">
              <div>
                <p class="font-semibold text-purple-800">✓ Messages结构化格式</p>
                <p class="text-purple-700">清晰区分system/user/assistant</p>
              </div>
              <div>
                <p class="font-semibold text-purple-800">✓ Special Tokens</p>
                <p class="text-purple-700">标记消息边界和角色</p>
              </div>
              <div>
                <p class="font-semibold text-purple-800">✓ 上下文记忆</p>
                <p class="text-purple-700">模型学会基于历史对话回答</p>
              </div>
              <div>
                <p class="font-semibold text-purple-800">✓ 选择性损失计算</p>
                <p class="text-purple-700">只对assistant内容计算loss</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mt-6 bg-gradient-to-r from-purple-100 to-pink-100 p-5 rounded-xl">
        <p class="font-bold text-purple-900 mb-3">📌 SFT数据特点总结</p>
        <div class="grid md:grid-cols-2 gap-4">
          <div class="space-y-2">
            <p class="text-sm text-purple-800">✓ 结构化（instruction-input-response）</p>
            <p class="text-sm text-purple-800">✓ 小规模但高质量（数千到数万样本）</p>
            <p class="text-sm text-purple-800">✓ 人工精心标注</p>
          </div>
          <div class="space-y-2">
            <p class="text-sm text-purple-800">✓ 任务多样（问答、摘要、对话...）</p>
            <p class="text-sm text-purple-800">✓ 监督学习</p>
            <p class="text-sm text-purple-800">✓ 塑造行为和风格</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 多轮对话数据对比 - 最能体现差异 -->
    <div class="card bg-gradient-to-br from-rose-50 to-pink-50 mb-8 border-4 border-rose-400">
      <h3 class="text-2xl font-bold text-rose-800 mb-6 flex items-center">
        <span class="text-4xl mr-3">🔥</span>
        核心对比：多轮对话在两种训练中的巨大差异
      </h3>

      <div class="bg-gradient-to-r from-rose-100 to-pink-100 p-4 rounded-lg mb-6">
        <p class="font-bold text-rose-900 mb-2">💡 为什么用多轮对话做对比？</p>
        <p class="text-sm text-rose-800">
          多轮对话是<strong>最能体现预训练和SFT数据本质差异</strong>的场景！
          预训练只看到"文本流"，而SFT必须理解"谁在说话、说了什么、该如何回应"。
        </p>
      </div>

      <div class="bg-white p-6 rounded-xl">
        <p class="font-bold text-xl mb-4 text-rose-900">📍 示例：编程问答对话</p>
        
        <div class="grid md:grid-cols-2 gap-6">
          <!-- 预训练：原始文本 -->
          <div class="bg-blue-50 p-5 rounded-lg">
            <h4 class="font-bold text-blue-800 mb-3 flex items-center">
              <span class="text-2xl mr-2">📚</span>
              预训练数据格式
            </h4>
            <div class="bg-white p-4 rounded border-2 border-blue-300">
              <p class="text-xs text-blue-600 mb-2 font-semibold">纯文本，无结构标记：</p>
              <div class="text-sm text-gray-800 leading-relaxed font-mono bg-gray-50 p-3 rounded">
这段代码为什么报错？for i in range(10) print(i) 这段代码缺少冒号！for循环语句末尾需要冒号。正确写法：for i in range(10): print(i) 谢谢！那range(10)会输出什么？range(10)会生成0到9的整数序列（不包括10）。
              </div>
            </div>
            <div class="mt-3 space-y-2 text-sm">
              <div class="bg-blue-100 p-3 rounded">
                <p class="font-semibold text-blue-900">训练任务：</p>
                <p class="text-blue-800">每个词预测下一个词</p>
              </div>
              <div class="bg-blue-100 p-3 rounded">
                <p class="font-semibold text-blue-900">损失计算：</p>
                <p class="text-blue-800">所有token都计算损失</p>
              </div>
              <div class="bg-red-100 p-3 rounded border-l-4 border-red-500">
                <p class="font-semibold text-red-900">❌ 严重问题：</p>
                <p class="text-red-800 text-xs space-y-1">
                  <span class="block">• 无法区分用户问题和助手回答</span>
                  <span class="block">• 无法区分对话轮次</span>
                  <span class="block">• 模型不知道该扮演什么角色</span>
                  <span class="block">• 可能学会像用户一样"提问"而非"回答"</span>
                </p>
              </div>
            </div>
          </div>

          <!-- SFT：结构化对话 -->
          <div class="bg-purple-50 p-5 rounded-lg">
            <h4 class="font-bold text-purple-800 mb-3 flex items-center">
              <span class="text-2xl mr-2">🎯</span>
              SFT数据格式
            </h4>
            <div class="bg-gray-900 p-4 rounded border-2 border-purple-300">
              <p class="text-xs text-purple-300 mb-2 font-semibold">结构化，带special tokens：</p>
              <div class="text-xs font-mono leading-relaxed">
<pre class="text-cyan-400"><span class="text-yellow-400">&lt;|im_start|&gt;</span><span class="text-green-400">user</span>
这段代码为什么报错？
for i in range(10)
    print(i)<span class="text-yellow-400">&lt;|im_end|&gt;</span>
<span class="text-yellow-400">&lt;|im_start|&gt;</span><span class="text-pink-400">assistant</span>
这段代码缺少冒号！<span class="text-yellow-400">&lt;|im_end|&gt;</span>
<span class="text-yellow-400">&lt;|im_start|&gt;</span><span class="text-green-400">user</span>
谢谢！range(10)输出什么？<span class="text-yellow-400">&lt;|im_end|&gt;</span>
<span class="text-yellow-400">&lt;|im_start|&gt;</span><span class="text-pink-400">assistant</span>
0到9的整数序列<span class="text-yellow-400">&lt;|im_end|&gt;</span></pre>
              </div>
            </div>
            <div class="mt-3 space-y-2 text-sm">
              <div class="bg-purple-100 p-3 rounded">
                <p class="font-semibold text-purple-900">训练任务：</p>
                <p class="text-purple-800">生成assistant角色的回答</p>
              </div>
              <div class="bg-purple-100 p-3 rounded">
                <p class="font-semibold text-purple-900">损失计算：</p>
                <p class="text-purple-800">只对assistant内容计算损失，user和special tokens的label设为-100</p>
              </div>
              <div class="bg-green-100 p-3 rounded border-l-4 border-green-500">
                <p class="font-semibold text-green-900">✅ 关键优势：</p>
                <p class="text-green-800 text-xs space-y-1">
                  <span class="block">• 明确区分用户和助手角色</span>
                  <span class="block">• 清晰的对话轮次和边界</span>
                  <span class="block">• 模型专注学习"助手"的回答</span>
                  <span class="block">• 可以包含system提示词塑造行为</span>
                </p>
              </div>
            </div>
          </div>
        </div>

        <div class="mt-6 bg-gradient-to-r from-rose-100 to-pink-100 p-5 rounded-lg border-l-4 border-rose-600">
          <p class="font-bold text-rose-900 mb-3 text-lg">🎯 这就是核心差异！</p>
          <div class="space-y-2 text-sm">
            <p class="text-rose-800">
              <strong>预训练：</strong>把对话当作普通文本流，学习"这个词后面可能跟什么词"。
              模型可能学会问问题（因为训练数据里有问题），但不知道自己该扮演什么角色。
            </p>
            <p class="text-rose-800">
              <strong>SFT：</strong>通过messages格式和special tokens，让模型明确学习
              "作为assistant角色，面对user的问题，应该如何回答"。
              这就是为什么SFT后的模型会"听话"、会"按角色行事"！
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- 同一个输入的对比 -->
    <div class="card bg-gradient-to-br from-amber-50 to-orange-50">
      <h3 class="text-2xl font-bold text-amber-800 mb-6 flex items-center">
        <span class="text-4xl mr-3">🔬</span>
        简单示例：单句文本在两种训练中的差异
      </h3>

      <div class="bg-white p-6 rounded-xl">
        <p class="font-bold text-lg mb-4">输入文本："人工智能正在改变世界"</p>
        
        <div class="grid md:grid-cols-2 gap-6">
          <!-- 预训练处理 -->
          <div class="bg-blue-50 p-5 rounded-lg">
            <h4 class="font-bold text-blue-800 mb-3">📚 预训练中的处理</h4>
            <div class="space-y-3 text-sm">
              <div>
                <p class="font-semibold text-gray-800">分词结果：</p>
                <div class="bg-white p-2 rounded mt-1 font-mono">
                  ["人工", "智能", "正在", "改变", "世界"]
                </div>
              </div>
              <div>
                <p class="font-semibold text-gray-800">训练样本（每个位置）：</p>
                <div class="bg-white p-2 rounded mt-1 space-y-1 text-xs">
                  <p>输入: [] → 预测: "人工"</p>
                  <p>输入: ["人工"] → 预测: "智能"</p>
                  <p>输入: ["人工", "智能"] → 预测: "正在"</p>
                  <p>输入: ["人工", "智能", "正在"] → 预测: "改变"</p>
                  <p>输入: ["人工", "智能", "正在", "改变"] → 预测: "世界"</p>
                </div>
              </div>
              <div>
                <p class="font-semibold text-gray-800">损失计算：</p>
                <div class="bg-white p-2 rounded mt-1">
                  CrossEntropyLoss(预测分布, 真实token)
                </div>
              </div>
            </div>
          </div>

          <!-- SFT处理 -->
          <div class="bg-purple-50 p-5 rounded-lg">
            <h4 class="font-bold text-purple-800 mb-3">🎯 SFT中的处理</h4>
            <div class="space-y-3 text-sm">
              <div>
                <p class="font-semibold text-gray-800">完整样本结构：</p>
                <div class="bg-white p-2 rounded mt-1 font-mono text-xs">
                  {
                    "instruction": "用一句话总结AI的影响",
                    "input": "",
                    "response": "人工智能正在改变世界"
                  }
                </div>
              </div>
              <div>
                <p class="font-semibold text-gray-800">训练目标：</p>
                <div class="bg-white p-2 rounded mt-1">
                  给定instruction，生成完整的response
                </div>
              </div>
              <div>
                <p class="font-semibold text-gray-800">损失计算：</p>
                <div class="bg-white p-2 rounded mt-1 text-xs">
                  只对response部分计算损失<br/>
                  CrossEntropyLoss(生成的response, 标准response)
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="mt-6 bg-amber-100 p-4 rounded-lg">
          <p class="font-bold text-amber-900 mb-2">🔍 关键差异</p>
          <div class="grid md:grid-cols-2 gap-4 text-sm">
            <div>
              <p class="font-semibold text-amber-800">预训练：</p>
              <ul class="list-disc list-inside text-gray-700 space-y-1">
                <li>学习语言的统计规律</li>
                <li>每个词都是训练目标</li>
                <li>纯文本，无任务概念</li>
              </ul>
            </div>
            <div>
              <p class="font-semibold text-amber-800">SFT：</p>
              <ul class="list-disc list-inside text-gray-700 space-y-1">
                <li>学习如何完成任务</li>
                <li>只对response计算损失</li>
                <li>有明确的指令和期望</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// 组件无需额外脚本
</script>

