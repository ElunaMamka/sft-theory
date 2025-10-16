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
              <div class="absolute inset-0 bg-gradient-to-r from-purple-400 via-purple-500 to-purple-600 h-12 rounded-full" style="width: 1.2%">
                <div class="pl-3 flex items-center h-full text-white font-bold whitespace-nowrap text-sm">
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

      <!-- 训练时间对比详解 -->
      <div class="card my-8 bg-gradient-to-br from-cyan-50 to-blue-50">
        <h3 class="text-2xl font-bold text-cyan-800 mb-6">⏰ 训练时间对比：从月到天的跨越</h3>
        
        <!-- 结论先行 -->
        <div class="bg-gradient-to-r from-blue-100 to-cyan-100 p-6 rounded-xl mb-8 border-l-4 border-blue-600">
          <h4 class="text-xl font-bold text-blue-800 mb-4 flex items-center">
            <span class="text-3xl mr-3">🎯</span>
            结论先行：预训练需要多久？
          </h4>
          <div class="bg-white p-5 rounded-lg">
            <p class="text-lg text-gray-800 mb-3">
              在理想的优化情况下，使用<strong class="text-blue-700">10张NVIDIA 3090显卡</strong>预训练一个<strong class="text-blue-700">0.5B（5亿）参数</strong>的模型，处理<strong class="text-blue-700">300B（3000亿）Token</strong>，大约需要：
            </p>
            <div class="text-center my-4">
              <p class="text-5xl font-bold text-blue-600">15 - 25 天</p>
              <p class="text-gray-600 mt-2">这还只是一个"小"模型！</p>
            </div>
            <div class="bg-yellow-50 p-4 rounded-lg mt-4">
              <p class="text-sm text-yellow-800">
                <strong>⚠️ 注意：</strong>这个时间是一个估算区间，实际时间会因诸多因素浮动，其中最关键的是 <strong>"计算效率"</strong>（MFU - Model FLOPs Utilization）。
              </p>
            </div>
          </div>
        </div>

        <!-- 估算步骤详解 -->
        <div class="space-y-6">
          <h4 class="text-xl font-bold text-gray-800">📊 估算步骤详解</h4>
          <p class="text-gray-700">我们可以分三步来计算预训练时间：</p>

          <!-- 步骤1: 计算总计算量 -->
          <div class="bg-white p-6 rounded-xl border-2 border-blue-200">
            <div class="flex items-center mb-4">
              <div class="bg-blue-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold mr-4">1</div>
              <h5 class="text-lg font-bold text-blue-800">计算总计算量 (Total FLOPs)</h5>
            </div>
            
            <p class="text-gray-700 mb-4">对于预训练一个Transformer模型，一个广泛接受的估算公式是：</p>
            
            <div class="bg-gray-900 text-green-400 p-4 rounded-lg font-mono text-lg text-center mb-4">
              Total FLOPs ≈ 6 × N × D
            </div>

            <div class="grid md:grid-cols-3 gap-4 mb-4">
              <div class="bg-blue-50 p-4 rounded-lg">
                <p class="font-bold text-blue-800 mb-2">N - 参数量</p>
                <p class="text-sm text-gray-700">Number of Parameters</p>
                <p class="text-xs text-gray-600 mt-2">模型的总参数数量</p>
              </div>
              <div class="bg-purple-50 p-4 rounded-lg">
                <p class="font-bold text-purple-800 mb-2">D - Token数量</p>
                <p class="text-sm text-gray-700">Number of Tokens</p>
                <p class="text-xs text-gray-600 mt-2">训练数据的Token总数</p>
              </div>
              <div class="bg-green-50 p-4 rounded-lg">
                <p class="font-bold text-green-800 mb-2">6 - 系数</p>
                <p class="text-sm text-gray-700">计算倍数</p>
                <p class="text-xs text-gray-600 mt-2">前向2N + 反向4N</p>
              </div>
            </div>

            <div class="bg-cyan-50 p-4 rounded-lg mb-4">
              <p class="font-semibold text-cyan-800 mb-2">💡 系数"6"的来源：</p>
              <ul class="text-sm text-gray-700 space-y-1 ml-4">
                <li>• <strong>前向传播</strong> (Forward Pass)：约需要 <strong>2×N</strong> 次计算</li>
                <li>• <strong>反向传播</strong> (Backward Pass)：约是前向的<strong>2倍</strong>，需要 <strong>4×N</strong> 次计算</li>
                <li>• <strong>总计</strong>：2N + 4N = 6N 次计算/每个Token</li>
              </ul>
            </div>

            <p class="font-bold text-gray-800 mb-2">现在代入具体数据：</p>
            <div class="bg-gradient-to-r from-gray-50 to-gray-100 p-5 rounded-lg space-y-3">
              <div class="flex items-center justify-between border-b pb-2">
                <span class="text-gray-700">N (参数量)</span>
                <span class="font-mono font-bold text-blue-600">0.5 × 10<sup>9</sup> = 500,000,000</span>
              </div>
              <div class="flex items-center justify-between border-b pb-2">
                <span class="text-gray-700">D (Token数量)</span>
                <span class="font-mono font-bold text-purple-600">300 × 10<sup>9</sup> = 300,000,000,000</span>
              </div>
              <div class="flex items-center justify-between border-b pb-2">
                <span class="text-gray-700">计算</span>
                <span class="font-mono text-sm text-gray-600">6 × (0.5×10<sup>9</sup>) × (300×10<sup>9</sup>)</span>
              </div>
              <div class="flex items-center justify-between bg-blue-100 p-3 rounded-lg">
                <span class="font-bold text-gray-800">Total FLOPs</span>
                <span class="font-mono font-bold text-2xl text-blue-700">9 × 10<sup>20</sup></span>
              </div>
            </div>

            <div class="bg-yellow-100 p-4 rounded-lg mt-4">
              <p class="text-sm text-yellow-800">
                <strong>📌 结论：</strong>完成这次训练大约需要 <strong>9×10<sup>20</sup></strong> 次浮点运算，相当于<strong>900,000,000,000,000,000,000次计算</strong>！
              </p>
            </div>
          </div>

          <!-- 步骤2: 估算硬件有效算力 -->
          <div class="bg-white p-6 rounded-xl border-2 border-purple-200">
            <div class="flex items-center mb-4">
              <div class="bg-purple-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold mr-4">2</div>
              <h5 class="text-lg font-bold text-purple-800">估算10张3090的有效算力</h5>
            </div>

            <div class="bg-red-50 p-4 rounded-lg mb-4 border-l-4 border-red-500">
              <p class="text-red-800 font-semibold">⚠️ 这是估算中最具挑战性也最容易产生误差的部分！</p>
            </div>

            <h6 class="font-bold text-gray-800 mb-3">1️⃣ 理论峰值算力</h6>
            <div class="grid md:grid-cols-2 gap-4 mb-4">
              <div class="bg-gray-50 p-4 rounded-lg">
                <p class="font-semibold text-gray-700 mb-2">FP32 (单精度)</p>
                <p class="text-3xl font-bold text-gray-600">~35.6 TFLOPS</p>
                <p class="text-xs text-gray-500 mt-1">每张3090卡</p>
              </div>
              <div class="bg-purple-50 p-4 rounded-lg border-2 border-purple-400">
                <p class="font-semibold text-purple-700 mb-2">BF16/FP16 (混合精度)</p>
                <p class="text-3xl font-bold text-purple-600">~142 TFLOPS</p>
                <p class="text-xs text-purple-600 mt-1">使用Tensor Cores ⚡</p>
              </div>
            </div>
            <p class="text-sm text-gray-600 mb-4">
              💡 TFLOPS = 10<sup>12</sup> FLOPs/second。模型预训练通常使用 <strong>BF16/FP16混合精度</strong>来加速，所以我们以 <strong>142 TFLOPS</strong> 作为理论峰值。
            </p>

            <h6 class="font-bold text-gray-800 mb-3">2️⃣ 有效算力与计算利用率 (MFU/HFU)</h6>
            <div class="bg-gradient-to-r from-yellow-50 to-orange-50 p-5 rounded-lg mb-4">
              <p class="text-gray-800 mb-3">
                在实际训练中，GPU<strong>不可能100%的时间都在进行数学计算</strong>。由于以下瓶颈，实际的有效算力远低于理论峰值：
              </p>
              <ul class="space-y-2 text-sm text-gray-700">
                <li class="flex items-start">
                  <span class="text-orange-500 mr-2">•</span>
                  <span><strong>数据加载</strong>：从硬盘/CPU到GPU的数据传输</span>
                </li>
                <li class="flex items-start">
                  <span class="text-orange-500 mr-2">•</span>
                  <span><strong>显存读写</strong>：参数、激活值的内存访问</span>
                </li>
                <li class="flex items-start">
                  <span class="text-orange-500 mr-2">•</span>
                  <span><strong>通信开销</strong>：多GPU之间的梯度同步</span>
                </li>
                <li class="flex items-start">
                  <span class="text-orange-500 mr-2">•</span>
                  <span><strong>计算依赖</strong>：某些操作必须等待前一步完成</span>
                </li>
              </ul>
            </div>

            <div class="bg-purple-50 p-5 rounded-lg mb-4">
              <p class="font-semibold text-purple-800 mb-3">📐 MFU (Model FLOPs Utilization)</p>
              <p class="text-sm text-gray-700 mb-3">
                这个比例被称为 <strong>模型浮点运算利用率</strong> 或 <strong>硬件浮点运算利用率 (HFU)</strong>，表示实际算力占理论峰值的百分比。
              </p>
              <div class="bg-white p-4 rounded-lg">
                <p class="text-gray-700 mb-2">对于<strong>3090这样的消费级卡</strong>，在没有经过极致优化的训练框架和代码下：</p>
                <p class="text-center text-3xl font-bold text-purple-600">MFU ≈ 30% - 50%</p>
                <p class="text-sm text-gray-600 text-center mt-2">这是一个比较合理的范围</p>
              </div>
            </div>

            <h6 class="font-bold text-gray-800 mb-3">3️⃣ 计算10张卡的总有效算力</h6>
            <div class="grid md:grid-cols-2 gap-4">
              <div class="bg-gradient-to-br from-orange-50 to-red-50 p-5 rounded-xl border-2 border-orange-300">
                <p class="font-bold text-orange-800 mb-3">较低利用率 (30%) - 悲观情况</p>
                <div class="space-y-2 text-sm">
                  <p class="text-gray-700">142 TFLOPS/GPU × 0.30 × 10 GPUs</p>
                  <p class="text-gray-700">≈ 426 TFLOPS</p>
                  <div class="bg-white p-3 rounded-lg mt-3">
                    <p class="font-mono font-bold text-orange-600 text-lg">= 4.26 × 10<sup>14</sup> FLOPs/s</p>
                  </div>
                </div>
              </div>

              <div class="bg-gradient-to-br from-green-50 to-emerald-50 p-5 rounded-xl border-2 border-green-300">
                <p class="font-bold text-green-800 mb-3">较高利用率 (50%) - 乐观情况</p>
                <div class="space-y-2 text-sm">
                  <p class="text-gray-700">142 TFLOPS/GPU × 0.50 × 10 GPUs</p>
                  <p class="text-gray-700">≈ 710 TFLOPS</p>
                  <div class="bg-white p-3 rounded-lg mt-3">
                    <p class="font-mono font-bold text-green-600 text-lg">= 7.1 × 10<sup>14</sup> FLOPs/s</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 步骤3: 计算总训练时间 -->
          <div class="bg-white p-6 rounded-xl border-2 border-green-200">
            <div class="flex items-center mb-4">
              <div class="bg-green-600 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold mr-4">3</div>
              <h5 class="text-lg font-bold text-green-800">计算总训练时间</h5>
            </div>

            <p class="text-gray-700 mb-4">现在我们用总计算量除以有效算力：</p>

            <div class="bg-gray-900 text-cyan-400 p-4 rounded-lg font-mono text-center mb-6">
              Total Time = Total FLOPs / Effective FLOPS
            </div>

            <div class="space-y-6">
              <!-- 乐观情况 -->
              <div class="bg-gradient-to-r from-green-50 to-emerald-50 p-5 rounded-xl">
                <h6 class="font-bold text-green-800 mb-3">✅ 按较高利用率 (50%) 计算 - 乐观情况</h6>
                <div class="space-y-3">
                  <div class="bg-white p-4 rounded-lg">
                    <p class="text-gray-700 mb-2">Time = 9×10<sup>20</sup> / 7.1×10<sup>14</sup></p>
                    <p class="text-gray-700">≈ <strong>1.267 × 10<sup>6</sup> seconds</strong></p>
                  </div>
                  <div class="bg-white p-4 rounded-lg">
                    <p class="text-gray-700 mb-2">换算成天：</p>
                    <p class="text-gray-700">1.267×10<sup>6</sup> / (3600 × 24)</p>
                    <div class="text-center mt-3">
                      <p class="text-5xl font-bold text-green-600">≈ 14.7 天</p>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 悲观情况 -->
              <div class="bg-gradient-to-r from-orange-50 to-red-50 p-5 rounded-xl">
                <h6 class="font-bold text-orange-800 mb-3">⚠️ 按较低利用率 (30%) 计算 - 悲观情况</h6>
                <div class="space-y-3">
                  <div class="bg-white p-4 rounded-lg">
                    <p class="text-gray-700 mb-2">Time = 9×10<sup>20</sup> / 4.26×10<sup>14</sup></p>
                    <p class="text-gray-700">≈ <strong>2.11 × 10<sup>6</sup> seconds</strong></p>
                  </div>
                  <div class="bg-white p-4 rounded-lg">
                    <p class="text-gray-700 mb-2">换算成天：</p>
                    <p class="text-gray-700">2.11×10<sup>6</sup> / (3600 × 24)</p>
                    <div class="text-center mt-3">
                      <p class="text-5xl font-bold text-orange-600">≈ 24.4 天</p>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 综合结论 -->
              <div class="bg-gradient-to-r from-blue-100 to-purple-100 p-6 rounded-xl border-2 border-blue-400">
                <p class="text-center text-2xl font-bold text-blue-800 mb-2">
                  📌 综上所述：<span class="text-blue-600">2-3.5周</span>
                </p>
                <p class="text-center text-gray-700">是一个比较科学和现实的估算范围</p>
              </div>
            </div>
          </div>

          <!-- 影响因素 -->
          <div class="bg-white p-6 rounded-xl border-2 border-indigo-200">
            <h5 class="text-lg font-bold text-indigo-800 mb-4">🔍 影响时间的其它关键因素</h5>
            <div class="space-y-4">
              <div class="bg-indigo-50 p-4 rounded-lg">
                <p class="font-semibold text-indigo-800 mb-2">1. 训练框架和代码优化</p>
                <p class="text-sm text-gray-700">
                  使用像 <strong>DeepSpeed、Megatron-LM</strong> 这样高度优化的框架，并正确配置<strong>ZeRO、流水线并行</strong>等技术，可以显著提高MFU。
                </p>
                <p class="text-xs text-indigo-600 mt-1">💡 优化良好的框架可将MFU从30%提升到50%甚至更高</p>
              </div>

              <div class="bg-purple-50 p-4 rounded-lg">
                <p class="font-semibold text-purple-800 mb-2">2. 显存 (VRAM)</p>
                <p class="text-sm text-gray-700">
                  0.5B模型本身不大，10张3090（每张24GB）的显存足够放下模型参数、梯度和优化器状态，并允许使用<strong>较大的batch size</strong>，这有利于提高计算效率。
                </p>
                <p class="text-xs text-purple-600 mt-1">✅ 更大的batch size → 更高的GPU利用率</p>
              </div>

              <div class="bg-blue-50 p-4 rounded-lg">
                <p class="font-semibold text-blue-800 mb-2">3. 互联带宽</p>
                <p class="text-sm text-gray-700 mb-2">
                  10张卡的连接方式对训练速度影响巨大：
                </p>
                <div class="grid md:grid-cols-2 gap-3 text-xs">
                  <div class="bg-white p-3 rounded">
                    <p class="font-semibold text-green-700">✅ 单台服务器内（NVLink/PCIe）</p>
                    <p class="text-gray-600">带宽高，通信快</p>
                  </div>
                  <div class="bg-white p-3 rounded">
                    <p class="font-semibold text-red-700">❌ 多台机器（以太网）</p>
                    <p class="text-gray-600">带宽低，通信慢</p>
                  </div>
                </div>
              </div>

              <div class="bg-green-50 p-4 rounded-lg">
                <p class="font-semibold text-green-800 mb-2">4. 数据加载</p>
                <p class="text-sm text-gray-700">
                  数据预处理和从硬盘到GPU的加载速度必须<strong>跟上GPU的计算速度</strong>，否则GPU会"饿死"（空闲等待数据），从而降低整体效率。
                </p>
                <p class="text-xs text-green-600 mt-1">🔧 使用SSD、多进程预加载、数据缓存等技术优化</p>
              </div>

              <div class="bg-red-50 p-4 rounded-lg">
                <p class="font-semibold text-red-800 mb-2">5. 稳定性和中断</p>
                <p class="text-sm text-gray-700">
                  长时间训练任务可能会因为硬件或软件问题中断。算上<strong>Debug、重启、从checkpoint加载</strong>的时间，实际花费的总时长通常会比纯计算时间更长。
                </p>
                <p class="text-xs text-red-600 mt-1">⚠️ 建议预留10-20%的时间buffer</p>
              </div>
            </div>
          </div>

          <!-- 与SFT对比 -->
          <div class="bg-gradient-to-br from-purple-600 to-pink-600 text-white p-6 rounded-xl">
            <h5 class="text-xl font-bold mb-4 flex items-center">
              <span class="text-3xl mr-3">⚡</span>
              而SFT只需要...
            </h5>
            <div class="grid md:grid-cols-2 gap-6">
              <div class="bg-white bg-opacity-20 backdrop-blur p-5 rounded-lg">
                <p class="font-bold mb-2">硬件配置</p>
                <p class="text-3xl font-bold mb-2">1-4 张 GPU</p>
                <p class="text-sm opacity-90">vs 预训练的10-1000张</p>
              </div>
              <div class="bg-white bg-opacity-20 backdrop-blur p-5 rounded-lg">
                <p class="font-bold mb-2">训练时间</p>
                <p class="text-3xl font-bold mb-2">数小时-2天</p>
                <p class="text-sm opacity-90">vs 预训练的2-4周</p>
              </div>
            </div>
            <div class="mt-6 bg-white bg-opacity-30 backdrop-blur p-5 rounded-lg text-center">
              <p class="text-2xl font-bold">
                ⚡ SFT时间 ≈ 预训练的 0.5% - 5%
              </p>
              <p class="text-lg mt-2 opacity-90">这就是为什么个人开发者也能快速迭代！</p>
            </div>
          </div>

          <!-- 实际案例参考 -->
          <div class="bg-gradient-to-r from-cyan-50 to-blue-50 p-6 rounded-xl border-l-4 border-cyan-600">
            <h5 class="text-lg font-bold text-cyan-800 mb-4">📚 真实案例参考</h5>
            <div class="space-y-3">
              <div class="bg-white p-4 rounded-lg">
                <p class="font-semibold text-gray-800 mb-2">LLaMA 65B (Meta)</p>
                <p class="text-sm text-gray-700">• 参数：650亿 • 数据：1.4万亿tokens • 硬件：2048张A100 • 时间：约21天</p>
              </div>
              <div class="bg-white p-4 rounded-lg">
                <p class="font-semibold text-gray-800 mb-2">GPT-3 175B (OpenAI)</p>
                <p class="text-sm text-gray-700">• 参数：1750亿 • 数据：300亿tokens • 硬件：数千张V100 • 时间：数周到数月</p>
              </div>
              <div class="bg-white p-4 rounded-lg">
                <p class="font-semibold text-gray-800 mb-2">Qwen2-7B (阿里)</p>
                <p class="text-sm text-gray-700">• 参数：70亿 • 数据：3万亿tokens • 硬件：未公开 • 时间：数周</p>
              </div>
            </div>
            <p class="text-sm text-cyan-700 mt-4">
              💡 <strong>规律：</strong>即使是科技巨头，预训练也需要按<strong>周</strong>计算时间；而SFT通常只需要<strong>小时到天</strong>！
            </p>
          </div>
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
        <div class="max-w-2xl mx-auto" style="max-height: 400px;">
          <InteractiveChart
            :data="pretrainingDataSourcesChart"
            type="pie"
            :options="{ 
              plugins: { legend: { position: 'right' } },
              maintainAspectRatio: true,
              aspectRatio: 2
            }"
          />
        </div>
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
          <div class="bg-yellow-100 border-l-4 border-yellow-600 p-4 mb-4 rounded">
            <p class="font-bold text-yellow-900 mb-2">⚠️ 重要：预训练通常不到1个epoch！</p>
            <p class="text-sm text-yellow-800">
              由于数据规模巨大（万亿tokens），预训练通常只进行一次遍历（<1 epoch）。
              训练进度按<strong>步数/tokens处理量</strong>衡量，而非epoch数。
              例如：LLaMA 65B在1.4T tokens上训练约21天（1 epoch）。
            </p>
          </div>
          <div class="grid md:grid-cols-3 gap-4 mt-6">
            <div class="bg-blue-50 p-4 rounded-lg">
              <p class="font-bold text-blue-800">初期（0-20%数据）</p>
              <p class="text-sm text-gray-700">损失快速下降，学习基本语法和词汇</p>
            </div>
            <div class="bg-indigo-50 p-4 rounded-lg">
              <p class="font-bold text-indigo-800">中期（20-80%数据）</p>
              <p class="text-sm text-gray-700">持续改进，掌握复杂语言模式和知识</p>
            </div>
            <div class="bg-purple-50 p-4 rounded-lg">
              <p class="font-bold text-purple-800">后期（80-100%数据）</p>
              <p class="text-sm text-gray-700">缓慢收敛，微调细节，趋于稳定</p>
            </div>
          </div>
        </div>
      </div>

      <!-- 预训练代码示例 -->
      <CodeBlock
        title="预训练过程完整模拟"
        file-path="code/part1/01_pretraining_simulation.py"
        language="Python"
        :runnable="true"
        description="运行此代码可以看到预训练的完整流程：加载数据→分词→预测下一个词→计算损失→更新参数"
        :code="`# 预训练模拟器 - 简化版
import random
from typing import List, Dict

class SimplePretraining:
    def __init__(self, vocab_size: int = 1000):
        self.vocab_size = vocab_size
        self.model_params = [random.random() for _ in range(100)]
        
    def load_text_data(self) -> List[str]:
        # 模拟加载海量文本（实际是万亿tokens）
        return [
            '人工智能正在改变世界',
            '机器学习是AI的核心技术',
            '深度学习使用神经网络'
        ]
    
    def predict_next_token(self, context_tokens: List[int]):
        # 预测下一个token的概率分布
        predictions = {i: random.random() for i in range(5)}
        total = sum(predictions.values())
        return {k: v/total for k, v in predictions.items()}
    
    def train_epoch(self, texts: List[str]) -> float:
        total_loss = 0
        for text in texts:
            tokens = self.tokenize(text)
            # 对每个位置预测下一个token
            for i in range(len(tokens) - 1):
                predictions = self.predict_next_token(tokens[:i+1])
                loss = self.calculate_loss(predictions, tokens[i+1])
                total_loss += loss
        return total_loss / len(texts)

# 运行预训练
model = SimplePretraining()
model.pretrain(num_epochs=10)

# 输出示例：
# Epoch 1/10 | Loss: 2.3456
# Epoch 2/10 | Loss: 2.1234
# ...
# ✅ 预训练完成！`"
      />

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

      <!-- 📝 预训练知识测验 -->
      <div class="my-8 space-y-4">
        <div class="flex items-center space-x-3 mb-6">
          <span class="text-4xl">🧠</span>
          <h3 class="text-2xl font-bold text-indigo-700">即学即测：预训练阶段</h3>
        </div>

        <QuizBox
          question="Q1. 预训练阶段，模型主要在学习什么？"
          :options="[
            '如何遵循人类指令',
            '语言的统计规律和世界知识',
            '如何进行特定任务（如翻译、问答）',
            '如何拒绝有害请求'
          ]"
          :correctAnswer="1"
          explanation="预训练阶段使用无监督学习，通过大量文本训练Next Token Prediction任务。在这个过程中，模型学习到：①语言的语法、词汇、句法结构；②世界知识（历史、科学、文化等）；③常识推理能力；④基本的语言理解能力。此时的模型像一个博学但不听话的学生——知道很多，但不知道如何按人类意图回答。"
        />

        <QuizBox
          question="Q2. 为什么预训练使用Next Token Prediction，而不是直接训练问答？"
          :options="[
            '因为Next Token Prediction更简单',
            '因为没有足够的问答数据',
            '因为Next Token Prediction能自动从无标注文本中学习',
            '因为Next Token Prediction训练更快'
          ]"
          :correctAnswer="2"
          explanation="<strong>核心原因是能够利用海量无标注文本！</strong><br><br>
          <strong>Next Token Prediction的优势：</strong><br>
          1. <strong>自监督学习</strong>：不需要人工标注，每个token都是下一个token的标签，可以利用互联网上的所有文本<br>
          2. <strong>知识学习</strong>：通过预测下一个词，模型学会语法规则、世界知识、常识推理<br>
          3. <strong>数据规模</strong>：问答数据需要人工标注（几十万条），而网页文本无需标注（数万亿tokens）<br><br>
          <strong>类比：</strong>就像学习语言，不是先学'如何回答问题'，而是先大量阅读，建立语感和知识，然后才学习对话技巧。"
        />

        <QuizBox
          question="Q3. 预训练模型输出'人工智能正在改变...'后，如何预测下一个词？"
          :options="[
            '随机选择一个词',
            '根据语法规则选择',
            '计算所有候选词的概率分布，选择概率最高的',
            '查找训练数据中的相同句子'
          ]"
          :correctAnswer="2"
          explanation="预训练模型使用<strong>概率预测</strong>机制：<br><br>
          1. <strong>前向传播</strong>：输入'人工智能正在改变'，模型输出所有词汇的概率分布<br>
          2. <strong>概率示例</strong>：'世界'(0.35)、'生活'(0.25)、'行业'(0.15)、'未来'(0.10)、其他(0.15)<br>
          3. <strong>选择策略</strong>：通常选择概率最高的词（greedy），或者使用采样方法增加多样性<br>
          4. <strong>训练目标</strong>：通过大量数据训练，让模型对正确词的预测概率越来越高<br><br>
          这就是为什么同样的开头，模型每次生成的内容可能不同——因为是基于概率分布采样的！"
        />
      </div>
    </section>

    <!--数据对比示例 - 放在两个阶段之间 -->
    <PretrainingVsSFTData />

    <!-- 模型对比代码示例 -->
    <CodeBlock
      title="预训练模型 vs SFT模型对比演示"
      file-path="code/part1/02_sft_vs_pretraining.py"
      language="Python"
      :runnable="true"
      description="此代码直观展示同一个问题，预训练模型和SFT模型的不同回答方式"
      :code="`# 对比预训练模型和SFT模型
class BaseModel:
    '''预训练基座模型'''
    def generate(self, prompt: str) -> str:
        # 可能发散，不一定直接回答
        if '总结' in prompt:
            return '人工智能是一个很有趣的话题。它涉及到计算机、算法...'
        return '我可以生成文本，但可能不会直接回答您的问题。'

class SFTModel:
    '''经过SFT的模型'''
    def generate(self, prompt: str) -> str:
        # 理解用户意图，给出针对性回答
        if '总结' in prompt:
            return '人工智能(AI)是指让计算机系统模拟人类智能行为的技术。'
        return '我会尽力按照您的指令来回答问题。'

# 测试对比
prompt = '请总结一下人工智能的定义'
base_model = BaseModel()
sft_model = SFTModel()

print('基座模型:', base_model.generate(prompt))
# 输出：人工智能是一个很有趣的话题...（发散）

print('SFT模型:', sft_model.generate(prompt))
# 输出：人工智能(AI)是指...（直接回答）`"
    />

    <!-- 数据规模对比代码 -->
    <CodeBlock
      title="数据规模对比可视化"
      file-path="code/part1/03_data_scale_comparison.py"
      language="Python"
      :runnable="true"
      description="生成可视化图表，展示预训练和SFT的数据规模差异（需要matplotlib）"
      :code="`# 数据规模分析和可视化
import matplotlib.pyplot as plt

class DataScaleAnalyzer:
    def __init__(self):
        self.pretraining_data = {
            'tokens': 1_000_000_000_000,  # 1万亿
            'storage_tb': 5_000
        }
        self.sft_data = {
            'samples': 10_000,
            'tokens': 5_000_000,  # 500万
            'storage_mb': 50
        }
    
    def visualize_comparison(self):
        # 生成对比图表
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        # Token数量对比（对数尺度）
        axes[0].bar(['预训练', 'SFT'], 
                   [self.pretraining_data['tokens'], 
                    self.sft_data['tokens']],
                   color=['#3b82f6', '#a855f7'])
        axes[0].set_yscale('log')
        axes[0].set_title('数据规模对比 - Tokens')
        
        plt.savefig('data_scale_comparison.png')
        print('图表已保存！')

analyzer = DataScaleAnalyzer()
analyzer.visualize_comparison()`"
    />

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

      <!-- 📝 SFT知识测验 -->
      <div class="my-8 space-y-4">
        <div class="flex items-center space-x-3 mb-6">
          <span class="text-4xl">🧠</span>
          <h3 class="text-2xl font-bold text-purple-700">即学即测：SFT阶段</h3>
        </div>

        <QuizBox
          question="Q4. SFT训练中，模型的哪些参数通常会被更新？"
          :options="[
            '只更新最后一层参数',
            '根据方法不同，可能更新全部参数或部分参数（如LoRA）',
            '只更新embedding层',
            '完全不更新参数，只调整输出策略'
          ]"
          :correctAnswer="1"
          explanation="<strong>根据方法不同，SFT有多种参数更新策略：</strong><br><br>
          <strong>1. 全参数微调（Full Fine-tuning）</strong><br>
          • 更新模型的<strong>所有参数</strong><br>
          • 效果最好，但需要大量显存<br>
          • 7B模型需要约80GB显存<br><br>
          <strong>2. LoRA（Low-Rank Adaptation）</strong><br>
          • 冻结原模型，只训练<strong>低秩矩阵</strong><br>
          • 只需更新0.1-1%的参数<br>
          • 显存需求大幅降低（约1/4）<br><br>
          <strong>3. Adapter、Prefix-tuning等</strong><br>
          • 插入新的小模块或前缀<br>
          • 更新参数更少<br><br>
          <strong>选择标准：</strong><br>
          • 资源充足 + 追求极致效果 → 全参数<br>
          • 资源有限 + 效果还行即可 → LoRA<br>
          • 多任务切换 → Adapter"
        />

        <QuizBox
          question="Q5. 同样的文本，在预训练和SFT中的处理方式有何不同？"
          :options="[
            '完全相同，都是预测下一个token',
            'SFT会对部分文本（如instruction）进行mask，只计算response的loss',
            'SFT使用更复杂的loss函数',
            'SFT需要对文本进行特殊编码'
          ]"
          :correctAnswer="1"
          explanation="<strong>SFT的关键技巧：只对答案部分计算loss！</strong><br><br>
          <strong>预训练：</strong><br>
          输入：'今天天气真好，我想去'<br>
          目标：预测每个位置的下一个token<br>
          计算loss：对所有token位置计算<br><br>
          <strong>SFT：</strong><br>
          输入：'[Instruction] 翻译成英文：你好 [Response] Hello'<br>
          目标：只预测Response部分<br>
          计算loss：只对'Hello'部分计算，Instruction部分mask掉<br><br>
          <strong>为什么这样做？</strong><br><br>
          1. <strong>避免浪费</strong>：我们不需要模型学会预测Instruction<br>
          2. <strong>更高效</strong>：集中优化Response质量<br>
          3. <strong>防止混淆</strong>：如果对Instruction也计算loss，模型可能学会'重复instruction'来降低loss<br><br>
          <strong>实现方式：</strong>通过attention_mask或labels=-100来mask掉instruction部分。"
        />

        <QuizBox
          question="Q6. 为什么说SFT数据质量比数量更重要？"
          :options="[
            '因为模型显存有限，装不下太多数据',
            '因为SFT是行为塑造，少量高质量示范比大量低质量数据更有效',
            '因为标注数据很贵',
            '因为训练时间有限'
          ]"
          :correctAnswer="1"
          explanation="<strong>SFT的本质是'行为示范'，而非'知识灌输'！</strong><br><br>
          <strong>真实对比：</strong><br>
          • <strong>1000条高质量数据</strong>：格式统一、回答准确、风格一致 → 模型效果优秀 ✅<br>
          • <strong>10万条低质量数据</strong>：格式混乱、回答矛盾、质量参差 → 模型效果糟糕 ❌<br><br>
          <strong>为什么质量更重要？</strong><br><br>
          1. <strong>模式学习</strong>：SFT是让模型学习'如何回答'的模式，而非记忆答案<br>
          2. <strong>快速收敛</strong>：高质量数据让模型快速理解期望的行为<br>
          3. <strong>避免混淆</strong>：低质量数据会给模型矛盾的信号，导致训练混乱<br>
          4. <strong>泛化能力</strong>：好的示范让模型学会通用的响应模式<br><br>
          <strong>知名案例：</strong><br>
          • Alpaca：只用52K条高质量数据，效果惊人<br>
          • Vicuna：用70K ShareGPT对话数据，质量优于很多大数据集模型<br><br>
          <strong>记住：</strong>100条完美示范 > 10000条噪声数据！"
        />
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

      <!-- 📝 数据规模与成本对比测验 -->
      <div class="my-8 space-y-4">
        <div class="flex items-center space-x-3 mb-6">
          <span class="text-4xl">🧠</span>
          <h3 class="text-2xl font-bold text-blue-700">即学即测：数据规模与成本</h3>
        </div>

        <QuizBox
          question="Q7. 预训练和SFT的数据量通常相差多少？"
          :options="[
            '相差10倍左右',
            '相差100倍左右',
            '相差100,000倍以上',
            '数据量差不多'
          ]"
          :correctAnswer="2"
          explanation="<strong>正确答案是相差100,000倍以上！</strong><br><br>
          <strong>真实数据对比：</strong><br>
          • <strong>预训练</strong>：通常使用数千亿到数万亿tokens<br>
          &nbsp;&nbsp;例如：LLaMA 65B使用1.4万亿tokens<br>
          • <strong>SFT</strong>：通常只需几千到几十万条样本<br>
          &nbsp;&nbsp;例如：Alpaca只用了52K条instruction数据<br><br>
          <strong>换算一下：</strong><br>
          • 预训练：1.4万亿 tokens ≈ 700万本书<br>
          • SFT：5万条 × 平均200 tokens = 1000万 tokens ≈ 5000本书<br>
          • 差距：1.4万亿 / 1000万 = <strong>14万倍</strong>！<br><br>
          这就是为什么预训练需要大公司的资源（数千万美元），而SFT可以由小团队完成（几千美元）。"
        />

        <QuizBox
          question="Q8. 为什么说'预训练是地基，SFT是装修'？"
          :options="[
            '因为预训练更重要，SFT不重要',
            '因为预训练建立能力基础，SFT塑造行为模式',
            '因为预训练花费更多钱',
            '因为SFT只是表面工作'
          ]"
          :correctAnswer="1"
          explanation="这个比喻非常贴切：<br>
          <strong>预训练=地基：</strong><br>
          • 决定了房子能建多高（模型能力上限）<br>
          • 一旦完成就很难改变<br>
          • 需要海量资源（数据、算力）<br>
          • 建立语言理解、知识储备等核心能力<br><br>
          <strong>SFT=装修：</strong><br>
          • 在坚实地基上塑造风格和用途<br>
          • 相对容易调整和优化<br>
          • 资源需求小得多<br>
          • 让模型变得听话、有用、符合特定需求<br><br>
          没有好地基，再好的装修也无济于事；有了好地基，合适的装修能让房子物尽其用。"
        />
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

      <!-- 📝 依赖关系测验 -->
      <div class="my-8 space-y-4">
        <div class="flex items-center space-x-3 mb-6">
          <span class="text-4xl">🧠</span>
          <h3 class="text-2xl font-bold text-amber-700">即学即测：两阶段依赖关系</h3>
        </div>

        <QuizBox
          question="Q9. 为什么SFT不能拯救一个预训练效果差的模型？"
          :options="[
            'SFT的数据量太小，无法弥补预训练的不足',
            'SFT主要是塑造行为，而非从零创造知识和能力',
            'SFT的成本太高，不值得在差模型上使用',
            'SFT会导致模型遗忘预训练知识'
          ]"
          :correctAnswer="1"
          explanation="<strong>SFT不是'知识注入器'，而是'行为塑造器'！</strong><br><br>
          <strong>为什么无法拯救差模型？</strong><br><br>
          1. <strong>数据量差距</strong><br>
          • 预训练：数千亿到万亿tokens<br>
          • SFT：几千到几万条样本<br>
          • 差距：10万倍以上<br>
          • 结论：SFT的数据量不足以弥补预训练的缺陷<br><br>
          2. <strong>学习目标不同</strong><br>
          • 预训练：学习语言规律、世界知识、推理能力<br>
          • SFT：学习如何表达、如何遵循指令<br>
          • SFT假设模型已经'懂'了，只是不知道'怎么说'<br><br>
          3. <strong>形象比喻</strong><br>
          • 预训练差=地基不牢<br>
          • SFT=装修<br>
          • 在沙滩上装修（地基差），房子还是会塌<br><br>
          <strong>实际建议：</strong><br>
          选择一个预训练效果好的基座模型，然后再进行SFT，事半功倍！"
        />

        <QuizBox
          question="Q10. 如果你只有一张3090显卡和一周时间，应该做什么？"
          :options="[
            '从零开始预训练一个小模型',
            '选择一个好的开源模型进行SFT',
            '同时做预训练和SFT',
            '只收集数据，不做训练'
          ]"
          :correctAnswer="1"
          explanation="<strong>毫无疑问，应该选择SFT！</strong><br><br>
          <strong>资源现实：</strong><br>
          • <strong>1张3090 + 1周时间</strong>：根本无法完成有意义的预训练<br>
          &nbsp;&nbsp;- 预训练需要：10-1000+张GPU，数周到数月<br>
          &nbsp;&nbsp;- 即使是0.5B的小模型，1张卡也需要数月时间<br><br>
          <strong>最佳策略：SFT</strong><br>
          1. <strong>选择基座模型</strong>：从HuggingFace下载高质量开源模型（如Qwen2-7B、LLaMA3-8B）<br>
          2. <strong>准备数据</strong>：收集/标注1000-10000条高质量样本（1-2天）<br>
          3. <strong>使用LoRA</strong>：1张3090足够训练7B模型<br>
          4. <strong>快速迭代</strong>：一周内可以完成多轮实验<br><br>
          <strong>真实案例：</strong><br>
          • 个人开发者用1张3090，3天时间，基于LLaMA2微调出专业领域助手<br>
          • 创业团队用4张3090，一周完成医疗问答模型的SFT<br><br>
          <strong>记住：</strong>站在巨人的肩膀上（使用开源基座模型）+ SFT = 个人也能打造专属AI！"
        />

        <QuizBox
          question="Q11. 选择基座模型时，哪个因素最重要？"
          :options="[
            '模型的参数量越大越好',
            '模型在目标领域的预训练数据量和质量',
            '模型的开源协议',
            '模型的下载速度'
          ]"
          :correctAnswer="1"
          explanation="<strong>基座模型的领域契合度最重要！</strong><br><br>
          <strong>为什么？</strong><br>
          SFT只能激活和引导预训练阶段学到的知识，如果基座模型在预训练时根本没见过目标领域的数据，SFT也无能为力。<br><br>
          <strong>实际案例：</strong><br><br>
          <strong>场景1：中文医疗问答</strong><br>
          • ❌ <strong>差选择</strong>：英文为主的GPT-2（70亿参数）<br>
          &nbsp;&nbsp;- 中文能力差，医疗知识少<br>
          • ✅ <strong>好选择</strong>：中文医疗数据训练的Qwen2（7亿参数）<br>
          &nbsp;&nbsp;- 虽然参数更少，但中文和医疗知识更丰富<br><br>
          <strong>场景2：代码生成</strong><br>
          • ❌ <strong>差选择</strong>：通用对话模型（14亿参数）<br>
          • ✅ <strong>好选择</strong>：CodeLLaMA（7亿参数，代码数据预训练）<br><br>
          <strong>选择标准：</strong><br>
          1. <strong>领域契合度</strong> > 参数量<br>
          2. <strong>语言契合度</strong> > 模型架构<br>
          3. <strong>预训练质量</strong> > 模型大小<br><br>
          <strong>实用建议：</strong><br>
          在HuggingFace上搜索时，查看模型的训练数据分布，选择与你目标任务最匹配的！"
        />
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

      <!-- 📝 SFT作用与误区测验 -->
      <div class="my-8 space-y-4">
        <div class="flex items-center space-x-3 mb-6">
          <span class="text-4xl">🧠</span>
          <h3 class="text-2xl font-bold text-green-700">即学即测：SFT的真正作用</h3>
        </div>

        <QuizBox
          question="Q12. 以下哪个说法是错误的？"
          :options="[
            'SFT可以让模型学会新的任务格式',
            'SFT可以完全改变模型的知识储备',
            'SFT可以让模型遵循特定的输出风格',
            'SFT可以让模型拒绝有害请求'
          ]"
          :correctAnswer="1"
          explanation="<strong>错误的是'SFT可以完全改变模型的知识储备'。</strong><br><br>
          <strong>为什么这是错误的？</strong><br>
          • SFT的数据量太小（几千到几万条）<br>
          • 无法从根本上改变预训练学到的海量知识<br>
          • 只能<strong>激活、引导、塑造</strong>已有知识的表达方式<br><br>
          <strong>其他选项为什么正确？</strong><br>
          <strong>A. 学会新任务格式 ✅</strong><br>
          例如：教会模型输出JSON格式、Markdown表格等。预训练见过这些格式，SFT教会何时使用。<br><br>
          <strong>C. 特定输出风格 ✅</strong><br>
          例如：专业、友好、简洁、详细等不同风格。<br><br>
          <strong>D. 拒绝有害请求 ✅</strong><br>
          通过示范正确的拒绝方式，让模型学会识别和拒绝。<br><br>
          <strong>核心原则：</strong>SFT改变的是'如何说'，而非'知道什么'。"
        />

        <QuizBox
          question="Q13. 以下哪个场景最不适合使用SFT？"
          :options="[
            '让模型学会按特定格式输出JSON',
            '让模型从零学习一门新的编程语言',
            '让模型适应医疗问答的专业话术',
            '让模型拒绝回答有害问题'
          ]"
          :correctAnswer="1"
          explanation="<strong>正确答案是'从零学习新编程语言'。</strong><br><br>
          <strong>原因分析：</strong><br>
          SFT的核心是<strong>解锁和引导</strong>预训练阶段已有的知识，而不是注入新知识。<br><br>
          • <strong>选项A（JSON格式）</strong>：✅适合SFT。模型在预训练中见过JSON，只需通过SFT学会何时、如何输出。<br>
          • <strong>选项B（新语言）</strong>：❌不适合SFT。如果预训练阶段完全没见过这门语言，SFT很难让模型学会（数据量太小）。<br>
          • <strong>选项C（医疗话术）</strong>：✅适合SFT。预训练有医疗知识，SFT塑造专业表达方式。<br>
          • <strong>选项D（拒绝有害）</strong>：✅适合SFT。通过demonstration教会模型什么该拒绝。<br><br>
          <strong>记住：</strong>SFT is for alignment, not for learning from scratch!"
        />

        <QuizBox
          question="Q14. 关于Loss值，以下哪个说法最准确？"
          :options="[
            'Loss越低，模型质量越好',
            'Loss只是参考指标，必须结合实际输出质量评估',
            'SFT的Loss一定比预训练的Loss低',
            'Loss低于1.0就说明模型训练成功'
          ]"
          :correctAnswer="1"
          explanation="<strong>Loss只是参考，实际质量才是王道！</strong><br><br>
          <strong>真实案例：</strong><br>
          • v0.1模型：Loss = 0.89，但所有输出都是免责声明 ❌<br>
          • v1.1模型：Loss = 1.05，但输出质量优秀 ✅<br><br>
          <strong>为什么Loss会误导？</strong><br><br>
          1. <strong>模型可以'取巧'</strong><br>
          • 通过重复降低Loss（重复的token预测准确率高）<br>
          • 但输出质量很差<br><br>
          2. <strong>过拟合</strong><br>
          • 训练集Loss很低<br>
          • 测试时效果很差<br><br>
          3. <strong>数据问题</strong><br>
          • 如果数据都是'建议就医'，Loss会很低<br>
          • 但模型只会说这一句<br><br>
          <strong>正确做法：</strong><br>
          • Loss作为训练监控指标<br>
          • 定期人工测试输出质量<br>
          • 准备多样化的测试集<br>
          • 关注真实场景表现"
        />
      </div>
    </section>

    <!-- Part1 总结 -->
    <section class="my-16">
      <div class="card bg-gradient-to-br from-indigo-600 to-purple-600 text-white p-8">
        <h2 class="text-4xl font-bold mb-4 flex items-center">
          <span class="text-5xl mr-4">🎉</span>
          恭喜完成Part1学习！
        </h2>
        <p class="text-xl opacity-90 mb-6">你已经掌握了预训练与SFT的核心概念</p>
        
        <div class="grid md:grid-cols-3 gap-6 mt-8">
          <div class="bg-white bg-opacity-20 backdrop-blur p-5 rounded-xl">
            <div class="text-4xl mb-3">📚</div>
            <p class="font-bold text-lg mb-2">预训练</p>
            <p class="text-sm opacity-90">建立语言能力和知识基础</p>
          </div>
          <div class="bg-white bg-opacity-20 backdrop-blur p-5 rounded-xl">
            <div class="text-4xl mb-3">💼</div>
            <p class="font-bold text-lg mb-2">SFT</p>
            <p class="text-sm opacity-90">塑造行为和遵循指令</p>
          </div>
          <div class="bg-white bg-opacity-20 backdrop-blur p-5 rounded-xl">
            <div class="text-4xl mb-3">🚀</div>
            <p class="font-bold text-lg mb-2">实践路径</p>
            <p class="text-sm opacity-90">基座模型 + SFT = 专属AI</p>
          </div>
        </div>

        <div class="mt-8 bg-white bg-opacity-30 backdrop-blur p-6 rounded-xl">
          <p class="text-lg font-bold mb-3">💡 核心要点回顾：</p>
          <ul class="space-y-2 text-sm">
            <li>• 预训练建立能力上限，SFT释放和引导这些能力</li>
            <li>• 预训练需要海量资源，SFT人人可及</li>
            <li>• SFT是行为塑造而非知识灌输</li>
            <li>• 选择好的基座模型是SFT成功的关键</li>
          </ul>
        </div>
      </div>
    </section>

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
import CodeBlock from '../components/CodeBlock.vue'
import PretrainingVsSFTData from '../components/PretrainingVsSFTData.vue'

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

