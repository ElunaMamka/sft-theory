<template>
  <div class="part2-page">
    <!-- 标题 -->
    <h1 class="section-title">第二部分：事半功倍——使用LoRA进行高效微调</h1>

    <!-- 引言 -->
    <AnalogyBox icon="🔌" title="核心类比：电源适配器">
      <p class="text-lg">
        想象你有一个<strong>墙上的插座</strong>（预训练模型）和一个<strong>新买的电器</strong>（特定任务），但插头不匹配。
      </p>
      <p class="text-lg mt-3">
        <strong>LoRA就是那个小巧、廉价、轻便的转换插头</strong>——它没有改变墙上的插座，却让你的新电器完美地工作起来！
      </p>
    </AnalogyBox>

    <!-- 全量微调的困境 -->
    <section class="my-12">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">"全量微调"的困境</h2>
      
      <div class="card bg-gradient-to-br from-red-50 to-orange-50 border-l-4 border-red-500">
        <div class="flex items-start space-x-4">
          <div class="text-5xl">⚠️</div>
          <div class="flex-1">
            <h3 class="text-2xl font-bold text-red-800 mb-4">全量微调 = 脑外科手术</h3>
            <p class="text-lg text-gray-700 mb-4">
              全量微调意味着要调整模型的<strong>所有参数</strong>（如GPT-3的1750亿个权重）。
              就像为每次新技能学习都进行一次复杂的脑部手术——风险高、成本大，而且可能导致"遗忘"！
            </p>
          </div>
        </div>
      </div>

      <div class="grid md:grid-cols-3 gap-6 my-8">
        <InfoCard icon="💸" title="巨大的计算开销" variant="error">
          <p>需要大量配备高显存的GPU，训练过程耗时且昂贵，资源需求有时不亚于一次小规模的预训练。</p>
        </InfoCard>

        <InfoCard icon="🧠" title="灾难性遗忘" variant="error">
          <p>模型全力学习新知识时，可能会覆盖或"忘记"预训练阶段学到的海量通用知识，泛化能力严重退化。</p>
        </InfoCard>

        <InfoCard icon="💾" title="存储与部署噩梦" variant="error">
          <p>10个任务需要保存10个完整的巨大模型副本，占用海量存储空间，部署维护异常复杂。</p>
        </InfoCard>
      </div>

      <AnalogyBox icon="🎓" title="类比：过度专业化的风险">
        <p>
          就像一位语言学家为了成为程序员，结果忘记了如何正常说话。全量微调让模型为了掌握新技能，
          可能会丢失原本宝贵的通用能力。
        </p>
      </AnalogyBox>

      <!-- 📝 全量微调困境测验 -->
      <div class="my-8 space-y-4">
        <div class="flex items-center space-x-3 mb-6">
          <span class="text-4xl">🧠</span>
          <h3 class="text-2xl font-bold text-red-700">即学即测：全量微调的挑战</h3>
        </div>

        <QuizBox
          question="Q1. 全参数微调一个7B模型大约需要多少显存？"
          :options="[
            '约7GB（模型大小）',
            '约14GB（模型的2倍）',
            '约80GB（模型+梯度+优化器状态）',
            '约100GB以上'
          ]"
          :correctAnswer="2"
          explanation="<strong>正确答案是约80GB！</strong><br><br>
          <strong>为什么需要这么多？</strong><br><br>
          <strong>1. 模型参数</strong>（7B × 2字节 = 14GB）<br>
          • 7B参数，半精度float16存储<br>
          • 每个参数2字节<br><br>
          <strong>2. 梯度</strong>（7B × 2字节 = 14GB）<br>
          • 每个参数都需要计算梯度<br>
          • 与参数量相同<br><br>
          <strong>3. 优化器状态</strong>（7B × 8字节 = 56GB）<br>
          • Adam优化器需要保存momentum和variance<br>
          • 每个参数需要8字节（2个状态 × 4字节）<br><br>
          <strong>总计：</strong>14 + 14 + 56 = <strong>84GB</strong><br><br>
          这就是为什么全参数微调需要A100（80GB）或多卡！<br>
          而LoRA只需要约20GB（减少75%）。"
        />

        <QuizBox
          question="Q2. 灾难性遗忘的主要原因是什么？"
          :options="[
            '训练时间太长',
            '学习率太大，覆盖了原有知识',
            '模型参数太多',
            '数据集太小'
          ]"
          :correctAnswer="1"
          explanation="<strong>学习率太大是灾难性遗忘的主要原因之一！</strong><br><br>
          <strong>为什么会遗忘？</strong><br><br>
          <strong>1. 参数被大幅更新</strong><br>
          • 全参数微调更新所有参数<br>
          • 新任务的梯度直接覆盖原参数<br>
          • 预训练学到的知识被'冲走'<br><br>
          <strong>2. 新旧任务分布差异大</strong><br>
          • 预训练：通用文本（维基、新闻等）<br>
          • 微调：特定领域（如医疗对话）<br>
          • 差异太大导致参数剧烈变化<br><br>
          <strong>3. 过度优化新任务</strong><br>
          • 为了在新任务上表现好<br>
          • 模型牺牲了通用能力<br><br>
          <strong>真实案例：</strong><br>
          • 微调前：模型能写诗、编程、回答常识<br>
          • 微调后：只会医疗对话，其他能力大幅下降<br><br>
          <strong>解决方法：</strong><br>
          • 使用LoRA（只更新少量参数）<br>
          • 降低学习率<br>
          • 混入通用数据<br>
          • 使用正则化技术"
        />

        <QuizBox
          question="Q3. 如果要对10个不同任务进行全参数微调，需要保存多少个模型？"
          :options="[
            '1个（同一个模型可以处理多任务）',
            '2个（基座模型+一个通用微调模型）',
            '10个（每个任务一个完整模型副本）',
            '11个（基座+10个任务模型）'
          ]"
          :correctAnswer="2"
          explanation="<strong>需要10个完整的模型副本！</strong><br><br>
          <strong>为什么不能共享？</strong><br><br>
          <strong>1. 参数直接冲突</strong><br>
          • 全参数微调更新所有参数<br>
          • 任务A的最优参数 ≠ 任务B的最优参数<br>
          • 无法在一个模型中同时优化多任务<br><br>
          <strong>2. 串扰问题严重</strong><br>
          • 如果用一个模型处理多任务<br>
          • 模型会混淆不同任务<br>
          • 例如：代码生成时突然输出医疗建议<br><br>
          <strong>存储成本惊人：</strong><br><br>
          <strong>7B模型（FP16）：</strong><br>
          • 单个模型：14GB<br>
          • 10个任务：140GB<br><br>
          <strong>65B模型：</strong><br>
          • 单个模型：130GB<br>
          • 10个任务：1.3TB！<br><br>
          <strong>LoRA的优势：</strong><br>
          • 基座模型：14GB（只存一次）<br>
          • 每个LoRA适配器：4-50MB<br>
          • 10个任务：14GB + 500MB ≈ 14.5GB<br>
          • <strong>节省125GB（90%）！</strong>"
        />
      </div>

      <!-- 全量微调问题演示代码 -->
      <CodeBlock
        title="全量微调的三大问题模拟"
        file-path="code/part2/01_full_finetuning_problems.py"
        language="Python"
        :runnable="true"
        description="运行此代码可以看到全量微调的计算开销、灾难性遗忘和存储成本的详细量化分析"
        :code="`# 全量微调问题模拟器
class FullFineTuningSimulator:
    def __init__(self, base_model_size='7B'):
        self.model_size = base_model_size
        self.params = 7_000_000_000  # 7B参数
    
    def calculate_memory_requirement(self):
        '''计算内存需求（FP32训练）'''
        # 模型参数
        model_memory = (self.params * 4) / (1024**3)
        # Adam优化器状态（2倍）
        optimizer_memory = model_memory * 2
        # 梯度
        gradient_memory = model_memory
        # 激活值
        activation_memory = model_memory * 0.5
        
        total = model_memory + optimizer_memory + gradient_memory + activation_memory
        
        print(f'内存需求分解:')
        print(f'  模型参数: {model_memory:.2f} GB')
        print(f'  优化器:   {optimizer_memory:.2f} GB')
        print(f'  梯度:     {gradient_memory:.2f} GB')
        print(f'  激活:     {activation_memory:.2f} GB')
        print(f'  总计:     {total:.2f} GB')
        return total
    
    def simulate_catastrophic_forgetting(self):
        '''模拟灾难性遗忘'''
        initial_general_knowledge = 95
        after_finetuning = 65  # 大幅下降
        
        print(f'\\n灾难性遗忘演示:')
        print(f'  初始通用能力: {initial_general_knowledge}分')
        print(f'  微调后: {after_finetuning}分')
        print(f'  损失: {initial_general_knowledge - after_finetuning}分')

# 运行
simulator = FullFineTuningSimulator()
simulator.calculate_memory_requirement()
simulator.simulate_catastrophic_forgetting()

# 输出示例：
# 内存需求: ~98 GB
# 灾难性遗忘: 95分 → 65分`"
      />
    </section>

    <!-- LoRA解决方案 -->
    <section class="my-12">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">解决方案：LoRA（低秩适配）</h2>
      
      <InfoCard icon="✨" title="什么是LoRA？" variant="success">
        <p class="text-lg">
          <strong>LoRA</strong>（Low-Rank Adaptation，低秩适配）是一种参数高效微调技术（PEFT），
          在微调时只更新模型中<strong>极小一部分（通常&lt;1%）的参数</strong>，大幅降低资源消耗。
        </p>
      </InfoCard>

      <!-- LoRA工作原理动画 -->
      <AnimatedIllustration 
        title="LoRA的工作机制"
        description="冻结大脑，添加微小适配器"
      >
        <div class="w-full max-w-5xl">
          <div class="flex items-center justify-around">
            <!-- 原始模型 -->
            <div class="text-center space-y-3">
              <div class="relative">
                <div class="text-6xl">🧠</div>
                <div class="absolute -top-2 -right-2 bg-blue-500 text-white rounded-full w-8 h-8 flex items-center justify-center text-xs">
                  冻结
                </div>
              </div>
              <div class="card bg-blue-50 p-3">
                <p class="font-bold text-blue-700">预训练模型</p>
                <p class="text-xs text-gray-600">70亿参数</p>
                <p class="text-xs text-gray-600">完全冻结 ❄️</p>
              </div>
            </div>

            <div class="text-3xl mx-4">+</div>

            <!-- LoRA适配器 -->
            <div class="text-center space-y-3">
              <div class="text-6xl animate-pulse">🔌</div>
              <div class="card bg-green-50 p-3">
                <p class="font-bold text-green-700">LoRA适配器</p>
                <p class="text-xs text-gray-600">~700万参数</p>
                <p class="text-xs text-gray-600">可训练 ✏️</p>
              </div>
            </div>

            <div class="text-3xl mx-4">=</div>

            <!-- 专业化模型 -->
            <div class="text-center space-y-3">
              <div class="text-6xl">💼</div>
              <div class="card bg-purple-50 p-3">
                <p class="font-bold text-purple-700">专业化模型</p>
                <p class="text-xs text-gray-600">完美适配任务</p>
                <p class="text-xs text-gray-600">保留通用能力 ✓</p>
              </div>
            </div>
          </div>
        </div>
      </AnimatedIllustration>

      <!-- LoRA步骤 -->
      <div class="card my-8 bg-gradient-to-br from-green-50 to-emerald-50">
        <h3 class="text-2xl font-bold text-green-800 mb-6">LoRA的两个关键步骤</h3>
        <div class="space-y-6">
          <div class="flex items-start space-x-4">
            <div class="bg-green-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold flex-shrink-0">
              1
            </div>
            <div class="flex-1">
              <h4 class="text-xl font-bold text-gray-800 mb-2">冻结"大脑" ❄️</h4>
              <p class="text-gray-700">
                将原始的、巨大的预训练模型权重完全<strong>"冻结"</strong>，使其在训练过程中保持不变。
                这保护了毕业生的核心知识体系，从根本上避免了灾难性遗忘。
              </p>
            </div>
          </div>

          <div class="flex items-start space-x-4">
            <div class="bg-green-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold flex-shrink-0">
              2
            </div>
            <div class="flex-1">
              <h4 class="text-xl font-bold text-gray-800 mb-2">附加微小的"适配器" 🔌</h4>
              <p class="text-gray-700">
                在模型的关键部分（通常是注意力层）注入微小的、可训练的新层（低秩矩阵）。
                在整个微调过程中，<strong>只有这些新增的、极少数的参数会被更新</strong>。
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- LoRA机制代码演示 -->
      <CodeBlock
        title="LoRA工作机制详解"
        file-path="code/part2/02_lora_mechanism.py"
        language="Python"
        :runnable="true"
        description="演示LoRA的核心：冻结原始权重W，训练低秩矩阵A和B，使得 W' = W + BA"
        :code="`# LoRA机制模拟
import numpy as np

class LoRALayer:
    def __init__(self, d=4096, r=8):
        '''
        d: 原始权重矩阵维度
        r: LoRA秩（rank），控制参数量
        '''
        # 原始权重（冻结）
        self.W = np.random.randn(d, d) * 0.1
        self.W.flags.writeable = False  # 冻结！
        
        # LoRA矩阵（可训练）
        self.lora_A = np.random.randn(d, r) * 0.01
        self.lora_B = np.zeros((r, d))
        
        # 参数量对比
        self.frozen_params = d * d  # 16,777,216
        self.trainable_params = d * r + r * d  # 65,536
        
        print(f'LoRA配置: d={d}, r={r}')
        print(f'冻结参数: {self.frozen_params:,}')
        print(f'训练参数: {self.trainable_params:,}')
        print(f'训练比例: {self.trainable_params/self.frozen_params*100:.3f}%')
    
    def forward(self, x):
        '''前向传播'''
        # 分别计算两部分
        base_output = x @ self.W
        lora_output = x @ self.lora_A @ self.lora_B
        # 加权合并（alpha/r是缩放因子）
        return base_output + (16.0/8) * lora_output

# 创建LoRA层
lora = LoRALayer(d=4096, r=8)

# 输出示例：
# LoRA配置: d=4096, r=8
# 冻结参数: 16,777,216
# 训练参数: 65,536
# 训练比例: 0.390%  ← 只训练0.4%的参数！`"
      />
    </section>

    <!-- LoRA详细可视化 -->
    <LoRAVisualization />

    <!-- LoRA数学原理 -->
    <LoRAMathExplanation />

    <!-- 📝 LoRA核心原理测验 -->
    <section class="my-12">
      <div class="my-8 space-y-4">
        <div class="flex items-center space-x-3 mb-6">
          <span class="text-4xl">🧠</span>
          <h3 class="text-2xl font-bold text-green-700">即学即测：LoRA核心原理</h3>
        </div>

        <QuizBox
          question="Q4. LoRA的核心思想是什么？"
          :options="[
            '删除不重要的参数',
            '用低秩矩阵近似参数更新',
            '只训练最后几层',
            '使用更小的学习率'
          ]"
          :correctAnswer="1"
          explanation="<strong>LoRA的核心是低秩矩阵分解！</strong><br><br>
          <strong>关键洞察：</strong><br>
          微调时的参数更新ΔW通常是<strong>低秩的</strong>（rank很小）<br><br>
          <strong>数学原理：</strong><br>
          • 原始更新：ΔW (d×d维，百万参数)<br>
          • LoRA分解：ΔW = A×B (两个小矩阵)<br>
          &nbsp;&nbsp;- A: d×r (r≪d)<br>
          &nbsp;&nbsp;- B: r×d<br>
          • 参数量：d×r + r×d ≪ d×d<br><br>
          <strong>举例（d=4096，r=8）：</strong><br>
          • 原始：4096×4096 = 16,777,216 参数<br>
          • LoRA：4096×8 + 8×4096 = 65,536 参数<br>
          • <strong>减少256倍！</strong><br><br>
          <strong>为什么可行？</strong><br>
          研究发现，神经网络的参数更新矩阵往往具有低秩结构，用少量参数就能很好地近似。"
        />

        <QuizBox
          question="Q5. 在LoRA中，rank参数r的典型取值范围是？"
          :options="[
            'r = 1-4',
            'r = 8-64',
            'r = 128-256',
            'r = 512-1024'
          ]"
          :correctAnswer="1"
          explanation="<strong>典型范围是r=8-64。</strong><br><br>
          <strong>不同r值的影响：</strong><br><br>
          <strong>r = 1-4：</strong><br>
          • 参数极少，存储成本最低<br>
          • 但表达能力有限<br>
          • 适合：简单任务、资源极度受限<br><br>
          <strong>r = 8-16（常用）：</strong><br>
          • 参数量和效果的良好平衡<br>
          • 大多数任务的首选<br>
          • 参数量约原模型的0.1-0.5%<br><br>
          <strong>r = 32-64：</strong><br>
          • 更强的表达能力<br>
          • 适合复杂任务<br>
          • 参数量约原模型的1-2%<br><br>
          <strong>r > 64：</strong><br>
          • 很少使用<br>
          • 失去了LoRA的参数效率优势<br>
          • 可能还不如全参数微调<br><br>
          <strong>经验法则：</strong><br>
          • 简单任务（如格式调整）：r=8<br>
          • 中等任务（如对话）：r=16<br>
          • 复杂任务（如代码生成）：r=32"
        />

        <QuizBox
          question="Q6. LoRA通常应用在模型的哪些层？"
          :options="[
            '只应用在embedding层',
            '只应用在输出层',
            '主要应用在attention的Q、V矩阵',
            '应用在所有层'
          ]"
          :correctAnswer="2"
          explanation="<strong>主要应用在attention的Q和V矩阵！</strong><br><br>
          <strong>为什么选择attention层？</strong><br><br>
          1. <strong>参数量大</strong><br>
          • attention层占模型参数的60-70%<br>
          • 优化这里效果最明显<br><br>
          2. <strong>效果好</strong><br>
          • 实验表明Q、V矩阵对微调最敏感<br>
          • K矩阵和FFN层效果相对较弱<br><br>
          <strong>常见配置对比：</strong><br><br>
          <strong>最小配置（省资源）：</strong><br>
          • 只训练Q矩阵<br>
          • 参数量最少<br>
          • 效果略有损失<br><br>
          <strong>标准配置（推荐）：</strong><br>
          • 训练Q和V矩阵<br>
          • 效果和资源的最佳平衡<br>
          • 大多数情况的首选<br><br>
          <strong>完整配置（效果最好）：</strong><br>
          • 训练Q、K、V、O矩阵<br>
          • 有时也包括FFN层<br>
          • 参数量增加，但仍远小于全参数<br><br>
          <strong>实现示例：</strong><br>
          <code>target_modules = ['q_proj', 'v_proj']  # 标准配置</code>"
        />

        <QuizBox
          question="Q7. LoRA的α（alpha）参数的作用是什么？"
          :options="[
            '控制rank的大小',
            '缩放LoRA输出的影响力',
            '学习率的倍数',
            '正则化系数'
          ]"
          :correctAnswer="1"
          explanation="<strong>α用于缩放LoRA的输出！</strong><br><br>
          <strong>数学表达：</strong><br>
          输出 = W₀×x + (α/r)×ΔW×x<br>
          其中ΔW = B×A<br><br>
          <strong>为什么需要α？</strong><br><br>
          <strong>1. 稳定训练</strong><br>
          • 不同的r值会导致输出尺度差异<br>
          • α/r进行归一化，保持稳定<br><br>
          <strong>2. 控制LoRA影响力</strong><br>
          • α大 → LoRA影响强<br>
          • α小 → LoRA影响弱<br>
          • 默认α=16时影响适中<br><br>
          <strong>典型配置：</strong><br>
          • r=8, α=16 → 缩放系数=2<br>
          • r=16, α=32 → 缩放系数=2<br>
          • r=32, α=64 → 缩放系数=2<br><br>
          <strong>经验法则：</strong><br>
          α通常设为r的2倍（α=2r），这样缩放系数恒为2，训练更稳定。<br><br>
          <strong>实际影响：</strong><br>
          • α太小：LoRA学不到东西<br>
          • α太大：可能破坏原模型<br>
          • α=2r：经过验证的好选择"
        />
      </div>
    </section>

    <!-- 形象类比集合 -->
    <section class="my-12">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">理解LoRA的多个类比</h2>
      
      <div class="grid md:grid-cols-2 gap-6">
        <AnalogyBox icon="🔌" title="类比1：电源适配器">
          <ul class="space-y-2">
            <li>🏠 <strong>墙上插座</strong> = 预训练LLM（固定不变）</li>
            <li>📱 <strong>新电器插头</strong> = 特定任务需求</li>
            <li>🔌 <strong>转换插头</strong> = LoRA适配器（小巧、可更换）</li>
          </ul>
          <p class="mt-3 font-semibold">
            没有改变墙上的插座，却让设备完美工作！
          </p>
        </AnalogyBox>

        <AnalogyBox icon="📝" title="类比2：备考小抄">
          <ul class="space-y-2">
            <li>📚 <strong>整本教科书</strong> = 预训练知识（海量信息）</li>
            <li>📄 <strong>浓缩小抄</strong> = LoRA适配器（关键要点）</li>
          </ul>
          <p class="mt-3 font-semibold">
            不需要重写教科书，只要一张小小的备忘录！
          </p>
        </AnalogyBox>

        <AnalogyBox icon="💡" title="类比3：聚光灯滤色片">
          <ul class="space-y-2">
            <li>💡 <strong>白色聚光灯</strong> = 预训练模型（强大基础）</li>
            <li>🎨 <strong>彩色滤光片</strong> = LoRA适配器（改变输出特性）</li>
          </ul>
          <p class="mt-3 font-semibold">
            无需重造灯具，只需一张滤色片就能改变光的颜色！
          </p>
        </AnalogyBox>

        <AnalogyBox icon="🎭" title="类比4：演员的角色面具">
          <ul class="space-y-2">
            <li>🎭 <strong>演员本人</strong> = 预训练模型（核心能力）</li>
            <li>🎨 <strong>角色面具/服装</strong> = LoRA适配器（角色特性）</li>
          </ul>
          <p class="mt-3 font-semibold">
            演员不需要改变自己，只需换上不同的面具扮演不同角色！
          </p>
        </AnalogyBox>
      </div>
    </section>

    <!-- 对比表格 -->
    <ComparisonTable
      title="全量微调 vs LoRA：性能对比"
      :headers="['维度', '全量微调', 'LoRA (PEFT)']"
      :rows="comparisonRows"
    />

    <!-- 参数规模可视化 -->
    <div class="my-8">
      <h3 class="text-2xl font-bold text-gray-800 mb-4">参数规模对比</h3>
      <div class="card">
        <div class="mb-6">
          <label class="block text-sm font-semibold text-gray-700 mb-2">选择模型规模：</label>
          <select 
            v-model="selectedModelSize" 
            class="px-4 py-2 border-2 border-gray-300 rounded-lg focus:border-blue-500 focus:outline-none"
          >
            <option value="7B">7B 参数模型</option>
            <option value="13B">13B 参数模型</option>
            <option value="70B">70B 参数模型</option>
          </select>
        </div>

        <div class="space-y-6">
          <!-- 线性刻度对比 -->
          <div>
            <div class="flex justify-between items-center mb-2">
              <span class="font-semibold text-blue-700">全量微调训练参数</span>
              <span class="text-lg font-bold">{{ formatNumber(loraData.full_finetuning?.trainable_params) }}</span>
            </div>
            <div class="w-full bg-gray-200 rounded-full h-8">
              <div class="bg-gradient-to-r from-blue-500 to-blue-600 h-8 rounded-full flex items-center justify-end px-3" style="width: 100%">
                <span class="text-white text-sm font-bold">100%</span>
              </div>
            </div>
          </div>

          <div>
            <div class="flex justify-between items-center mb-2">
              <span class="font-semibold text-green-700">LoRA训练参数（实际比例）</span>
              <span class="text-lg font-bold">{{ formatNumber(loraData.lora?.trainable_params) }}</span>
            </div>
            <div class="w-full bg-gray-200 rounded-full h-8">
              <div 
                class="bg-gradient-to-r from-green-500 to-green-600 h-8 rounded-full transition-all duration-500 flex items-center px-2" 
                :style="{ width: loraPercentage + '%' }"
              >
                <span class="text-white text-xs font-bold whitespace-nowrap">{{ loraPercentage.toFixed(3) }}%</span>
              </div>
            </div>
            <p class="text-xs text-gray-500 mt-1">⚠️ 太小了，几乎看不见！让我们用对数刻度重新展示...</p>
          </div>

          <!-- 对数刻度对比 -->
          <div class="bg-gradient-to-r from-indigo-50 to-purple-50 p-6 rounded-xl">
            <h4 class="font-bold text-gray-800 mb-4 flex items-center">
              <span class="text-2xl mr-2">📊</span>
              对数刻度可视化（更直观）
            </h4>
            
            <div class="space-y-4">
              <div>
                <div class="flex justify-between items-center mb-2">
                  <span class="font-semibold text-blue-700">全量微调</span>
                  <span class="text-sm font-bold">{{ formatNumber(loraData.full_finetuning?.trainable_params) }} 参数</span>
                </div>
                <div class="w-full bg-gray-200 rounded-full h-10 relative">
                  <div class="bg-gradient-to-r from-blue-500 to-blue-700 h-10 rounded-full flex items-center justify-center" style="width: 100%">
                    <span class="text-white font-bold">10¹⁰ (百亿级)</span>
                  </div>
                </div>
              </div>

              <div>
                <div class="flex justify-between items-center mb-2">
                  <span class="font-semibold text-green-700">LoRA</span>
                  <span class="text-sm font-bold">{{ formatNumber(loraData.lora?.trainable_params) }} 参数</span>
                </div>
                <div class="w-full bg-gray-200 rounded-full h-10 relative">
                  <div class="bg-gradient-to-r from-green-500 to-green-700 h-10 rounded-full flex items-center justify-center" style="width: 25%">
                    <span class="text-white font-bold text-sm">10⁶ (百万级)</span>
                  </div>
                </div>
              </div>
            </div>

            <div class="mt-4 bg-white p-4 rounded-lg">
              <p class="text-sm text-gray-700">
                💡 <strong>解释</strong>：在对数刻度上，每一个数量级差距用25%的长度表示。
                全量微调是10¹⁰级别（百亿），LoRA是10⁶级别（百万），相差约<strong>4个数量级（10,000倍）</strong>！
              </p>
            </div>
          </div>

          <div class="bg-purple-50 p-6 rounded-lg border-2 border-purple-200">
            <p class="text-2xl text-center mb-3">
              <strong class="text-purple-700">LoRA仅需训练 {{ loraPercentage.toFixed(3) }}% 的参数！</strong>
            </p>
            <p class="text-center text-gray-700 text-lg">
              节省了 <strong class="text-purple-600">{{ (100 - loraPercentage).toFixed(2) }}%</strong> 的训练成本
            </p>
            <div class="mt-4 grid grid-cols-3 gap-4 text-center">
              <div class="bg-white p-3 rounded-lg">
                <p class="text-3xl font-bold text-purple-600">{{ (loraData.full_finetuning?.trainable_params / loraData.lora?.trainable_params).toFixed(0) }}x</p>
                <p class="text-xs text-gray-600 mt-1">参数减少倍数</p>
              </div>
              <div class="bg-white p-3 rounded-lg">
                <p class="text-3xl font-bold text-green-600">3.8x</p>
                <p class="text-xs text-gray-600 mt-1">内存节省</p>
              </div>
              <div class="bg-white p-3 rounded-lg">
                <p class="text-3xl font-bold text-blue-600">100x</p>
                <p class="text-xs text-gray-600 mt-1">速度提升</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 参数对比详细代码 -->
    <CodeBlock
      title="多模型规模参数量对比分析"
      file-path="code/part2/03_parameter_comparison.py"
      language="Python"
      :runnable="true"
      description="详细对比7B/13B/30B/70B模型的参数量、内存需求、存储空间，并生成可视化图表"
      :code="`# 参数对比分析器
class ParameterComparison:
    def __init__(self):
        self.model_sizes = {
            '7B': 7_000_000_000,
            '13B': 13_000_000_000,
            '70B': 70_000_000_000
        }
        self.lora_config = {
            'rank': 8,
            'num_layers': 32,
            'dim': 4096
        }
    
    def calculate_lora_params(self, model_size_name):
        total_params = self.model_sizes[model_size_name]
        
        # 每层LoRA: (d*r) + (r*d) = 2*d*r
        params_per_layer = 2 * self.lora_config['dim'] * self.lora_config['rank']
        total_lora_params = params_per_layer * self.lora_config['num_layers']
        
        ratio = (total_lora_params / total_params) * 100
        
        print(f'{model_size_name}模型:')
        print(f'  全量微调: {total_params:,} 参数')
        print(f'  LoRA:     {total_lora_params:,} 参数')
        print(f'  训练比例: {ratio:.3f}%')
        print(f'  减少倍数: {total_params/total_lora_params:.0f}x')
        return {
            '全量': total_params,
            'LoRA': total_lora_params,
            '比例': ratio
        }

comparator = ParameterComparison()
for model in ['7B', '13B', '70B']:
    comparator.calculate_lora_params(model)

# 输出示例：
# 7B模型: 减少 3,333x
# 13B模型: 减少 6,166x
# 70B模型: 减少 33,333x`"
    />

    <!-- 可组合的AI技能 -->
    <section class="my-12">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">革命性架构：可组合的AI技能</h2>
      
      <div class="card bg-gradient-to-br from-indigo-50 to-purple-50">
        <div class="flex items-start space-x-4">
          <div class="text-5xl">🎯</div>
          <div class="flex-1">
            <h3 class="text-2xl font-bold text-indigo-800 mb-4">中心辐射型（Hub-and-Spoke）模型</h3>
            <p class="text-lg text-gray-700 mb-4">
              由于LoRA适配器非常小且独立，我们可以训练出许多针对不同任务的适配器，
              形成一个强大的中央基座模型，可以根据需要动态地加载、卸载甚至组合这些轻量级的"技能模块"。
            </p>
          </div>
        </div>

        <AnimatedIllustration 
          description="一个基座模型 + 多个可插拔的LoRA技能模块"
        >
          <div class="w-full max-w-4xl">
            <div class="flex items-center justify-center">
              <!-- 中心基座模型 -->
              <div class="relative">
                <div class="text-8xl">🧠</div>
                <p class="text-center font-bold text-gray-700 mt-2">基座模型</p>
                
                <!-- 周围的LoRA适配器 -->
                <div class="absolute -top-16 -left-16">
                  <div class="text-3xl">📧</div>
                  <p class="text-xs">邮件总结</p>
                </div>
                <div class="absolute -top-16 -right-16">
                  <div class="text-3xl">💻</div>
                  <p class="text-xs">代码生成</p>
                </div>
                <div class="absolute -bottom-16 -left-16">
                  <div class="text-3xl">✍️</div>
                  <p class="text-xs">创意写作</p>
                </div>
                <div class="absolute -bottom-16 -right-16">
                  <div class="text-3xl">🗄️</div>
                  <p class="text-xs">SQL查询</p>
                </div>
              </div>
            </div>
          </div>
        </AnimatedIllustration>

        <div class="mt-6 space-y-3">
          <InfoCard icon="💰" title="降低基础设施成本" variant="success">
            <p>不需要为每个任务保存完整模型，只需保存小小的适配器文件（几MB vs 几GB）</p>
          </InfoCard>
          <InfoCard icon="🔄" title="动态专业化能力" variant="success">
            <p>可以在运行时快速切换不同的LoRA模块，让模型瞬间转换专业领域</p>
          </InfoCard>
          <InfoCard icon="🎨" title="可插拔AI能力" variant="success">
            <p>将模型从静态工具转变为支持"可插拔"AI能力的动态平台</p>
          </InfoCard>
        </div>
      </div>

      <!-- Hub-and-Spoke架构代码演示 -->
      <CodeBlock
        title="Hub-and-Spoke多任务架构实现"
        file-path="code/part2/04_lora_adapters_demo.py"
        language="Python"
        :runnable="true"
        description="演示如何用一个基座模型+多个LoRA适配器构建多任务系统，实现快速任务切换"
        :code="`# Hub-and-Spoke架构演示
class BaseModel:
    '''基座模型（冻结）'''
    def __init__(self, model_size='7B'):
        self.name = f'LLaMA-2-{model_size}'
        print(f'✅ 加载基座模型: {self.name}')
        print(f'   状态: 🔒 完全冻结')

class LoRAAdapter:
    '''LoRA适配器'''
    def __init__(self, name, task, rank=8):
        self.name = name
        self.task = task
        self.params = 4096 * rank * 2  # A和B矩阵
        print(f'  📦 创建适配器: {name}')
        print(f'     任务: {task}, 参数: {self.params:,}')
    
    def get_storage_size(self):
        return (self.params * 2) / (1024**2)  # FP16, MB

class MultiTaskModel:
    '''多任务模型系统'''
    def __init__(self, base_model):
        self.base_model = base_model
        self.adapters = {}
        self.current_adapter = None
    
    def add_adapter(self, adapter):
        self.adapters[adapter.name] = adapter
        print(f'✅ 已添加: {adapter.name}')
    
    def switch_adapter(self, name):
        self.current_adapter = self.adapters[name]
        print(f'🔄 切换到: {name}')

# 创建系统
base = BaseModel('7B')
system = MultiTaskModel(base)

# 添加多个适配器
adapters = [
    LoRAAdapter('email_summary', '邮件总结', rank=8),
    LoRAAdapter('code_gen', 'Python代码生成', rank=16),
    LoRAAdapter('sql_query', 'SQL查询生成', rank=8),
]

for adapter in adapters:
    system.add_adapter(adapter)

# 快速切换任务
system.switch_adapter('code_gen')
system.switch_adapter('sql_query')

# 输出示例：
# ✅ 加载基座: LLaMA-2-7B (13 GB)
# 📦 邮件总结适配器 (4 MB)
# 📦 代码生成适配器 (8 MB)
# 🔄 任务切换 < 1秒`"
      />

      <!-- 📝 LoRA优势与应用测验 -->
      <div class="my-8 space-y-4">
        <div class="flex items-center space-x-3 mb-6">
          <span class="text-4xl">🧠</span>
          <h3 class="text-2xl font-bold text-indigo-700">即学即测：LoRA的优势与应用</h3>
        </div>

        <QuizBox
          question="Q8. 相比全参数微调，LoRA的训练速度如何？"
          :options="[
            '慢很多（因为多了矩阵分解）',
            '差不多',
            '快1.5-3倍',
            '快10倍以上'
          ]"
          :correctAnswer="2"
          explanation="<strong>LoRA训练速度快1.5-3倍！</strong><br><br>
          <strong>为什么更快？</strong><br><br>
          <strong>1. 反向传播计算量少</strong><br>
          • 只计算0.1-1%参数的梯度<br>
          • 其余99%参数冻结，不计算梯度<br>
          • 反向传播时间减少30-50%<br><br>
          <strong>2. 优化器更新快</strong><br>
          • Adam需要更新的参数少<br>
          • momentum和variance状态也少<br>
          • 优化器步骤快50-70%<br><br>
          <strong>3. 显存占用少，可以用更大batch</strong><br>
          • 全参数：batch_size=2（受显存限制）<br>
          • LoRA：batch_size=8（显存够用）<br>
          • 更大batch → 训练更快收敛<br><br>
          <strong>实际测试（7B模型，单A100）：</strong><br>
          • 全参数微调：2.5小时/epoch<br>
          • LoRA微调：1.0小时/epoch<br>
          • <strong>快2.5倍！</strong><br><br>
          <strong>注意：</strong>前向传播时间基本不变（都要过完整模型），主要节省在反向传播和优化器更新。"
        />

        <QuizBox
          question="Q9. 如何合并(merge)多个LoRA适配器？"
          :options="[
            '不能合并，只能分开使用',
            '可以直接加权平均合并到基座模型',
            '需要重新训练',
            '合并后会丢失所有能力'
          ]"
          :correctAnswer="1"
          explanation="<strong>可以直接加权平均合并到基座模型！</strong><br><br>
          <strong>合并原理：</strong><br><br>
          <strong>数学表达：</strong><br>
          • LoRA输出：W' = W₀ + ΔW = W₀ + B×A<br>
          • 合并后：W_new = W₀ + α×(B×A)<br>
          • α是缩放系数，控制影响力<br><br>
          <strong>合并步骤：</strong><br><br>
          1. <strong>加载基座模型</strong><br>
          2. <strong>加载LoRA权重</strong><br>
          3. <strong>计算ΔW = B×A</strong><br>
          4. <strong>合并：W_new = W₀ + ΔW</strong><br>
          5. <strong>保存新模型</strong><br><br>
          <strong>优点：</strong><br>
          • 推理时无额外计算<br>
          • 与原模型推理速度完全相同<br>
          • 可以部署到不支持LoRA的环境<br><br>
          <strong>缺点：</strong><br>
          • 占用空间变大（需要保存完整模型）<br>
          • 失去了任务切换的灵活性<br><br>
          <strong>实现示例（PyTorch）：</strong><br>
          <code>
          model = PeftModel.from_pretrained(base_model, lora_path)<br>
          merged_model = model.merge_and_unload()<br>
          merged_model.save_pretrained('merged_model')
          </code>"
        />

        <QuizBox
          question="Q10. 关于LoRA的存储大小，以下哪个说法正确？"
          :options="[
            '一个7B模型的LoRA通常需要14GB',
            '一个7B模型的LoRA通常需要2-50MB',
            '一个7B模型的LoRA通常需要500MB-2GB',
            'LoRA大小与基座模型相同'
          ]"
          :correctAnswer="1"
          explanation="<strong>一个7B模型的LoRA通常只需要2-50MB！</strong><br><br>
          <strong>为什么这么小？</strong><br><br>
          <strong>计算实例（7B模型，r=16）：</strong><br><br>
          • 应用层数：32层 × 2矩阵(Q,V)<br>
          • 每个矩阵参数：4096×16 + 16×4096 = 131,072<br>
          • 总参数：32 × 2 × 131,072 = 8,388,608 ≈ 8.4M参数<br>
          • FP16存储：8.4M × 2字节 = 16.8MB<br><br>
          <strong>不同rank的大小对比：</strong><br><br>
          <strong>r=8（简单任务）：</strong><br>
          • 约4-8MB<br>
          • 适合格式调整、简单对话<br><br>
          <strong>r=16（标准配置）：</strong><br>
          • 约16-32MB<br>
          • 适合大多数SFT任务<br><br>
          <strong>r=32（复杂任务）：</strong><br>
          • 约32-64MB<br>
          • 适合代码生成、复杂推理<br><br>
          <strong>r=64（极限）：</strong><br>
          • 约64-128MB<br>
          • 很少使用，接近全参数微调<br><br>
          <strong>实际意义：</strong><br>
          • U盘就能装100个LoRA适配器！<br>
          • 可以轻松分享和版本管理<br>
          • 适合快速实验和迭代"
        />

        <QuizBox
          question="Q11. 【代码题】使用PEFT库初始化LoRA模型的正确顺序是？"
          :options="[
            '1. 加载LoRA配置 → 2. 加载基座模型 → 3. 应用LoRA',
            '1. 加载基座模型 → 2. 加载LoRA配置 → 3. 应用LoRA',
            '1. 应用LoRA → 2. 加载基座模型 → 3. 加载LoRA配置',
            '1. 加载LoRA配置 → 2. 应用LoRA → 3. 加载基座模型'
          ]"
          :correctAnswer="1"
          explanation="<strong>正确顺序：先加载基座模型，再配置LoRA，最后应用！</strong><br><br>
          <strong>完整代码示例：</strong><br>
          <pre><code>from transformers import AutoModelForCausalLM
from peft import LoraConfig, get_peft_model

# 步骤1: 加载基座模型
base_model = AutoModelForCausalLM.from_pretrained(
    'meta-llama/Llama-2-7b-hf',
    torch_dtype=torch.float16,
    device_map='auto'
)

# 步骤2: 配置LoRA参数
lora_config = LoraConfig(
    r=16,                          # rank
    lora_alpha=32,                 # alpha = 2*r
    target_modules=['q_proj', 'v_proj'],  # 目标层
    lora_dropout=0.05,
    bias='none',
    task_type='CAUSAL_LM'
)

# 步骤3: 应用LoRA到基座模型
model = get_peft_model(base_model, lora_config)

# 查看可训练参数
model.print_trainable_parameters()
# 输出: trainable params: 4,194,304 || all params: 6,742,609,920 || trainable%: 0.06%</code></pre><br><br>
          <strong>为什么是这个顺序？</strong><br><br>
          1. <strong>必须先有基座模型</strong><br>
          • LoRA是在现有模型上添加适配器<br>
          • 没有基座模型，LoRA无从附着<br><br>
          2. <strong>配置要在应用前完成</strong><br>
          • LoraConfig定义了要修改哪些层<br>
          • get_peft_model根据配置插入LoRA层<br><br>
          3. <strong>应用后才能训练</strong><br>
          • get_peft_model返回的是包装后的模型<br>
          • 这个模型已经冻结了原始参数，只训练LoRA参数<br><br>
          <strong>常见错误：</strong><br>
          • ❌ 先配置LoRA再加载模型：会报错找不到模型<br>
          • ❌ 直接在基座模型上训练：变成了全参数微调！"
        />

        <QuizBox
          question="Q12. 【代码题】LoRA训练循环中，正确的执行顺序是？"
          :options="[
            '1. forward → 2. loss.backward() → 3. optimizer.step() → 4. optimizer.zero_grad()',
            '1. forward → 2. optimizer.zero_grad() → 3. loss.backward() → 4. optimizer.step()',
            '1. optimizer.zero_grad() → 2. forward → 3. loss.backward() → 4. optimizer.step()',
            '1. optimizer.step() → 2. forward → 3. loss.backward() → 4. optimizer.zero_grad()'
          ]"
          :correctAnswer="2"
          explanation="<strong>正确顺序：清零梯度 → 前向传播 → 反向传播 → 更新参数！</strong><br><br>
          <strong>完整训练循环代码：</strong><br>
          <pre><code>from transformers import Trainer, TrainingArguments
import torch

# 训练配置
training_args = TrainingArguments(
    output_dir='./lora_output',
    num_train_epochs=3,
    per_device_train_batch_size=4,
    learning_rate=2e-4,
    logging_steps=10
)

# 标准PyTorch训练循环（手动版）
for epoch in range(num_epochs):
    model.train()
    for batch in train_dataloader:
        # 步骤1: 清零上一步的梯度（重要！）
        optimizer.zero_grad()
        
        # 步骤2: 前向传播
        outputs = model(
            input_ids=batch['input_ids'],
            attention_mask=batch['attention_mask'],
            labels=batch['labels']
        )
        loss = outputs.loss
        
        # 步骤3: 反向传播，计算梯度
        loss.backward()
        
        # 步骤4: 根据梯度更新参数
        optimizer.step()
        
        # 可选: 学习率调度
        scheduler.step()
        
# 使用Trainer的简化版本（推荐）
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    data_collator=data_collator,
)
trainer.train()  # 自动处理上述所有步骤！</code></pre><br><br>
          <strong>为什么是这个顺序？</strong><br><br>
          <strong>1. optimizer.zero_grad() 在最前</strong><br>
          • PyTorch默认会<strong>累积梯度</strong><br>
          • 如果不清零，新梯度会叠加到旧梯度上<br>
          • 结果：梯度爆炸，训练失败<br><br>
          <strong>2. forward（前向传播）</strong><br>
          • 输入数据通过模型<br>
          • 得到预测结果和loss<br>
          • 此时还没有梯度<br><br>
          <strong>3. loss.backward()（反向传播）</strong><br>
          • 根据loss计算每个参数的梯度<br>
          • 梯度存储在param.grad中<br>
          • LoRA：只有可训练参数有梯度！<br><br>
          <strong>4. optimizer.step()（参数更新）</strong><br>
          • 根据梯度更新参数<br>
          • θ_new = θ_old - lr × grad<br>
          • 完成一次优化步骤<br><br>
          <strong>常见错误：</strong><br>
          • ❌ 忘记zero_grad()：梯度累积导致训练不稳定<br>
          • ❌ step()在backward()前：没有梯度，参数不更新<br>
          • ❌ backward()在forward()前：没有loss，无法反向传播"
        />
      </div>
    </section>

    <!-- Part2 总结 -->
    <section class="my-16">
      <div class="card bg-gradient-to-br from-purple-600 to-pink-600 text-white p-8">
        <h2 class="text-4xl font-bold mb-4 flex items-center">
          <span class="text-5xl mr-4">🎉</span>
          恭喜完成Part2学习！
        </h2>
        <p class="text-xl opacity-90 mb-6">你已经掌握了LoRA高效微调的核心技术</p>
        
        <div class="grid md:grid-cols-3 gap-6 mt-8">
          <div class="bg-white bg-opacity-20 backdrop-blur p-5 rounded-xl">
            <div class="text-4xl mb-3">💾</div>
            <p class="font-bold text-lg mb-2">资源节省</p>
            <p class="text-sm opacity-90">显存减少75%，存储减少99%</p>
          </div>
          <div class="bg-white bg-opacity-20 backdrop-blur p-5 rounded-xl">
            <div class="text-4xl mb-3">⚡</div>
            <p class="font-bold text-lg mb-2">训练加速</p>
            <p class="text-sm opacity-90">速度提升1.5-3倍</p>
          </div>
          <div class="bg-white bg-opacity-20 backdrop-blur p-5 rounded-xl">
            <div class="text-4xl mb-3">🔧</div>
            <p class="font-bold text-lg mb-2">灵活部署</p>
            <p class="text-sm opacity-90">一个基座+多个适配器</p>
          </div>
        </div>

        <div class="mt-8 bg-white bg-opacity-30 backdrop-blur p-6 rounded-xl">
          <p class="text-lg font-bold mb-3">💡 核心要点回顾：</p>
          <ul class="space-y-2 text-sm">
            <li>• LoRA通过低秩矩阵分解大幅减少可训练参数</li>
            <li>• rank和alpha是两个关键超参数</li>
            <li>• 主要应用于attention层的Q、V矩阵</li>
            <li>• 可以轻松合并、组合和切换适配器</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- 导航 -->
    <div class="flex justify-between mt-16">
      <router-link to="/part1" class="btn-secondary">
        ← 上一部分
      </router-link>
      <router-link to="/part3" class="btn-primary">
        下一部分：SFT数据集 →
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import axios from 'axios'
import AnalogyBox from '../components/AnalogyBox.vue'
import AnimatedIllustration from '../components/AnimatedIllustration.vue'
import InfoCard from '../components/InfoCard.vue'
import ComparisonTable from '../components/ComparisonTable.vue'
import QuizBox from '../components/QuizBox.vue'
import CodeBlock from '../components/CodeBlock.vue'
import LoRAVisualization from '../components/LoRAVisualization.vue'
import LoRAMathExplanation from '../components/LoRAMathExplanation.vue'

const selectedModelSize = ref('7B')
const loraData = ref({})

const comparisonRows = [
  {
    label: '训练的参数量',
    values: ['全部（例如70亿）', { text: '极小一部分（<0.1%）', highlight: true }]
  },
  {
    label: '内存/显存占用',
    values: [{ text: '非常高（需要多张专业级GPU）', highlight: true }, { text: '低（通常单张消费级GPU即可）', highlight: true }]
  },
  {
    label: '训练速度',
    values: ['慢', { text: '快', highlight: true }]
  },
  {
    label: '灾难性遗忘风险',
    values: [{ text: '高', highlight: true }, { text: '非常低（基座模型被冻结）', highlight: true }]
  },
  {
    label: '每个任务的存储',
    values: ['完整模型（如14GB）', { text: '微小适配器（如几MB）', highlight: true }]
  }
]

const loraPercentage = computed(() => {
  if (!loraData.value.lora || !loraData.value.full_finetuning) return 0.1
  return (loraData.value.lora.trainable_params / loraData.value.full_finetuning.trainable_params) * 100
})

const formatNumber = (num) => {
  if (!num) return '...'
  if (num >= 1e9) return (num / 1e9).toFixed(2) + 'B'
  if (num >= 1e6) return (num / 1e6).toFixed(2) + 'M'
  if (num >= 1e3) return (num / 1e3).toFixed(2) + 'K'
  return num.toString()
}

const fetchLoraData = async () => {
  try {
    const response = await axios.get(`/api/lora-comparison?model_size=${selectedModelSize.value}`)
    loraData.value = response.data
  } catch (error) {
    console.error('获取LoRA数据失败:', error)
  }
}

onMounted(() => {
  fetchLoraData()
})

watch(selectedModelSize, () => {
  fetchLoraData()
})
</script>
