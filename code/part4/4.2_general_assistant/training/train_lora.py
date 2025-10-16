"""
4.1 中医问诊助手 - LoRA微调训练脚本
完整的训练流程，包括数据加载、模型训练、评估
"""

import os
import sys
import torch
from datasets import load_from_disk
from transformers import (
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling,
)

# 添加项目路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.model_config import ModelConfig, LoRAConfig, TrainingConfig
from model.model_utils import (
    load_tokenizer,
    load_model_for_training,
    format_instruction,
)


class TCMTrainer:
    """中医问诊助手训练器"""
    
    def __init__(self, 
                 model_cfg: ModelConfig,
                 lora_cfg: LoRAConfig,
                 train_cfg: TrainingConfig):
        self.model_cfg = model_cfg
        self.lora_cfg = lora_cfg
        self.train_cfg = train_cfg
        
        self.tokenizer = None
        self.model = None
        self.train_dataset = None
        self.eval_dataset = None
    
    def setup(self):
        """初始化设置"""
        print("="*80)
        print("🚀 中医问诊助手 - LoRA微调训练")
        print("="*80)
        
        # 1. 加载tokenizer
        self.tokenizer = load_tokenizer(
            self.model_cfg.model_name_or_path,
            trust_remote_code=self.model_cfg.trust_remote_code,
            use_fast=self.model_cfg.use_fast_tokenizer,
        )
        
        # 2. 加载并配置模型
        self.model = load_model_for_training(
            model_name_or_path=self.model_cfg.model_name_or_path,
            load_in_4bit=self.model_cfg.load_in_4bit,
            lora_r=self.lora_cfg.r,
            lora_alpha=self.lora_cfg.lora_alpha,
            lora_dropout=self.lora_cfg.lora_dropout,
        )
        
        print(f"\n✅ 初始化完成！")
    
    def load_data(self, train_data_path: str, eval_data_path: str):
        """加载数据集"""
        print("\n" + "="*80)
        print("📚 加载训练数据")
        print("="*80)
        
        # 加载HuggingFace格式的数据
        self.train_dataset = load_from_disk(train_data_path)
        self.eval_dataset = load_from_disk(eval_data_path)
        
        print(f"  训练集: {len(self.train_dataset)} 条")
        print(f"  验证集: {len(self.eval_dataset)} 条")
        
        # 数据预处理
        self.train_dataset = self.train_dataset.map(
            self.tokenize_function,
            remove_columns=self.train_dataset.column_names,
            desc="Tokenizing train dataset",
        )
        
        self.eval_dataset = self.eval_dataset.map(
            self.tokenize_function,
            remove_columns=self.eval_dataset.column_names,
            desc="Tokenizing eval dataset",
        )
        
        print(f"  ✅ 数据加载和tokenization完成")
    
    def tokenize_function(self, examples):
        """Tokenization函数"""
        # 使用预先生成的text字段（已包含instruction+input+output）
        outputs = self.tokenizer(
            examples['text'],
            truncation=True,
            max_length=self.model_cfg.max_length,
            padding=False,  # 动态padding
            return_tensors=None,
        )
        
        # 设置labels（用于计算loss）
        outputs['labels'] = outputs['input_ids'].copy()
        
        return outputs
    
    def create_trainer(self):
        """创建Trainer"""
        print("\n" + "="*80)
        print("⚙️ 配置训练器")
        print("="*80)
        
        # 训练参数
        training_args = TrainingArguments(
            output_dir=self.train_cfg.output_dir,
            num_train_epochs=self.train_cfg.num_train_epochs,
            per_device_train_batch_size=self.train_cfg.per_device_train_batch_size,
            per_device_eval_batch_size=self.train_cfg.per_device_eval_batch_size,
            gradient_accumulation_steps=self.train_cfg.gradient_accumulation_steps,
            learning_rate=self.train_cfg.learning_rate,
            lr_scheduler_type=self.train_cfg.lr_scheduler_type,
            warmup_ratio=self.train_cfg.warmup_ratio,
            weight_decay=self.train_cfg.weight_decay,
            max_grad_norm=self.train_cfg.max_grad_norm,
            logging_steps=self.train_cfg.logging_steps,
            logging_dir=self.train_cfg.logging_dir,
            save_strategy=self.train_cfg.save_strategy,
            save_steps=self.train_cfg.save_steps,
            save_total_limit=self.train_cfg.save_total_limit,
            evaluation_strategy=self.train_cfg.evaluation_strategy,
            eval_steps=self.train_cfg.eval_steps,
            fp16=self.train_cfg.fp16,
            bf16=self.train_cfg.bf16,
            optim=self.train_cfg.optim,
            seed=self.train_cfg.seed,
            dataloader_num_workers=self.train_cfg.dataloader_num_workers,
            remove_unused_columns=self.train_cfg.remove_unused_columns,
            report_to=self.train_cfg.report_to,
            load_best_model_at_end=True,
            metric_for_best_model="eval_loss",
            greater_is_better=False,
        )
        
        # Data collator（用于动态padding）
        data_collator = DataCollatorForLanguageModeling(
            tokenizer=self.tokenizer,
            mlm=False,  # Causal LM不需要MLM
        )
        
        # 创建Trainer
        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=self.train_dataset,
            eval_dataset=self.eval_dataset,
            tokenizer=self.tokenizer,
            data_collator=data_collator,
        )
        
        print(f"  ✅ Trainer配置完成")
        print(f"     实际batch size: {self.train_cfg.per_device_train_batch_size * self.train_cfg.gradient_accumulation_steps}")
        print(f"     总训练步数: {len(self.train_dataset) // (self.train_cfg.per_device_train_batch_size * self.train_cfg.gradient_accumulation_steps) * self.train_cfg.num_train_epochs}")
        
        return trainer
    
    def train(self):
        """执行训练"""
        print("\n" + "="*80)
        print("🏋️ 开始训练")
        print("="*80)
        
        # 创建trainer
        trainer = self.create_trainer()
        
        # 训练
        train_result = trainer.train()
        
        # 保存最终模型
        print("\n💾 保存模型...")
        trainer.save_model()
        self.tokenizer.save_pretrained(self.train_cfg.output_dir)
        
        # 保存训练指标
        metrics = train_result.metrics
        trainer.log_metrics("train", metrics)
        trainer.save_metrics("train", metrics)
        trainer.save_state()
        
        print(f"\n✅ 训练完成！")
        print(f"   模型保存到: {self.train_cfg.output_dir}")
        print(f"   训练损失: {metrics['train_loss']:.4f}")
        
        return trainer


def main():
    """主训练函数"""
    # 配置
    model_cfg = ModelConfig(
        model_name_or_path="baichuan-inc/Baichuan2-7B-Base",
        max_length=2048,
        load_in_4bit=True,
    )
    
    lora_cfg = LoRAConfig(
        r=8,
        lora_alpha=16,
        lora_dropout=0.05,
    )
    
    train_cfg = TrainingConfig(
        output_dir="./output/tcm_sft_lora",
        num_train_epochs=3,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        learning_rate=2e-4,
        logging_steps=10,
        save_steps=100,
        eval_steps=100,
    )
    
    # 创建训练器
    trainer = TCMTrainer(model_cfg, lora_cfg, train_cfg)
    
    # 初始化
    trainer.setup()
    
    # 加载数据
    trainer.load_data(
        train_data_path="../data/processed/train",
        eval_data_path="../data/processed/val",
    )
    
    # 训练
    trainer.train()
    
    print("\n" + "="*80)
    print("🎉 训练流程全部完成！")
    print("="*80)
    print("\n后续步骤:")
    print("  1. 查看训练日志: tensorboard --logdir ./logs")
    print("  2. 测试模型: python ../inference/test_model.py")
    print("  3. 交互式演示: python ../inference/interactive_demo.py")


if __name__ == "__main__":
    # 检查环境
    print("环境检查:")
    print(f"  Python: {sys.version}")
    print(f"  PyTorch: {torch.__version__}")
    print(f"  CUDA可用: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"  CUDA版本: {torch.version.cuda}")
        print(f"  GPU数量: {torch.cuda.device_count()}")
        print(f"  GPU名称: {torch.cuda.get_device_name(0)}")
    print()
    
    # 运行训练
    main()

