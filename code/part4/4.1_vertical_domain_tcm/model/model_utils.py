"""
4.1 中医问诊助手 - 模型工具函数
加载模型、tokenizer、LoRA等通用函数
"""

import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
)
from peft import (
    LoraConfig,
    get_peft_model,
    prepare_model_for_kbit_training,
    PeftModel,
)
from typing import Optional


def load_tokenizer(model_name_or_path: str, 
                   trust_remote_code: bool = True,
                   use_fast: bool = True):
    """
    加载tokenizer
    """
    print(f"📥 加载Tokenizer: {model_name_or_path}")
    
    tokenizer = AutoTokenizer.from_pretrained(
        model_name_or_path,
        trust_remote_code=trust_remote_code,
        use_fast=use_fast,
    )
    
    # 设置padding token
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        print("  ⚠️ pad_token未设置，使用eos_token作为pad_token")
    
    # 设置padding方向（左padding用于生成任务）
    tokenizer.padding_side = 'left'
    
    print(f"  ✅ Tokenizer加载完成")
    print(f"     词表大小: {len(tokenizer)}")
    print(f"     pad_token: {tokenizer.pad_token} (id: {tokenizer.pad_token_id})")
    print(f"     eos_token: {tokenizer.eos_token} (id: {tokenizer.eos_token_id})")
    
    return tokenizer


def load_base_model(model_name_or_path: str,
                    load_in_4bit: bool = True,
                    load_in_8bit: bool = False,
                    device_map: str = "auto",
                    trust_remote_code: bool = True):
    """
    加载基座模型（支持量化）
    """
    print(f"\n📥 加载基座模型: {model_name_or_path}")
    
    # 量化配置
    quantization_config = None
    if load_in_4bit:
        print("  🔧 启用4-bit量化（QLoRA）")
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
        )
    elif load_in_8bit:
        print("  🔧 启用8-bit量化")
        quantization_config = BitsAndBytesConfig(
            load_in_8bit=True,
        )
    
    # 加载模型
    model = AutoModelForCausalLM.from_pretrained(
        model_name_or_path,
        quantization_config=quantization_config,
        device_map=device_map,
        trust_remote_code=trust_remote_code,
        torch_dtype=torch.bfloat16 if not (load_in_4bit or load_in_8bit) else None,
    )
    
    # 统计参数量
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    
    print(f"  ✅ 模型加载完成")
    print(f"     总参数: {total_params:,}")
    print(f"     可训练参数: {trainable_params:,}")
    print(f"     设备映射: {device_map}")
    
    # 显存占用
    if torch.cuda.is_available():
        memory_allocated = torch.cuda.memory_allocated() / 1024**3
        memory_reserved = torch.cuda.memory_reserved() / 1024**3
        print(f"     GPU显存: 已分配 {memory_allocated:.2f}GB / 已保留 {memory_reserved:.2f}GB")
    
    return model


def prepare_model_for_lora(model, use_gradient_checkpointing: bool = True):
    """
    为LoRA训练准备模型
    """
    print(f"\n🔧 准备模型用于LoRA训练...")
    
    # 准备量化模型
    model = prepare_model_for_kbit_training(
        model,
        use_gradient_checkpointing=use_gradient_checkpointing
    )
    
    if use_gradient_checkpointing:
        model.config.use_cache = False
        print("  ✅ 启用梯度检查点（降低显存占用）")
    
    return model


def add_lora_adapters(model, 
                      r: int = 8,
                      lora_alpha: int = 16,
                      lora_dropout: float = 0.05,
                      target_modules: Optional[list] = None):
    """
    添加LoRA适配器
    """
    print(f"\n🔧 添加LoRA适配器...")
    
    if target_modules is None:
        # 默认目标模块（适用于大多数Transformer模型）
        target_modules = [
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj"
        ]
    
    # LoRA配置
    lora_config = LoraConfig(
        r=r,
        lora_alpha=lora_alpha,
        lora_dropout=lora_dropout,
        target_modules=target_modules,
        bias="none",
        task_type="CAUSAL_LM",
    )
    
    # 应用LoRA
    model = get_peft_model(model, lora_config)
    
    # 统计可训练参数
    model.print_trainable_parameters()
    
    return model


def load_model_for_training(model_name_or_path: str,
                           load_in_4bit: bool = True,
                           lora_r: int = 8,
                           lora_alpha: int = 16,
                           lora_dropout: float = 0.05):
    """
    一键加载并配置训练模型（完整流程）
    """
    print("="*80)
    print("🚀 加载并配置训练模型")
    print("="*80)
    
    # 1. 加载基座模型
    model = load_base_model(
        model_name_or_path=model_name_or_path,
        load_in_4bit=load_in_4bit,
    )
    
    # 2. 准备LoRA训练
    model = prepare_model_for_lora(model)
    
    # 3. 添加LoRA适配器
    model = add_lora_adapters(
        model,
        r=lora_r,
        lora_alpha=lora_alpha,
        lora_dropout=lora_dropout,
    )
    
    print("\n" + "="*80)
    print("✅ 模型准备完成，可以开始训练！")
    print("="*80)
    
    return model


def load_lora_model_for_inference(base_model_path: str,
                                  lora_adapter_path: str,
                                  load_in_4bit: bool = False):
    """
    加载LoRA模型用于推理
    """
    print("="*80)
    print("🚀 加载LoRA模型用于推理")
    print("="*80)
    
    # 1. 加载基座模型
    base_model = load_base_model(
        model_name_or_path=base_model_path,
        load_in_4bit=load_in_4bit,
    )
    
    # 2. 加载LoRA权重
    print(f"\n📥 加载LoRA适配器: {lora_adapter_path}")
    model = PeftModel.from_pretrained(
        base_model,
        lora_adapter_path,
    )
    
    # 3. 合并权重（可选，用于加速推理）
    # model = model.merge_and_unload()
    # print("  ✅ LoRA权重已合并到基座模型")
    
    print("  ✅ LoRA模型加载完成")
    
    return model


def format_instruction(instruction: str, 
                      input_text: str,
                      output_text: Optional[str] = None) -> str:
    """
    格式化指令为训练格式
    采用Llama-2风格的prompt
    """
    if output_text is None:
        # 推理模式
        prompt = f"""<s>[INST] <<SYS>>
{instruction}
<</SYS>>

{input_text} [/INST]"""
    else:
        # 训练模式
        prompt = f"""<s>[INST] <<SYS>>
{instruction}
<</SYS>>

{input_text} [/INST] {output_text} </s>"""
    
    return prompt


if __name__ == "__main__":
    # 测试加载流程
    print("测试模型加载流程...\n")
    
    # 注意：这只是演示，实际运行需要先下载模型
    model_name = "baichuan-inc/Baichuan2-7B-Base"
    
    print("示例配置:")
    print(f"  基座模型: {model_name}")
    print(f"  量化: 4-bit")
    print(f"  LoRA rank: 8")
    print(f"  LoRA alpha: 16")
    
    print("\n如需实际加载，请取消注释以下代码:")
    print("# model = load_model_for_training(model_name)")

