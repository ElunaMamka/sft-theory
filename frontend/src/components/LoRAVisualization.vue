<template>
  <div class="my-12">
    <h2 class="text-3xl font-bold text-gray-800 mb-8 text-center">
      🔬 LoRA工作机制可视化详解
    </h2>

    <!-- 参数量对比 -->
    <div class="card mb-8 bg-gradient-to-br from-red-50 to-orange-50">
      <h3 class="text-2xl font-bold text-red-800 mb-6 flex items-center">
        <span class="text-4xl mr-3">📊</span>
        具体参数量对比（7B模型）
      </h3>

      <div class="grid md:grid-cols-2 gap-6 mb-6">
        <!-- 全量微调 -->
        <div class="bg-white p-6 rounded-xl shadow-lg border-2 border-red-200">
          <div class="flex items-center justify-between mb-4">
            <h4 class="font-bold text-xl text-red-700">全量微调</h4>
            <span class="text-3xl">😰</span>
          </div>
          
          <div class="space-y-3">
            <div class="bg-red-50 p-4 rounded-lg">
              <p class="text-sm text-gray-700 mb-1">总参数量</p>
              <p class="text-3xl font-bold text-red-800">7,000,000,000</p>
              <p class="text-sm text-gray-600 mt-1">（70亿参数）</p>
            </div>
            
            <div class="bg-red-50 p-3 rounded">
              <p class="text-sm font-semibold text-gray-800">训练参数</p>
              <p class="text-xl font-bold text-red-700">100%</p>
              <p class="text-xs text-gray-600">所有参数都需要训练</p>
            </div>
            
            <div class="bg-red-50 p-3 rounded">
              <p class="text-sm font-semibold text-gray-800">内存需求（FP32）</p>
              <p class="text-xl font-bold text-red-700">~98 GB</p>
              <p class="text-xs text-gray-600">模型 + 优化器 + 梯度 + 激活</p>
            </div>
            
            <div class="bg-red-50 p-3 rounded">
              <p class="text-sm font-semibold text-gray-800">存储（每任务）</p>
              <p class="text-xl font-bold text-red-700">~13 GB</p>
              <p class="text-xs text-gray-600">FP16格式</p>
            </div>
          </div>
        </div>

        <!-- LoRA -->
        <div class="bg-white p-6 rounded-xl shadow-lg border-2 border-green-200">
          <div class="flex items-center justify-between mb-4">
            <h4 class="font-bold text-xl text-green-700">LoRA (r=8)</h4>
            <span class="text-3xl">🎉</span>
          </div>
          
          <div class="space-y-3">
            <div class="bg-green-50 p-4 rounded-lg">
              <p class="text-sm text-gray-700 mb-1">LoRA参数量</p>
              <p class="text-3xl font-bold text-green-800">2,097,152</p>
              <p class="text-sm text-gray-600 mt-1">（约200万参数）</p>
            </div>
            
            <div class="bg-green-50 p-3 rounded">
              <p class="text-sm font-semibold text-gray-800">训练参数</p>
              <p class="text-xl font-bold text-green-700">0.03%</p>
              <p class="text-xs text-gray-600">仅训练LoRA部分</p>
            </div>
            
            <div class="bg-green-50 p-3 rounded">
              <p class="text-sm font-semibold text-gray-800">内存需求（混合）</p>
              <p class="text-xl font-bold text-green-700">~26 GB</p>
              <p class="text-xs text-gray-600">基座FP16 + LoRA FP32</p>
            </div>
            
            <div class="bg-green-50 p-3 rounded">
              <p class="text-sm font-semibold text-gray-800">存储（每任务）</p>
              <p class="text-xl font-bold text-green-700">~4 MB</p>
              <p class="text-xs text-gray-600">仅保存适配器</p>
            </div>
          </div>
        </div>
      </div>

      <!-- 改进幅度 -->
      <div class="bg-gradient-to-r from-orange-100 to-yellow-100 p-6 rounded-xl">
        <h4 class="font-bold text-orange-900 mb-4">✨ LoRA的改进</h4>
        <div class="grid md:grid-cols-4 gap-4">
          <div class="text-center">
            <p class="text-4xl font-bold text-orange-700">3,333x</p>
            <p class="text-sm text-gray-700 mt-1">参数量减少</p>
          </div>
          <div class="text-center">
            <p class="text-4xl font-bold text-orange-700">3.8x</p>
            <p class="text-sm text-gray-700 mt-1">内存节省</p>
          </div>
          <div class="text-center">
            <p class="text-4xl font-bold text-orange-700">3,250x</p>
            <p class="text-sm text-gray-700 mt-1">存储减少</p>
          </div>
          <div class="text-center">
            <p class="text-4xl font-bold text-orange-700">100x</p>
            <p class="text-sm text-gray-700 mt-1">训练速度提升</p>
          </div>
        </div>
      </div>
    </div>

    <!-- LoRA矩阵分解详解 -->
    <div class="card mb-8 bg-gradient-to-br from-purple-50 to-indigo-50">
      <h3 class="text-2xl font-bold text-purple-800 mb-6 flex items-center">
        <span class="text-4xl mr-3">🧮</span>
        LoRA矩阵分解详解
      </h3>

      <!-- 全量微调的权重更新 -->
      <div class="mb-8">
        <h4 class="font-bold text-lg text-gray-800 mb-4">传统全量微调：直接更新大矩阵</h4>
        <div class="bg-white p-6 rounded-xl">
          <div class="flex items-center justify-center space-x-4 mb-4">
            <div class="text-center">
              <div class="bg-blue-100 p-6 rounded-lg border-2 border-blue-300">
                <p class="font-mono text-sm text-blue-800 mb-2">W (原始权重)</p>
                <div class="grid grid-cols-8 gap-1">
                  <div v-for="i in 64" :key="i" class="w-3 h-3 bg-blue-400 rounded-sm"></div>
                </div>
                <p class="text-xs text-gray-600 mt-2">4096 × 4096</p>
              </div>
            </div>
            
            <div class="text-3xl">+</div>
            
            <div class="text-center">
              <div class="bg-red-100 p-6 rounded-lg border-2 border-red-300">
                <p class="font-mono text-sm text-red-800 mb-2">ΔW (更新)</p>
                <div class="grid grid-cols-8 gap-1">
                  <div v-for="i in 64" :key="i" class="w-3 h-3 bg-red-400 rounded-sm"></div>
                </div>
                <p class="text-xs text-gray-600 mt-2">4096 × 4096</p>
              </div>
            </div>
            
            <div class="text-3xl">=</div>
            
            <div class="text-center">
              <div class="bg-purple-100 p-6 rounded-lg border-2 border-purple-300">
                <p class="font-mono text-sm text-purple-800 mb-2">W' (新权重)</p>
                <div class="grid grid-cols-8 gap-1">
                  <div v-for="i in 64" :key="i" class="w-3 h-3 bg-purple-400 rounded-sm"></div>
                </div>
                <p class="text-xs text-gray-600 mt-2">4096 × 4096</p>
              </div>
            </div>
          </div>
          
          <div class="bg-red-50 p-4 rounded-lg mt-4">
            <p class="font-semibold text-red-900 mb-2">❌ 问题：</p>
            <p class="text-sm text-gray-700">需要训练 4096 × 4096 = <strong>16,777,216个参数</strong></p>
          </div>
        </div>
      </div>

      <!-- LoRA的低秩分解 -->
      <div>
        <h4 class="font-bold text-lg text-gray-800 mb-4">LoRA：低秩分解（r=8）</h4>
        <div class="bg-white p-6 rounded-xl">
          <div class="flex items-center justify-center space-x-3 mb-4">
            <div class="text-center">
              <div class="bg-blue-100 p-6 rounded-lg border-2 border-blue-300">
                <p class="font-mono text-sm text-blue-800 mb-2">W (冻结)</p>
                <div class="grid grid-cols-8 gap-1">
                  <div v-for="i in 64" :key="i" class="w-3 h-3 bg-gray-300 rounded-sm"></div>
                </div>
                <p class="text-xs text-gray-600 mt-2">4096 × 4096</p>
                <p class="text-xs text-blue-600 mt-1">🔒 不训练</p>
              </div>
            </div>
            
            <div class="text-3xl">+</div>
            
            <div class="text-center">
              <div class="bg-green-100 p-4 rounded-lg border-2 border-green-300">
                <p class="font-mono text-sm text-green-800 mb-2">B</p>
                <div class="grid grid-cols-2 gap-1">
                  <div v-for="i in 16" :key="i" class="w-3 h-3 bg-green-400 rounded-sm"></div>
                </div>
                <p class="text-xs text-gray-600 mt-2">4096 × 8</p>
              </div>
            </div>
            
            <div class="text-2xl">×</div>
            
            <div class="text-center">
              <div class="bg-green-100 p-4 rounded-lg border-2 border-green-300">
                <p class="font-mono text-sm text-green-800 mb-2">A</p>
                <div class="grid grid-cols-8 gap-1">
                  <div v-for="i in 16" :key="i" class="w-3 h-3 bg-green-500 rounded-sm"></div>
                </div>
                <p class="text-xs text-gray-600 mt-2">8 × 4096</p>
              </div>
            </div>
            
            <div class="text-3xl">=</div>
            
            <div class="text-center">
              <div class="bg-purple-100 p-6 rounded-lg border-2 border-purple-300">
                <p class="font-mono text-sm text-purple-800 mb-2">W' (新权重)</p>
                <div class="grid grid-cols-8 gap-1">
                  <div v-for="i in 64" :key="i" class="w-3 h-3 bg-purple-400 rounded-sm"></div>
                </div>
                <p class="text-xs text-gray-600 mt-2">4096 × 4096</p>
              </div>
            </div>
          </div>
          
          <div class="bg-green-50 p-4 rounded-lg mt-4">
            <p class="font-semibold text-green-900 mb-2">✅ LoRA优势：</p>
            <p class="text-sm text-gray-700 mb-2">
              只需训练 B 和 A：(4096 × 8) + (8 × 4096) = <strong>65,536个参数</strong>
            </p>
            <p class="text-sm font-bold text-green-700">
              参数减少：16,777,216 → 65,536（减少<strong>256倍</strong>！）
            </p>
          </div>
        </div>
      </div>

      <!-- 数学公式 -->
      <div class="bg-indigo-100 p-6 rounded-xl mt-6">
        <h4 class="font-bold text-indigo-900 mb-4">📐 数学表达</h4>
        <div class="bg-white p-4 rounded-lg space-y-3 font-mono text-sm">
          <div>
            <p class="text-gray-700">全量微调：</p>
            <p class="text-lg text-blue-700">W' = W + ΔW</p>
            <p class="text-xs text-gray-600">参数量：d × d（如 4096 × 4096）</p>
          </div>
          <div class="border-t pt-3">
            <p class="text-gray-700">LoRA：</p>
            <p class="text-lg text-green-700">W' = W + B × A</p>
            <p class="text-xs text-gray-600">参数量：d × r + r × d = 2dr（如 2 × 4096 × 8）</p>
          </div>
          <div class="border-t pt-3">
            <p class="text-gray-700">前向传播：</p>
            <p class="text-lg text-purple-700">h = x(W + BA) = xW + xBA</p>
            <p class="text-xs text-gray-600">可以分别计算，然后相加</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Hub-and-Spoke架构 -->
    <div class="card bg-gradient-to-br from-cyan-50 to-blue-50">
      <h3 class="text-2xl font-bold text-cyan-800 mb-6 flex items-center">
        <span class="text-4xl mr-3">🎯</span>
        Hub-and-Spoke 多任务架构
      </h3>

      <div class="bg-white p-8 rounded-xl">
        <!-- 架构图 -->
        <div class="flex items-center justify-center mb-8">
          <div class="relative">
            <!-- 中心：基座模型 -->
            <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-10">
              <div class="bg-gradient-to-br from-blue-500 to-indigo-600 text-white p-8 rounded-full shadow-2xl border-4 border-white">
                <div class="text-center">
                  <p class="text-2xl font-bold">🧠</p>
                  <p class="text-sm font-bold mt-1">基座模型</p>
                  <p class="text-xs">7B参数</p>
                </div>
              </div>
            </div>

            <!-- 辐条：LoRA适配器 -->
            <div class="grid grid-cols-3 gap-8" style="margin-top: 100px;">
              <div v-for="(task, index) in tasks" :key="index" class="text-center">
                <div class="bg-gradient-to-br from-green-400 to-emerald-500 text-white p-4 rounded-lg shadow-lg transform hover:scale-105 transition-transform">
                  <p class="text-xl mb-1">{{ task.icon }}</p>
                  <p class="text-xs font-bold">{{ task.name }}</p>
                  <p class="text-xs opacity-80">{{ task.size }}</p>
                </div>
                <!-- 连线 -->
                <div class="h-16 w-0.5 bg-gradient-to-b from-green-400 to-transparent mx-auto"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- 说明 -->
        <div class="grid md:grid-cols-2 gap-6">
          <div class="bg-blue-50 p-5 rounded-lg">
            <h4 class="font-bold text-blue-900 mb-3">🏠 Hub（中心）</h4>
            <ul class="space-y-2 text-sm text-gray-700">
              <li>• <strong>一个基座模型</strong>（7B参数）</li>
              <li>• 完全冻结，不训练</li>
              <li>• 所有任务共享</li>
              <li>• 内存中只加载一次</li>
              <li>• 存储：~13 GB</li>
            </ul>
          </div>

          <div class="bg-green-50 p-5 rounded-lg">
            <h4 class="font-bold text-green-900 mb-3">🎯 Spokes（辐条）</h4>
            <ul class="space-y-2 text-sm text-gray-700">
              <li>• <strong>多个LoRA适配器</strong>（每个2-4MB）</li>
              <li>• 每个任务一个适配器</li>
              <li>• 可以快速切换</li>
              <li>• 可以动态加载/卸载</li>
              <li>• 6个任务总计：~24 MB</li>
            </ul>
          </div>
        </div>

        <!-- 对比 -->
        <div class="mt-6 bg-gradient-to-r from-cyan-100 to-blue-100 p-5 rounded-xl">
          <h4 class="font-bold text-cyan-900 mb-3">💡 存储对比（6个任务）</h4>
          <div class="grid md:grid-cols-2 gap-4 text-sm">
            <div class="bg-white p-4 rounded">
              <p class="font-semibold text-red-700 mb-2">❌ 传统方案</p>
              <p>6个完整模型 × 13GB = <strong class="text-xl">78 GB</strong></p>
            </div>
            <div class="bg-white p-4 rounded">
              <p class="font-semibold text-green-700 mb-2">✅ LoRA方案</p>
              <p>1个基座(13GB) + 6个适配器(24MB) = <strong class="text-xl">~13 GB</strong></p>
            </div>
          </div>
          <p class="text-center mt-4 text-cyan-800 font-bold">节省空间：65 GB（83%减少）</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const tasks = ref([
  { name: '邮件总结', icon: '📧', size: '4 MB' },
  { name: '代码生成', icon: '💻', size: '4 MB' },
  { name: 'SQL查询', icon: '🗄️', size: '4 MB' },
  { name: '创意写作', icon: '✍️', size: '4 MB' },
  { name: '客服对话', icon: '💬', size: '4 MB' },
  { name: '中英翻译', icon: '🌐', size: '4 MB' }
])
</script>

<style scoped>
.grid-cols-8 {
  grid-template-columns: repeat(8, minmax(0, 1fr));
}
</style>

