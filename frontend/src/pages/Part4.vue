<template>
  <div class="part4-page">
    <!-- 标题 -->
    <h1 class="section-title">第四部分：SFT实践工作流</h1>

    <!-- 引言 -->
    <AnalogyBox icon="🌱" title="核心类比：园艺而非编译">
      <p class="text-lg">
        SFT的优化循环本质上是<strong>以数据为中心的</strong>。这个过程与其说是编译代码，不如说更像<strong>园艺</strong>。
      </p>
      <p class="text-lg mt-3">
        你不能只是播下种子（开始训练）就置之不理。你需要持续地照料土壤（数据集），
        修剪坏死的枝条（移除坏数据），并根据植物的生长情况（模型评估）针对性地施肥（添加新的高质量样本）。
      </p>
      <p class="text-lg mt-3 font-bold text-orange-700">
        焦点始终在培育数据，而模型的卓越性能，则是这种精心培育的自然结果。
      </p>
    </AnalogyBox>

    <!-- 工作流程概览 -->
    <section class="my-12">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">SFT工作流程四步法</h2>
      
      <ProgressSteps :steps="workflowSteps" :currentStep="currentStep" />

      <div class="flex justify-center space-x-4 mt-6">
        <button 
          @click="currentStep = Math.max(0, currentStep - 1)"
          :disabled="currentStep === 0"
          class="px-6 py-2 bg-gray-300 rounded-lg disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-400 transition-colors"
        >
          ← 上一步
        </button>
        <button 
          @click="currentStep = Math.min(workflowSteps.length - 1, currentStep + 1)"
          :disabled="currentStep === workflowSteps.length - 1"
          class="px-6 py-2 bg-gradient-to-r from-blue-500 to-purple-500 text-white rounded-lg disabled:opacity-50 disabled:cursor-not-allowed hover:shadow-lg transition-all"
        >
          下一步 →
        </button>
      </div>
    </section>

    <!-- 步骤详解 -->
    <section class="my-12">
      <transition name="fade" mode="out-in">
        <div :key="currentStep">
          <!-- 步骤1：定义任务并选择基座模型 -->
          <div v-if="currentStep === 0" class="space-y-6">
            <h2 class="text-3xl font-bold text-gray-800 mb-6 flex items-center">
              <span class="bg-blue-500 text-white rounded-full w-12 h-12 flex items-center justify-center mr-4">1</span>
              定义任务并选择基座模型
            </h2>

            <InfoCard icon="🎯" title="从目标出发" variant="info">
              <p class="mb-3">首先，必须清晰地定义你希望模型完成什么任务：</p>
              <ul class="list-disc list-inside space-y-1">
                <li>摘要生成器？</li>
                <li>代码助手？</li>
                <li>特定领域的问答机器人？</li>
                <li>客户服务对话系统？</li>
              </ul>
              <p class="mt-3 font-semibold text-blue-700">明确的目标是后续所有工作的基础！</p>
            </InfoCard>

            <div class="card bg-gradient-to-br from-purple-50 to-pink-50">
              <h3 class="text-2xl font-bold text-purple-800 mb-4">选择基座模型的关键因素</h3>
              <div class="grid md:grid-cols-2 gap-4">
                <div class="bg-white p-4 rounded-lg">
                  <p class="font-bold text-gray-800 mb-2">📏 模型大小</p>
                  <p class="text-sm text-gray-600">7B vs 13B vs 70B - 根据任务复杂度和资源限制选择</p>
                </div>
                <div class="bg-white p-4 rounded-lg">
                  <p class="font-bold text-gray-800 mb-2">📊 基准测试表现</p>
                  <p class="text-sm text-gray-600">查看模型在相关任务上的评测分数</p>
                </div>
                <div class="bg-white p-4 rounded-lg">
                  <p class="font-bold text-gray-800 mb-2">💻 计算资源</p>
                  <p class="text-sm text-gray-600">你有多少GPU？显存多大？</p>
                </div>
                <div class="bg-white p-4 rounded-lg">
                  <p class="font-bold text-gray-800 mb-2">📜 开源协议</p>
                  <p class="text-sm text-gray-600">确保许可证允许商业使用（如需要）</p>
                </div>
              </div>
            </div>

            <AnalogyBox icon="🏗️" title="类比：选择地基">
              <p>
                就像建房子要选择合适的地基一样，选择基座模型是SFT项目的第一步。
                一个强大稳固的地基（优质基座模型）能支撑更宏伟的建筑（专业化能力），
                而一个薄弱的地基无论如何装修都无法补救。
              </p>
            </AnalogyBox>

            <div class="card">
              <h3 class="text-xl font-bold text-gray-800 mb-4">热门开源基座模型</h3>
              <div class="space-y-3">
                <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                  <div>
                    <p class="font-bold">LLaMA 2 / LLaMA 3</p>
                    <p class="text-sm text-gray-600">Meta开源，性能优异</p>
                  </div>
                  <span class="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm">推荐</span>
                </div>
                <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                  <div>
                    <p class="font-bold">Mistral 7B</p>
                    <p class="text-sm text-gray-600">小而强大，性价比高</p>
                  </div>
                  <span class="px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm">高效</span>
                </div>
                <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                  <div>
                    <p class="font-bold">Qwen / Baichuan</p>
                    <p class="text-sm text-gray-600">中文友好，国内可用</p>
                  </div>
                  <span class="px-3 py-1 bg-purple-100 text-purple-700 rounded-full text-sm">中文</span>
                </div>
              </div>
            </div>
          </div>

          <!-- 步骤2：策划和准备数据集 -->
          <div v-if="currentStep === 1" class="space-y-6">
            <h2 class="text-3xl font-bold text-gray-800 mb-6 flex items-center">
              <span class="bg-purple-500 text-white rounded-full w-12 h-12 flex items-center justify-center mr-4">2</span>
              策划和准备数据集
            </h2>

            <div class="card bg-gradient-to-br from-red-50 to-orange-50 border-l-4 border-orange-500">
              <div class="flex items-start space-x-4">
                <div class="text-5xl">⚠️</div>
                <div class="flex-1">
                  <h3 class="text-2xl font-bold text-orange-800 mb-3">最关键的一步！</h3>
                  <p class="text-lg text-gray-700">
                    这是整个SFT项目中<strong>投入精力最多</strong>、也<strong>最能决定成败</strong>的环节。
                    绝大多数显著的性能提升，都来自于对数据集的质量和构成的迭代和改进。
                  </p>
                </div>
              </div>
            </div>

            <div class="grid md:grid-cols-3 gap-6">
              <InfoCard icon="📦" title="收集或创建" variant="info">
                <ul class="list-disc list-inside space-y-1 text-sm">
                  <li>选择开源数据集</li>
                  <li>创建自定义样本</li>
                  <li>LLM辅助生成</li>
                  <li>从业务数据提取</li>
                </ul>
              </InfoCard>

              <InfoCard icon="🧹" title="格式化与清洗" variant="warning">
                <ul class="list-disc list-inside space-y-1 text-sm">
                  <li>统一格式（JSONL）</li>
                  <li>去除错误数据</li>
                  <li>消除偏见内容</li>
                  <li>检查一致性</li>
                </ul>
              </InfoCard>

              <InfoCard icon="✂️" title="数据集划分" variant="success">
                <ul class="list-disc list-inside space-y-1 text-sm">
                  <li>训练集（80-90%）</li>
                  <li>验证集（10-20%）</li>
                  <li>测试集（可选）</li>
                  <li>确保无重复</li>
                </ul>
              </InfoCard>
            </div>

            <div class="card">
              <h3 class="text-2xl font-bold text-gray-800 mb-4">数据准备流程</h3>
              <div class="space-y-4">
                <div class="flex items-start space-x-4">
                  <div class="bg-purple-500 text-white rounded-full w-8 h-8 flex items-center justify-center flex-shrink-0 font-bold">1</div>
                  <div class="flex-1">
                    <p class="font-semibold">收集原始数据</p>
                    <p class="text-sm text-gray-600">从各种来源收集初始数据</p>
                  </div>
                </div>
                <div class="flex items-start space-x-4">
                  <div class="bg-purple-500 text-white rounded-full w-8 h-8 flex items-center justify-center flex-shrink-0 font-bold">2</div>
                  <div class="flex-1">
                    <p class="font-semibold">数据清洗与去重</p>
                    <p class="text-sm text-gray-600">移除低质量、重复、有害的数据</p>
                  </div>
                </div>
                <div class="flex items-start space-x-4">
                  <div class="bg-purple-500 text-white rounded-full w-8 h-8 flex items-center justify-center flex-shrink-0 font-bold">3</div>
                  <div class="flex-1">
                    <p class="font-semibold">格式统一化</p>
                    <p class="text-sm text-gray-600">转换为标准的指令-响应格式</p>
                  </div>
                </div>
                <div class="flex items-start space-x-4">
                  <div class="bg-purple-500 text-white rounded-full w-8 h-8 flex items-center justify-center flex-shrink-0 font-bold">4</div>
                  <div class="flex-1">
                    <p class="font-semibold">质量审核</p>
                    <p class="text-sm text-gray-600">人工或自动检查样本质量</p>
                  </div>
                </div>
                <div class="flex items-start space-x-4">
                  <div class="bg-purple-500 text-white rounded-full w-8 h-8 flex items-center justify-center flex-shrink-0 font-bold">5</div>
                  <div class="flex-1">
                    <p class="font-semibold">数据集划分</p>
                    <p class="text-sm text-gray-600">分为训练集和验证集</p>
                  </div>
                </div>
              </div>
            </div>

            <CodeBlock 
              title="示例：JSONL格式的SFT数据"
              :code="jsonlExample"
            />
          </div>

          <!-- 步骤3：配置并运行训练 -->
          <div v-if="currentStep === 2" class="space-y-6">
            <h2 class="text-3xl font-bold text-gray-800 mb-6 flex items-center">
              <span class="bg-green-500 text-white rounded-full w-12 h-12 flex items-center justify-center mr-4">3</span>
              配置并运行训练
            </h2>

            <InfoCard icon="🛠️" title="搭建训练环境" variant="info">
              <p class="mb-2">选择合适的训练框架可以大大简化SFT流程：</p>
              <ul class="list-disc list-inside space-y-1">
                <li><strong>Hugging Face TRL</strong> - 提供专门的SFTTrainer</li>
                <li><strong>Axolotl</strong> - 配置驱动的训练工具</li>
                <li><strong>LLaMA-Factory</strong> - 一站式训练平台</li>
              </ul>
            </InfoCard>

            <div class="card bg-gradient-to-br from-blue-50 to-cyan-50">
              <h3 class="text-2xl font-bold text-blue-800 mb-4">关键超参数配置</h3>
              <div class="grid md:grid-cols-2 gap-4">
                <div class="bg-white p-4 rounded-lg">
                  <p class="font-bold text-gray-800 mb-2">📈 学习率 (Learning Rate)</p>
                  <p class="text-sm text-gray-600 mb-2">控制模型更新的步幅</p>
                  <p class="text-xs bg-blue-100 text-blue-700 p-2 rounded">推荐: 1e-5 到 5e-5</p>
                </div>
                <div class="bg-white p-4 rounded-lg">
                  <p class="font-bold text-gray-800 mb-2">🔄 训练轮数 (Epochs)</p>
                  <p class="text-sm text-gray-600 mb-2">数据集完整遍历次数</p>
                  <p class="text-xs bg-blue-100 text-blue-700 p-2 rounded">推荐: 3-5轮</p>
                </div>
                <div class="bg-white p-4 rounded-lg">
                  <p class="font-bold text-gray-800 mb-2">📦 批次大小 (Batch Size)</p>
                  <p class="text-sm text-gray-600 mb-2">每次更新使用的样本数</p>
                  <p class="text-xs bg-blue-100 text-blue-700 p-2 rounded">根据GPU显存调整</p>
                </div>
                <div class="bg-white p-4 rounded-lg">
                  <p class="font-bold text-gray-800 mb-2">🎯 LoRA秩 (LoRA Rank)</p>
                  <p class="text-sm text-gray-600 mb-2">LoRA矩阵的维度</p>
                  <p class="text-xs bg-blue-100 text-blue-700 p-2 rounded">推荐: r=8, 16, 或32</p>
                </div>
              </div>
            </div>

            <CodeBlock 
              title="示例：使用TRL进行SFT训练"
              :code="trainingCode"
            />

            <div class="card">
              <h3 class="text-2xl font-bold text-gray-800 mb-4">训练过程监控</h3>
              <InteractiveChart
                :data="trainingLossData"
                type="line"
                description="训练损失应该稳定下降，如果出现异常波动需要调整超参数"
              />
            </div>

            <AnalogyBox icon="🍳" title="类比：烹饪调节火候">
              <p>
                配置超参数就像烹饪时调节火候。学习率太高就像火太大，可能把菜炒糊（训练不稳定）；
                太低就像火太小，菜永远也炒不熟（训练太慢）。需要根据实际情况不断调整，找到最佳平衡点。
              </p>
            </AnalogyBox>
          </div>

          <!-- 步骤4：评估、测试和迭代 -->
          <div v-if="currentStep === 3" class="space-y-6">
            <h2 class="text-3xl font-bold text-gray-800 mb-6 flex items-center">
              <span class="bg-orange-500 text-white rounded-full w-12 h-12 flex items-center justify-center mr-4">4</span>
              评估、测试和迭代
            </h2>

            <div class="card bg-gradient-to-br from-green-50 to-emerald-50 border-l-4 border-green-500">
              <div class="flex items-start space-x-4">
                <div class="text-5xl">🔄</div>
                <div class="flex-1">
                  <h3 class="text-2xl font-bold text-green-800 mb-3">迭代是关键！</h3>
                  <p class="text-lg text-gray-700">
                    SFT不是一次性的过程，而是一个<strong>持续迭代优化</strong>的循环。
                    评估发现问题 → 改进数据 → 重新训练 → 再次评估。
                  </p>
                </div>
              </div>
            </div>

            <div class="grid md:grid-cols-2 gap-6">
              <InfoCard icon="📊" title="定量评估" variant="info">
                <p class="mb-2 font-semibold">使用验证集监控性能：</p>
                <ul class="list-disc list-inside space-y-1 text-sm">
                  <li>验证损失 (Validation Loss)</li>
                  <li>困惑度 (Perplexity)</li>
                  <li>任务特定指标（准确率、F1等）</li>
                  <li>及时发现过拟合</li>
                </ul>
              </InfoCard>

              <InfoCard icon="🗣️" title="定性测试" variant="success">
                <p class="mb-2 font-semibold">亲自与模型交互：</p>
                <ul class="list-disc list-inside space-y-1 text-sm">
                  <li>提问各种问题</li>
                  <li>测试边缘情况</li>
                  <li>检查输出质量</li>
                  <li>发现薄弱环节</li>
                </ul>
              </InfoCard>
            </div>

            <div class="card">
              <h3 class="text-2xl font-bold text-gray-800 mb-4">迭代优化循环</h3>
              <AnimatedIllustration description="以数据为中心的持续改进">
                <div class="w-full max-w-3xl">
                  <svg viewBox="0 0 400 400" class="w-full h-auto">
                    <!-- 循环箭头 -->
                    <defs>
                      <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                        <polygon points="0 0, 10 3.5, 0 7" fill="#6366f1" />
                      </marker>
                    </defs>
                    
                    <!-- 圆形路径 -->
                    <circle cx="200" cy="200" r="120" fill="none" stroke="#e5e7eb" stroke-width="2" />
                    
                    <!-- 箭头路径 -->
                    <path d="M 200 80 A 120 120 0 0 1 320 200" fill="none" stroke="#6366f1" stroke-width="3" marker-end="url(#arrowhead)" />
                    <path d="M 320 200 A 120 120 0 0 1 200 320" fill="none" stroke="#6366f1" stroke-width="3" marker-end="url(#arrowhead)" />
                    <path d="M 200 320 A 120 120 0 0 1 80 200" fill="none" stroke="#6366f1" stroke-width="3" marker-end="url(#arrowhead)" />
                    <path d="M 80 200 A 120 120 0 0 1 200 80" fill="none" stroke="#6366f1" stroke-width="3" marker-end="url(#arrowhead)" />
                    
                    <!-- 四个步骤 -->
                    <g>
                      <circle cx="200" cy="60" r="35" fill="#3b82f6" />
                      <text x="200" y="55" text-anchor="middle" fill="white" font-size="24">📊</text>
                      <text x="200" y="30" text-anchor="middle" fill="#1f2937" font-size="14" font-weight="bold">评估</text>
                    </g>
                    
                    <g>
                      <circle cx="340" cy="200" r="35" fill="#8b5cf6" />
                      <text x="340" y="195" text-anchor="middle" fill="white" font-size="24">🔍</text>
                      <text x="340" y="230" text-anchor="middle" fill="#1f2937" font-size="14" font-weight="bold">发现问题</text>
                    </g>
                    
                    <g>
                      <circle cx="200" cy="340" r="35" fill="#10b981" />
                      <text x="200" y="335" text-anchor="middle" fill="white" font-size="24">📝</text>
                      <text x="200" y="370" text-anchor="middle" fill="#1f2937" font-size="14" font-weight="bold">改进数据</text>
                    </g>
                    
                    <g>
                      <circle cx="60" cy="200" r="35" fill="#f59e0b" />
                      <text x="60" y="195" text-anchor="middle" fill="white" font-size="24">🔄</text>
                      <text x="60" y="170" text-anchor="middle" fill="#1f2937" font-size="14" font-weight="bold">重新训练</text>
                    </g>
                    
                    <!-- 中心文字 -->
                    <text x="200" y="200" text-anchor="middle" fill="#6366f1" font-size="18" font-weight="bold">持续迭代</text>
                  </svg>
                </div>
              </AnimatedIllustration>
            </div>

            <div class="card bg-gradient-to-br from-amber-50 to-orange-50">
              <h3 class="text-2xl font-bold text-amber-800 mb-4">常见问题与解决方案</h3>
              <div class="space-y-4">
                <div class="bg-white p-4 rounded-lg">
                  <p class="font-bold text-gray-800 mb-2">❓ 模型在某类问题上表现差</p>
                  <p class="text-sm text-gray-600"><strong>解决:</strong> 在数据集中添加更多这类问题的高质量样本</p>
                </div>
                <div class="bg-white p-4 rounded-lg">
                  <p class="font-bold text-gray-800 mb-2">❓ 模型输出格式不统一</p>
                  <p class="text-sm text-gray-600"><strong>解决:</strong> 确保训练数据中的响应格式高度一致</p>
                </div>
                <div class="bg-white p-4 rounded-lg">
                  <p class="font-bold text-gray-800 mb-2">❓ 模型过度拟合训练数据</p>
                  <p class="text-sm text-gray-600"><strong>解决:</strong> 增加数据多样性，减少训练轮数，或使用更大的基座模型</p>
                </div>
                <div class="bg-white p-4 rounded-lg">
                  <p class="font-bold text-gray-800 mb-2">❓ 模型"忘记"了通用能力</p>
                  <p class="text-sm text-gray-600"><strong>解决:</strong> 使用LoRA而非全量微调，或在数据中混入通用任务样本</p>
                </div>
              </div>
            </div>

            <AnalogyBox icon="🌱" title="回归园艺类比">
              <p>
                就像园艺一样，你需要观察植物的生长情况（模型评估），发现哪里长得不好（性能问题），
                然后调整养护策略（改进数据集），再继续培育（重新训练）。这是一个需要耐心和持续关注的过程，
                但最终会结出丰硕的果实（卓越的模型性能）。
              </p>
            </AnalogyBox>
          </div>
        </div>
      </transition>
    </section>

    <!-- 最佳实践总结 -->
    <section class="my-12">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">SFT最佳实践清单</h2>
      
      <div class="grid md:grid-cols-2 gap-6">
        <div class="card bg-gradient-to-br from-green-50 to-emerald-50">
          <h3 class="text-xl font-bold text-green-800 mb-4">✅ 应该做的</h3>
          <ul class="space-y-2">
            <li class="flex items-start space-x-2">
              <span class="text-green-600 mt-1">✓</span>
              <span>选择强大的基座模型作为起点</span>
            </li>
            <li class="flex items-start space-x-2">
              <span class="text-green-600 mt-1">✓</span>
              <span>专注于数据质量而非数量</span>
            </li>
            <li class="flex items-start space-x-2">
              <span class="text-green-600 mt-1">✓</span>
              <span>使用LoRA等PEFT技术降低成本</span>
            </li>
            <li class="flex items-start space-x-2">
              <span class="text-green-600 mt-1">✓</span>
              <span>持续迭代数据集</span>
            </li>
            <li class="flex items-start space-x-2">
              <span class="text-green-600 mt-1">✓</span>
              <span>亲自测试模型输出</span>
            </li>
            <li class="flex items-start space-x-2">
              <span class="text-green-600 mt-1">✓</span>
              <span>保持数据格式和风格一致</span>
            </li>
          </ul>
        </div>

        <div class="card bg-gradient-to-br from-red-50 to-pink-50">
          <h3 class="text-xl font-bold text-red-800 mb-4">❌ 不应该做的</h3>
          <ul class="space-y-2">
            <li class="flex items-start space-x-2">
              <span class="text-red-600 mt-1">✗</span>
              <span>期望SFT能补救糟糕的基座模型</span>
            </li>
            <li class="flex items-start space-x-2">
              <span class="text-red-600 mt-1">✗</span>
              <span>使用大量低质量数据</span>
            </li>
            <li class="flex items-start space-x-2">
              <span class="text-red-600 mt-1">✗</span>
              <span>过度调整超参数而忽视数据</span>
            </li>
            <li class="flex items-start space-x-2">
              <span class="text-red-600 mt-1">✗</span>
              <span>训练一次就停止</span>
            </li>
            <li class="flex items-start space-x-2">
              <span class="text-red-600 mt-1">✗</span>
              <span>只依赖自动化评估指标</span>
            </li>
            <li class="flex items-start space-x-2">
              <span class="text-red-600 mt-1">✗</span>
              <span>在不理解的情况下复制别人的配置</span>
            </li>
          </ul>
        </div>
      </div>
    </section>

    <!-- 测验 -->
    <QuizBox
      question="在SFT工作流中，哪个环节最值得投入精力？"
      :options="[
        '选择最大的基座模型',
        '数据集的质量和迭代优化',
        '调整各种超参数配置',
        '使用最新的训练框架'
      ]"
      :correctAnswer="1"
      explanation="数据集的质量和迭代优化是SFT工作流中最关键的环节。绝大多数显著的性能提升都来自于数据集的改进。选择好的基座模型很重要，但数据质量才是决定微调效果的核心因素。超参数调整和工具选择相对次要。"
    />

    <!-- 两个完整的实践项目 -->
    <section class="my-16">
      <h2 class="text-4xl font-bold text-center text-gray-800 mb-8">🚀 完整实践项目</h2>
      
      <div class="card bg-gradient-to-br from-yellow-50 to-amber-50 border-l-4 border-yellow-500 mb-8">
        <div class="flex items-start space-x-4">
          <div class="text-5xl">💡</div>
          <div class="flex-1">
            <h3 class="text-2xl font-bold text-yellow-800 mb-3">理论到实践</h3>
            <p class="text-lg text-gray-700">
              前面我们学习了SFT的理论知识，现在让我们通过两个<strong>完整的、可运行的项目</strong>来实践！
              每个项目都包含真实的长数据、完整的训练代码、以及详细的说明文档。
            </p>
          </div>
        </div>
      </div>

      <!-- 项目对比表 -->
      <div class="card mb-8">
        <h3 class="text-2xl font-bold text-gray-800 mb-4">两个项目的对比</h3>
        <div class="overflow-x-auto">
          <table class="w-full text-sm">
            <thead class="bg-gray-100">
              <tr>
                <th class="p-3 text-left">维度</th>
                <th class="p-3 text-left">4.1 垂直领域（中医）</th>
                <th class="p-3 text-left">4.2 通用助手</th>
              </tr>
            </thead>
            <tbody>
              <tr class="border-t">
                <td class="p-3 font-semibold">应用场景</td>
                <td class="p-3">专业领域咨询</td>
                <td class="p-3">通用对话助手</td>
              </tr>
              <tr class="border-t bg-gray-50">
                <td class="p-3 font-semibold">数据范围</td>
                <td class="p-3">单一领域（中医）</td>
                <td class="p-3">多领域（10+任务类型）</td>
              </tr>
              <tr class="border-t">
                <td class="p-3 font-semibold">数据量示例</td>
                <td class="p-3">4条高质量长数据</td>
                <td class="p-3">10条多任务数据</td>
              </tr>
              <tr class="border-t bg-gray-50">
                <td class="p-3 font-semibold">专业深度</td>
                <td class="p-3">⭐⭐⭐⭐⭐</td>
                <td class="p-3">⭐⭐⭐</td>
              </tr>
              <tr class="border-t">
                <td class="p-3 font-semibold">泛化能力</td>
                <td class="p-3">⭐⭐</td>
                <td class="p-3">⭐⭐⭐⭐⭐</td>
              </tr>
              <tr class="border-t bg-gray-50">
                <td class="p-3 font-semibold">训练方法</td>
                <td class="p-3">LoRA微调</td>
                <td class="p-3">LoRA或全参数</td>
              </tr>
              <tr class="border-t">
                <td class="p-3 font-semibold">显存需求</td>
                <td class="p-3">8GB（单卡足够）</td>
                <td class="p-3">8GB（LoRA）/ 56GB（全参数）</td>
              </tr>
              <tr class="border-t bg-gray-50">
                <td class="p-3 font-semibold">训练时间</td>
                <td class="p-3">2-3小时</td>
                <td class="p-3">12-16小时</td>
              </tr>
              <tr class="border-t">
                <td class="p-3 font-semibold">难度</td>
                <td class="p-3">⭐⭐⭐</td>
                <td class="p-3">⭐⭐⭐⭐</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- 4.1 垂直领域项目 -->
      <div class="card bg-gradient-to-br from-green-50 to-emerald-50 mb-8">
        <div class="flex items-start space-x-4 mb-6">
          <div class="text-6xl">🏥</div>
          <div class="flex-1">
            <h3 class="text-3xl font-bold text-green-800 mb-2">4.1 垂直领域SFT：中医问诊助手</h3>
            <p class="text-lg text-gray-700">将通用模型微调为专业的中医问诊助手</p>
          </div>
        </div>

        <div class="bg-white p-6 rounded-lg mb-4">
          <h4 class="text-xl font-bold text-gray-800 mb-3">项目特点</h4>
          <div class="grid md:grid-cols-2 gap-4">
            <div class="flex items-start space-x-2">
              <span class="text-green-500 text-xl">✓</span>
              <div>
                <p class="font-semibold">真实完整的数据</p>
                <p class="text-sm text-gray-600">4条真实的中医问诊对话，每条1000-2000字</p>
              </div>
            </div>
            <div class="flex items-start space-x-2">
              <span class="text-green-500 text-xl">✓</span>
              <div>
                <p class="font-semibold">专业深度</p>
                <p class="text-sm text-gray-600">包含症状分析、辨证、治则、方药建议等</p>
              </div>
            </div>
            <div class="flex items-start space-x-2">
              <span class="text-green-500 text-xl">✓</span>
              <div>
                <p class="font-semibold">LoRA高效微调</p>
                <p class="text-sm text-gray-600">只训练0.1%参数，单卡8GB即可运行</p>
              </div>
            </div>
            <div class="flex items-start space-x-2">
              <span class="text-green-500 text-xl">✓</span>
              <div>
                <p class="font-semibold">完整的训练流程</p>
                <p class="text-sm text-gray-600">从数据准备到模型部署的全流程代码</p>
              </div>
            </div>
          </div>
        </div>

        <div class="bg-white p-6 rounded-lg mb-4">
          <h4 class="text-xl font-bold text-gray-800 mb-3">项目结构</h4>
          <CodeBlock 
            title="4.1 项目目录结构"
            language="bash"
            :code="project41Structure"
            :filePath="'code/part4/4.1_vertical_domain_tcm/'"
          />
        </div>

        <div class="bg-white p-6 rounded-lg mb-4">
          <h4 class="text-xl font-bold text-gray-800 mb-3">数据示例</h4>
          <p class="text-gray-700 mb-3">以下是一条真实的中医问诊数据样本（部分展示）：</p>
          <div class="bg-gray-50 p-4 rounded border-l-4 border-green-500 text-sm">
            <p class="font-semibold text-gray-800 mb-2">【患者输入】</p>
            <p class="text-gray-700 mb-3">
              "医生您好，我最近总是感觉很累，白天也没精神，晚上睡眠质量也不好，经常做梦。而且手脚经常冰凉，特别是冬天更严重。吃饭也没什么胃口，有时候还会有点恶心的感觉。舌头看起来颜色比较淡，边缘有齿痕..."
            </p>
            <p class="font-semibold text-gray-800 mb-2">【医生回复】（节选）</p>
            <p class="text-gray-700">
              "根据您描述的症状，我进行详细分析：<br><br>
              <strong>症状归纳：</strong>1. 主症：神疲乏力、精神不振 2. 睡眠：睡眠质量差、多梦...<br>
              <strong>辨证分析：</strong>您的这些症状符合中医的'脾肾阳虚'证型...<br>
              <strong>治则治法：</strong>温补脾肾、健脾助运...<br>
              <strong>方药建议：</strong>可以考虑使用附子理中丸合金匮肾气丸加减..."
            </p>
          </div>
        </div>

        <div class="bg-white p-6 rounded-lg mb-4">
          <h4 class="text-xl font-bold text-gray-800 mb-3">快速开始</h4>
          <CodeBlock 
            title="一键运行完整流程"
            language="bash"
            :code="project41Quickstart"
            :filePath="'code/part4/4.1_vertical_domain_tcm/run_full_pipeline.sh'"
          />
        </div>

        <!-- 真实场景特色 -->
        <div class="bg-gradient-to-r from-orange-50 to-red-50 p-6 rounded-lg mb-4 border-l-4 border-orange-500">
          <h4 class="text-2xl font-bold text-orange-800 mb-4 flex items-center">
            <span class="text-3xl mr-2">🔥</span>
            真实SFT场景：不只是理论，更是实战！
          </h4>
          
          <p class="text-gray-700 mb-4">
            本项目的核心价值在于<strong>真实性</strong>。我们不仅提供训练代码，更重要的是展示：
          </p>

          <div class="grid md:grid-cols-3 gap-4 mb-4">
            <div class="bg-white p-4 rounded-lg">
              <p class="font-bold text-red-700 mb-2">📊 真实的数据筛选</p>
              <p class="text-sm text-gray-600">5轮筛选迭代，发现问题后回溯修正</p>
              <code class="text-xs bg-gray-100 px-2 py-1 rounded block mt-2">
                data_filtering_pipeline.py
              </code>
            </div>

            <div class="bg-white p-4 rounded-lg">
              <p class="font-bold text-red-700 mb-2">🔍 真实的问题诊断</p>
              <p class="text-sm text-gray-600">复读、知识缺失等5大典型问题</p>
              <code class="text-xs bg-gray-100 px-2 py-1 rounded block mt-2">
                problem_diagnosis_and_fix.py
              </code>
            </div>

            <div class="bg-white p-4 rounded-lg">
              <p class="font-bold text-red-700 mb-2">📝 完整的迭代记录</p>
              <p class="text-sm text-gray-600">7天从失败到成功的详细日志</p>
              <code class="text-xs bg-gray-100 px-2 py-1 rounded block mt-2">
                ITERATION_LOG.md
              </code>
            </div>
          </div>

          <div class="bg-white p-4 rounded-lg">
            <h5 class="font-bold text-gray-800 mb-3">💡 真实场景示例</h5>
            
            <div class="space-y-3">
              <div class="border-l-4 border-red-500 pl-3">
                <p class="font-semibold text-red-700">场景1：数据筛选的多轮迭代</p>
                <p class="text-sm text-gray-600 mt-1">
                  第一遍用规则匹配筛选，第二遍用AI模型打分，结果发现高分数据还有问题！
                  只能回过头来重新筛选，添加新规则。
                </p>
                <p class="text-xs text-gray-500 mt-1">
                  👉 <code class="bg-gray-100 px-1 rounded">python data/data_filtering_pipeline.py</code>
                </p>
              </div>

              <div class="border-l-4 border-orange-500 pl-3">
                <p class="font-semibold text-orange-700">场景2：模型复读问题</p>
                <p class="text-sm text-gray-600 mt-1">
                  训练完发现模型会重复同一句话3次！分析原因：数据中有重复 + 解码参数未设置。
                  解决方案：数据去重 + 设置repetition_penalty=1.2
                </p>
                <p class="text-xs text-gray-500 mt-1">
                  👉 <code class="bg-gray-100 px-1 rounded">python training/problem_diagnosis_and_fix.py</code>
                </p>
              </div>

              <div class="border-l-4 border-yellow-500 pl-3">
                <p class="font-semibold text-yellow-700">场景3：专业知识缺失</p>
                <p class="text-sm text-gray-600 mt-1">
                  测试发现：不管什么症状都诊断为"脾肾阳虚"。原因：训练数据中90%都是这个证型！
                  解决：数据平衡采样 + 补充其他证型数据
                </p>
              </div>

              <div class="border-l-4 border-green-500 pl-3">
                <p class="font-semibold text-green-700">场景4：从v0.1失败到v1.1成功</p>
                <p class="text-sm text-gray-600 mt-1">
                  完整的7天迭代记录：v0.1完全无用 → v0.2严重复读 → v0.3判断错误 → 
                  v1.0基本可用 → v1.1效果优秀（准确率92%）
                </p>
                <p class="text-xs text-gray-500 mt-1">
                  👉 查看 <code class="bg-gray-100 px-1 rounded">ITERATION_LOG.md</code>
                </p>
              </div>
            </div>
          </div>

          <div class="mt-4 p-3 bg-orange-100 rounded">
            <p class="text-sm text-orange-800">
              <strong>💡 学习建议：</strong>
              先运行 <code class="bg-white px-2 py-1 rounded">data_filtering_pipeline.py</code> 和 
              <code class="bg-white px-2 py-1 rounded">problem_diagnosis_and_fix.py</code>，
              体验真实的SFT调试过程，再进行实际训练！
            </p>
          </div>
        </div>

        <div class="mt-4 p-4 bg-green-100 rounded-lg">
          <p class="text-green-800">
            <strong>📂 完整代码路径：</strong>
            <code class="bg-white px-2 py-1 rounded">sft-theory/code/part4/4.1_vertical_domain_tcm/</code>
          </p>
        </div>
      </div>

      <!-- 4.2 通用助手项目 -->
      <div class="card bg-gradient-to-br from-blue-50 to-indigo-50 mb-8">
        <div class="flex items-start space-x-4 mb-6">
          <div class="text-6xl">🤖</div>
          <div class="flex-1">
            <h3 class="text-3xl font-bold text-blue-800 mb-2">4.2 通用SFT：多任务对话助手</h3>
            <p class="text-lg text-gray-700">构建能处理多种任务的通用AI助手</p>
          </div>
        </div>

        <div class="bg-white p-6 rounded-lg mb-4">
          <h4 class="text-xl font-bold text-gray-800 mb-3">项目特点</h4>
          <div class="grid md:grid-cols-2 gap-4">
            <div class="flex items-start space-x-2">
              <span class="text-blue-500 text-xl">✓</span>
              <div>
                <p class="font-semibold">多任务数据</p>
                <p class="text-sm text-gray-600">涵盖10+种任务：问答、代码、推理、写作等</p>
              </div>
            </div>
            <div class="flex items-start space-x-2">
              <span class="text-blue-500 text-xl">✓</span>
              <div>
                <p class="font-semibold">强大泛化能力</p>
                <p class="text-sm text-gray-600">一个模型处理多种任务，适应性强</p>
              </div>
            </div>
            <div class="flex items-start space-x-2">
              <span class="text-blue-500 text-xl">✓</span>
              <div>
                <p class="font-semibold">灵活训练策略</p>
                <p class="text-sm text-gray-600">支持LoRA和全参数微调</p>
              </div>
            </div>
            <div class="flex items-start space-x-2">
              <span class="text-blue-500 text-xl">✓</span>
              <div>
                <p class="font-semibold">分布式训练</p>
                <p class="text-sm text-gray-600">支持多GPU并行，加速训练</p>
              </div>
            </div>
          </div>
        </div>

        <div class="bg-white p-6 rounded-lg mb-4">
          <h4 class="text-xl font-bold text-gray-800 mb-3">任务类型覆盖</h4>
          <div class="grid md:grid-cols-3 gap-3">
            <div class="bg-blue-50 p-3 rounded">
              <p class="font-semibold text-blue-800">📚 问答推理</p>
              <p class="text-xs text-gray-600">知识问答、逻辑推理</p>
            </div>
            <div class="bg-blue-50 p-3 rounded">
              <p class="font-semibold text-blue-800">💻 代码生成</p>
              <p class="text-xs text-gray-600">算法实现、代码解释</p>
            </div>
            <div class="bg-blue-50 p-3 rounded">
              <p class="font-semibold text-blue-800">✍️ 创意写作</p>
              <p class="text-xs text-gray-600">故事续写、文案创作</p>
            </div>
            <div class="bg-blue-50 p-3 rounded">
              <p class="font-semibold text-blue-800">🧮 数学计算</p>
              <p class="text-xs text-gray-600">应用题解答、推导证明</p>
            </div>
            <div class="bg-blue-50 p-3 rounded">
              <p class="font-semibold text-blue-800">📝 文本摘要</p>
              <p class="text-xs text-gray-600">长文总结、要点提取</p>
            </div>
            <div class="bg-blue-50 p-3 rounded">
              <p class="font-semibold text-blue-800">🌐 翻译转换</p>
              <p class="text-xs text-gray-600">多语言翻译</p>
            </div>
            <div class="bg-blue-50 p-3 rounded">
              <p class="font-semibold text-blue-800">🔍 信息抽取</p>
              <p class="text-xs text-gray-600">实体识别、关系抽取</p>
            </div>
            <div class="bg-blue-50 p-3 rounded">
              <p class="font-semibold text-blue-800">💡 头脑风暴</p>
              <p class="text-xs text-gray-600">创意生成、方案设计</p>
            </div>
            <div class="bg-blue-50 p-3 rounded">
              <p class="font-semibold text-blue-800">📊 观点分析</p>
              <p class="text-xs text-gray-600">论点评估、批判性思考</p>
            </div>
          </div>
        </div>

        <div class="bg-white p-6 rounded-lg mb-4">
          <h4 class="text-xl font-bold text-gray-800 mb-3">数据示例</h4>
          <p class="text-gray-700 mb-3">多任务数据格式示例：</p>
          <div class="space-y-3">
            <div class="bg-gray-50 p-3 rounded border-l-4 border-blue-500 text-sm">
              <p class="font-semibold text-blue-800">任务：代码生成</p>
              <p class="text-gray-700 mt-1"><strong>输入：</strong>"实现一个LRU缓存，时间复杂度O(1)"</p>
              <p class="text-gray-700 mt-1"><strong>输出：</strong>完整的Python代码实现+详细注释（约100行）</p>
            </div>
            <div class="bg-gray-50 p-3 rounded border-l-4 border-purple-500 text-sm">
              <p class="font-semibold text-purple-800">任务：逻辑推理</p>
              <p class="text-gray-700 mt-1"><strong>输入：</strong>"三个盒子标签都错了，如何确定真实内容？"</p>
              <p class="text-gray-700 mt-1"><strong>输出：</strong>详细的推理过程+步骤解析（约500字）</p>
            </div>
            <div class="bg-gray-50 p-3 rounded border-l-4 border-green-500 text-sm">
              <p class="font-semibold text-green-800">任务：创意写作</p>
              <p class="text-gray-700 mt-1"><strong>输入：</strong>"续写科幻故事：2157年，能源只剩48小时..."</p>
              <p class="text-gray-700 mt-1"><strong>输出：</strong>引人入胜的故事续写（约300字）</p>
            </div>
          </div>
        </div>

        <div class="bg-white p-6 rounded-lg mb-4">
          <h4 class="text-xl font-bold text-gray-800 mb-3">快速开始</h4>
          <CodeBlock 
            title="一键运行完整流程"
            language="bash"
            :code="project42Quickstart"
            :filePath="'code/part4/4.2_general_assistant/run_full_pipeline.sh'"
          />
        </div>

        <!-- 多任务特色场景 -->
        <div class="bg-gradient-to-r from-purple-50 to-indigo-50 p-6 rounded-lg mb-4 border-l-4 border-purple-500">
          <h4 class="text-2xl font-bold text-purple-800 mb-4 flex items-center">
            <span class="text-3xl mr-2">🔥</span>
            多任务SFT挑战：比单任务复杂10倍！
          </h4>
          
          <p class="text-gray-700 mb-4">
            多任务SFT不是简单地混合数据！展示了比单任务(4.1)更复杂的挑战：
          </p>

          <div class="grid md:grid-cols-3 gap-4 mb-4">
            <div class="bg-white p-4 rounded-lg">
              <p class="font-bold text-purple-700 mb-2">📊 任务平衡</p>
              <p class="text-sm text-gray-600">10+种任务的数量、质量、难度平衡</p>
              <code class="text-xs bg-gray-100 px-2 py-1 rounded block mt-2">
                data_filtering_multitask.py
              </code>
            </div>

            <div class="bg-white p-4 rounded-lg">
              <p class="font-bold text-purple-700 mb-2">🔀 任务串扰</p>
              <p class="text-sm text-gray-600">翻译变问答、代码变头脑风暴</p>
              <code class="text-xs bg-gray-100 px-2 py-1 rounded block mt-2">
                multitask_problems_diagnosis.py
              </code>
            </div>

            <div class="bg-white p-4 rounded-lg">
              <p class="font-bold text-purple-700 mb-2">📝 迭代更长</p>
              <p class="text-sm text-gray-600">15天(单任务7天)，挑战更大</p>
              <code class="text-xs bg-gray-100 px-2 py-1 rounded block mt-2">
                MULTITASK_ITERATION_LOG.md
              </code>
            </div>
          </div>

          <div class="bg-white p-4 rounded-lg">
            <h5 class="font-bold text-gray-800 mb-3">💡 多任务特有场景</h5>
            
            <div class="space-y-3">
              <div class="border-l-4 border-purple-500 pl-3">
                <p class="font-semibold text-purple-700">场景1：任务性能严重不均</p>
                <p class="text-sm text-gray-600 mt-1">
                  v0.1测试结果：问答85% ✅  翻译38% ❌ 相差47%！
                  原因：问答600条数据，翻译只有50条。
                  解决：上采样+下采样，平衡至100-150条/任务
                </p>
                <p class="text-xs text-gray-500 mt-1">
                  👉 <code class="bg-gray-100 px-1 rounded">python data/data_filtering_multitask.py</code>
                </p>
              </div>

              <div class="border-l-4 border-indigo-500 pl-3">
                <p class="font-semibold text-indigo-700">场景2：任务串扰（多任务特有）</p>
                <p class="text-sm text-gray-600 mt-1">
                  任务：翻译"I love AI" → 期望：我爱人工智能
                  实际：AI是一种计算机技术...（开始回答问答！）
                  原因：问答任务"污染"了翻译任务
                </p>
                <p class="text-xs text-gray-500 mt-1">
                  👉 <code class="bg-gray-100 px-1 rounded">python training/multitask_problems_diagnosis.py</code>
                </p>
              </div>

              <div class="border-l-4 border-pink-500 pl-3">
                <p class="font-semibold text-pink-700">场景3：数据平衡后串扰加剧</p>
                <p class="text-sm text-gray-600 mt-1">
                  v0.2平衡数据后，任务串扰反而更严重！问答开始列举多个答案（头脑风暴影响），
                  代码开始反问用户（对话影响）。根本原因：不同任务对模型行为的要求是矛盾的！
                </p>
              </div>

              <div class="border-l-4 border-blue-500 pl-3">
                <p class="font-semibold text-blue-700">场景4：分阶段训练解决冲突</p>
                <p class="text-sm text-gray-600 mt-1">
                  v1.0创新：第1阶段混合训练 → 第2阶段任务分组 → 第3阶段困难任务强化。
                  结果：准确率提升至82%，串扰率降至3%
                </p>
                <p class="text-xs text-gray-500 mt-1">
                  👉 查看 <code class="bg-gray-100 px-1 rounded">MULTITASK_ITERATION_LOG.md</code>
                </p>
              </div>

              <div class="border-l-4 border-green-500 pl-3">
                <p class="font-semibold text-green-700">对比单任务：挑战差异</p>
                <p class="text-sm text-gray-600 mt-1">
                  单任务(4.1中医)：主要挑战是数据质量、专业深度，迭代7天<br>
                  多任务(4.2通用)：主要挑战是任务平衡、任务串扰，迭代15天<br>
                  多任务复杂度 ≈ 单任务 × 10倍！
                </p>
              </div>
            </div>
          </div>

          <div class="mt-4 p-3 bg-purple-100 rounded">
            <p class="text-sm text-purple-800">
              <strong>💡 学习建议：</strong>
              先完成4.1单任务项目，理解基础流程后，再尝试4.2多任务项目。
              多任务的挑战是质的飞跃，需要更多耐心和实验！
            </p>
          </div>
        </div>

        <div class="mt-4 p-4 bg-blue-100 rounded-lg">
          <p class="text-blue-800">
            <strong>📂 完整代码路径：</strong>
            <code class="bg-white px-2 py-1 rounded">sft-theory/code/part4/4.2_general_assistant/</code>
          </p>
        </div>
      </div>

      <!-- 学习建议 -->
      <div class="card bg-gradient-to-br from-purple-50 to-pink-50">
        <h3 class="text-2xl font-bold text-purple-800 mb-4">🎓 学习路径建议</h3>
        
        <div class="space-y-4">
          <div class="bg-white p-4 rounded-lg">
            <p class="font-bold text-gray-800 mb-2">初学者：先从4.1开始</p>
            <ul class="list-disc list-inside text-sm text-gray-600 space-y-1">
              <li>数据少、训练快、效果明显</li>
              <li>单卡即可运行，门槛低</li>
              <li>容易理解垂直领域微调的概念</li>
            </ul>
          </div>

          <div class="bg-white p-4 rounded-lg">
            <p class="font-bold text-gray-800 mb-2">进阶者：尝试4.2</p>
            <ul class="list-disc list-inside text-sm text-gray-600 space-y-1">
              <li>理解多任务学习的复杂性</li>
              <li>实验不同的训练策略</li>
              <li>尝试分布式训练</li>
            </ul>
          </div>

          <div class="bg-white p-4 rounded-lg">
            <p class="font-bold text-gray-800 mb-2">高级玩家：对比实验</p>
            <ul class="list-disc list-inside text-sm text-gray-600 space-y-1">
              <li>比较LoRA vs 全参数微调的效果</li>
              <li>研究不同LoRA rank的影响</li>
              <li>探索数据量与性能的关系</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- 课程总结 -->
    <section class="my-16">
      <div class="card bg-gradient-to-br from-blue-50 via-purple-50 to-pink-50 border-2 border-purple-300">
        <h2 class="text-4xl font-bold text-center bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent mb-8">
          🎓 课程总结
        </h2>
        
        <div class="grid md:grid-cols-2 gap-6 mb-8">
          <div class="bg-white p-6 rounded-xl">
            <h3 class="text-xl font-bold text-blue-700 mb-3">📚 预训练 vs SFT</h3>
            <p class="text-gray-700">预训练构建知识大脑，SFT教会如何工作。两者共生但单向依赖。</p>
          </div>
          
          <div class="bg-white p-6 rounded-xl">
            <h3 class="text-xl font-bold text-purple-700 mb-3">🔌 LoRA高效微调</h3>
            <p class="text-gray-700">像电源适配器一样，只训练极少参数，避免遗忘，支持可插拔技能。</p>
          </div>
          
          <div class="bg-white p-6 rounded-xl">
            <h3 class="text-xl font-bold text-green-700 mb-3">📊 数据是行为蓝图</h3>
            <p class="text-gray-700">质量远胜于数量，塑造AI的风格、语气和行为模式。</p>
          </div>
          
          <div class="bg-white p-6 rounded-xl">
            <h3 class="text-xl font-bold text-orange-700 mb-3">🔄 以数据为中心</h3>
            <p class="text-gray-700">SFT是持续迭代的过程，像园艺一样需要精心培育。</p>
          </div>
        </div>

        <div class="bg-gradient-to-r from-blue-500 to-purple-500 text-white p-6 rounded-xl text-center">
          <p class="text-2xl font-bold mb-3">🎉 恭喜完成SFT原理课程！</p>
          <p class="text-lg">
            现在你已经掌握了打造专属AI助手的基础知识和实战经验。
            两个完整的实践项目为你提供了从理论到实践的桥梁。
            创造高度专业化的AI解决方案的能力已经掌握在你手中！
          </p>
        </div>
      </div>
    </section>

    <!-- Part4 总结 -->
    <section class="my-16">
      <div class="card bg-gradient-to-br from-indigo-600 to-purple-600 text-white p-8">
        <h2 class="text-4xl font-bold mb-4 flex items-center">
          <span class="text-5xl mr-4">🎉</span>
          恭喜完成全部课程！
        </h2>
        <p class="text-xl opacity-90 mb-6">你已经掌握了SFT从理论到实践的完整知识体系</p>
        
        <div class="grid md:grid-cols-4 gap-6 mt-8">
          <div class="bg-white bg-opacity-20 backdrop-blur p-5 rounded-xl">
            <div class="text-4xl mb-3">📚</div>
            <p class="font-bold text-lg mb-2">Part1</p>
            <p class="text-sm opacity-90">预训练 vs SFT</p>
          </div>
          <div class="bg-white bg-opacity-20 backdrop-blur p-5 rounded-xl">
            <div class="text-4xl mb-3">⚡</div>
            <p class="font-bold text-lg mb-2">Part2</p>
            <p class="text-sm opacity-90">LoRA高效微调</p>
          </div>
          <div class="bg-white bg-opacity-20 backdrop-blur p-5 rounded-xl">
            <div class="text-4xl mb-3">📊</div>
            <p class="font-bold text-lg mb-2">Part3</p>
            <p class="text-sm opacity-90">SFT数据集</p>
          </div>
          <div class="bg-white bg-opacity-20 backdrop-blur p-5 rounded-xl">
            <div class="text-4xl mb-3">🚀</div>
            <p class="font-bold text-lg mb-2">Part4</p>
            <p class="text-sm opacity-90">实践工作流</p>
          </div>
        </div>

        <div class="mt-8 bg-white bg-opacity-30 backdrop-blur p-6 rounded-xl">
          <p class="text-lg font-bold mb-3">💡 完整学习路径回顾：</p>
          <ul class="space-y-2 text-sm">
            <li>• 理解了预训练和SFT的本质区别与协作关系</li>
            <li>• 掌握了LoRA参数高效微调的原理和实践</li>
            <li>• 学会了构建高质量SFT数据集的方法</li>
            <li>• 完整实践了两个真实的SFT项目（垂直领域+通用助手）</li>
          </ul>
        </div>

        <div class="mt-6 bg-gradient-to-r from-yellow-400 to-orange-400 text-gray-900 p-6 rounded-xl">
          <p class="text-xl font-bold mb-2">🎯 下一步行动</p>
          <p class="text-sm">
            现在你已经具备了完整的SFT知识！建议：<br>
            1. 运行两个实践项目的代码，亲手体验真实的SFT流程<br>
            2. 选择一个你感兴趣的领域，开始你的第一个SFT项目<br>
            3. 加入社区，与其他开发者交流经验
          </p>
        </div>
      </div>
    </section>

    <!-- 综合测验 -->
    <section class="my-16">
      <div class="card bg-gradient-to-br from-purple-600 to-pink-600 text-white p-6 mb-8">
        <h2 class="text-3xl font-bold mb-2">🧠 最终测验：SFT实战全面检验</h2>
        <p class="text-lg opacity-90">测试你对整个SFT实践流程的掌握程度</p>
      </div>

      <div class="space-y-6">
        <!-- 题目1 -->
        <QuizBox
          question="1. SFT项目的第一步应该是什么？"
          :options="[
            '立即开始收集大量数据',
            '明确定义任务目标和期望行为',
            '选择最大的预训练模型',
            '直接开始训练'
          ]"
          :correctAnswer="1"
          explanation="<strong>明确任务目标是第一步！</strong><br><br>
          <strong>为什么？</strong><br>
          目标不清晰 → 数据方向不明 → 训练效果差 → 返工浪费<br><br>
          <strong>需要明确的内容：</strong><br><br>
          <strong>1. 任务类型</strong><br>
          • 问答？对话？摘要？翻译？代码生成？<br>
          • 通用助手 vs 垂直领域？<br><br>
          <strong>2. 期望行为</strong><br>
          • 输出格式（JSON/Markdown/纯文本）<br>
          • 语气风格（正式/随和/专业）<br>
          • 响应长度（简洁/详细）<br>
          • 是否需要推理步骤？<br><br>
          <strong>3. 成功标准</strong><br>
          • 准确率目标（如85%以上）<br>
          • 特定能力（如不能有幻觉）<br>
          • 格式要求（100%遵循JSON）<br><br>
          <strong>4. 边界条件</strong><br>
          • 什么情况下应该拒绝？<br>
          • 如何处理模糊输入？<br>
          • 安全和合规要求<br><br>
          <strong>案例对比：</strong><br><br>
          ❌ <strong>模糊目标：</strong><br>
          '做一个中医助手'<br>
          （不知道要什么功能，如何衡量成功）<br><br>
          ✅ <strong>明确目标：</strong><br>
          '基于用户症状描述，进行中医辨证分析，输出证型判断、病因分析和调理建议。格式统一，必须包含禁忌事项。准确率目标85%以上。'<br><br>
          <strong>有了明确目标才能：</strong><br>
          • 高效收集相关数据<br>
          • 设计合理的评估指标<br>
          • 避免无谓的迭代"
        />

        <!-- 题目2 -->
        <QuizBox
          question="2. 如何选择合适的基座模型？"
          :options="[
            '总是选最大的模型',
            '总是选最新的模型',
            '根据任务复杂度、资源预算、推理速度综合选择',
            '随机选一个'
          ]"
          :correctAnswer="2"
          explanation="<strong>需要综合权衡！</strong><br><br>
          <strong>考虑因素：</strong><br><br>
          <strong>1. 任务复杂度 ⭐⭐⭐⭐⭐</strong><br>
          • <strong>简单任务</strong>（格式转换、简单分类）<br>
          &nbsp;&nbsp;→ 1-3B模型足够<br>
          &nbsp;&nbsp;→ Qwen-1.8B, Gemma-2B<br><br>
          • <strong>中等任务</strong>（问答、摘要、写作）<br>
          &nbsp;&nbsp;→ 7-13B模型<br>
          &nbsp;&nbsp;→ LLaMA2-7B, Baichuan2-7B<br><br>
          • <strong>复杂任务</strong>（复杂推理、代码生成）<br>
          &nbsp;&nbsp;→ 30B+模型<br>
          &nbsp;&nbsp;→ LLaMA2-70B, Qwen-72B<br><br>
          <strong>2. 资源预算 ⭐⭐⭐⭐</strong><br>
          • GPU显存限制<br>
          • 训练时间成本<br>
          • 存储成本<br><br>
          <strong>示例：</strong><br>
          • 7B模型 + LoRA: 20GB显存，2小时训练<br>
          • 70B模型 + LoRA: 80GB显存，12小时训练<br><br>
          <strong>3. 推理速度 ⭐⭐⭐⭐</strong><br>
          • 在线服务需要低延迟<br>
          • 1B模型：50ms/次<br>
          • 7B模型：200ms/次<br>
          • 70B模型：2000ms/次<br><br>
          <strong>4. 领域相关性 ⭐⭐⭐</strong><br>
          • 中文任务 → 中文预训练模型（Qwen, Baichuan）<br>
          • 代码任务 → CodeLLaMA, DeepSeek-Coder<br>
          • 通用任务 → LLaMA2, Mistral<br><br>
          <strong>决策矩阵：</strong><br><br>
          | 场景 | 推荐模型 | 理由 |<br>
          |------|----------|------|<br>
          | 个人项目，简单任务 | 1-3B | 资源友好 |<br>
          | 企业应用，中等复杂度 | 7-13B | 性能平衡 |<br>
          | 科研/高端应用 | 30B+ | 性能优先 |<br><br>
          <strong>误区：</strong><br>
          ✗ '最大的模型肯定最好' → 但成本10倍，效果可能只提升10%<br>
          ✗ '最新的模型肯定最好' → 但可能不稳定，社区资源少"
        />

        <!-- 题目3 -->
        <QuizBox
          question="3. SFT训练通常需要多少epoch？"
          :options="[
            '1 epoch（一轮就够）',
            '3-5 epochs（最常见）',
            '10-20 epochs',
            '越多越好'
          ]"
          :correctAnswer="1"
          explanation="<strong>通常3-5 epochs最合适！</strong><br><br>
          <strong>为什么不需要太多epoch？</strong><br><br>
          <strong>1. 预训练基础已经很强</strong><br>
          • 模型已经懂语言和常识<br>
          • SFT只是调整行为，不是从零学习<br>
          • 几轮就能建立新的行为模式<br><br>
          <strong>2. 过拟合风险</strong><br>
          • SFT数据量相对小（几千条）<br>
          • epoch太多容易过拟合<br>
          • 表现：训练集准确率99%，测试集60%<br><br>
          <strong>实际建议：</strong><br><br>
          <strong>数据量 < 1000条：</strong><br>
          • 2-3 epochs<br>
          • 更多轮容易过拟合<br><br>
          <strong>数据量 1000-10000条：</strong><br>
          • 3-5 epochs ⭐ 推荐<br>
          • 最常见配置<br><br>
          <strong>数据量 > 10000条：</strong><br>
          • 1-3 epochs<br>
          • 数据充足，少量epoch即可<br><br>
          <strong>如何判断合适的epoch数？</strong><br><br>
          1. <strong>观察验证集Loss</strong><br>
          &nbsp;&nbsp;• Epoch 1: Loss 2.5 → 1.8<br>
          &nbsp;&nbsp;• Epoch 2: Loss 1.8 → 1.5<br>
          &nbsp;&nbsp;• Epoch 3: Loss 1.5 → 1.4<br>
          &nbsp;&nbsp;• Epoch 4: Loss 1.4 → 1.45 ⚠️ 开始上升！<br>
          &nbsp;&nbsp;→ 停在Epoch 3<br><br>
          2. <strong>Early Stopping</strong><br>
          &nbsp;&nbsp;• 设置patience=2<br>
          &nbsp;&nbsp;• 验证Loss连续2个epoch不下降就停止<br><br>
          3. <strong>实际测试</strong><br>
          &nbsp;&nbsp;• 每个epoch后测试几个样本<br>
          &nbsp;&nbsp;• 感觉效果不再提升就停止<br><br>
          <strong>警告信号：</strong><br>
          • 训练Loss还在降，但验证Loss上升 → 过拟合<br>
          • 输出开始'背诵'训练数据 → 过拟合<br>
          • 格式完美但内容僵化 → 过拟合"
        />

        <!-- 题目4 -->
        <QuizBox
          question="4. 学习率应该设置多大？"
          :options="[
            '和预训练一样（1e-4）',
            '比预训练小得多（1e-5到5e-5）',
            '比预训练大（1e-3）',
            '学习率不重要'
          ]"
          :correctAnswer="1"
          explanation="<strong>SFT学习率应该比预训练小！</strong><br><br>
          <strong>典型值：1e-5 到 5e-5</strong><br><br>
          <strong>为什么要小？</strong><br><br>
          <strong>1. 避免破坏预训练知识</strong><br>
          • 预训练耗费巨大算力学到的知识很珍贵<br>
          • 大学习率会'覆盖'这些知识<br>
          • 小学习率是'微调'，不是'重训练'<br><br>
          <strong>2. 防止灾难性遗忘</strong><br>
          • 学习率太大：学会新任务，忘掉旧能力<br>
          • 学习率小：新旧能力共存<br><br>
          <strong>推荐设置：</strong><br><br>
          <strong>全参数微调：</strong><br>
          • learning_rate = 1e-5<br>
          • 非常保守，避免破坏<br><br>
          <strong>LoRA微调：</strong><br>
          • learning_rate = 1e-4 到 3e-4<br>
          • 可以稍大，因为原参数被冻结<br>
          • 只更新适配器，风险小<br><br>
          <strong>不同模型大小：</strong><br>
          • 1-3B模型：2e-4（可以稍大）<br>
          • 7-13B模型：1e-4（中等）<br>
          • 30B+模型：5e-5（更保守）<br><br>
          <strong>学习率调度：</strong><br><br>
          推荐使用<strong>cosine schedule + warmup</strong><br>
          <pre><code>warmup_ratio = 0.1  # 前10%步数warmup<br>
lr_scheduler_type = 'cosine'<br><br>
# 学习率变化：<br>
# 0 → warmup → peak_lr → cosine衰减 → 0.1*peak_lr</code></pre><br><br>
          <strong>错误案例：</strong><br>
          • lr=1e-3（预训练学习率）<br>
          &nbsp;&nbsp;→ 模型在Epoch 1就'忘掉'预训练知识<br>
          &nbsp;&nbsp;→ Loss剧烈震荡<br>
          &nbsp;&nbsp;→ 输出变成乱码<br><br>
          <strong>调试技巧：</strong><br>
          如果Loss不下降 → 尝试增大学习率<br>
          如果Loss震荡 → 减小学习率<br>
          如果模型'变傻' → 学习率太大"
        />

        <!-- 题目5 -->
        <QuizBox
          question="5. 如何判断模型是否过拟合？"
          :options="[
            '训练Loss很低',
            '训练Loss很低，但验证Loss开始上升',
            '训练时间很长',
            '模型参数很多'
          ]"
          :correctAnswer="1"
          explanation="<strong>训练Loss和验证Loss走势背离是过拟合的标志！</strong><br><br>
          <strong>正常训练：</strong><br>
          • 训练Loss：2.5 → 1.8 → 1.4 → 1.2 ↓<br>
          • 验证Loss：2.6 → 1.9 → 1.5 → 1.3 ↓<br>
          • 两者同步下降 ✅<br><br>
          <strong>过拟合：</strong><br>
          • 训练Loss：2.5 → 1.8 → 1.2 → 0.8 ↓<br>
          • 验证Loss：2.6 → 1.9 → 1.5 → 1.8 ↑<br>
          • 训练降，验证升 ❌<br><br>
          <strong>其他过拟合症状：</strong><br><br>
          <strong>1. '背诵'训练数据</strong><br>
          测试输入略微不同，但输出几乎完全复制训练样本<br><br>
          <strong>2. 泛化能力差</strong><br>
          • 训练集：95%准确率<br>
          • 测试集：60%准确率<br>
          • 差距>15% → 过拟合<br><br>
          <strong>3. 对输入变化极度敏感</strong><br>
          • '请翻译这句话' → 完美输出<br>
          • '翻译这句话' → 乱码输出<br>
          → 过拟合到特定表述<br><br>
          <strong>4. 输出僵化</strong><br>
          • 总是用相同的开场白<br>
          • 总是用相同的句式<br>
          • 缺少灵活性<br><br>
          <strong>如何避免过拟合？</strong><br><br>
          <strong>1. Early Stopping ⭐⭐⭐⭐⭐</strong><br>
          <pre><code>early_stopping_patience = 2<br>
# 验证Loss连续2个epoch不降就停</code></pre><br><br>
          <strong>2. 增加数据</strong><br>
          • 更多样化的数据<br>
          • 数据增强<br><br>
          <strong>3. 减少epoch</strong><br>
          • 从5 epoch降到3 epoch<br><br>
          <strong>4. 正则化</strong><br>
          • Weight decay = 0.01<br>
          • Dropout（如果架构支持）<br><br>
          <strong>5. 数据增强</strong><br>
          • 改写、paraphrase<br>
          • 增加多样性<br><br>
          <strong>检查清单：</strong><br>
          ☐ 每个epoch后在验证集上评估<br>
          ☐ 绘制训练/验证Loss曲线<br>
          ☐ 在多个测试样本上手动测试<br>
          ☐ 观察输出的多样性"
        />

        <!-- 题目6 -->
        <QuizBox
          question="6. 训练中断了，应该怎么办？"
          :options="[
            '从头开始重新训练',
            '从最近的checkpoint恢复',
            '放弃这次训练',
            '直接使用当前模型'
          ]"
          :correctAnswer="1"
          explanation="<strong>从checkpoint恢复，节省时间和成本！</strong><br><br>
          <strong>Checkpoint机制：</strong><br><br>
          训练过程中定期保存模型状态，包括：<br>
          • 模型参数<br>
          • 优化器状态<br>
          • 当前epoch和step<br>
          • 学习率调度器状态<br><br>
          <strong>如何配置：</strong><br><br>
          <pre><code>training_args = TrainingArguments(<br>
  save_strategy='steps',<br>
  save_steps=500,  # 每500步保存一次<br>
  save_total_limit=3,  # 只保留最近3个checkpoint<br>
)</code></pre><br><br>
          <strong>恢复训练：</strong><br><br>
          <pre><code># 自动检测最近的checkpoint<br>
trainer.train(resume_from_checkpoint=True)<br><br>
# 或指定特定checkpoint<br>
trainer.train(resume_from_checkpoint='./checkpoints/checkpoint-1500')</code></pre><br><br>
          <strong>示例：</strong><br>
          • 目标：训练3 epochs<br>
          • 在Epoch 2, Step 800时中断<br>
          • 从checkpoint-800恢复<br>
          • 只需完成剩余的Epoch 2和Epoch 3<br>
          • 节省：约60%时间<br><br>
          <strong>最佳实践：</strong><br><br>
          <strong>1. 频繁保存（小数据集）</strong><br>
          save_steps = 100-500<br>
          损失：最多重复500步<br><br>
          <strong>2. 适度保存（大数据集）</strong><br>
          save_steps = 1000-5000<br>
          平衡存储成本和恢复成本<br><br>
          <strong>3. 保留多个checkpoint</strong><br>
          save_total_limit = 3<br>
          以防最新的有问题<br><br>
          <strong>4. 按epoch保存</strong><br>
          <pre><code>save_strategy = 'epoch'<br>
# 每个epoch结束保存一次</code></pre><br><br>
          <strong>checkpoint管理：</strong><br><br>
          <strong>存储结构：</strong><br>
          <pre><code>output_dir/<br>
├── checkpoint-500/<br>
│   ├── pytorch_model.bin<br>
│   ├── optimizer.pt<br>
│   └── trainer_state.json<br>
├── checkpoint-1000/<br>
└── checkpoint-1500/  # 最新</code></pre><br><br>
          <strong>注意：</strong><br>
          • 确保有足够磁盘空间<br>
          • 定期清理旧checkpoint<br>
          • 最终模型单独保存"
        />

        <!-- 题目7 -->
        <QuizBox
          question="7. 如何评估SFT模型的效果？"
          :options="[
            '只看训练Loss',
            '只看验证Loss',
            '自动评估指标 + 人工评估 + 实际应用测试',
            '随便测几个样本'
          ]"
          :correctAnswer="2"
          explanation="<strong>需要多维度综合评估！</strong><br><br>
          <strong>1. 自动评估指标 ⭐⭐⭐</strong><br><br>
          <strong>准确率类：</strong><br>
          • 分类任务：准确率、F1<br>
          • 生成任务：BLEU、ROUGE<br>
          • 快速但不够全面<br><br>
          <strong>2. 人工评估 ⭐⭐⭐⭐⭐</strong><br><br>
          <strong>评估维度：</strong><br>
          • <strong>准确性：</strong>信息是否正确？<br>
          • <strong>相关性：</strong>是否回答了问题？<br>
          • <strong>完整性：</strong>是否遗漏关键信息？<br>
          • <strong>流畅性：</strong>语言是否自然？<br>
          • <strong>格式：</strong>是否遵循要求？<br><br>
          <strong>方法：</strong><br>
          • 准备100-200个测试样本<br>
          • 覆盖不同场景和难度<br>
          • 逐个人工评分（1-5分）<br>
          • 计算平均分和通过率<br><br>
          <strong>3. 对比评估 ⭐⭐⭐⭐</strong><br><br>
          • vs 基座模型（看SFT提升多少）<br>
          • vs 其他SFT方法<br>
          • vs 商业API（如GPT-4）<br><br>
          <strong>4. 实际应用测试 ⭐⭐⭐⭐⭐</strong><br><br>
          <strong>A/B Testing：</strong><br>
          • 50%用户用新模型<br>
          • 50%用户用旧模型<br>
          • 对比用户满意度、任务完成率<br><br>
          <strong>5. 边界测试 ⭐⭐⭐⭐</strong><br><br>
          测试模型的极限：<br>
          • 超长输入<br>
          • 模糊指令<br>
          • 对抗样本<br>
          • 有害请求（应该拒绝）<br><br>
          <strong>评估示例（中医助手）：</strong><br><br>
          <strong>自动指标：</strong><br>
          • 证型分类准确率：92%<br>
          • JSON格式正确率：100%<br><br>
          <strong>人工评估（100样本）：</strong><br>
          • 辨证准确性：4.2/5.0<br>
          • 建议合理性：4.5/5.0<br>
          • 专业度：4.7/5.0<br>
          • 安全性：5.0/5.0<br><br>
          <strong>对比基线：</strong><br>
          • 基座模型：准确率35%<br>
          • SFT后：准确率92%<br>
          • 提升：+57%<br><br>
          <strong>边界测试：</strong><br>
          • 拒绝开处方：✅<br>
          • 警告孕妇禁忌：✅<br>
          • 处理含糊症状：✅<br><br>
          <strong>评估清单：</strong><br>
          ☐ 准备分层测试集（各类别均衡）<br>
          ☐ 自动指标基线对比<br>
          ☐ 至少100个样本的人工评估<br>
          ☐ 边界和安全测试<br>
          ☐ 如可能，进行A/B测试"
        />

        <!-- 题目8 -->
        <QuizBox
          question="8. 发现模型输出格式不一致，最可能的原因是？"
          :options="[
            '模型太小',
            '训练数据中格式不统一',
            '学习率设置不对',
            '训练epoch太少'
          ]"
          :correctAnswer="1"
          explanation="<strong>训练数据格式不统一是格式问题的主要原因！</strong><br><br>
          <strong>模型会忠实学习数据中的所有模式。</strong><br><br>
          <strong>常见格式不一致案例：</strong><br><br>
          <strong>1. JSON vs Markdown</strong><br>
          • 50%数据用JSON格式<br>
          • 50%数据用Markdown<br>
          → 模型随机选择格式<br><br>
          <strong>2. 有无标题</strong><br>
          • 60%数据有'【辨证分析】'标题<br>
          • 40%数据直接输出内容<br>
          → 模型有时加标题，有时不加<br><br>
          <strong>3. 列表格式</strong><br>
          • 数据A：'1. 2. 3.'（数字列表）<br>
          • 数据B：'• • •'（bullet points）<br>
          • 数据C：'- - -'（横线列表）<br>
          → 模型三种都用<br><br>
          <strong>4. 日期格式</strong><br>
          • '2024-01-15'<br>
          • '2024年1月15日'<br>
          • '01/15/2024'<br>
          → 输出格式随机<br><br>
          <strong>诊断方法：</strong><br><br>
          <strong>步骤1：检查训练数据</strong><br>
          <pre><code>python data/check_format_consistency.py<br><br>
# 输出：<br>
# JSON格式：45%<br>
# Markdown格式：32%<br>
# 纯文本：23%<br>
# ⚠️ 格式不统一！</code></pre><br><br>
          <strong>步骤2：统计输出格式</strong><br>
          测试100个样本，记录格式分布<br><br>
          <strong>步骤3：找到相关性</strong><br>
          • 如果测试格式分布 ≈ 训练格式分布<br>
          → 证明是数据问题<br><br>
          <strong>解决方案：</strong><br><br>
          <strong>方案1：统一训练数据格式（推荐）⭐⭐⭐⭐⭐</strong><br>
          • 将所有数据转为统一格式<br>
          • 重新训练<br>
          • 彻底解决<br><br>
          <strong>方案2：后处理</strong><br>
          • 训练后，强制转换输出格式<br>
          • 治标不治本<br>
          • 可能引入新错误<br><br>
          <strong>方案3：格式指令强化</strong><br>
          • 在每个instruction中明确格式要求<br>
          • '请以JSON格式输出，包含...'<br>
          • 辅助手段，但数据统一更重要<br><br>
          <strong>预防措施：</strong><br>
          ☐ 数据收集时就制定格式规范<br>
          ☐ 使用模板确保一致性<br>
          ☐ 训练前自动验证格式<br>
          ☐ 设置格式校验脚本"
        />

        <!-- 题目9 -->
        <QuizBox
          question="9. 模型在某个特定类型任务上表现很差，应该怎么办？"
          :options="[
            '增加整体数据量',
            '增加该类型任务的数据',
            '提高学习率',
            '增加训练epoch'
          ]"
          :correctAnswer="1"
          explanation="<strong>针对性地增加该类型任务的数据！</strong><br><br>
          <strong>长板理论 vs 短板理论：</strong><br><br>
          ✗ <strong>错误思路：</strong>整体增加数据<br>
          • 所有任务各增加100条<br>
          • 但弱项任务占比不变<br>
          • 问题依旧<br><br>
          ✓ <strong>正确思路：</strong>补强短板<br>
          • 重点增加弱项任务数据<br>
          • 调整数据分布<br>
          • 针对性提升<br><br>
          <strong>诊断流程：</strong><br><br>
          <strong>1. 按任务类型分类测试</strong><br>
          • 问答：90%准确率 ✅<br>
          • 摘要：85%准确率 ✅<br>
          • 翻译：60%准确率 ❌<br>
          • 代码：55%准确率 ❌<br><br>
          <strong>2. 检查训练数据分布</strong><br>
          • 问答：1000条（40%）<br>
          • 摘要：800条（32%）<br>
          • 翻译：400条（16%）← 少<br>
          • 代码：300条（12%）← 很少<br><br>
          <strong>3. 发现相关性</strong><br>
          表现差的任务，数据也少 → 因果关系明确<br><br>
          <strong>解决方案：</strong><br><br>
          <strong>方案1：数据补充（根本解决）⭐⭐⭐⭐⭐</strong><br>
          • 翻译：400 → 800条（翻倍）<br>
          • 代码：300 → 800条（接近3倍）<br>
          • 重新训练<br>
          • 预期：翻译和代码准确率提升到80%+<br><br>
          <strong>方案2：平衡采样 ⭐⭐⭐⭐</strong><br>
          <pre><code>from torch.utils.data import WeightedRandomSampler<br><br>
# 让每个任务类型在训练中出现概率相等<br>
task_weights = {<br>
  '问答': 0.25,<br>
  '摘要': 0.25,<br>
  '翻译': 0.25,  # 上采样<br>
  '代码': 0.25   # 上采样<br>
}</code></pre><br>
          → 即使数据少，也能充分学习<br><br>
          <strong>方案3：数据增强 ⭐⭐⭐</strong><br>
          • 为弱项任务生成更多样本<br>
          • 改写、变体<br>
          • 快速增加多样性<br><br>
          <strong>方案4：分阶段训练 ⭐⭐⭐</strong><br>
          • 第一阶段：只训练弱项任务<br>
          • 第二阶段：混合训练所有任务<br>
          • 让模型先克服短板<br><br>
          <strong>实际案例：</strong><br><br>
          某通用助手模型：<br>
          • 问题：代码生成准确率只有45%<br>
          • 诊断：代码数据只占12%<br>
          • 方案：补充500条代码数据<br>
          • 结果：准确率提升到78%<br>
          • 成本：3天数据准备 + 1天重新训练<br><br>
          <strong>预防措施：</strong><br>
          ☐ 训练前分析任务类型分布<br>
          ☐ 确保每个任务至少500条数据<br>
          ☐ 使用平衡采样<br>
          ☐ 分任务类型评估"
        />

        <!-- 题目10 -->
        <QuizBox
          question="10. 什么时候应该考虑从头训练，而不是微调？"
          :options="[
            '总是微调更好',
            '当任务与预训练差异极大，或需要专有知识时',
            '当数据很多时',
            '当GPU资源充足时'
          ]"
          :correctAnswer="1"
          explanation="<strong>极少数情况下，从头训练可能更合适！</strong><br><br>
          <strong>通常：微调 > 从头训练</strong><br><br>
          • 微调利用预训练知识<br>
          • 数据需求少<br>
          • 训练快<br>
          • 成本低<br><br>
          <strong>但以下情况考虑从头训练：</strong><br><br>
          <strong>1. 领域差异巨大 ⚠️</strong><br><br>
          <strong>示例：基因序列分析</strong><br>
          • 预训练：自然语言（英文、中文）<br>
          • 目标：DNA序列（ATCG）<br>
          • 差异：词汇表、语法、模式完全不同<br>
          → 预训练知识几乎无用<br><br>
          <strong>2. 专有tokenizer需求 ⚠️</strong><br><br>
          • 化学分子式（SMILES notation）<br>
          • 音乐符号（ABC notation）<br>
          • 专业代码（Verilog, VHDL）<br>
          → 需要完全不同的tokenizer<br><br>
          <strong>3. 特殊架构需求 ⚠️</strong><br><br>
          • 需要特定的注意力机制<br>
          • 需要特殊的位置编码<br>
          • 预训练模型架构不匹配<br><br>
          <strong>4. 严格的隐私/安全要求 ⚠️</strong><br><br>
          • 军事/政府应用<br>
          • 不信任公开预训练模型<br>
          • 需要完全可控的训练过程<br><br>
          <strong>5. 极大规模数据 ⚠️</strong><br><br>
          • 拥有数十亿条领域数据<br>
          • 预训练级别的资源<br>
          • 预训练知识变得不那么重要<br><br>
          <strong>成本对比：</strong><br><br>
          <strong>微调7B模型（LoRA）：</strong><br>
          • 数据：1000-10000条<br>
          • GPU：1×A100<br>
          • 时间：几小时<br>
          • 成本：$50-200<br><br>
          <strong>从头训练7B模型：</strong><br>
          • 数据：数十亿tokens<br>
          • GPU：64-256×A100<br>
          • 时间：几周到几月<br>
          • 成本：$100,000-1,000,000<br><br>
          <strong>决策树：</strong><br><br>
          1. 任务是自然语言相关吗？<br>
          &nbsp;&nbsp;→ 是：微调（99%情况）<br>
          &nbsp;&nbsp;→ 否：考虑从头训练<br><br>
          2. 有足够数据吗（>1B tokens）？<br>
          &nbsp;&nbsp;→ 否：只能微调<br>
          &nbsp;&nbsp;→ 是：继续评估<br><br>
          3. 有足够预算吗（>$10万）？<br>
          &nbsp;&nbsp;→ 否：只能微调<br>
          &nbsp;&nbsp;→ 是：可以考虑从头训练<br><br>
          4. 预训练模型能满足70%需求吗？<br>
          &nbsp;&nbsp;→ 是：微调<br>
          &nbsp;&nbsp;→ 否：从头训练<br><br>
          <strong>推荐：</strong><br>
          • 99%的应用：微调<br>
          • 0.9%的应用：大规模继续预训练+微调<br>
          • 0.1%的应用：从头训练<br><br>
          <strong>即使看似需要从头训练，也先尝试微调！</strong>"
        />

        <!-- 题目11 -->
        <QuizBox
          question="11. 真实的SFT项目中，最耗时的环节是什么？"
          :options="[
            '模型训练',
            '数据准备和迭代优化',
            '模型选择',
            '环境配置'
          ]"
          :correctAnswer="1"
          explanation="<strong>数据准备和迭代优化占80%时间！</strong><br><br>
          <strong>真实时间分配（7天项目）：</strong><br><br>
          <strong>Day 1-4（57%）：数据相关</strong><br>
          • Day 1: 收集数据（发现质量问题）<br>
          • Day 2: 清洗和筛选（发现分布问题）<br>
          • Day 3-4: 补充和平衡数据<br><br>
          <strong>Day 5（14%）：首次训练</strong><br>
          • 配置训练参数<br>
          • 运行训练（2小时）<br>
          • 发现新问题<br><br>
          <strong>Day 6（14%）：问题诊断</strong><br>
          • 测试发现问题<br>
          • 诊断根本原因<br>
          • 又回到数据修正<br><br>
          <strong>Day 7（14%）：重新训练和验证</strong><br>
          • 修正后重新训练<br>
          • 全面测试<br>
          • 部署准备<br><br>
          <strong>为什么数据最耗时？</strong><br><br>
          <strong>1. 数据收集难</strong><br>
          • 找高质量数据源<br>
          • 清洗和格式化<br>
          • 人工审核<br><br>
          <strong>2. 发现问题慢</strong><br>
          • 训练完才发现数据问题<br>
          • 需要回溯重新筛选<br>
          • 迭代多次<br><br>
          <strong>3. 质量控制严</strong><br>
          • 每条数据都要审核<br>
          • 格式统一化<br>
          • 去重、去噪<br><br>
          <strong>4. 多轮迭代</strong><br>
          • 第一轮：基础数据（发现不够）<br>
          • 第二轮：补充数据（发现不平衡）<br>
          • 第三轮：平衡数据（发现格式问题）<br>
          • 第四轮：格式统一（终于可以）<br><br>
          <strong>对比：训练本身很快</strong><br>
          • 7B模型 + LoRA：2小时<br>
          • 但是数据准备：2-4天<br><br>
          <strong>实际案例（中医助手）：</strong><br><br>
          <strong>总计7天项目：</strong><br>
          • 数据收集：1天<br>
          • 数据清洗：1天<br>
          • 发现问题重筛：1天<br>
          • 数据平衡补充：1.5天<br>
          • 首次训练：0.5天（其中训练2小时）<br>
          • 问题诊断：0.5天<br>
          • 数据修正：0.5天<br>
          • 重新训练：0.5天（其中训练2小时）<br>
          • 验证测试：0.5天<br><br>
          <strong>数据相关：5天（71%）</strong><br>
          <strong>训练相关：2天（29%，其中实际训练仅4小时）</strong><br><br>
          <strong>经验教训：</strong><br><br>
          1. <strong>前期投入数据准备</strong><br>
          &nbsp;&nbsp;• 宁愿多花时间准备数据<br>
          &nbsp;&nbsp;• 也不要急着训练<br>
          &nbsp;&nbsp;• '磨刀不误砍柴工'<br><br>
          2. <strong>建立数据管道</strong><br>
          &nbsp;&nbsp;• 自动化数据验证<br>
          &nbsp;&nbsp;• 格式检查脚本<br>
          &nbsp;&nbsp;• 分布分析工具<br><br>
          3. <strong>小规模验证</strong><br>
          &nbsp;&nbsp;• 用100-200条种子数据先训练<br>
          &nbsp;&nbsp;• 快速发现数据问题<br>
          &nbsp;&nbsp;• 避免大规模返工<br><br>
          <strong>记住：</strong>SFT项目是数据项目，不是训练项目！"
        />

        <!-- 题目12 -->
        <QuizBox
          question="12. 如何判断是否需要增加模型规模（如从7B升级到70B）？"
          :options="[
            '直接用最大的模型',
            '当任务极度复杂，7B模型已经优化到极限仍不达标时',
            '当有GPU资源时',
            '当数据量超过1万条时'
          ]"
          :correctAnswer="1"
          explanation="<strong>只有在优化到极限仍不满足时，才升级模型！</strong><br><br>
          <strong>决策流程：</strong><br><br>
          <strong>第1步：优化当前模型</strong><br><br>
          在考虑升级前，先确保：<br>
          ☐ 数据质量已优化（无噪声、格式统一）<br>
          ☐ 数据量充足（每个任务>500条）<br>
          ☐ 数据分布平衡（无严重偏见）<br>
          ☐ 训练参数已调优（lr、epoch、batch_size）<br>
          ☐ 多次迭代改进<br><br>
          <strong>第2步：诊断瓶颈</strong><br><br>
          <strong>模型能力问题：</strong>⚠️ 考虑升级<br>
          • 复杂推理失败<br>
          • 长上下文理解差<br>
          • 多步骤任务能力弱<br><br>
          <strong>数据/训练问题：</strong>❌ 不要升级<br>
          • 数据分布不均<br>
          • 数据质量差<br>
          • 训练参数不当<br>
          → 换大模型也没用<br><br>
          <strong>第3步：小规模测试</strong><br><br>
          用同样的数据，测试更大模型：<br>
          • 7B模型：准确率75%<br>
          • 13B模型：准确率77%（+2%）<br>
          • 70B模型：准确率81%（+6%）<br><br>
          如果提升<5%，不值得升级！<br><br>
          <strong>成本效益分析：</strong><br><br>
          <strong>7B模型：</strong><br>
          • 训练：1×A100，2小时，$20<br>
          • 推理：1×A100，200ms/次<br>
          • 部署：简单<br><br>
          <strong>70B模型：</strong><br>
          • 训练：4×A100，12小时，$500<br>
          • 推理：4×A100，2000ms/次（10倍慢）<br>
          • 部署：复杂（模型并行）<br><br>
          <strong>ROI计算：</strong><br>
          • 成本增加：25倍<br>
          • 性能提升：6%<br>
          • 推理慢：10倍<br>
          → 大多数情况下不值得<br><br>
          <strong>何时值得升级？</strong><br><br>
          <strong>1. 任务需要深度推理 ✅</strong><br>
          • 多步数学证明<br>
          • 复杂代码生成<br>
          • 长篇论文写作<br>
          → 7B模型能力确实不够<br><br>
          <strong>2. 准确率要求极高 ✅</strong><br>
          • 医疗诊断（95%+ vs 90%）<br>
          • 法律分析<br>
          • 金融风控<br>
          → 每1%提升都很关键<br><br>
          <strong>3. 离线批处理 ✅</strong><br>
          • 不需要实时响应<br>
          • 推理慢可以接受<br>
          → 成本压力小<br><br>
          <strong>4. 预算充足 ✅</strong><br>
          • GPU资源不是瓶颈<br>
          • 追求最佳效果<br><br>
          <strong>何时不值得升级？</strong><br><br>
          ❌ <strong>在线服务（需要低延迟）</strong><br>
          ❌ <strong>简单任务（分类、格式转换）</strong><br>
          ❌ <strong>预算受限</strong><br>
          ❌ <strong>数据问题未解决</strong><br><br>
          <strong>折中方案：</strong><br><br>
          1. <strong>使用13B模型</strong><br>
          &nbsp;&nbsp;• 性能提升明显（vs 7B）<br>
          &nbsp;&nbsp;• 成本可控（vs 70B）<br>
          &nbsp;&nbsp;• 最佳平衡点<br><br>
          2. <strong>蒸馏（Distillation）</strong><br>
          &nbsp;&nbsp;• 用70B模型生成数据<br>
          &nbsp;&nbsp;• 训练7B模型<br>
          &nbsp;&nbsp;• 获得大模型部分能力<br><br>
          3. <strong>混合部署</strong><br>
          &nbsp;&nbsp;• 简单任务：7B模型<br>
          &nbsp;&nbsp;• 复杂任务：70B模型<br>
          &nbsp;&nbsp;• 路由分发<br><br>
          <strong>记住：</strong><br>
          90%的性能提升来自数据和训练优化<br>
          只有10%来自更大的模型！"
        />

        <!-- 题目13 -->
        <QuizBox
          question="13. 【代码题】SFT数据预处理的正确顺序是？"
          :options="[
            '1. 加载原始数据 → 2. 格式化为instruction-response → 3. 数据质量过滤 → 4. Tokenization',
            '1. Tokenization → 2. 加载原始数据 → 3. 格式化 → 4. 质量过滤',
            '1. 加载原始数据 → 2. 数据质量过滤 → 3. 格式化为instruction-response → 4. Tokenization',
            '1. 格式化 → 2. 质量过滤 → 3. 加载数据 → 4. Tokenization'
          ]"
          :correctAnswer="2"
          explanation="<strong>正确顺序：加载 → 过滤 → 格式化 → Tokenization！</strong><br><br>
          <strong>为什么是这个顺序？</strong><br><br>
          <strong>1. 先加载原始数据</strong><br>
          • 这是起点，从文件/数据库读取<br><br>
          <strong>2. 质量过滤要早做</strong><br>
          • ⚡ 减少后续计算量<br>
          • 过滤掉30%低质量数据，节省30%时间<br>
          • 如果最后过滤，前面的格式化和tokenization都浪费了<br><br>
          <strong>3. 格式化在tokenization前</strong><br>
          • 格式化后才是完整的训练文本<br>
          • Tokenizer需要完整文本才能正确编码<br><br>
          <strong>4. Tokenization最后</strong><br>
          • 最耗时的步骤（10000条需要5-10分钟）<br>
          • 只对高质量、格式化的数据tokenize<br>
          • 避免重复计算<br><br>
          <strong>时间对比：</strong><br>
          • 错误顺序（tokenize在前）：浪费15%时间<br>
          • 正确顺序（tokenize在后）：高效，节省时间<br><br>
          <strong>常见错误：</strong><br>
          • ❌ Tokenize后再格式化：token丢失上下文<br>
          • ❌ 格式化后才过滤：浪费格式化时间<br>
          • ❌ 多次tokenize：每次都要重新计算"
        />

        <!-- 题目14 -->
        <QuizBox
          question="14. 【代码题】LoRA训练后，保存模型的最佳方式是？"
          :options="[
            '保存完整的merged模型（14GB）',
            '只保存LoRA适配器（20MB）',
            '保存完整checkpoint包括optimizer',
            '不保存，每次重新训练'
          ]"
          :correctAnswer="1"
          explanation="<strong>只保存LoRA适配器是最佳实践！</strong><br><br>
          <strong>为什么选择保存LoRA适配器？</strong><br><br>
          <strong>优势对比：</strong><br>
          • LoRA适配器：20MB，上传10秒，版本管理轻松<br>
          • 完整模型：14GB，上传1小时，版本管理困难<br>
          • Checkpoint：28GB，上传2小时，非常困难<br><br>
          <strong>实际场景：</strong><br><br>
          <strong>多任务部署：</strong><br>
          • 基座模型：14GB（只加载一次）<br>
          • 3个任务适配器：20MB × 3 = 60MB<br>
          • 总存储：14.06GB vs 完整模型42GB<br>
          • <strong>节省66%存储！</strong><br><br>
          <strong>版本迭代：</strong><br>
          • v1.0, v1.1, v2.0适配器各20MB<br>
          • 可以快速A/B测试，切换只需几秒<br><br>
          <strong>何时保存完整模型？</strong><br>
          • ✅ 部署环境不支持PEFT库<br>
          • ✅ 需要最简单的加载方式<br>
          • ❌ 不适合：多任务切换、频繁迭代、存储受限<br><br>
          <strong>最佳实践：</strong><br>
          训练时保存适配器，部署时按需选择：<br>
          • 云端推理：直接用适配器（省带宽）<br>
          • 边缘设备：合并后部署（省内存）<br>
          • A/B测试：保留多个适配器（灵活）"
        />

        <!-- 题目15 -->
        <QuizBox
          question="15. 【代码题】使用Trainer API时，哪些参数设置是必需的？"
          :options="[
            '只需要output_dir',
            'output_dir + num_train_epochs',
            'output_dir + num_train_epochs + learning_rate + batch_size',
            '所有参数都必须设置'
          ]"
          :correctAnswer="0"
          explanation="<strong>只有output_dir是必需的，其他都有默认值！</strong><br><br>
          <strong>TrainingArguments的智能设计：</strong><br><br>
          <strong>必需参数：</strong><br>
          • output_dir：必须指定，否则无法保存模型<br><br>
          <strong>重要参数（有合理默认值）：</strong><br>
          • num_train_epochs：默认3<br>
          • learning_rate：默认5e-5<br>
          • per_device_train_batch_size：默认8<br><br>
          <strong>推荐的配置顺序：</strong><br><br>
          <strong>1. 基础路径</strong><br>
          • output_dir, logging_dir<br><br>
          <strong>2. 训练参数</strong><br>
          • num_train_epochs, batch_size<br><br>
          <strong>3. 优化器配置</strong><br>
          • learning_rate, weight_decay<br><br>
          <strong>4. 评估与保存</strong><br>
          • eval_steps, save_steps<br><br>
          <strong>5. 性能优化</strong><br>
          • fp16, gradient_accumulation_steps<br><br>
          <strong>常用参数速查：</strong><br>
          • learning_rate: LoRA用2e-4，全参数用5e-5<br>
          • num_train_epochs: 3-5轮<br>
          • batch_size: 4-8（取决于GPU显存）<br>
          • warmup_ratio: 0.03-0.1<br>
          • eval_steps: 500<br>
          • fp16: True（A100用bf16）<br><br>
          <strong>不同任务的配置：</strong><br>
          • 小数据集（1000条）：多轮训练，频繁评估<br>
          • 大数据集（10万+）：1轮即可，降低评估频率<br>
          • 多GPU训练：注意gradient_accumulation_steps<br><br>
          <strong>常见错误：</strong><br>
          • ❌ learning_rate太大（大于1e-3）：训练不稳定<br>
          • ❌ 没设置eval_strategy：无法监控过拟合<br>
          • ❌ save_total_limit未设置：磁盘被checkpoint占满<br>
          • ❌ fp16和bf16同时设置：冲突报错"
        />
      </div>
    </section>

    <!-- 导航 -->
    <div class="flex justify-between mt-16">
      <router-link to="/part3" class="btn-secondary">
        ← 上一部分
      </router-link>
      <router-link to="/" class="btn-primary">
        返回首页 🏠
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import AnalogyBox from '../components/AnalogyBox.vue'
import AnimatedIllustration from '../components/AnimatedIllustration.vue'
import InfoCard from '../components/InfoCard.vue'
import ProgressSteps from '../components/ProgressSteps.vue'
import InteractiveChart from '../components/InteractiveChart.vue'
import CodeBlock from '../components/CodeBlock.vue'
import QuizBox from '../components/QuizBox.vue'

const currentStep = ref(0)

const workflowSteps = [
  {
    title: '定义任务',
    description: '选择基座模型'
  },
  {
    title: '准备数据',
    description: '策划数据集'
  },
  {
    title: '运行训练',
    description: '配置参数'
  },
  {
    title: '评估迭代',
    description: '持续优化'
  }
]

const jsonlExample = `{"instruction": "请用三句话总结以下文章。", "input": "埃菲尔铁塔是法国巴黎的标志性建筑...", "response": "埃菲尔铁塔是巴黎标志性建筑..."}
{"instruction": "根据上下文回答问题。", "input": "上下文：埃菲尔铁塔于1889年建成。问题：埃菲尔铁塔何时完工？", "response": "埃菲尔铁塔于1889年完工。"}
{"instruction": "你是一个友好的助手。", "input": "今天天气怎么样？", "response": "您好！根据最新气象数据，今日天气晴朗，适合户外活动。"}`

const trainingCode = `from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import SFTTrainer, SFTConfig
from peft import LoraConfig

# 加载基座模型
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")

# 配置LoRA
lora_config = LoraConfig(
    r=16,  # LoRA秩
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05
)

# 配置训练
training_args = SFTConfig(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    learning_rate=2e-5,
    logging_steps=10
)

# 开始训练
trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    peft_config=lora_config
)

trainer.train()`

const trainingLossData = ref({
  labels: [],
  datasets: []
})

// 项目代码示例
const project41Structure = `4.1_vertical_domain_tcm/
├── README.md              # 项目说明
├── requirements.txt       # 依赖包
├── data/                  # 数据目录
│   ├── raw_examples.py        # 真实中医问诊数据
│   ├── prepare_dataset.py     # 数据预处理
│   └── dataset_analysis.py    # 数据分析
├── model/                 # 模型配置
│   ├── model_config.py        # 配置参数
│   └── model_utils.py         # 工具函数
├── training/              # 训练脚本
│   ├── train_lora.py          # LoRA训练
│   ├── train_distributed.py   # 分布式训练
│   └── training_config.yaml   # 训练配置
├── inference/             # 推理脚本
│   ├── test_model.py          # 测试脚本
│   └── interactive_demo.py    # 交互演示
└── run_full_pipeline.sh   # 一键运行脚本`

const project41Quickstart = `# 方式1：一键运行完整流程
cd code/part4/4.1_vertical_domain_tcm
bash run_full_pipeline.sh

# 方式2：逐步运行
# 1. 安装依赖
pip install -r requirements.txt

# 2. 准备数据
cd data
python raw_examples.py       # 生成原始数据
python prepare_dataset.py    # 预处理数据
cd ..

# 3. 训练模型
cd training
python train_lora.py         # LoRA微调（约2-3小时）
cd ..

# 4. 测试模型
cd inference
python test_model.py         # 运行测试
python interactive_demo.py   # 交互式演示`

const project42Quickstart = `# 方式1：一键运行完整流程
cd code/part4/4.2_general_assistant
bash run_full_pipeline.sh

# 方式2：逐步运行
# 1. 安装依赖
pip install -r requirements.txt

# 2. 准备数据
cd data
python raw_examples.py       # 生成多任务数据
python prepare_dataset.py    # 预处理数据
cd ..

# 3. 训练模型（选择一种）
cd training
python train_lora.py         # LoRA微调（推荐，约12小时）
# 或
python train_full.py         # 全参数微调（需要更多资源）
cd ..

# 4. 测试模型
cd inference
python test_model.py         # 运行测试
python interactive_demo.py   # 交互式演示`

onMounted(async () => {
  try {
    const response = await axios.get('/api/generate-training-curve?epochs=10')
    const data = response.data
    
    trainingLossData.value = {
      labels: data.sft.x.map((_, i) => i % 10 === 0 ? `Step ${i}` : ''),
      datasets: [
        {
          label: 'SFT训练损失',
          data: data.sft.y,
          borderColor: 'rgb(168, 85, 247)',
          backgroundColor: 'rgba(168, 85, 247, 0.1)',
          tension: 0.4
        }
      ]
    }
  } catch (error) {
    console.error('获取数据失败:', error)
    // 使用模拟数据
    const steps = Array.from({ length: 100 }, (_, i) => i)
    const loss = steps.map(s => 2.0 * Math.exp(-1.5 * s / 100) + 0.3 + Math.random() * 0.05)
    
    trainingLossData.value = {
      labels: steps.map((_, i) => i % 10 === 0 ? `Step ${i}` : ''),
      datasets: [
        {
          label: 'SFT训练损失',
          data: loss,
          borderColor: 'rgb(168, 85, 247)',
          backgroundColor: 'rgba(168, 85, 247, 0.1)',
          tension: 0.4
        }
      ]
    }
  }
})
</script>

