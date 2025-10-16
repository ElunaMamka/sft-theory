<template>
  <div class="part1-page">
    <!-- 标题 -->
    <h1 class="section-title">第一部分：现代LLM的"两阶段"成长之旅</h1>

    <!-- 引言 -->
    <AnalogyBox icon="🎓" title="核心类比：大学毕业生的成长">
      <p>
        一个现代大型语言模型的诞生和成熟，就像一个人的教育历程：
      </p>
      <ul class="list-disc list-inside mt-2 space-y-1">
        <li><strong>预训练阶段</strong> = 大学通识教育（广泛学习，掌握基础知识）</li>
        <li><strong>SFT阶段</strong> = 专业实习培训（聚焦技能，胜任具体工作）</li>
      </ul>
    </AnalogyBox>

    <!-- 两阶段对比可视化 -->
    <AnimatedIllustration 
      title="LLM的两阶段成长"
      description="从知识宝库到实用助手的转变过程"
    >
      <div class="w-full max-w-4xl">
        <div class="flex items-center justify-around">
          <!-- 预训练阶段 -->
          <div class="text-center space-y-4 flex-1">
            <div class="text-7xl animate-pulse-slow">📚</div>
            <div class="card bg-blue-50 p-4">
              <h4 class="font-bold text-blue-700 mb-2">阶段一：预训练</h4>
              <p class="text-sm text-gray-600">通识教育</p>
            </div>
            <div class="text-sm space-y-1 text-gray-700">
              <p>💾 海量文本数据</p>
              <p>🧠 学习语言规律</p>
              <p>📖 积累世界知识</p>
            </div>
          </div>

          <!-- 箭头 -->
          <div class="text-5xl mx-8 text-blue-500">→</div>

          <!-- SFT阶段 -->
          <div class="text-center space-y-4 flex-1">
            <div class="text-7xl animate-pulse-slow">💼</div>
            <div class="card bg-purple-50 p-4">
              <h4 class="font-bold text-purple-700 mb-2">阶段二：SFT</h4>
              <p class="text-sm text-gray-600">专业培训</p>
            </div>
            <div class="text-sm space-y-1 text-gray-700">
              <p>🎯 精标注样本</p>
              <p>🤝 学习遵循指令</p>
              <p>✨ 塑造行为模式</p>
            </div>
          </div>
        </div>
      </div>
    </AnimatedIllustration>

    <!-- 第一阶段：预训练 -->
    <section class="my-12">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">第一阶段：奠定基础（预训练）</h2>
      
      <InfoCard icon="🏗️" title="预训练的目标" variant="info">
        <p>让模型学习人类语言的基本模式、语法结构、逻辑推理和海量的世界知识。</p>
        <p class="mt-2"><strong>核心任务</strong>：预测下一个词（因果语言建模 - CLM）</p>
      </InfoCard>

      <div class="grid md:grid-cols-2 gap-6 my-6">
        <InfoCard icon="📊" title="数据规模" variant="info">
          <ul class="list-disc list-inside space-y-1">
            <li>数据量：<strong>数万亿个词元</strong></li>
            <li>来源：维基百科、书籍、网站、代码库</li>
            <li>特点：未经人工标注的原始文本</li>
          </ul>
        </InfoCard>

        <InfoCard icon="💰" title="计算成本" variant="warning">
          <ul class="list-disc list-inside space-y-1">
            <li>GPU数量：<strong>成百上千张</strong></li>
            <li>训练时间：数周至数月</li>
            <li>总成本：<strong>数百万美元</strong></li>
          </ul>
        </InfoCard>
      </div>

      <AnalogyBox icon="🏫" title="形象类比：图书馆的自学">
        <p>
          预训练就像让一个学生独自在巨大的图书馆里自学。他阅读每一本书，尝试理解每个句子，
          预测下一个词。虽然没有老师指导，但通过海量的阅读，他掌握了语言的规律和世界的知识。
        </p>
        <p class="mt-2 font-semibold text-orange-600">
          这个过程是"自监督"的——数据本身就提供了学习信号！
        </p>
      </AnalogyBox>

      <div class="my-8">
        <InteractiveChart
          title="预训练损失曲线"
          description="模型在预训练过程中逐渐学习语言模式"
          :data="pretrainingChartData"
          type="line"
        />
      </div>
    </section>

    <!-- 第二阶段：SFT -->
    <section class="my-12">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">第二阶段：磨练技能（监督式微调）</h2>
      
      <InfoCard icon="🎯" title="SFT的目标" variant="success">
        <p>将基座模型改造为能够胜任特定、有用任务的工具，使其行为与用户意图对齐。</p>
        <p class="mt-2"><strong>核心任务</strong>：学习如何遵循指令、以特定方式响应</p>
      </InfoCard>

      <div class="grid md:grid-cols-2 gap-6 my-6">
        <InfoCard icon="📝" title="数据特点" variant="success">
          <ul class="list-disc list-inside space-y-1">
            <li>数据量：<strong>数百至数十万样本</strong></li>
            <li>格式：精心设计的"指令-响应"对</li>
            <li>特点：高质量、经过人工标注</li>
          </ul>
        </InfoCard>

        <InfoCard icon="⚡" title="资源优势" variant="success">
          <ul class="list-disc list-inside space-y-1">
            <li>成本：相对低廉（千-万美元级）</li>
            <li>时间：数小时至数天</li>
            <li><strong>个人开发者也能负担！</strong></li>
          </ul>
        </InfoCard>
      </div>

      <AnalogyBox icon="👔" title="形象类比：在职培训">
        <p>
          SFT就像公司为新员工提供的在职培训。虽然这位员工（基座模型）已经有扎实的知识基础，
          但还需要学习如何礼貌地与客户沟通、如何使用公司的工作流程、如何以专业的方式完成任务。
        </p>
        <p class="mt-2 font-semibold text-orange-600">
          培训师（人类专家）通过示范（标注数据）教会员工正确的工作方式！
        </p>
      </AnalogyBox>
    </section>

    <!-- 对比表格 -->
    <ComparisonTable
      title="预训练 vs SFT：关键区别"
      :headers="['维度', '预训练 (Pre-training)', 'SFT (Supervised Fine-Tuning)']"
      :rows="comparisonRows"
    />

    <!-- 关系说明 -->
    <section class="my-12">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">两阶段的共生关系</h2>
      
      <div class="card bg-gradient-to-br from-amber-50 to-orange-50 border-l-4 border-amber-500">
        <div class="flex items-start space-x-4">
          <div class="text-5xl">⚠️</div>
          <div class="flex-1">
            <h3 class="text-2xl font-bold text-amber-800 mb-4">单向依赖关系</h3>
            <div class="space-y-3 text-gray-700 text-lg">
              <p>
                <strong>✓ SFT依赖预训练</strong>：SFT的成功在根本上依赖于预训练阶段打下的坚实基础。
                一个优秀的预训练模型可以通过SFT变得更加出色。
              </p>
              <p>
                <strong>✗ 预训练不依赖SFT</strong>：即便是最完美的SFT数据集，也无法拯救一个预训练效果差的模型。
              </p>
              <p class="font-bold text-amber-700 bg-amber-100 p-3 rounded-lg">
                💡 关键洞察：SFT是在"解锁"和"引导"模型已有的潜力，而非从零创造潜力！
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SFT的真正作用 -->
    <section class="my-12">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">SFT的真正作用：塑造行为而非灌输知识</h2>
      
      <div class="grid md:grid-cols-2 gap-6">
        <InfoCard icon="❌" title="常见误解" variant="error">
          <p class="font-semibold">SFT的主要目的是向模型灌输新的事实知识</p>
          <p class="mt-2 text-sm">虽然可以在一定程度上补充知识，但这不是核心目标</p>
        </InfoCard>

        <InfoCard icon="✅" title="真实作用" variant="success">
          <p class="font-semibold">SFT的核心是塑造模型的行为模式</p>
          <ul class="list-disc list-inside mt-2 text-sm space-y-1">
            <li>遵循特定指令格式</li>
            <li>采纳某种语气或人格</li>
            <li>以期望的结构生成输出</li>
          </ul>
        </InfoCard>
      </div>

      <div class="card my-6 bg-gradient-to-br from-green-50 to-emerald-50">
        <h3 class="text-2xl font-bold text-green-800 mb-4">SFT的核心价值</h3>
        <div class="text-lg text-gray-700 space-y-3">
          <p>
            预训练教会了模型<strong>语言的规律</strong>和<strong>世界的事实</strong>
          </p>
          <p class="text-3xl text-center my-4">↓</p>
          <p>
            SFT教会模型<strong>如何应用这些知识</strong>
          </p>
          <div class="bg-white p-4 rounded-lg mt-4">
            <p class="font-semibold text-green-700">实际应用示例：</p>
            <ul class="list-disc list-inside mt-2 space-y-1">
              <li>调整模型的语气、正式程度或品牌声调</li>
              <li>确保输出符合特定格式（如JSON、聊天模板）</li>
              <li>教会模型特定的推理步骤展示方式</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- 测验 -->
    <QuizBox
      question="为什么说SFT不能拯救一个预训练效果差的模型？"
      :options="[
        'SFT的数据量太小，无法弥补预训练的不足',
        'SFT主要是塑造行为，而非从零创造知识和能力',
        'SFT的成本太高，不值得在差模型上使用',
        'SFT会导致模型遗忘预训练知识'
      ]"
      :correctAnswer="1"
      explanation="SFT的作用是解锁和引导模型已有的潜力，塑造其行为模式。如果预训练阶段没有建立好知识基础和语言理解能力，SFT就像在沙滩上建房子——缺乏坚实的地基，再好的装修也无济于事。"
    />

    <!-- 导航 -->
    <div class="flex justify-between mt-16">
      <router-link to="/" class="btn-secondary">
        ← 返回首页
      </router-link>
      <router-link to="/part2" class="btn-primary">
        下一部分：LoRA高效微调 →
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
import ComparisonTable from '../components/ComparisonTable.vue'
import InteractiveChart from '../components/InteractiveChart.vue'
import QuizBox from '../components/QuizBox.vue'

const comparisonRows = [
  {
    label: '主要目标',
    values: ['学习通用的语言规律、事实知识和推理能力', '适应特定任务；与用户意图对齐']
  },
  {
    label: '数据类型',
    values: ['未经标注的原始文本', '经过标注的、高质量的"指令-响应"对']
  },
  {
    label: '数据规模',
    values: [{ text: '巨大（万亿级词元）', highlight: true }, { text: '较小（数百至数十万样本）', highlight: true }]
  },
  {
    label: '学习方法',
    values: ['自监督学习（如：预测下一个词）', '监督学习（从"正确范例"中学习）']
  },
  {
    label: '计算成本',
    values: [{ text: '极其高昂（数百万美元级别）', highlight: true }, { text: '相对低廉，易于获取', highlight: true }]
  },
  {
    label: '最终产出',
    values: ['通用型"基座模型"', '专用型、遵循指令的"助手模型"']
  }
]

const pretrainingChartData = ref({
  labels: [],
  datasets: []
})

onMounted(async () => {
  try {
    const response = await axios.get('/api/generate-training-curve?epochs=20')
    const data = response.data
    
    pretrainingChartData.value = {
      labels: data.pretrain.x.map((_, i) => i % 20 === 0 ? `Epoch ${Math.floor(i / 10)}` : ''),
      datasets: [
        {
          label: '预训练损失',
          data: data.pretrain.y,
          borderColor: 'rgb(59, 130, 246)',
          backgroundColor: 'rgba(59, 130, 246, 0.1)',
          tension: 0.4
        }
      ]
    }
  } catch (error) {
    console.error('获取数据失败:', error)
    // 使用模拟数据
    const epochs = Array.from({ length: 200 }, (_, i) => i)
    const loss = epochs.map(e => 4.0 * Math.exp(-0.3 * e / 10) + 0.5)
    
    pretrainingChartData.value = {
      labels: epochs.map((_, i) => i % 20 === 0 ? `Epoch ${Math.floor(i / 10)}` : ''),
      datasets: [
        {
          label: '预训练损失',
          data: loss,
          borderColor: 'rgb(59, 130, 246)',
          backgroundColor: 'rgba(59, 130, 246, 0.1)',
          tension: 0.4
        }
      ]
    }
  }
})
</script>

