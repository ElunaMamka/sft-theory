"""
演示代码：LoRA工作机制
文件位置：code/part2/02_lora_mechanism.py

详细演示LoRA的两个核心步骤：
1. 冻结预训练模型
2. 添加低秩适配器
"""

import numpy as np
from typing import Tuple, List


class LoRALayer:
    """LoRA层的简化实现"""
    
    def __init__(self, input_dim: int, output_dim: int, rank: int = 8, alpha: float = 16):
        """
        初始化LoRA层
        
        Args:
            input_dim: 输入维度
            output_dim: 输出维度
            rank: LoRA秩（控制适配器大小）
            alpha: LoRA缩放因子
        """
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.rank = rank
        self.alpha = alpha
        self.scaling = alpha / rank
        
        # LoRA矩阵：W = B @ A
        self.lora_A = np.random.randn(input_dim, rank) * 0.01
        self.lora_B = np.zeros((rank, output_dim))
        
        # 原始冻结权重（不训练）
        self.frozen_weight = np.random.randn(input_dim, output_dim) * 0.1
        
    def forward(self, x: np.ndarray) -> np.ndarray:
        """
        前向传播
        
        Args:
            x: 输入 shape (batch, input_dim)
            
        Returns:
            输出 shape (batch, output_dim)
        """
        # 原始权重的输出（冻结）
        original_output = x @ self.frozen_weight
        
        # LoRA适配器的输出（可训练）
        lora_output = (x @ self.lora_A @ self.lora_B) * self.scaling
        
        # 合并输出
        return original_output + lora_output
    
    def count_parameters(self) -> dict:
        """统计参数量"""
        frozen_params = self.input_dim * self.output_dim
        trainable_params = self.input_dim * self.rank + self.rank * self.output_dim
        
        return {
            "冻结参数": frozen_params,
            "可训练参数（LoRA）": trainable_params,
            "参数总量": frozen_params + trainable_params,
            "训练参数比例": f"{trainable_params / (frozen_params + trainable_params) * 100:.3f}%"
        }


def demonstrate_lora_mechanism():
    """演示LoRA机制"""
    
    print("="*80)
    print("🔌 LoRA (Low-Rank Adaptation) 工作机制演示")
    print("="*80)
    
    # 创建一个LoRA层（模拟注意力层）
    input_dim = 4096  # 典型的隐藏层维度
    output_dim = 4096
    rank = 8  # LoRA秩
    
    print(f"\n📐 层配置：")
    print(f"  输入维度: {input_dim}")
    print(f"  输出维度: {output_dim}")
    print(f"  LoRA秩 (r): {rank}")
    
    lora_layer = LoRALayer(input_dim, output_dim, rank)
    
    # 步骤1：展示冻结机制
    print(f"\n{'='*80}")
    print("步骤 1: 冻结预训练模型权重 ❄️")
    print(f"{'='*80}")
    
    print(f"\n🧊 原始权重矩阵 W:")
    print(f"  • 形状: ({input_dim}, {output_dim})")
    print(f"  • 参数量: {input_dim * output_dim:,}")
    print(f"  • 状态: 🔒 完全冻结（requires_grad=False）")
    print(f"  • 作用: 保留预训练知识，防止遗忘")
    
    # 步骤2：展示LoRA适配器
    print(f"\n{'='*80}")
    print("步骤 2: 添加低秩适配器矩阵 🔌")
    print(f"{'='*80}")
    
    print(f"\n🎯 LoRA分解：ΔW = B @ A")
    print(f"\n  矩阵 A:")
    print(f"    • 形状: ({input_dim}, {rank})")
    print(f"    • 参数量: {input_dim * rank:,}")
    print(f"    • 初始化: 高斯随机数")
    
    print(f"\n  矩阵 B:")
    print(f"    • 形状: ({rank}, {output_dim})")
    print(f"    • 参数量: {rank * output_dim:,}")
    print(f"    • 初始化: 全零（训练开始时ΔW=0）")
    
    # 参数统计
    print(f"\n{'='*80}")
    print("📊 参数统计对比")
    print(f"{'='*80}")
    
    stats = lora_layer.count_parameters()
    for key, value in stats.items():
        print(f"  {key}: {value if isinstance(value, str) else f'{value:,}'}")
    
    # 可视化分解过程
    print(f"\n{'='*80}")
    print("🎨 LoRA的数学本质")
    print(f"{'='*80}")
    
    print("""
原始全量微调：
  y = x @ W_new
  需要更新: W_new (所有参数)

LoRA方法：
  y = x @ (W_frozen + ΔW)
  y = x @ (W_frozen + B @ A)
  
  其中:
  • W_frozen: 冻结的预训练权重
  • ΔW = B @ A: 低秩更新（仅训练B和A）
  • rank << min(input_dim, output_dim)
    """)
    
    # 前向传播演示
    print(f"\n{'='*80}")
    print("🔄 前向传播流程")
    print(f"{'='*80}")
    
    batch_size = 2
    x = np.random.randn(batch_size, input_dim)
    
    print(f"\n输入 x: shape {x.shape}")
    print(f"  ↓")
    print(f"1️⃣  x @ W_frozen  →  原始模型输出")
    print(f"  ↓")
    print(f"2️⃣  x @ A @ B  →  LoRA适配器输出")
    print(f"  ↓")
    print(f"3️⃣  原始输出 + LoRA输出  →  最终输出")
    
    output = lora_layer.forward(x)
    print(f"\n输出 y: shape {output.shape}")
    
    # LoRA的优势
    print(f"\n{'='*80}")
    print("✨ LoRA的核心优势")
    print(f"{'='*80}")
    
    trainable_ratio = stats["可训练参数（LoRA）"] / stats["参数总量"] * 100
    
    print(f"""
1. 参数效率 💾
   • 只训练 {trainable_ratio:.2f}% 的参数
   • 内存占用大幅减少
   • 训练速度显著提升

2. 防止遗忘 🛡️
   • 原始权重完全冻结
   • 预训练知识得到保护
   • 灾难性遗忘风险极低

3. 模块化部署 🔌
   • LoRA适配器可以单独保存（仅几MB）
   • 支持动态加载/卸载
   • 一个基座模型 + 多个适配器
    """)


def compare_with_full_finetuning():
    """与全量微调对比"""
    
    print(f"\n{'='*80}")
    print("⚖️  LoRA vs 全量微调 - 具体数字对比")
    print(f"{'='*80}")
    
    # 以7B模型为例
    model_size = 7_000_000_000
    lora_rank = 8
    num_lora_layers = 32  # 假设32个attention层应用LoRA
    dim = 4096
    
    # 全量微调
    full_params = model_size
    full_storage_gb = (model_size * 2) / (1024**3)  # FP16
    
    # LoRA
    lora_params_per_layer = dim * lora_rank * 2  # A和B矩阵
    total_lora_params = lora_params_per_layer * num_lora_layers
    lora_storage_mb = (total_lora_params * 2) / (1024**2)  # FP16
    
    print(f"\n模型规模: 7B参数")
    print(f"\n全量微调:")
    print(f"  • 可训练参数: {full_params:,}")
    print(f"  • 存储需求: {full_storage_gb:.2f} GB")
    
    print(f"\nLoRA (r={lora_rank}):")
    print(f"  • 可训练参数: {total_lora_params:,}")
    print(f"  • 存储需求: {lora_storage_mb:.2f} MB")
    
    print(f"\n📉 减少倍数:")
    print(f"  • 参数量: {full_params / total_lora_params:.1f}x")
    print(f"  • 存储: {full_storage_gb * 1024 / lora_storage_mb:.1f}x")
    
    print("\n📁 代码位置: code/part2/02_lora_mechanism.py")


if __name__ == "__main__":
    demonstrate_lora_mechanism()
    compare_with_full_finetuning()

