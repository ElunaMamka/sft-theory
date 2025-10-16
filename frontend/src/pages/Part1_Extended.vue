<template>
  <div class="part1-page">
    <!-- 标题 -->
    <h1 class="section-title">第一部分：现代LLM的"两阶段"成长之旅</h1>

    <!-- 引言部分 - 扩充 -->
    <div class="card bg-gradient-to-br from-indigo-50 to-purple-50 mb-8">
      <div class="flex items-start space-x-6">
        <div class="text-8xl">🎓</div>
        <div class="flex-1">
          <h2 class="text-3xl font-bold text-indigo-800 mb-4">AI也需要"教育"</h2>
          <p class="text-lg text-gray-700 leading-relaxed mb-3">
            想象一下，一个大型语言模型（LLM）就像一位才华横溢的<strong class="text-indigo-700">大学毕业生</strong>。
            这位毕业生博览群书，通晓古今，几乎阅读了图书馆里的每一本书，掌握了海量的通用知识。
          </p>
          <p class="text-lg text-gray-700 leading-relaxed mb-3">
            然而，尽管他知识渊博，却没有丝毫实际工作经验。他不知道如何礼貌地回答客户的服务咨询，
            也不懂得如何精准地总结一份法律文件。<strong class="text-indigo-700">他拥有巨大的潜力，但尚未具备将其应用于特定任务的能力</strong>。
          </p>
          <p class="text-lg text-gray-700 leading-relaxed bg-indigo-100 p-4 rounded-lg">
            <strong class="text-indigo-800">监督式微调（SFT）</strong>正是将这位"通才毕业生"转变为"领域专家"的桥梁——
            相当于一套专门的<strong>在职培训体系</strong>！
          </p>
        </div>
      </div>
    </div>

    <!-- 核心类比可视化 -->
    <AnalogyBox icon="🎓" title="核心类比：从学生到职场精英的旅程">
      <div class="grid md:grid-cols-2 gap-6 mt-4">
        <div class="bg-blue-50 p-4 rounded-lg">
          <h4 class="font-bold text-blue-800 mb-3 flex items-center">
            <span class="text-2xl mr-2">📚</span>
            预训练 = 大学教育
          </h4>
          <ul class="space-y-2 text-gray-700">
            <li class="flex items-start">
              <span class="text-blue-500 mr-2">•</span>
              <span>阅读海量教材（网络文本）</span>
            </li>
            <li class="flex items-start">
              <span class="text-blue-500 mr-2">•</span>
              <span>学习各学科基础知识</span>
            </li>
            <li class="flex items-start">
              <span class="text-blue-500 mr-2">•</span>
              <span>培养通用思维能力</span>
            </li>
            <li class="flex items-start">
              <span class="text-blue-500 mr-2">•</span>
              <span>但缺乏实践经验</span>
            </li>
          </ul>
        </div>

        <div class="bg-purple-50 p-4 rounded-lg">
          <h4 class="font-bold text-purple-800 mb-3 flex items-center">
            <span class="text-2xl mr-2">💼</span>
            SFT = 在职培训
          </h4>
          <ul class="space-y-2 text-gray-700">
            <li class="flex items-start">
              <span class="text-purple-500 mr-2">•</span>
              <span>师傅示范（高质量样本）</span>
            </li>
            <li class="flex items-start">
              <span class="text-purple-500 mr-2">•</span>
              <span>学习专业技能和流程</span>
            </li>
            <li class="flex items-start">
              <span class="text-purple-500 mr-2">•</span>
              <span>掌握公司文化和风格</span>
            </li>
            <li class="flex items-start">
              <span class="text-purple-500 mr-2">•</span>
              <span>成为岗位专家</span>
            </li>
          </ul>
        </div>
      </div>
    </AnalogyBox>

    <!-- 两阶段对比大型可视化 -->
    <AnimatedIllustration 
      title="LLM的完整成长路径"
      description="从原始文本到智能助手的蜕变"
    >
      <div class="w-full max-w-6xl">
        <div class="grid md:grid-cols-3 gap-8 items-center">
          <!-- 原始数据 -->
          <div class="text-center space-y-4">
            <div class="text-7xl">📄</div>
            <div class="card bg-gray-50 p-4">
              <h4 class="font-bold text-gray-700 mb-2">原始状态</h4>
              <p class="text-sm text-gray-600">海量文本数据</p>
            </div>
            <div class="text-xs space-y-1 text-gray-600">
              <p>维基百科</p>
              <p>书籍语料</p>
              <p>网页内容</p>
              <p>代码仓库</p>
            </div>
          </div>

          <div class="space-y-6">
            <!-- 预训练箭头 -->
            <div class="text-center">
              <div class="text-4xl text-blue-500 mb-2">↓</div>
              <div class="bg-blue-100 p-3 rounded-lg">
                <p class="font-bold text-blue-800">预训练</p>
                <p class="text-xs text-blue-600">自监督学习</p>
              </div>
              <div class="text-center space-y-3 mt-3">
                <div class="text-6xl animate-pulse-slow">📚</div>
                <div class="card bg-blue-50 p-4">
                  <h4 class="font-bold text-blue-700 mb-2">基座模型</h4>
                  <p class="text-sm text-gray-600">通用知识宝库</p>
                </div>
                <div class="text-xs space-y-1 text-gray-700">
                  <p>✓ 理解语言</p>
                  <p>✓ 掌握知识</p>
                  <p>✗ 缺乏专业技能</p>
                </div>
              </div>
            </div>

            <!-- SFT箭头 -->
            <div class="text-center mt-4">
              <div class="text-4xl text-purple-500 mb-2">↓</div>
              <div class="bg-purple-100 p-3 rounded-lg">
                <p class="font-bold text-purple-800">SFT</p>
                <p class="text-xs text-purple-600">监督学习</p>
              </div>
            </div>
          </div>

          <!-- 最终模型 -->
          <div class="text-center space-y-4">
            <div class="text-7xl">🤖</div>
            <div class="card bg-gradient-to-br from-green-50 to-emerald-50 p-4">
              <h4 class="font-bold text-green-700 mb-2">专业助手</h4>
              <p class="text-sm text-gray-600">智能AI系统</p>
            </div>
            <div class="text-xs space-y-1 text-gray-700">
              <p>✓ 遵循指令</p>
              <p>✓ 专业回答</p>
              <p>✓ 符合风格</p>
              <p>✓ 价值对齐</p>
            </div>
          </div>
        </div>
      </div>
    </AnimatedIllustration>

    <!-- 两阶段详细对比 -->
    <section class="my-12">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">两个阶段的深度对比</h2>
      
      <!-- 数据规模对比可视化 -->
      <div class="card my-8">
        <h3 class="text-2xl font-bold text-gray-800 mb-6">数据规模对比</h3>
        <div class="space-y-6">
          <div>
            <div class="flex justify-between items-center mb-3">
              <span class="font-bold text-blue-700 text-lg">预训练数据量</span>
              <span class="text-2xl font-bold text-blue-700">数万亿词元</span>
            </div>
            <div class="w-full bg-gray-200 rounded-full h-12 relative overflow-hidden">
              <div class="absolute inset-0 bg-gradient-to-r from-blue-400 via-blue-500 to-blue-600 h-12 rounded-full" style="width: 100%">
                <div class="flex items-center justify-center h-full text-white font-bold">
                  1,000,000,000,000+ tokens
                </div>
              </div>
            </div>
            <p class="text-sm text-gray-600 mt-2">相当于数百万本书的内容</p>
          </div>

          <div>
            <div class="flex justify-between items-center mb-3">
              <span class="font-bold text-purple-700 text-lg">SFT数据量</span>
              <span class="text-2xl font-bold text-purple-700">数千至数十万样本</span>
            </div>
            <div class="w-full bg-gray-200 rounded-full h-12 relative overflow-hidden">
              <div class="absolute inset-0 bg-gradient-to-r from-purple-400 via-purple-500 to-purple-600 h-12 rounded-full" style="width: 0.001%">
                <div class="pl-3 flex items-center h-full text-white font-bold whitespace-nowrap">
                  1,000 - 100,000 samples
                </div>
              </div>
            </div>
            <p class="text-sm text-gray-600 mt-2">精心设计的高质量指令-响应对</p>
          </div>

          <div class="bg-gradient-to-r from-amber-50 to-orange-50 p-4 rounded-lg">
            <p class="text-center text-lg">
              <strong class="text-orange-700">规模差异：超过 1,000,000 倍！</strong>
            </p>
            <p class="text-center text-gray-600 mt-2">但SFT的影响力并不因数据量小而减弱</p>
          </div>
        </div>
      </div>

      <!-- 成本对比可视化 -->
      <div class="card my-8 bg-gradient-to-br from-yellow-50 to-amber-50">
        <h3 class="text-2xl font-bold text-amber-800 mb-6">💰 成本投入对比</h3>
        <div class="grid md:grid-cols-2 gap-6">
          <div class="bg-white p-6 rounded-xl">
            <h4 class="text-xl font-bold text-blue-700 mb-4">预训练成本</h4>
            <div class="space-y-4">
              <div class="flex justify-between items-center border-b pb-2">
                <span class="text-gray-700">GPU数量</span>
                <span class="font-bold text-blue-600">1000+ 张</span>
              </div>
              <div class="flex justify-between items-center border-b pb-2">
                <span class="text-gray-700">训练时间</span>
                <span class="font-bold text-blue-600">2-6 个月</span>
              </div>
              <div class="flex justify-between items-center border-b pb-2">
                <span class="text-gray-700">电力消耗</span>
                <span class="font-bold text-blue-600">数百万度</span>
              </div>
              <div class="flex justify-between items-center border-b pb-2">
                <span class="text-gray-700">人力成本</span>
                <span class="font-bold text-blue-600">数十人团队</span>
              </div>
              <div class="flex justify-between items-center bg-blue-100 p-3 rounded-lg mt-4">
                <span class="text-gray-800 font-bold">总成本</span>
                <span class="font-bold text-blue-700 text-xl">$5M - $100M</span>
              </div>
            </div>
          </div>

          <div class="bg-white p-6 rounded-xl">
            <h4 class="text-xl font-bold text-purple-700 mb-4">SFT成本</h4>
            <div class="space-y-4">
              <div class="flex justify-between items-center border-b pb-2">
                <span class="text-gray-700">GPU数量</span>
                <span class="font-bold text-purple-600">1-8 张</span>
              </div>
              <div class="flex justify-between items-center border-b pb-2">
                <span class="text-gray-700">训练时间</span>
                <span class="font-bold text-purple-600">数小时-数天</span>
              </div>
              <div class="flex justify-between items-center border-b pb-2">
                <span class="text-gray-700">电力消耗</span>
                <span class="font-bold text-purple-600">数百度</span>
              </div>
              <div class="flex justify-between items-center border-b pb-2">
                <span class="text-gray-700">人力成本</span>
                <span class="font-bold text-purple-600">1-5人小组</span>
              </div>
              <div class="flex justify-between items-center bg-purple-100 p-3 rounded-lg mt-4">
                <span class="text-gray-800 font-bold">总成本</span>
                <span class="font-bold text-purple-700 text-xl">$1K - $50K</span>
              </div>
            </div>
          </div>
        </div>
        
        <div class="mt-6 bg-green-100 p-4 rounded-lg text-center">
          <p class="text-lg font-bold text-green-800">
            SFT成本仅为预训练的 <span class="text-2xl">0.1% - 1%</span> 
          </p>
          <p class="text-gray-700 mt-2">这使得个人和小团队也能打造专属AI</p>
        </div>
      </div>
    </section>

    <!-- 第一阶段：预训练详解 -->
    <section class="my-16">
      <div class="card bg-gradient-to-br from-blue-600 to-indigo-600 text-white p-8 mb-8">
        <h2 class="text-4xl font-bold mb-4">第一阶段：奠定基础（预训练）</h2>
        <p class="text-xl opacity-90">Building the Foundation</p>
      </div>

      <!-- 预训练目标 -->
      <InfoCard icon="🎯" title="预训练的三大核心目标" variant="info">
        <div class="grid md:grid-cols-3 gap-4 mt-4">
          <div class="bg-blue-50 p-4 rounded-lg">
            <h5 class="font-bold text-blue-800 mb-2">1. 语言理解</h5>
            <p class="text-sm text-gray-700">掌握语法、句法、语义</p>
          </div>
          <div class="bg-blue-50 p-4 rounded-lg">
            <h5 class="font-bold text-blue-800 mb-2">2. 知识积累</h5>
            <p class="text-sm text-gray-700">学习事实、概念、常识</p>
          </div>
          <div class="bg-blue-50 p-4 rounded-lg">
            <h5 class="font-bold text-blue-800 mb-2">3. 推理能力</h5>
            <p class="text-sm text-gray-700">培养逻辑思维和推理</p>
          </div>
        </div>
        <p class="mt-4 text-lg"><strong>核心任务</strong>：预测下一个词（因果语言建模 - CLM）</p>
      </InfoCard>

      <!-- 预训练数据来源可视化 -->
      <div class="card my-8">
        <h3 class="text-2xl font-bold text-gray-800 mb-6">📚 预训练数据来源分布</h3>
        <InteractiveChart
          :data="pretrainingDataSourcesChart"
          type="pie"
          :options="{ plugins: { legend: { position: 'right' } } }"
        />
        <div class="grid md:grid-cols-4 gap-4 mt-6">
          <div class="bg-blue-50 p-4 rounded-lg text-center">
            <div class="text-3xl mb-2">🌐</div>
            <p class="font-bold text-blue-800">网页文本</p>
            <p class="text-sm text-gray-600">CommonCrawl等</p>
          </div>
          <div class="bg-green-50 p-4 rounded-lg text-center">
            <div class="text-3xl mb-2">📖</div>
            <p class="font-bold text-green-800">书籍语料</p>
            <p class="text-sm text-gray-600">Project Gutenberg</p>
          </div>
          <div class="bg-purple-50 p-4 rounded-lg text-center">
            <div class="text-3xl mb-2">💻</div>
            <p class="font-bold text-purple-800">代码仓库</p>
            <p class="text-sm text-gray-600">GitHub等</p>
          </div>
          <div class="bg-orange-50 p-4 rounded-lg text-center">
            <div class="text-3xl mb-2">📰</div>
            <p class="font-bold text-orange-800">学术论文</p>
            <p class="text-sm text-gray-600">arXiv、PubMed</p>
          </div>
        </div>
      </div>

      <!-- 预训练过程详细步骤 -->
      <div class="card my-8 bg-gradient-to-br from-indigo-50 to-blue-50">
        <h3 class="text-2xl font-bold text-indigo-800 mb-6">🔄 预训练的完整流程</h3>
        <div class="space-y-6">
          <div class="flex items-start space-x-4" v-for="(step, index) in pretrainingSteps" :key="index">
            <div class="bg-indigo-600 text-white rounded-full w-12 h-12 flex items-center justify-center font-bold text-lg flex-shrink-0">
              {{ index + 1 }}
            </div>
            <div class="flex-1 bg-white p-4 rounded-lg">
              <h4 class="font-bold text-gray-800 mb-2">{{ step.title }}</h4>
              <p class="text-gray-700 mb-2">{{ step.description }}</p>
              <div class="bg-blue-50 p-3 rounded text-sm text-blue-800">
                <strong>示例：</strong>{{ step.example }}
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 类比：图书馆自学 - 扩充版 -->
      <AnalogyBox icon="🏫" title="深度类比：图书馆的自学之旅">
        <div class="space-y-4">
          <p class="text-lg">
            预训练就像让一个学生独自在巨大的图书馆里自学。他阅读每一本书，尝试理解每个句子，
            预测下一个词。虽然没有老师指导，但通过海量的阅读，他掌握了语言的规律和世界的知识。
          </p>
          
          <div class="grid md:grid-cols-3 gap-4 mt-4">
            <div class="bg-orange-50 p-4 rounded-lg">
              <h5 class="font-bold text-orange-800 mb-2">📚 读什么？</h5>
              <p class="text-sm">图书馆里的所有书籍 = 互联网的所有文本</p>
            </div>
            <div class="bg-orange-50 p-4 rounded-lg">
              <h5 class="font-bold text-orange-800 mb-2">✏️ 怎么学？</h5>
              <p class="text-sm">猜下一个词 = 自监督学习信号</p>
            </div>
            <div class="bg-orange-50 p-4 rounded-lg">
              <h5 class="font-bold text-orange-800 mb-2">🎯 学到啥？</h5>
              <p class="text-sm">语言规律+世界知识 = 基座模型能力</p>
            </div>
          </div>

          <p class="mt-4 font-semibold text-orange-700 bg-orange-100 p-3 rounded-lg">
            💡 关键洞察：这个过程是"自监督"的——数据本身就提供了学习信号！不需要人工标注！
          </p>
        </div>
      </AnalogyBox>

      <!-- 预训练损失曲线 -->
      <div class="my-8">
        <div class="card">
          <h3 class="text-2xl font-bold text-gray-800 mb-4">📉 预训练损失曲线演变</h3>
          <InteractiveChart
            description="模型在预训练过程中逐渐学习语言模式，损失持续下降"
            :data="pretrainingChartData"
            type="line"
          />
          <div class="grid md:grid-cols-3 gap-4 mt-6">
            <div class="bg-blue-50 p-4 rounded-lg">
              <p class="font-bold text-blue-800">初期（Epoch 0-5）</p>
              <p class="text-sm text-gray-700">损失快速下降，学习基本语法</p>
            </div>
            <div class="bg-indigo-50 p-4 rounded-lg">
              <p class="font-bold text-indigo-800">中期（Epoch 5-15）</p>
              <p class="text-sm text-gray-700">持续改进，掌握复杂模式</p>
            </div>
            <div class="bg-purple-50 p-4 rounded-lg">
              <p class="font-bold text-purple-800">后期（Epoch 15+）</p>
              <p class="text-sm text-gray-700">缓慢收敛，趋于稳定</p>
            </div>
          </div>
        </div>
      </div>

      <!-- 预训练的产出 -->
      <div class="card my-8 bg-gradient-to-br from-cyan-50 to-blue-50">
        <h3 class="text-2xl font-bold text-cyan-800 mb-4">🎁 预训练的最终产出：基座模型</h3>
        <div class="grid md:grid-cols-2 gap-6">
          <div>
            <h4 class="font-bold text-gray-800 mb-3">✅ 基座模型具备的能力</h4>
            <ul class="space-y-2">
              <li class="flex items-start">
                <span class="text-green-500 text-xl mr-2">✓</span>
                <span class="text-gray-700">流畅地生成文本</span>
              </li>
              <li class="flex items-start">
                <span class="text-green-500 text-xl mr-2">✓</span>
                <span class="text-gray-700">理解语言的基本结构</span>
              </li>
              <li class="flex items-start">
                <span class="text-green-500 text-xl mr-2">✓</span>
                <span class="text-gray-700">掌握大量事实知识</span>
              </li>
              <li class="flex items-start">
                <span class="text-green-500 text-xl mr-2">✓</span>
                <span class="text-gray-700">进行基本逻辑推理</span>
              </li>
              <li class="flex items-start">
                <span class="text-green-500 text-xl mr-2">✓</span>
                <span class="text-gray-700">跨领域的通用能力</span>
              </li>
            </ul>
          </div>
          <div>
            <h4 class="font-bold text-gray-800 mb-3">❌ 基座模型缺少的能力</h4>
            <ul class="space-y-2">
              <li class="flex items-start">
                <span class="text-red-500 text-xl mr-2">✗</span>
                <span class="text-gray-700">遵循用户指令</span>
              </li>
              <li class="flex items-start">
                <span class="text-red-500 text-xl mr-2">✗</span>
                <span class="text-gray-700">以助手方式对话</span>
              </li>
              <li class="flex items-start">
                <span class="text-red-500 text-xl mr-2">✗</span>
                <span class="text-gray-700">拒绝不当请求</span>
              </li>
              <li class="flex items-start">
                <span class="text-red-500 text-xl mr-2">✗</span>
                <span class="text-gray-700">保持特定风格/语气</span>
              </li>
              <li class="flex items-start">
                <span class="text-red-500 text-xl mr-2">✗</span>
                <span class="text-gray-700">专业化任务执行</span>
              </li>
            </ul>
          </div>
        </div>
        <div class="mt-6 bg-yellow-100 p-4 rounded-lg text-center">
          <p class="text-lg font-bold text-yellow-800">
            💡 这就是为什么需要SFT！基座模型有知识但不会"用"
          </p>
        </div>
      </div>
    </section>

    <!-- 第二阶段：SFT详解 -->
    <section class="my-16">
      <div class="card bg-gradient-to-br from-purple-600 to-pink-600 text-white p-8 mb-8">
        <h2 class="text-4xl font-bold mb-4">第二阶段：磨练技能（监督式微调）</h2>
        <p class="text-xl opacity-90">Sharpening the Skills</p>
      </div>

      <!-- SFT目标 -->
      <InfoCard icon="🎯" title="SFT的核心使命" variant="success">
        <div class="bg-green-50 p-6 rounded-lg mt-4">
          <p class="text-lg text-gray-800 mb-4">
            将基座模型改造为能够胜任<strong>特定、有用任务</strong>的工具，
            使其行为方式与<strong>用户的意图</strong>对齐。
          </p>
          <div class="grid md:grid-cols-4 gap-3">
            <div class="bg-white p-3 rounded text-center">
              <div class="text-2xl mb-1">🎯</div>
              <p class="text-sm font-semibold">遵循指令</p>
            </div>
            <div class="bg-white p-3 rounded text-center">
              <div class="text-2xl mb-1">🎨</div>
              <p class="text-sm font-semibold">特定风格</p>
            </div>
            <div class="bg-white p-3 rounded text-center">
              <div class="text-2xl mb-1">⚙️</div>
              <p class="text-sm font-semibold">任务专精</p>
            </div>
            <div class="bg-white p-3 rounded text-center">
              <div class="text-2xl mb-1">🛡️</div>
              <p class="text-sm font-semibold">价值对齐</p>
            </div>
          </div>
        </div>
      </InfoCard>

      <!-- SFT数据特点可视化 -->
      <div class="card my-8">
        <h3 class="text-2xl font-bold text-gray-800 mb-6">📊 SFT数据集特征全景</h3>
        <div class="grid md:grid-cols-3 gap-6">
          <div class="bg-purple-50 p-6 rounded-xl">
            <h4 class="font-bold text-purple-800 mb-4 text-xl">数据规模</h4>
            <div class="text-4xl font-bold text-purple-600 mb-2">100 - 100K</div>
            <p class="text-gray-700">样本数量</p>
            <div class="mt-4 space-y-2 text-sm">
              <p>• 小规模：100-1,000（快速原型）</p>
              <p>• 中规模：1,000-10,000（通用应用）</p>
              <p>• 大规模：10,000-100,000（企业级）</p>
            </div>
          </div>

          <div class="bg-pink-50 p-6 rounded-xl">
            <h4 class="font-bold text-pink-800 mb-4 text-xl">数据格式</h4>
            <div class="text-2xl font-bold text-pink-600 mb-2">指令-响应对</div>
            <p class="text-gray-700">结构化样本</p>
            <div class="mt-4 space-y-2 text-sm">
              <p>• Instruction: 任务描述</p>
              <p>• Input: 上下文内容</p>
              <p>• Response: 期望输出</p>
            </div>
          </div>

          <div class="bg-indigo-50 p-6 rounded-xl">
            <h4 class="font-bold text-indigo-800 mb-4 text-xl">数据质量</h4>
            <div class="text-2xl font-bold text-indigo-600 mb-2">极其重要</div>
            <p class="text-gray-700">决定成败</p>
            <div class="mt-4 space-y-2 text-sm">
              <p>• 相关性：高度针对任务</p>
              <p>• 多样性：覆盖各种场景</p>
              <p>• 准确性：无错误标注</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SFT过程可视化 -->
      <div class="card my-8 bg-gradient-to-br from-violet-50 to-purple-50">
        <h3 class="text-2xl font-bold text-violet-800 mb-6">🔄 SFT训练过程详解</h3>
        <div class="space-y-6">
          <div class="flex items-center space-x-4" v-for="(step, index) in sftProcessSteps" :key="index">
            <div class="bg-gradient-to-br from-purple-500 to-pink-500 text-white rounded-full w-14 h-14 flex items-center justify-center font-bold text-xl flex-shrink-0">
              {{ index + 1 }}
            </div>
            <div class="flex-1 bg-white p-5 rounded-xl shadow-sm">
              <div class="flex items-center justify-between mb-2">
                <h4 class="font-bold text-gray-800 text-lg">{{ step.title }}</h4>
                <span class="text-2xl">{{ step.icon }}</span>
              </div>
              <p class="text-gray-700 mb-3">{{ step.description }}</p>
              <div class="bg-purple-50 p-3 rounded-lg">
                <p class="text-sm text-purple-800"><strong>具体操作：</strong>{{ step.action }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- SFT类比：在职培训 - 扩充版 -->
      <AnalogyBox icon="👔" title="深度类比：公司的在职培训体系">
        <div class="space-y-4">
          <p class="text-lg">
            SFT就像公司为新员工提供的在职培训。虽然这位员工（基座模型）已经有扎实的知识基础，
            但还需要学习如何礼貌地与客户沟通、如何使用公司的工作流程、如何以专业的方式完成任务。
          </p>
          
          <div class="grid md:grid-cols-2 gap-6 mt-4">
            <div class="bg-orange-50 p-5 rounded-lg">
              <h5 class="font-bold text-orange-800 mb-3 text-lg">员工入职培训</h5>
              <ul class="space-y-2 text-sm">
                <li class="flex items-start">
                  <span class="text-orange-500 mr-2">1.</span>
                  <span><strong>师傅示范</strong> - 看老员工如何处理业务</span>
                </li>
                <li class="flex items-start">
                  <span class="text-orange-500 mr-2">2.</span>
                  <span><strong>模仿学习</strong> - 按照标准流程操作</span>
                </li>
                <li class="flex items-start">
                  <span class="text-orange-500 mr-2">3.</span>
                  <span><strong>反复练习</strong> - 处理各种场景案例</span>
                </li>
                <li class="flex items-start">
                  <span class="text-orange-500 mr-2">4.</span>
                  <span><strong>形成习惯</strong> - 内化工作方式和风格</span>
                </li>
              </ul>
            </div>

            <div class="bg-purple-50 p-5 rounded-lg">
              <h5 class="font-bold text-purple-800 mb-3 text-lg">模型SFT训练</h5>
              <ul class="space-y-2 text-sm">
                <li class="flex items-start">
                  <span class="text-purple-500 mr-2">1.</span>
                  <span><strong>示范数据</strong> - 高质量的指令-响应对</span>
                </li>
                <li class="flex items-start">
                  <span class="text-purple-500 mr-2">2.</span>
                  <span><strong>监督学习</strong> - 最小化与标准答案的差异</span>
                </li>
                <li class="flex items-start">
                  <span class="text-purple-500 mr-2">3.</span>
                  <span><strong>多样训练</strong> - 覆盖各类任务场景</span>
                </li>
                <li class="flex items-start">
                  <span class="text-purple-500 mr-2">4.</span>
                  <span><strong>行为固化</strong> - 学会特定的响应模式</span>
                </li>
              </ul>
            </div>
          </div>

          <div class="bg-gradient-to-r from-orange-100 to-purple-100 p-4 rounded-lg mt-4">
            <p class="text-center text-lg font-semibold text-gray-800">
              💼 培训师（人类专家）通过示范（标注数据）教会员工（模型）正确的工作方式！
            </p>
          </div>
        </div>
      </AnalogyBox>

      <!-- SFT资源优势 -->
      <div class="card my-8">
        <h3 class="text-2xl font-bold text-gray-800 mb-6">⚡ SFT的资源优势：人人可及</h3>
        <div class="grid md:grid-cols-4 gap-4">
          <div class="bg-green-50 p-5 rounded-lg text-center">
            <div class="text-4xl mb-3">💰</div>
            <p class="font-bold text-green-800 mb-2">成本低</p>
            <p class="text-2xl font-bold text-green-600">$1K-$50K</p>
            <p class="text-sm text-gray-600 mt-2">vs 预训练的数百万美元</p>
          </div>
          <div class="bg-blue-50 p-5 rounded-lg text-center">
            <div class="text-4xl mb-3">⏱️</div>
            <p class="font-bold text-blue-800 mb-2">时间短</p>
            <p class="text-2xl font-bold text-blue-600">数小时-数天</p>
            <p class="text-sm text-gray-600 mt-2">vs 预训练的数月</p>
          </div>
          <div class="bg-purple-50 p-5 rounded-lg text-center">
            <div class="text-4xl mb-3">🖥️</div>
            <p class="font-bold text-purple-800 mb-2">硬件少</p>
            <p class="text-2xl font-bold text-purple-600">1-8 GPU</p>
            <p class="text-sm text-gray-600 mt-2">vs 预训练的上千GPU</p>
          </div>
          <div class="bg-pink-50 p-5 rounded-lg text-center">
            <div class="text-4xl mb-3">👥</div>
            <p class="font-bold text-pink-800 mb-2">团队小</p>
            <p class="text-2xl font-bold text-pink-600">1-5人</p>
            <p class="text-sm text-gray-600 mt-2">vs 预训练的数十人</p>
          </div>
        </div>
        <div class="mt-6 bg-gradient-to-r from-green-100 to-blue-100 p-5 rounded-lg text-center">
          <p class="text-xl font-bold text-gray-800">
            🎉 个人开发者、创业团队、中小企业都能负担！
          </p>
          <p class="text-gray-700 mt-2">这正是开源LLM革命的意义所在</p>
        </div>
      </div>
    </section>

    <!-- 详细对比表格 - 多维度扩充 -->
    <section class="my-16">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">📋 预训练 vs SFT：全方位对比</h2>
      
      <ComparisonTable
        title="核心差异总览"
        :headers="['维度', '预训练 (Pre-training)', 'SFT (Supervised Fine-Tuning)']"
        :rows="comparisonRows"
      />

      <!-- 额外的对比维度 -->
      <div class="grid md:grid-cols-2 gap-8 mt-8">
        <div class="card">
          <h3 class="text-xl font-bold text-blue-700 mb-4">预训练的特点</h3>
          <ul class="space-y-3">
            <li class="flex items-start">
              <span class="text-blue-500 text-xl mr-3">📊</span>
              <div>
                <p class="font-semibold">数据驱动型</p>
                <p class="text-sm text-gray-600">规模压倒一切</p>
              </div>
            </li>
            <li class="flex items-start">
              <span class="text-blue-500 text-xl mr-3">🤖</span>
              <div>
                <p class="font-semibold">自动化程度高</p>
                <p class="text-sm text-gray-600">无需人工标注</p>
              </div>
            </li>
            <li class="flex items-start">
              <span class="text-blue-500 text-xl mr-3">🌐</span>
              <div>
                <p class="font-semibold">通用性强</p>
                <p class="text-sm text-gray-600">不针对特定任务</p>
              </div>
            </li>
            <li class="flex items-start">
              <span class="text-blue-500 text-xl mr-3">💸</span>
              <div>
                <p class="font-semibold">一次投资长期受益</p>
                <p class="text-sm text-gray-600">基座可多次微调</p>
              </div>
            </li>
          </ul>
        </div>

        <div class="card">
          <h3 class="text-xl font-bold text-purple-700 mb-4">SFT的特点</h3>
          <ul class="space-y-3">
            <li class="flex items-start">
              <span class="text-purple-500 text-xl mr-3">🎯</span>
              <div>
                <p class="font-semibold">质量驱动型</p>
                <p class="text-sm text-gray-600">精不在多</p>
              </div>
            </li>
            <li class="flex items-start">
              <span class="text-purple-500 text-xl mr-3">👥</span>
              <div>
                <p class="font-semibold">人工参与度高</p>
                <p class="text-sm text-gray-600">需要专家标注</p>
              </div>
            </li>
            <li class="flex items-start">
              <span class="text-purple-500 text-xl mr-3">🔧</span>
              <div>
                <p class="font-semibold">专用性强</p>
                <p class="text-sm text-gray-600">针对特定应用</p>
              </div>
            </li>
            <li class="flex items-start">
              <span class="text-purple-500 text-xl mr-3">🔄</span>
              <div>
                <p class="font-semibold">迭代优化容易</p>
                <p class="text-sm text-gray-600">快速调整改进</p>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </section>

    <!-- 两阶段的关系 - 扩充 -->
    <section class="my-16">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">🔗 两阶段的共生关系</h2>
      
      <div class="card bg-gradient-to-br from-amber-50 to-orange-50 border-l-4 border-amber-500 mb-8">
        <div class="flex items-start space-x-6">
          <div class="text-7xl">⚠️</div>
          <div class="flex-1">
            <h3 class="text-3xl font-bold text-amber-800 mb-5">单向依赖关系</h3>
            
            <div class="grid md:grid-cols-2 gap-6 mb-6">
              <div class="bg-white p-5 rounded-lg">
                <h4 class="font-bold text-green-700 mb-3 text-lg flex items-center">
                  <span class="text-2xl mr-2">✓</span>
                  SFT依赖预训练
                </h4>
                <p class="text-gray-700 mb-3">
                  SFT的成功在根本上依赖于预训练阶段打下的坚实基础。
                </p>
                <div class="bg-green-50 p-3 rounded">
                  <p class="text-sm text-green-800">
                    <strong>类比：</strong>在职培训需要员工已有基础学历和通用能力
                  </p>
                </div>
              </div>

              <div class="bg-white p-5 rounded-lg">
                <h4 class="font-bold text-red-700 mb-3 text-lg flex items-center">
                  <span class="text-2xl mr-2">✗</span>
                  预训练不依赖SFT
                </h4>
                <p class="text-gray-700 mb-3">
                  即便是最完美的SFT数据集，也无法拯救一个预训练效果差的模型。
                </p>
                <div class="bg-red-50 p-3 rounded">
                  <p class="text-sm text-red-800">
                    <strong>类比：</strong>最好的培训也救不了基础太差的员工
                  </p>
                </div>
              </div>
            </div>

            <div class="bg-gradient-to-r from-amber-100 to-yellow-100 p-6 rounded-xl">
              <p class="font-bold text-amber-800 text-xl mb-3">💡 关键洞察</p>
              <p class="text-lg text-gray-800 leading-relaxed">
                SFT是在<strong>"解锁"和"引导"</strong>模型已有的潜力，而非从零创造潜力！
                这意味着，在选择一个模型进行微调项目时，<strong>基座模型的质量和能力是决定项目成败上限的最关键因素</strong>。
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- 关系可视化 -->
      <div class="card">
        <h3 class="text-2xl font-bold text-gray-800 mb-6">依赖关系可视化</h3>
        <div class="flex items-center justify-center space-x-8 p-8">
          <div class="text-center">
            <div class="w-48 h-48 bg-gradient-to-br from-blue-400 to-blue-600 rounded-full flex items-center justify-center text-white text-5xl font-bold shadow-2xl">
              强
            </div>
            <p class="mt-4 font-bold text-blue-700 text-xl">预训练基座</p>
            <p class="text-sm text-gray-600">能力上限高</p>
          </div>

          <div class="text-center">
            <div class="text-6xl text-green-500">+</div>
            <p class="text-sm text-gray-600 mt-2">加上</p>
          </div>

          <div class="text-center">
            <div class="w-48 h-48 bg-gradient-to-br from-purple-400 to-purple-600 rounded-full flex items-center justify-center text-white text-5xl font-bold shadow-2xl">
              好
            </div>
            <p class="mt-4 font-bold text-purple-700 text-xl">SFT数据</p>
            <p class="text-sm text-gray-600">质量优秀</p>
          </div>

          <div class="text-center">
            <div class="text-6xl text-yellow-500">=</div>
            <p class="text-sm text-gray-600 mt-2">产出</p>
          </div>

          <div class="text-center">
            <div class="w-48 h-48 bg-gradient-to-br from-green-400 to-emerald-600 rounded-full flex items-center justify-center text-white text-4xl font-bold shadow-2xl">
              卓越
            </div>
            <p class="mt-4 font-bold text-green-700 text-xl">专业助手</p>
            <p class="text-sm text-gray-600">性能出色</p>
          </div>
        </div>

        <div class="mt-6 bg-red-50 p-5 rounded-lg border-2 border-red-200">
          <p class="text-center font-bold text-red-800 text-lg">
            ⚠️ 弱基座 + 好数据 = 平庸结果（受基座限制）
          </p>
        </div>
      </div>
    </section>

    <!-- SFT的真正作用 - 大幅扩充 -->
    <section class="my-16">
      <div class="card bg-gradient-to-br from-emerald-600 to-green-600 text-white p-8 mb-8">
        <h2 class="text-4xl font-bold mb-4">SFT的真正作用：塑造行为而非灌输知识</h2>
        <p class="text-xl opacity-90">Shaping Behavior, Not Just Adding Facts</p>
      </div>

      <!-- 误解 vs 真相 -->
      <div class="grid md:grid-cols-2 gap-8 mb-8">
        <div class="card bg-gradient-to-br from-red-50 to-pink-50 border-2 border-red-300">
          <h3 class="text-2xl font-bold text-red-800 mb-4 flex items-center">
            <span class="text-4xl mr-3">❌</span>
            常见误解
          </h3>
          <div class="space-y-4">
            <div class="bg-white p-4 rounded-lg">
              <p class="font-semibold text-red-700 mb-2">误解1：SFT是知识注入器</p>
              <p class="text-sm text-gray-700">认为SFT的主要目的是向模型灌输新的事实知识</p>
            </div>
            <div class="bg-white p-4 rounded-lg">
              <p class="font-semibold text-red-700 mb-2">误解2：数据越多越好</p>
              <p class="text-sm text-gray-700">以为SFT数据集要和预训练一样大才有效</p>
            </div>
            <div class="bg-white p-4 rounded-lg">
              <p class="font-semibold text-red-700 mb-2">误解3：可以弥补预训练不足</p>
              <p class="text-sm text-gray-700">期待通过SFT补救预训练效果差的模型</p>
            </div>
          </div>
        </div>

        <div class="card bg-gradient-to-br from-green-50 to-emerald-50 border-2 border-green-300">
          <h3 class="text-2xl font-bold text-green-800 mb-4 flex items-center">
            <span class="text-4xl mr-3">✅</span>
            真实作用
          </h3>
          <div class="space-y-4">
            <div class="bg-white p-4 rounded-lg">
              <p class="font-semibold text-green-700 mb-2">核心目标：行为塑造</p>
              <p class="text-sm text-gray-700">教会模型"如何说"而不只是"说什么"</p>
            </div>
            <div class="bg-white p-4 rounded-lg">
              <p class="font-semibold text-green-700 mb-2">精品策略：质量为王</p>
              <p class="text-sm text-gray-700">数百条高质量样本胜过数万条噪声数据</p>
            </div>
            <div class="bg-white p-4 rounded-lg">
              <p class="font-semibold text-green-700 mb-2">能力解锁：引导潜力</p>
              <p class="text-sm text-gray-700">激发和引导预训练已建立的能力</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SFT塑造的具体方面 -->
      <div class="card my-8 bg-gradient-to-br from-indigo-50 to-purple-50">
        <h3 class="text-2xl font-bold text-indigo-800 mb-6">🎨 SFT塑造AI的哪些方面？</h3>
        <div class="grid md:grid-cols-2 gap-6">
          <div class="bg-white p-6 rounded-xl">
            <h4 class="font-bold text-lg text-gray-800 mb-4 flex items-center">
              <span class="text-3xl mr-3">📝</span>
              格式与结构
            </h4>
            <ul class="space-y-3 text-sm">
              <li class="flex items-start">
                <span class="text-indigo-500 mr-2">•</span>
                <div>
                  <p class="font-semibold">JSON输出</p>
                  <p class="text-gray-600">严格遵守JSON Schema</p>
                </div>
              </li>
              <li class="flex items-start">
                <span class="text-indigo-500 mr-2">•</span>
                <div>
                  <p class="font-semibold">Markdown格式</p>
                  <p class="text-gray-600">使用标题、列表、代码块</p>
                </div>
              </li>
              <li class="flex items-start">
                <span class="text-indigo-500 mr-2">•</span>
                <div>
                  <p class="font-semibold">步骤化输出</p>
                  <p class="text-gray-600">分步骤展示推理过程</p>
                </div>
              </li>
            </ul>
          </div>

          <div class="bg-white p-6 rounded-xl">
            <h4 class="font-bold text-lg text-gray-800 mb-4 flex items-center">
              <span class="text-3xl mr-3">🎭</span>
              风格与语气
            </h4>
            <ul class="space-y-3 text-sm">
              <li class="flex items-start">
                <span class="text-purple-500 mr-2">•</span>
                <div>
                  <p class="font-semibold">正式程度</p>
                  <p class="text-gray-600">学术、商务或随意风格</p>
                </div>
              </li>
              <li class="flex items-start">
                <span class="text-purple-500 mr-2">•</span>
                <div>
                  <p class="font-semibold">情感倾向</p>
                  <p class="text-gray-600">友好、专业或中性语气</p>
                </div>
              </li>
              <li class="flex items-start">
                <span class="text-purple-500 mr-2">•</span>
                <div>
                  <p class="font-semibold">品牌个性</p>
                  <p class="text-gray-600">特定的表达习惯和风格</p>
                </div>
              </li>
            </ul>
          </div>

          <div class="bg-white p-6 rounded-xl">
            <h4 class="font-bold text-lg text-gray-800 mb-4 flex items-center">
              <span class="text-3xl mr-3">🧠</span>
              推理与思考
            </h4>
            <ul class="space-y-3 text-sm">
              <li class="flex items-start">
                <span class="text-blue-500 mr-2">•</span>
                <div>
                  <p class="font-semibold">思维链(CoT)</p>
                  <p class="text-gray-600">展示逐步推理过程</p>
                </div>
              </li>
              <li class="flex items-start">
                <span class="text-blue-500 mr-2">•</span>
                <div>
                  <p class="font-semibold">解释性回答</p>
                  <p class="text-gray-600">不仅给答案还说原因</p>
                </div>
              </li>
              <li class="flex items-start">
                <span class="text-blue-500 mr-2">•</span>
                <div>
                  <p class="font-semibold">反思机制</p>
                  <p class="text-gray-600">检查和修正自己的输出</p>
                </div>
              </li>
            </ul>
          </div>

          <div class="bg-white p-6 rounded-xl">
            <h4 class="font-bold text-lg text-gray-800 mb-4 flex items-center">
              <span class="text-3xl mr-3">🛡️</span>
              安全与价值观
            </h4>
            <ul class="space-y-3 text-sm">
              <li class="flex items-start">
                <span class="text-green-500 mr-2">•</span>
                <div>
                  <p class="font-semibold">拒绝策略</p>
                  <p class="text-gray-600">识别并拒绝不当请求</p>
                </div>
              </li>
              <li class="flex items-start">
                <span class="text-green-500 mr-2">•</span>
                <div>
                  <p class="font-semibold">免责声明</p>
                  <p class="text-gray-600">在适当时机添加警告</p>
                </div>
              </li>
              <li class="flex items-start">
                <span class="text-green-500 mr-2">•</span>
                <div>
                  <p class="font-semibold">价值对齐</p>
                  <p class="text-gray-600">符合人类价值观和伦理</p>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- 实际应用示例 -->
      <div class="card my-8">
        <h3 class="text-2xl font-bold text-gray-800 mb-6">💼 SFT实际应用案例</h3>
        <div class="space-y-6">
          <div class="bg-gradient-to-r from-blue-50 to-cyan-50 p-6 rounded-xl">
            <h4 class="font-bold text-blue-800 mb-3 text-lg">案例1：客服助手的语气调整</h4>
            <div class="grid md:grid-cols-2 gap-4">
              <div class="bg-white p-4 rounded-lg">
                <p class="font-semibold text-red-700 mb-2">❌ 未经SFT的回答</p>
                <p class="text-sm text-gray-700 italic">"你的订单没发货。系统显示库存不足。"</p>
                <p class="text-xs text-gray-500 mt-2">冷淡、缺乏同理心</p>
              </div>
              <div class="bg-white p-4 rounded-lg">
                <p class="font-semibold text-green-700 mb-2">✅ SFT后的回答</p>
                <p class="text-sm text-gray-700 italic">"非常抱歉给您带来不便！您的订单由于库存原因暂时延迟发货。我们正在加急补货，预计3天内发出。感谢您的耐心等待！"</p>
                <p class="text-xs text-gray-500 mt-2">友好、专业、有同理心</p>
              </div>
            </div>
          </div>

          <div class="bg-gradient-to-r from-purple-50 to-pink-50 p-6 rounded-xl">
            <h4 class="font-bold text-purple-800 mb-3 text-lg">案例2：代码助手的格式规范</h4>
            <div class="grid md:grid-cols-2 gap-4">
              <div class="bg-white p-4 rounded-lg">
                <p class="font-semibold text-red-700 mb-2">❌ 未经SFT的输出</p>
                <pre class="text-xs bg-gray-900 text-gray-100 p-2 rounded mt-2">def add(a,b):return a+b</pre>
                <p class="text-xs text-gray-500 mt-2">无注释、格式混乱</p>
              </div>
              <div class="bg-white p-4 rounded-lg">
                <p class="font-semibold text-green-700 mb-2">✅ SFT后的输出</p>
                <pre class="text-xs bg-gray-900 text-gray-100 p-2 rounded mt-2">def add(a: int, b: int) -> int:
    """两数相加
    
    Args:
        a: 第一个数
        b: 第二个数
    
    Returns:
        两数之和
    """
    return a + b</pre>
                <p class="text-xs text-gray-500 mt-2">规范、有文档、易维护</p>
              </div>
            </div>
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
      explanation="SFT的作用是解锁和引导模型已有的潜力，塑造其行为模式。如果预训练阶段没有建立好知识基础和语言理解能力，SFT就像在沙滩上建房子——缺乏坚实的地基，再好的装修也无济于事。SFT不是知识注入器，而是行为塑造器。"
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

// 预训练步骤数据
const pretrainingSteps = [
  {
    title: '数据收集与清洗',
    description: '从互联网、书籍、代码库等来源收集海量文本，并进行去重、过滤有害内容等清洗工作',
    example: '抓取维基百科全部文章、GitHub公开代码、CommonCrawl网页数据等'
  },
  {
    title: '分词(Tokenization)',
    description: '将文本分割成模型可以理解的小单元（tokens），通常使用BPE或WordPiece算法',
    example: '"Hello World" → ["Hello", "World"] 或 ["Hel", "lo", "Wor", "ld"]'
  },
  {
    title: '构建训练批次',
    description: '将token序列组织成固定长度的批次，准备送入模型进行训练',
    example: '将文本切分为2048或4096个token的序列'
  },
  {
    title: '前向传播',
    description: '模型读取输入序列，对每个位置预测下一个token的概率分布',
    example: '给定"The cat sat on the"，预测下一个词可能是"mat"(0.6), "floor"(0.3), "chair"(0.1)'
  },
  {
    title: '计算损失',
    description: '比较模型预测与实际下一个词，计算交叉熵损失（预测越准确，损失越小）',
    example: '如果实际词是"mat"但模型给它的概率只有0.1，则损失较大'
  },
  {
    title: '反向传播与更新',
    description: '根据损失梯度更新模型参数，使模型下次预测更准确',
    example: '调整神经网络权重，让模型对"mat"的预测概率从0.1提升到0.6'
  },
  {
    title: '重复迭代',
    description: '在整个数据集上重复以上过程数个epoch，直到模型收敛',
    example: '遍历万亿tokens可能需要数周到数月时间'
  }
]

// SFT过程步骤
const sftProcessSteps = [
  {
    title: '准备指令数据集',
    icon: '📋',
    description: '收集或创建高质量的指令-响应对，每对包含清晰的任务描述和期望输出',
    action: '格式化为JSONL文件，包含instruction、input、response字段'
  },
  {
    title: '加载基座模型',
    icon: '🧠',
    description: '选择合适的预训练模型作为起点，如LLaMA-2-7B、Mistral-7B等',
    action: '使用HuggingFace加载模型和tokenizer'
  },
  {
    title: '配置训练参数',
    icon: '⚙️',
    description: '设置学习率、批次大小、训练轮数等关键超参数，如果使用LoRA还需配置rank等',
    action: '创建TrainingArguments或SFTConfig对象'
  },
  {
    title: '监督训练',
    icon: '🎯',
    description: '模型学习将输入映射到标准响应，最小化预测输出与目标响应之间的差异',
    action: '使用SFTTrainer或类似工具运行训练循环'
  },
  {
    title: '验证与评估',
    icon: '📊',
    description: '在验证集上检查模型性能，确保没有过拟合，必要时调整参数',
    action: '计算验证损失、困惑度等指标'
  },
  {
    title: '保存模型',
    icon: '💾',
    description: '保存微调后的模型参数（全量或LoRA适配器），以便后续部署使用',
    action: '保存checkpoint到本地或上传到HuggingFace Hub'
  }
]

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
    values: [{ text: '极其高昂（数百万美元级别）', highlight: true }, { text: '相对低廉（数千至数万美元）', highlight: true }]
  },
  {
    label: '训练时间',
    values: ['数周至数月', '数小时至数天']
  },
  {
    label: '硬件需求',
    values: ['1000+ GPU', '1-8 GPU']
  },
  {
    label: '最终产出',
    values: ['通用型"基座模型"', '专用型、遵循指令的"助手模型"']
  },
  {
    label: '可访问性',
    values: ['仅大型机构可负担', '个人和小团队可负担']
  }
]

const pretrainingChartData = ref({
  labels: [],
  datasets: []
})

const pretrainingDataSourcesChart = ref({
  labels: ['网页文本', '书籍语料', '代码仓库', '学术论文', '其他'],
  datasets: [{
    label: '数据来源分布',
    data: [45, 20, 15, 10, 10],
    backgroundColor: [
      'rgba(59, 130, 246, 0.8)',
      'rgba(16, 185, 129, 0.8)',
      'rgba(139, 92, 246, 0.8)',
      'rgba(251, 146, 60, 0.8)',
      'rgba(156, 163, 175, 0.8)'
    ],
    borderColor: [
      'rgb(59, 130, 246)',
      'rgb(16, 185, 129)',
      'rgb(139, 92, 246)',
      'rgb(251, 146, 60)',
      'rgb(156, 163, 175)'
    ],
    borderWidth: 2
  }]
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
          tension: 0.4,
          fill: true
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
          tension: 0.4,
          fill: true
        }
      ]
    }
  }
})
</script>

