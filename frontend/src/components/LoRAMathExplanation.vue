<template>
  <div class="my-12">
    <h2 class="text-3xl font-bold text-gray-800 mb-8 text-center">
      📐 LoRA的数学原理深度解析
    </h2>

    <!-- 核心公式 -->
    <div class="card mb-8 bg-gradient-to-br from-blue-50 to-indigo-50">
      <h3 class="text-2xl font-bold text-blue-800 mb-6 flex items-center">
        <span class="text-4xl mr-3">🧮</span>
        核心数学公式
      </h3>

      <div class="bg-white p-8 rounded-xl shadow-lg">
        <!-- 基本公式 -->
        <div class="mb-8">
          <h4 class="font-bold text-lg text-gray-800 mb-4">1. 基本公式</h4>
          <div class="bg-gray-50 p-6 rounded-lg border-2 border-blue-200">
            <div class="text-center space-y-4">
              <div>
                <p class="text-sm text-gray-600 mb-2">全量微调：</p>
                <p class="text-2xl font-mono text-blue-700">W' = W + ΔW</p>
              </div>
              <div class="border-t-2 border-gray-300 pt-4">
                <p class="text-sm text-gray-600 mb-2">LoRA（低秩分解）：</p>
                <p class="text-2xl font-mono text-green-700">W' = W + BA</p>
                <p class="text-sm text-gray-500 mt-2">其中 B ∈ ℝ<sup>d×r</sup>, A ∈ ℝ<sup>r×d</sup>, r ≪ d</p>
              </div>
            </div>
          </div>
        </div>

        <!-- 符号说明 -->
        <div class="mb-8">
          <h4 class="font-bold text-lg text-gray-800 mb-4">2. 符号说明</h4>
          <div class="grid md:grid-cols-2 gap-4">
            <div class="bg-blue-50 p-4 rounded-lg">
              <p class="font-semibold text-blue-800 mb-2">W ∈ ℝ<sup>d×d</sup></p>
              <p class="text-sm text-gray-700">原始预训练权重矩阵（冻结）</p>
              <p class="text-xs text-gray-500 mt-1">例如：d = 4096，则 W 是 4096×4096 的矩阵</p>
            </div>
            
            <div class="bg-red-50 p-4 rounded-lg">
              <p class="font-semibold text-red-800 mb-2">ΔW ∈ ℝ<sup>d×d</sup></p>
              <p class="text-sm text-gray-700">权重更新矩阵（全量微调时需要训练）</p>
              <p class="text-xs text-gray-500 mt-1">参数量：d² = 4096² = 16,777,216</p>
            </div>
            
            <div class="bg-green-50 p-4 rounded-lg">
              <p class="font-semibold text-green-800 mb-2">B ∈ ℝ<sup>d×r</sup></p>
              <p class="text-sm text-gray-700">LoRA矩阵B（可训练）</p>
              <p class="text-xs text-gray-500 mt-1">例如：4096×8 矩阵，参数量 = 32,768</p>
            </div>
            
            <div class="bg-green-50 p-4 rounded-lg">
              <p class="font-semibold text-green-800 mb-2">A ∈ ℝ<sup>r×d</sup></p>
              <p class="text-sm text-gray-700">LoRA矩阵A（可训练）</p>
              <p class="text-xs text-gray-500 mt-1">例如：8×4096 矩阵，参数量 = 32,768</p>
            </div>
            
            <div class="bg-purple-50 p-4 rounded-lg">
              <p class="font-semibold text-purple-800 mb-2">r（秩）</p>
              <p class="text-sm text-gray-700">低秩维度，通常 r ≪ d</p>
              <p class="text-xs text-gray-500 mt-1">常见值：4, 8, 16, 32</p>
            </div>
            
            <div class="bg-purple-50 p-4 rounded-lg">
              <p class="font-semibold text-purple-800 mb-2">α（alpha）</p>
              <p class="text-sm text-gray-700">缩放因子，控制LoRA的影响程度</p>
              <p class="text-xs text-gray-500 mt-1">通常 α = 16 或 α = 2r</p>
            </div>
          </div>
        </div>

        <!-- 参数量计算 -->
        <div class="mb-8">
          <h4 class="font-bold text-lg text-gray-800 mb-4">3. 参数量计算</h4>
          <div class="bg-gradient-to-r from-orange-50 to-yellow-50 p-6 rounded-lg">
            <div class="space-y-4">
              <div>
                <p class="font-semibold text-orange-800 mb-2">全量微调参数量：</p>
                <div class="bg-white p-4 rounded font-mono text-sm">
                  <p>|ΔW| = d × d = 4096 × 4096 = <strong class="text-red-600">16,777,216</strong></p>
                </div>
              </div>
              
              <div>
                <p class="font-semibold text-green-800 mb-2">LoRA参数量：</p>
                <div class="bg-white p-4 rounded font-mono text-sm space-y-2">
                  <p>|B| + |A| = (d × r) + (r × d)</p>
                  <p>= 2 × d × r</p>
                  <p>= 2 × 4096 × 8</p>
                  <p>= <strong class="text-green-600">65,536</strong></p>
                </div>
              </div>
              
              <div>
                <p class="font-semibold text-purple-800 mb-2">参数减少比例：</p>
                <div class="bg-white p-4 rounded font-mono text-sm">
                  <p>减少倍数 = d² / (2dr) = d / (2r)</p>
                  <p>= 4096 / (2 × 8) = 4096 / 16</p>
                  <p>= <strong class="text-purple-600">256 倍</strong></p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 前向传播 -->
    <div class="card mb-8 bg-gradient-to-br from-green-50 to-emerald-50">
      <h3 class="text-2xl font-bold text-green-800 mb-6 flex items-center">
        <span class="text-4xl mr-3">⚡</span>
        前向传播过程
      </h3>

      <div class="bg-white p-8 rounded-xl shadow-lg">
        <div class="space-y-6">
          <!-- 输入 -->
          <div class="flex items-center space-x-4">
            <div class="bg-blue-100 p-4 rounded-lg flex-shrink-0 w-32 text-center">
              <p class="font-bold text-blue-800">输入</p>
              <p class="text-sm text-gray-600 mt-1">x ∈ ℝ<sup>b×d</sup></p>
            </div>
            <div class="text-2xl text-gray-400">→</div>
            <div class="flex-1 bg-gray-50 p-4 rounded-lg">
              <p class="text-sm text-gray-700">批次大小 b，特征维度 d</p>
              <p class="text-xs text-gray-500">例如：x 的形状是 [32, 4096]</p>
            </div>
          </div>

          <!-- 基座模型计算 -->
          <div class="border-l-4 border-blue-500 pl-4">
            <h4 class="font-bold text-blue-800 mb-3">步骤1：基座模型计算（冻结路径）</h4>
            <div class="bg-blue-50 p-4 rounded-lg">
              <p class="font-mono text-lg text-blue-700 mb-2">h_base = x · W</p>
              <p class="text-sm text-gray-700">• W 是冻结的，不参与梯度更新</p>
              <p class="text-sm text-gray-700">• 计算复杂度：O(b × d²)</p>
              <p class="text-sm text-gray-700">• 输出形状：[b, d] → 例如 [32, 4096]</p>
            </div>
          </div>

          <!-- LoRA计算 -->
          <div class="border-l-4 border-green-500 pl-4">
            <h4 class="font-bold text-green-800 mb-3">步骤2：LoRA适配器计算（可训练路径）</h4>
            <div class="bg-green-50 p-4 rounded-lg space-y-3">
              <div>
                <p class="font-mono text-lg text-green-700 mb-2">h_lora = (x · B) · A</p>
                <p class="text-sm text-gray-700">分步计算：</p>
              </div>
              
              <div class="ml-4 space-y-2">
                <div class="bg-white p-3 rounded border-l-2 border-green-400">
                  <p class="font-mono text-sm text-gray-800">① temp = x · B</p>
                  <p class="text-xs text-gray-600">形状：[b, d] · [d, r] = [b, r]</p>
                  <p class="text-xs text-gray-600">例如：[32, 4096] · [4096, 8] = [32, 8]</p>
                </div>
                
                <div class="bg-white p-3 rounded border-l-2 border-green-400">
                  <p class="font-mono text-sm text-gray-800">② h_lora = temp · A</p>
                  <p class="text-xs text-gray-600">形状：[b, r] · [r, d] = [b, d]</p>
                  <p class="text-xs text-gray-600">例如：[32, 8] · [8, 4096] = [32, 4096]</p>
                </div>
              </div>
              
              <div class="bg-yellow-50 p-3 rounded">
                <p class="text-sm text-gray-700">💡 <strong>关键优势</strong>：虽然最终 BA 的形状是 [d, d]，但我们<strong>从不显式计算BA</strong>！</p>
                <p class="text-xs text-gray-600 mt-1">通过矩阵乘法的结合律，先算 xB 再算结果×A，大幅降低计算量</p>
              </div>
            </div>
          </div>

          <!-- 缩放和合并 -->
          <div class="border-l-4 border-purple-500 pl-4">
            <h4 class="font-bold text-purple-800 mb-3">步骤3：缩放与合并</h4>
            <div class="bg-purple-50 p-4 rounded-lg">
              <p class="font-mono text-lg text-purple-700 mb-3">h = h_base + (α/r) × h_lora</p>
              <div class="space-y-2">
                <p class="text-sm text-gray-700">• <strong>α</strong>：缩放因子（通常 α = 16）</p>
                <p class="text-sm text-gray-700">• <strong>α/r</strong>：归一化缩放（例如 16/8 = 2）</p>
                <p class="text-sm text-gray-700">• 这个缩放因子控制LoRA对最终输出的影响程度</p>
              </div>
              
              <div class="mt-4 bg-white p-3 rounded">
                <p class="text-xs text-gray-600"><strong>为什么需要缩放？</strong></p>
                <p class="text-xs text-gray-600">防止LoRA的影响过大或过小。α/r 的设计让不同rank的LoRA有相似的初始影响。</p>
              </div>
            </div>
          </div>

          <!-- 输出 -->
          <div class="flex items-center space-x-4">
            <div class="flex-1 bg-gray-50 p-4 rounded-lg">
              <p class="text-sm text-gray-700">最终输出：合并后的特征表示</p>
              <p class="text-xs text-gray-500">形状保持不变：[b, d]</p>
            </div>
            <div class="text-2xl text-gray-400">→</div>
            <div class="bg-purple-100 p-4 rounded-lg flex-shrink-0 w-32 text-center">
              <p class="font-bold text-purple-800">输出</p>
              <p class="text-sm text-gray-600 mt-1">h ∈ ℝ<sup>b×d</sup></p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 反向传播 -->
    <div class="card mb-8 bg-gradient-to-br from-orange-50 to-red-50">
      <h3 class="text-2xl font-bold text-orange-800 mb-6 flex items-center">
        <span class="text-4xl mr-3">🔙</span>
        反向传播与梯度更新
      </h3>

      <div class="bg-white p-8 rounded-xl shadow-lg">
        <div class="space-y-6">
          <div class="bg-orange-50 p-4 rounded-lg">
            <h4 class="font-bold text-orange-800 mb-3">梯度流向</h4>
            <div class="space-y-3">
              <div class="flex items-center space-x-3">
                <div class="bg-red-500 w-3 h-3 rounded-full"></div>
                <p class="text-sm text-gray-700">损失函数 L 对输出 h 的梯度：∂L/∂h</p>
              </div>
              
              <div class="ml-6 border-l-2 border-red-300 pl-4 space-y-2">
                <div class="flex items-center space-x-3">
                  <div class="bg-gray-400 w-2 h-2 rounded-full"></div>
                  <p class="text-sm text-gray-600">冻结路径（W）：梯度不传播，<strong>∂L/∂W = 0</strong></p>
                </div>
                
                <div class="flex items-center space-x-3">
                  <div class="bg-green-500 w-2 h-2 rounded-full"></div>
                  <p class="text-sm text-gray-700">LoRA路径（B, A）：梯度正常传播</p>
                </div>
              </div>
            </div>
          </div>

          <div class="bg-green-50 p-4 rounded-lg">
            <h4 class="font-bold text-green-800 mb-3">梯度计算</h4>
            <div class="space-y-3 font-mono text-sm">
              <div class="bg-white p-3 rounded">
                <p class="text-gray-800">∂L/∂A = (xB)<sup>T</sup> · (∂L/∂h)</p>
                <p class="text-xs text-gray-600 mt-1">形状：[r, d]</p>
              </div>
              
              <div class="bg-white p-3 rounded">
                <p class="text-gray-800">∂L/∂B = x<sup>T</sup> · ((∂L/∂h) · A<sup>T</sup>)</p>
                <p class="text-xs text-gray-600 mt-1">形状：[d, r]</p>
              </div>
            </div>
          </div>

          <div class="bg-blue-50 p-4 rounded-lg">
            <h4 class="font-bold text-blue-800 mb-3">参数更新（Adam优化器）</h4>
            <div class="space-y-2 font-mono text-sm">
              <p class="text-gray-800">A ← A - η · Adam(∂L/∂A)</p>
              <p class="text-gray-800">B ← B - η · Adam(∂L/∂B)</p>
              <p class="text-xs text-gray-600 mt-2">η: 学习率，通常 1e-4 到 1e-3</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 初始化策略 -->
    <div class="card mb-8 bg-gradient-to-br from-cyan-50 to-blue-50">
      <h3 class="text-2xl font-bold text-cyan-800 mb-6 flex items-center">
        <span class="text-4xl mr-3">🎲</span>
        初始化策略
      </h3>

      <div class="bg-white p-8 rounded-xl shadow-lg">
        <div class="grid md:grid-cols-2 gap-6">
          <div class="bg-blue-50 p-5 rounded-lg">
            <h4 class="font-bold text-blue-800 mb-3">矩阵 A 的初始化</h4>
            <p class="text-sm text-gray-700 mb-3">使用<strong>高斯分布</strong>随机初始化：</p>
            <div class="bg-white p-3 rounded font-mono text-sm mb-3">
              A ~ N(0, σ²)
            </div>
            <p class="text-xs text-gray-600">通常 σ = 1/√r 或使用 Kaiming 初始化</p>
            <p class="text-xs text-gray-600 mt-2"><strong>目的</strong>：提供初始的非对称性，打破对称</p>
          </div>

          <div class="bg-green-50 p-5 rounded-lg">
            <h4 class="font-bold text-green-800 mb-3">矩阵 B 的初始化</h4>
            <p class="text-sm text-gray-700 mb-3">初始化为<strong>全零矩阵</strong>：</p>
            <div class="bg-white p-3 rounded font-mono text-sm mb-3">
              B = 0<sub>d×r</sub>
            </div>
            <p class="text-xs text-gray-600">这确保 BA = 0 在训练开始时</p>
            <p class="text-xs text-gray-600 mt-2"><strong>目的</strong>：训练初期，W' = W + BA = W，保持预训练权重不变</p>
          </div>
        </div>

        <div class="mt-6 bg-purple-50 p-5 rounded-lg">
          <h4 class="font-bold text-purple-800 mb-3">💡 为什么这样初始化？</h4>
          <ul class="space-y-2 text-sm text-gray-700">
            <li>✓ <strong>从预训练权重开始</strong>：训练初期模型行为与预训练模型完全一致</li>
            <li>✓ <strong>平滑过渡</strong>：随着训练进行，BA 逐渐学习到任务特定的调整</li>
            <li>✓ <strong>稳定性</strong>：避免训练初期的大幅波动</li>
            <li>✓ <strong>继承能力</strong>：充分利用预训练模型已有的知识</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- 低秩假设 -->
    <div class="card bg-gradient-to-br from-purple-50 to-pink-50">
      <h3 class="text-2xl font-bold text-purple-800 mb-6 flex items-center">
        <span class="text-4xl mr-3">🔬</span>
        理论基础：低秩假设
      </h3>

      <div class="bg-white p-8 rounded-xl shadow-lg">
        <div class="space-y-6">
          <div>
            <h4 class="font-bold text-gray-800 mb-3">核心假设</h4>
            <div class="bg-purple-50 p-5 rounded-lg">
              <p class="text-lg text-gray-800 mb-3">
                在微调过程中，权重的更新矩阵 <strong>ΔW</strong> 具有<strong>低秩（low-rank）</strong>特性
              </p>
              <p class="text-sm text-gray-700">
                换句话说：ΔW 的有效秩 r ≪ d，可以用两个低秩矩阵的乘积来近似
              </p>
            </div>
          </div>

          <div>
            <h4 class="font-bold text-gray-800 mb-3">数学表述</h4>
            <div class="bg-gray-50 p-5 rounded-lg">
              <p class="font-mono text-center text-lg mb-4">rank(ΔW) = r ≪ min(d₁, d₂)</p>
              <p class="text-sm text-gray-700 text-center">因此可以分解为：ΔW ≈ BA</p>
            </div>
          </div>

          <div>
            <h4 class="font-bold text-gray-800 mb-3">实验验证</h4>
            <div class="bg-blue-50 p-5 rounded-lg">
              <p class="text-sm text-gray-700 mb-3">微软研究院的实验表明：</p>
              <ul class="space-y-2 text-sm text-gray-700">
                <li>• 对于大多数下游任务，<strong>r = 4 或 r = 8</strong> 就足够了</li>
                <li>• 即使 r 很小（如1%的原始维度），性能也接近全量微调</li>
                <li>• 更大的 r 带来边际收益递减</li>
              </ul>
            </div>
          </div>

          <div>
            <h4 class="font-bold text-gray-800 mb-3">直观解释</h4>
            <div class="bg-gradient-to-r from-green-50 to-emerald-50 p-5 rounded-lg">
              <p class="text-sm text-gray-700 mb-3">
                <strong>为什么微调的更新是低秩的？</strong>
              </p>
              <ul class="space-y-2 text-sm text-gray-700">
                <li>1️⃣ <strong>预训练已学习通用特征</strong>：大部分知识已经编码在 W 中</li>
                <li>2️⃣ <strong>任务特定调整有限</strong>：微调只需要在少数几个"方向"上调整</li>
                <li>3️⃣ <strong>信息冗余</strong>：d × d 的完整更新包含大量冗余信息</li>
                <li>4️⃣ <strong>本质维度低</strong>：任务特定的知识可以用少数主成分表示</li>
              </ul>
            </div>
          </div>

          <div>
            <h4 class="font-bold text-gray-800 mb-3">类比理解</h4>
            <div class="bg-yellow-50 p-5 rounded-lg">
              <p class="text-sm text-gray-700">
                🎨 <strong>类比</strong>：想象你在调整一张高分辨率图片的色调。虽然图片有数百万像素，
                但"调整色调"这个操作本质上只涉及几个参数（色相、饱和度、亮度）。
                你不需要独立调整每个像素，只需要在几个关键维度上做调整。
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// 纯展示组件，无需额外脚本
</script>

<style scoped>
sup {
  font-size: 0.7em;
  vertical-align: super;
}

sub {
  font-size: 0.7em;
  vertical-align: sub;
}
</style>

