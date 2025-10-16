"""
演示代码：全量微调的三大问题
文件位置：code/part2/01_full_finetuning_problems.py

展示全量微调面临的挑战：
1. 巨大的计算开销
2. 灾难性遗忘
3. 存储与部署困难
"""

import random
from typing import List, Dict


class FullFineTuningSimulator:
    """全量微调模拟器"""
    
    def __init__(self, model_size: int = 7_000_000_000):
        """
        初始化模型
        
        Args:
            model_size: 模型参数量（默认7B）
        """
        self.model_size = model_size
        self.original_params = self._initialize_params()
        self.current_params = self.original_params.copy()
        
        # 模拟预训练获得的能力
        self.pretrained_knowledge = {
            "通用语言理解": 0.9,
            "数学推理": 0.8,
            "代码生成": 0.75,
            "常识问答": 0.85
        }
        
    def _initialize_params(self) -> Dict[str, float]:
        """初始化模型参数"""
        return {
            f"layer_{i}_param_{j}": random.random()
            for i in range(10)  # 简化为10层
            for j in range(100)  # 每层100个参数
        }
    
    def calculate_memory_requirement(self) -> Dict[str, float]:
        """
        计算全量微调的内存需求
        
        Returns:
            内存需求详情（GB）
        """
        # FP32: 4 bytes per parameter
        model_memory = (self.model_size * 4) / (1024**3)
        
        # Optimizer states (Adam): 2x parameters
        optimizer_memory = model_memory * 2
        
        # Gradients: 1x parameters
        gradient_memory = model_memory
        
        # Activations (估算)
        activation_memory = model_memory * 0.5
        
        total_memory = model_memory + optimizer_memory + gradient_memory + activation_memory
        
        return {
            "模型参数": round(model_memory, 2),
            "优化器状态": round(optimizer_memory, 2),
            "梯度": round(gradient_memory, 2),
            "激活值": round(activation_memory, 2),
            "总计": round(total_memory, 2)
        }
    
    def simulate_catastrophic_forgetting(self, task_focus: str, epochs: int = 10):
        """
        模拟灾难性遗忘
        
        Args:
            task_focus: 专注训练的任务
            epochs: 训练轮数
        """
        print(f"\n{'='*70}")
        print(f"🧠 灾难性遗忘模拟 - 专注训练：{task_focus}")
        print(f"{'='*70}")
        
        print(f"\n📊 训练前的能力分布：")
        for skill, score in self.pretrained_knowledge.items():
            print(f"  {skill}: {score:.2f}")
        
        # 模拟训练过程：专注的任务提升，其他能力下降
        for epoch in range(epochs):
            for skill in self.pretrained_knowledge:
                if skill == task_focus:
                    # 专注的任务能力提升
                    self.pretrained_knowledge[skill] = min(
                        1.0, 
                        self.pretrained_knowledge[skill] + random.uniform(0.01, 0.03)
                    )
                else:
                    # 其他能力逐渐遗忘
                    self.pretrained_knowledge[skill] = max(
                        0.0,
                        self.pretrained_knowledge[skill] - random.uniform(0.02, 0.05)
                    )
        
        print(f"\n📉 训练{epochs}轮后的能力分布：")
        for skill, score in self.pretrained_knowledge.items():
            emoji = "📈" if skill == task_focus else "📉"
            print(f"  {emoji} {skill}: {score:.2f}")
        
        print(f"\n⚠️  观察到严重的灾难性遗忘！")
        print(f"  专注任务提升，但其他能力大幅下降")
    
    def calculate_storage_cost(self, num_tasks: int = 10):
        """
        计算多任务存储成本
        
        Args:
            num_tasks: 需要微调的任务数量
        """
        # FP16: 2 bytes per parameter
        size_per_model_gb = (self.model_size * 2) / (1024**3)
        
        print(f"\n{'='*70}")
        print(f"💾 存储成本分析 - {num_tasks}个不同任务")
        print(f"{'='*70}")
        
        print(f"\n📦 单个全量微调模型大小：{size_per_model_gb:.2f} GB")
        print(f"🔢 任务数量：{num_tasks}")
        print(f"💰 总存储需求：{size_per_model_gb * num_tasks:.2f} GB")
        
        print(f"\n⚠️  存储问题：")
        print(f"  • 每个任务需要保存一个完整的模型副本")
        print(f"  • 10个任务需要 {size_per_model_gb * num_tasks:.0f}GB 存储空间")
        print(f"  • 模型切换需要加载整个模型到内存")
        print(f"  • 部署和维护复杂度呈线性增长")


def demonstrate_problems():
    """演示全量微调的问题"""
    
    print("="*70)
    print("🚨 全量微调的三大困境")
    print("="*70)
    
    # 创建7B参数模型
    model = FullFineTuningSimulator(model_size=7_000_000_000)
    
    # 问题1：计算开销
    print(f"\n{'#'*70}")
    print("问题 1: 巨大的计算开销")
    print(f"{'#'*70}")
    
    memory_req = model.calculate_memory_requirement()
    print(f"\n💻 训练7B模型的内存需求（FP32）：")
    for component, size in memory_req.items():
        print(f"  {component}: {size} GB")
    
    print(f"\n⚠️  需要 {memory_req['总计']} GB 内存！")
    print(f"  • 单张A100 GPU (80GB) 不够用")
    print(f"  • 需要多GPU并行训练")
    print(f"  • 训练时间长达数天甚至数周")
    
    # 问题2：灾难性遗忘
    print(f"\n{'#'*70}")
    print("问题 2: 灾难性遗忘")
    print(f"{'#'*70}")
    
    model.simulate_catastrophic_forgetting(
        task_focus="代码生成",
        epochs=10
    )
    
    # 问题3：存储与部署
    print(f"\n{'#'*70}")
    print("问题 3: 存储与部署困难")
    print(f"{'#'*70}")
    
    model.calculate_storage_cost(num_tasks=10)
    
    # 总结
    print(f"\n{'='*70}")
    print("💡 总结：为什么需要LoRA？")
    print(f"{'='*70}")
    print("""
全量微调就像每次学习新技能都要进行一次"脑部手术"：
• 风险高（灾难性遗忘）
• 成本大（计算和存储）
• 效率低（训练慢、部署难）

我们需要一种更智能的方法 ——— 这就是LoRA！
    """)
    
    print("\n📁 代码位置: code/part2/01_full_finetuning_problems.py")


if __name__ == "__main__":
    demonstrate_problems()

