"""
4.1 中医问诊助手 - 分布式训练脚本
支持多GPU训练、DeepSpeed、FSDP等
"""

import os
import torch
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
from accelerate import Accelerator
from train_lora import TCMTrainer
from model.model_config import ModelConfig, LoRAConfig, TrainingConfig


def setup_distributed():
    """设置分布式训练环境"""
    if 'RANK' in os.environ and 'WORLD_SIZE' in os.environ:
        rank = int(os.environ['RANK'])
        world_size = int(os.environ['WORLD_SIZE'])
        local_rank = int(os.environ['LOCAL_RANK'])
    else:
        print("未检测到分布式环境，使用单GPU训练")
        return False
    
    torch.cuda.set_device(local_rank)
    dist.init_process_group(backend='nccl')
    
    if rank == 0:
        print(f"分布式训练设置:")
        print(f"  World size: {world_size}")
        print(f"  Rank: {rank}")
        print(f"  Local rank: {local_rank}")
    
    return True


def train_with_accelerate():
    """
    使用Accelerate进行分布式训练
    Accelerate会自动处理多GPU、混合精度、梯度累积等
    """
    print("="*80)
    print("🚀 使用Accelerate进行分布式训练")
    print("="*80)
    
    # 创建Accelerator
    accelerator = Accelerator(
        gradient_accumulation_steps=4,
        mixed_precision='bf16',  # 'fp16' | 'bf16' | 'no'
        log_with='tensorboard',
        project_dir='./logs',
    )
    
    if accelerator.is_main_process:
        print(f"\n加速器信息:")
        print(f"  设备: {accelerator.device}")
        print(f"  分布式类型: {accelerator.distributed_type}")
        print(f"  进程数: {accelerator.num_processes}")
        print(f"  混合精度: {accelerator.mixed_precision}")
    
    # 配置
    model_cfg = ModelConfig(
        model_name_or_path="baichuan-inc/Baichuan2-7B-Base",
        load_in_4bit=False,  # 分布式训练时不使用量化
    )
    
    lora_cfg = LoRAConfig(r=8, lora_alpha=16)
    
    train_cfg = TrainingConfig(
        output_dir="./output/tcm_sft_lora_distributed",
        num_train_epochs=3,
        per_device_train_batch_size=2,  # 每个GPU的batch size
        gradient_accumulation_steps=4,
        learning_rate=2e-4,
    )
    
    # 创建训练器
    trainer = TCMTrainer(model_cfg, lora_cfg, train_cfg)
    trainer.setup()
    trainer.load_data(
        train_data_path="../data/processed/train",
        eval_data_path="../data/processed/val",
    )
    
    # 使用Accelerate的Trainer会自动处理分布式
    trainer.train()
    
    if accelerator.is_main_process:
        print("\n✅ 分布式训练完成！")


def train_with_deepspeed():
    """
    使用DeepSpeed进行分布式训练
    DeepSpeed提供ZeRO优化，可以训练更大的模型
    """
    print("="*80)
    print("🚀 使用DeepSpeed进行分布式训练")
    print("="*80)
    
    # DeepSpeed配置
    deepspeed_config = {
        "train_batch_size": "auto",
        "train_micro_batch_size_per_gpu": "auto",
        "gradient_accumulation_steps": "auto",
        
        "optimizer": {
            "type": "AdamW",
            "params": {
                "lr": "auto",
                "betas": "auto",
                "eps": "auto",
                "weight_decay": "auto"
            }
        },
        
        "scheduler": {
            "type": "WarmupDecayLR",
            "params": {
                "warmup_min_lr": "auto",
                "warmup_max_lr": "auto",
                "warmup_num_steps": "auto",
                "total_num_steps": "auto"
            }
        },
        
        "fp16": {
            "enabled": False
        },
        
        "bf16": {
            "enabled": True
        },
        
        "zero_optimization": {
            "stage": 2,  # ZeRO stage 0/1/2/3
            "offload_optimizer": {
                "device": "cpu",  # 将optimizer状态offload到CPU
                "pin_memory": True
            },
            "allgather_partitions": True,
            "allgather_bucket_size": 2e8,
            "reduce_scatter": True,
            "reduce_bucket_size": 2e8,
            "overlap_comm": True,
            "contiguous_gradients": True
        },
        
        "gradient_clipping": 1.0,
        
        "steps_per_print": 10,
        "wall_clock_breakdown": False
    }
    
    # 保存DeepSpeed配置
    import json
    with open('deepspeed_config.json', 'w') as f:
        json.dump(deepspeed_config, f, indent=2)
    
    print("DeepSpeed配置已保存到: deepspeed_config.json")
    print("\n使用方法:")
    print("  deepspeed --num_gpus=4 train_distributed.py")
    
    # 配置
    model_cfg = ModelConfig(
        model_name_or_path="baichuan-inc/Baichuan2-7B-Base",
        load_in_4bit=False,
    )
    
    lora_cfg = LoRAConfig(r=8, lora_alpha=16)
    
    train_cfg = TrainingConfig(
        output_dir="./output/tcm_sft_lora_deepspeed",
        num_train_epochs=3,
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        learning_rate=2e-4,
        deepspeed='deepspeed_config.json',
    )
    
    # 训练
    trainer = TCMTrainer(model_cfg, lora_cfg, train_cfg)
    trainer.setup()
    trainer.load_data(
        train_data_path="../data/processed/train",
        eval_data_path="../data/processed/val",
    )
    trainer.train()


def print_usage_guide():
    """打印使用指南"""
    print("="*80)
    print("📖 分布式训练使用指南")
    print("="*80)
    
    print("\n【方式1：torchrun（推荐）】")
    print("  单机多卡:")
    print("    torchrun --nproc_per_node=4 train_distributed.py")
    print()
    print("  多机多卡:")
    print("    # 主节点")
    print("    torchrun --nproc_per_node=4 --nnodes=2 --node_rank=0 \\")
    print("             --master_addr=192.168.1.1 --master_port=29500 \\")
    print("             train_distributed.py")
    print("    # 从节点")
    print("    torchrun --nproc_per_node=4 --nnodes=2 --node_rank=1 \\")
    print("             --master_addr=192.168.1.1 --master_port=29500 \\")
    print("             train_distributed.py")
    
    print("\n【方式2：Accelerate】")
    print("  1. 配置:")
    print("     accelerate config")
    print("  2. 训练:")
    print("     accelerate launch train_distributed.py")
    
    print("\n【方式3：DeepSpeed】")
    print("  单机多卡:")
    print("    deepspeed --num_gpus=4 train_distributed.py")
    print()
    print("  多机多卡:")
    print("    deepspeed --num_gpus=4 --num_nodes=2 \\")
    print("              --master_addr=192.168.1.1 --master_port=29500 \\")
    print("              train_distributed.py")
    
    print("\n【性能对比】")
    print("  单GPU (V100 32GB):")
    print("    - Batch size: 4")
    print("    - 训练速度: ~2 samples/s")
    print("    - 预计时间: 3小时（1000条数据，3 epochs）")
    print()
    print("  4x GPU (V100 32GB):")
    print("    - Batch size: 16 (4x4)")
    print("    - 训练速度: ~7 samples/s")
    print("    - 预计时间: 45分钟")
    print("    - 加速比: 约4倍")
    
    print("\n【显存优化技巧】")
    print("  1. 梯度检查点: 降低40%显存，增加20%时间")
    print("  2. ZeRO Stage 1: 降低4倍optimizer显存")
    print("  3. ZeRO Stage 2: 降低8倍optimizer+gradient显存")
    print("  4. ZeRO Stage 3: 降低N倍所有参数显存（N=GPU数）")
    print("  5. Offload to CPU: 几乎无限显存，但慢50%")
    
    print("\n" + "="*80)


def main():
    """主函数"""
    import sys
    
    if len(sys.argv) > 1:
        mode = sys.argv[1]
        if mode == 'accelerate':
            train_with_accelerate()
        elif mode == 'deepspeed':
            train_with_deepspeed()
        else:
            print(f"未知模式: {mode}")
            print_usage_guide()
    else:
        print_usage_guide()
        print("\n示例:")
        print("  python train_distributed.py accelerate")
        print("  python train_distributed.py deepspeed")


if __name__ == "__main__":
    main()

