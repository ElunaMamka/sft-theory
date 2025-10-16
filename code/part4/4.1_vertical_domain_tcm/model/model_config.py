"""
4.1 中医问诊助手 - 模型配置
定义模型参数、LoRA配置等
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ModelConfig:
    """模型基础配置"""
    
    # 基座模型选择
    model_name_or_path: str = "baichuan-inc/Baichuan2-7B-Base"
    # 其他可选模型:
    # - "Qwen/Qwen-7B"
    # - "THUDM/chatglm3-6b"
    # - "01-ai/Yi-6B"
    
    # 模型参数
    max_length: int = 2048  # 最大序列长度
    cache_dir: Optional[str] = "./model_cache"  # 模型缓存目录
    
    # 量化配置（节省显存）
    load_in_8bit: bool = False  # 8-bit量化
    load_in_4bit: bool = True   # 4-bit量化（推荐）
    
    # Tokenizer配置
    trust_remote_code: bool = True  # 信任远程代码
    use_fast_tokenizer: bool = True


@dataclass
class LoRAConfig:
    """LoRA微调配置"""
    
    # LoRA核心参数
    r: int = 8  # LoRA rank（秩）
    # r的选择:
    # - r=4: 极致参数效率，适合资源受限
    # - r=8: 推荐值，平衡性能和效率
    # - r=16: 更强表达能力，适合复杂任务
    # - r=64: 接近全参数微调效果
    
    lora_alpha: int = 16  # LoRA缩放参数
    # 一般设置为 r 的 2倍
    
    lora_dropout: float = 0.05  # Dropout概率
    
    # 目标模块（哪些层使用LoRA）
    target_modules: list = field(default_factory=lambda: [
        "q_proj",   # Query投影
        "k_proj",   # Key投影  
        "v_proj",   # Value投影
        "o_proj",   # Output投影
        "gate_proj", # MLP Gate
        "up_proj",   # MLP Up
        "down_proj", # MLP Down
    ])
    # 注意：不同模型的层名称可能不同
    
    # 任务类型
    task_type: str = "CAUSAL_LM"  # 因果语言模型
    
    # 偏置处理
    bias: str = "none"  # "none" | "all" | "lora_only"
    
    def get_trainable_params(self, base_params: int) -> dict:
        """计算可训练参数量"""
        # LoRA参数量 = 2 * d * r * num_layers
        # 假设7B模型，hidden_size=4096，32层，7个目标模块
        d = 4096
        num_layers = 32
        num_targets = len(self.target_modules)
        
        lora_params = 2 * d * self.r * num_layers * num_targets
        
        return {
            'base_params': base_params,
            'lora_params': lora_params,
            'trainable_ratio': lora_params / base_params,
            'trainable_percentage': f"{(lora_params / base_params * 100):.3f}%"
        }


@dataclass
class TrainingConfig:
    """训练配置"""
    
    # 输出目录
    output_dir: str = "./output/tcm_sft_lora"
    
    # 训练轮数
    num_train_epochs: int = 3
    
    # Batch size
    per_device_train_batch_size: int = 4
    per_device_eval_batch_size: int = 4
    gradient_accumulation_steps: int = 4
    # 实际batch_size = per_device_train_batch_size * gradient_accumulation_steps
    # = 4 * 4 = 16
    
    # 学习率
    learning_rate: float = 2e-4  # LoRA推荐学习率
    # 注意：LoRA的学习率通常比全参数微调大10倍
    # 全参数: 1e-5 ~ 5e-5
    # LoRA: 1e-4 ~ 5e-4
    
    # 优化器
    optim: str = "adamw_torch"
    # 可选: "adamw_8bit" (节省显存)
    
    # 学习率调度
    lr_scheduler_type: str = "cosine"
    warmup_ratio: float = 0.03  # warmup步数占比
    
    # 权重衰减
    weight_decay: float = 0.01
    
    # 梯度裁剪
    max_grad_norm: float = 1.0
    
    # 保存策略
    save_strategy: str = "steps"
    save_steps: int = 100
    save_total_limit: int = 3  # 最多保存3个checkpoint
    
    # 评估策略
    evaluation_strategy: str = "steps"
    eval_steps: int = 100
    
    # 日志
    logging_steps: int = 10
    logging_dir: str = "./logs"
    report_to: str = "tensorboard"  # "wandb" | "tensorboard" | "none"
    
    # 混合精度训练
    fp16: bool = False  # FP16
    bf16: bool = True   # BF16（推荐，更稳定）
    # 注意：需要GPU支持（A100, H100等）
    
    # 其他
    seed: int = 42
    dataloader_num_workers: int = 4
    remove_unused_columns: bool = False
    
    # DeepSpeed配置（分布式训练）
    deepspeed: Optional[str] = None  # DeepSpeed配置文件路径


def print_config_summary():
    """打印配置摘要"""
    print("="*80)
    print("⚙️  模型配置摘要")
    print("="*80)
    
    model_cfg = ModelConfig()
    lora_cfg = LoRAConfig()
    train_cfg = TrainingConfig()
    
    print(f"\n【基座模型】")
    print(f"  模型: {model_cfg.model_name_or_path}")
    print(f"  最大长度: {model_cfg.max_length}")
    print(f"  量化: {'4-bit' if model_cfg.load_in_4bit else '8-bit' if model_cfg.load_in_8bit else '无'}")
    
    print(f"\n【LoRA配置】")
    print(f"  Rank (r): {lora_cfg.r}")
    print(f"  Alpha: {lora_cfg.lora_alpha}")
    print(f"  Dropout: {lora_cfg.lora_dropout}")
    print(f"  目标模块: {', '.join(lora_cfg.target_modules)}")
    
    # 参数量估算
    base_params = 7_000_000_000  # 7B模型
    params_info = lora_cfg.get_trainable_params(base_params)
    print(f"\n【参数量】")
    print(f"  基座参数: {params_info['base_params']:,}")
    print(f"  LoRA参数: {params_info['lora_params']:,}")
    print(f"  训练比例: {params_info['trainable_percentage']}")
    
    print(f"\n【训练配置】")
    print(f"  训练轮数: {train_cfg.num_train_epochs}")
    print(f"  有效Batch Size: {train_cfg.per_device_train_batch_size * train_cfg.gradient_accumulation_steps}")
    print(f"  学习率: {train_cfg.learning_rate}")
    print(f"  优化器: {train_cfg.optim}")
    print(f"  LR调度: {train_cfg.lr_scheduler_type}")
    print(f"  混合精度: {'BF16' if train_cfg.bf16 else 'FP16' if train_cfg.fp16 else 'FP32'}")
    
    print("\n" + "="*80)


if __name__ == "__main__":
    print_config_summary()
    
    # 显示配置建议
    print("\n💡 配置建议:")
    print("\n  【显存占用估算】")
    print("    - 4-bit量化 + LoRA r=8: ~8GB")
    print("    - 8-bit量化 + LoRA r=8: ~12GB")
    print("    - FP16 + LoRA r=8: ~20GB")
    print("    - 全参数微调: ~56GB+")
    
    print("\n  【LoRA rank选择】")
    print("    - r=4:  极致效率，适合简单任务")
    print("    - r=8:  推荐值，性能和效率平衡 ✅")
    print("    - r=16: 更强能力，适合复杂任务")
    print("    - r=64: 接近全参数效果")
    
    print("\n  【学习率设置】")
    print("    - LoRA: 1e-4 ~ 5e-4（推荐2e-4）")
    print("    - 全参数: 1e-5 ~ 5e-5")
    print("    - 注意：LoRA学习率通常是全参数的10倍")

