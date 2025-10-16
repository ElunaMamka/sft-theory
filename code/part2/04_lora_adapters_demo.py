"""
演示代码：LoRA适配器的可组合性
文件位置：code/part2/04_lora_adapters_demo.py

展示如何用一个基座模型 + 多个LoRA适配器实现多任务
"""

import numpy as np
from typing import Dict, List


class BaseModel:
    """基座模型（冻结）"""
    
    def __init__(self, model_size: str = "7B"):
        self.model_size = model_size
        self.name = f"LLaMA-2-{model_size}"
        # 模拟冻结的权重
        self.frozen_weights = np.random.randn(100, 100) * 0.1
        print(f"✅ 加载基座模型: {self.name}")
        print(f"   参数量: {model_size}")
        print(f"   状态: 🔒 完全冻结")
    
    def forward(self, x: np.ndarray) -> np.ndarray:
        """基座模型的前向传播"""
        return x @ self.frozen_weights


class LoRAAdapter:
    """LoRA适配器"""
    
    def __init__(self, name: str, task: str, rank: int = 8):
        self.name = name
        self.task = task
        self.rank = rank
        
        # LoRA矩阵 A 和 B
        self.lora_A = np.random.randn(100, rank) * 0.01
        self.lora_B = np.zeros((rank, 100))
        
        # 计算参数量
        self.params = 100 * rank * 2  # A和B的参数
        
        print(f"  📦 创建适配器: {name}")
        print(f"     任务: {task}")
        print(f"     参数量: {self.params:,}")
    
    def forward(self, x: np.ndarray) -> np.ndarray:
        """LoRA适配器的前向传播"""
        return (x @ self.lora_A @ self.lora_B) * (16.0 / self.rank)  # scaling
    
    def get_storage_size(self) -> float:
        """获取存储大小（MB）"""
        # FP16: 2 bytes per parameter
        return (self.params * 2) / (1024**2)


class MultiTaskModel:
    """支持多任务的模型（一个基座 + 多个LoRA）"""
    
    def __init__(self, base_model: BaseModel):
        self.base_model = base_model
        self.adapters: Dict[str, LoRAAdapter] = {}
        self.current_adapter = None
        
        print(f"\n🎯 创建多任务模型系统")
        print(f"   基座: {base_model.name}")
    
    def add_adapter(self, adapter: LoRAAdapter):
        """添加一个LoRA适配器"""
        self.adapters[adapter.name] = adapter
        print(f"✅ 已添加适配器: {adapter.name} ({adapter.task})")
    
    def switch_adapter(self, adapter_name: str):
        """切换到指定的适配器"""
        if adapter_name in self.adapters:
            self.current_adapter = self.adapters[adapter_name]
            print(f"🔄 切换到适配器: {adapter_name}")
        else:
            raise ValueError(f"未找到适配器: {adapter_name}")
    
    def forward(self, x: np.ndarray) -> np.ndarray:
        """前向传播（基座 + 当前适配器）"""
        # 基座模型输出
        base_output = self.base_model.forward(x)
        
        # 如果有活跃的适配器，加上适配器的输出
        if self.current_adapter:
            adapter_output = self.current_adapter.forward(x)
            return base_output + adapter_output
        
        return base_output
    
    def get_total_storage(self) -> float:
        """计算总存储需求（GB）"""
        # 基座模型（FP16）
        base_size = (7_000_000_000 * 2) / (1024**3)  # 7B模型示例
        
        # 所有适配器
        adapters_size = sum(adapter.get_storage_size() 
                          for adapter in self.adapters.values()) / 1024
        
        return base_size + adapters_size
    
    def print_summary(self):
        """打印系统摘要"""
        print(f"\n{'='*70}")
        print(f"📊 多任务模型系统摘要")
        print(f"{'='*70}")
        
        print(f"\n🧠 基座模型:")
        print(f"   名称: {self.base_model.name}")
        print(f"   大小: ~13 GB (FP16)")
        print(f"   状态: 冻结（所有任务共享）")
        
        print(f"\n🔌 LoRA适配器列表:")
        total_adapter_size = 0
        for name, adapter in self.adapters.items():
            size_mb = adapter.get_storage_size()
            total_adapter_size += size_mb
            print(f"   • {name:<20} | {adapter.task:<30} | {size_mb:.2f} MB")
        
        print(f"\n💾 存储需求:")
        print(f"   基座模型: ~13 GB")
        print(f"   所有适配器: {total_adapter_size:.2f} MB")
        print(f"   总计: ~{13 + total_adapter_size/1024:.2f} GB")
        
        print(f"\n💡 存储优势:")
        # 如果用全量微调
        full_ft_storage = 13 * len(self.adapters)
        print(f"   全量微调需要: {full_ft_storage} GB ({len(self.adapters)}个任务 × 13GB)")
        print(f"   LoRA方案需要: ~{13 + total_adapter_size/1024:.2f} GB")
        savings = full_ft_storage - (13 + total_adapter_size/1024)
        print(f"   节省空间: {savings:.1f} GB ({savings/full_ft_storage*100:.1f}%)")


def demonstrate_hub_and_spoke():
    """演示Hub-and-Spoke架构"""
    
    print("="*70)
    print("🎯 演示：Hub-and-Spoke 多任务架构")
    print("="*70)
    
    # 1. 创建基座模型（Hub - 中心）
    print("\n步骤1: 加载基座模型")
    print("-"*70)
    base_model = BaseModel("7B")
    
    # 2. 创建多任务系统
    print("\n步骤2: 创建多任务系统")
    print("-"*70)
    multi_task_model = MultiTaskModel(base_model)
    
    # 3. 创建多个LoRA适配器（Spokes - 辐条）
    print("\n步骤3: 创建专用LoRA适配器")
    print("-"*70)
    
    adapters = [
        LoRAAdapter("email_summary", "邮件总结", rank=8),
        LoRAAdapter("code_generation", "Python代码生成", rank=16),
        LoRAAdapter("sql_query", "SQL查询生成", rank=8),
        LoRAAdapter("creative_writing", "创意写作", rank=16),
        LoRAAdapter("customer_service", "客户服务对话", rank=8),
        LoRAAdapter("translation_cn_en", "中英翻译", rank=8),
    ]
    
    # 4. 添加所有适配器
    print("\n步骤4: 将适配器加载到系统")
    print("-"*70)
    for adapter in adapters:
        multi_task_model.add_adapter(adapter)
    
    # 5. 演示任务切换
    print("\n步骤5: 演示快速任务切换")
    print("-"*70)
    
    test_input = np.random.randn(1, 100)
    
    tasks = ["email_summary", "code_generation", "customer_service"]
    for task_name in tasks:
        multi_task_model.switch_adapter(task_name)
        output = multi_task_model.forward(test_input)
        print(f"   执行任务完成: {task_name}")
    
    # 6. 打印摘要
    multi_task_model.print_summary()
    
    # 7. 对比
    print(f"\n{'='*70}")
    print("🔍 方案对比")
    print(f"{'='*70}")
    
    print(f"\n【传统方案：每个任务一个完整模型】")
    print(f"  需要训练: {len(adapters)}个完整模型")
    print(f"  总存储: {len(adapters) * 13} GB")
    print(f"  切换任务: 需要重新加载整个模型（慢）")
    print(f"  维护成本: 高（管理{len(adapters)}个大模型）")
    
    print(f"\n【LoRA方案：一个基座 + 多个适配器】")
    print(f"  需要训练: 1个基座 + {len(adapters)}个轻量适配器")
    total_size = 13 + sum(a.get_storage_size() for a in adapters) / 1024
    print(f"  总存储: {total_size:.2f} GB")
    print(f"  切换任务: 仅需加载适配器（快，几MB）")
    print(f"  维护成本: 低（管理1个基座 + {len(adapters)}个小文件）")
    
    print(f"\n💡 关键优势:")
    print(f"  ✓ 存储节省: {len(adapters) * 13 - total_size:.1f} GB")
    print(f"  ✓ 灵活组合: 可以动态加载/卸载适配器")
    print(f"  ✓ 快速迭代: 新任务只需训练一个小适配器")
    print(f"  ✓ 易于部署: 基座模型一次加载，适配器按需切换")
    
    print("\n📁 代码位置: code/part2/04_lora_adapters_demo.py")


if __name__ == "__main__":
    demonstrate_hub_and_spoke()

