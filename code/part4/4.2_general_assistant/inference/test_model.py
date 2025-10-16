"""
4.1 中医问诊助手 - 模型测试脚本
测试训练好的模型效果
"""

import sys
import os
import torch

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.model_utils import (
    load_tokenizer,
    load_lora_model_for_inference,
    format_instruction,
)


class TCMInferenceEngine:
    """中医推理引擎"""
    
    def __init__(self, base_model_path: str, lora_adapter_path: str):
        self.base_model_path = base_model_path
        self.lora_adapter_path = lora_adapter_path
        
        print("="*80)
        print("🏥 中医问诊助手 - 模型测试")
        print("="*80)
        
        # 加载模型和tokenizer
        self.tokenizer = load_tokenizer(base_model_path)
        self.model = load_lora_model_for_inference(
            base_model_path=base_model_path,
            lora_adapter_path=lora_adapter_path,
            load_in_4bit=True,
        )
        
        self.model.eval()
        print("\n✅ 模型加载完成，准备就绪！\n")
    
    def generate(self, 
                prompt: str,
                max_new_tokens: int = 1024,
                temperature: float = 0.7,
                top_p: float = 0.9,
                top_k: int = 50,
                repetition_penalty: float = 1.1):
        """生成回复"""
        
        # Tokenize
        inputs = self.tokenizer(prompt, return_tensors="pt")
        inputs = {k: v.to(self.model.device) for k, v in inputs.items()}
        
        # Generate
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
                repetition_penalty=repetition_penalty,
                do_sample=True,
                eos_token_id=self.tokenizer.eos_token_id,
                pad_token_id=self.tokenizer.pad_token_id,
            )
        
        # Decode
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # 提取回复部分（去掉输入的prompt）
        response = response[len(prompt):].strip()
        
        return response
    
    def test_single_case(self, 
                        instruction: str, 
                        patient_input: str,
                        expected_keywords: list = None):
        """测试单个案例"""
        print("="*80)
        print("📋 测试案例")
        print("="*80)
        
        print(f"\n【患者输入】")
        print(patient_input)
        
        # 格式化prompt
        prompt = format_instruction(instruction, patient_input)
        
        # 生成回复
        print(f"\n【模型回复】")
        response = self.generate(prompt)
        print(response)
        
        # 检查关键词
        if expected_keywords:
            print(f"\n【关键词检查】")
            for keyword in expected_keywords:
                if keyword in response:
                    print(f"  ✅ {keyword}")
                else:
                    print(f"  ❌ {keyword} (未提及)")
        
        print("\n" + "="*80)
        return response


def run_test_suite():
    """运行测试套件"""
    
    # 配置
    BASE_MODEL_PATH = "baichuan-inc/Baichuan2-7B-Base"
    LORA_ADAPTER_PATH = "../training/output/tcm_sft_lora"
    
    # 创建推理引擎
    engine = TCMInferenceEngine(BASE_MODEL_PATH, LORA_ADAPTER_PATH)
    
    # 测试用例
    test_cases = [
        {
            "instruction": "你是一位经验丰富的中医师，请根据患者的症状进行问诊和诊断。",
            "input": "医生您好，我最近总是感觉很累，手脚冰凉，吃饭也没什么胃口。舌头颜色比较淡。",
            "expected_keywords": ["辨证", "脾", "阳虚", "建议", "方药"]
        },
        {
            "instruction": "你是一位经验丰富的中医师，请根据患者的症状进行问诊和诊断。",
            "input": "我这段时间口干口苦，脾气很大容易发火，大便也很干。舌头红，苔黄。",
            "expected_keywords": ["肝", "湿热", "火旺", "治则", "清热"]
        },
        {
            "instruction": "你是一位经验丰富的中医师，请根据患者的症状进行问诊和诊断。",
            "input": "最近心慌心悸，晚上失眠，手心脚心发热，夜里会出汗。",
            "expected_keywords": ["心", "阴虚", "安神", "养阴", "滋阴"]
        },
    ]
    
    # 运行测试
    print("\n" + "="*80)
    print("🧪 开始测试")
    print("="*80)
    
    results = []
    for idx, case in enumerate(test_cases, 1):
        print(f"\n\n{'='*80}")
        print(f"测试用例 {idx}/{len(test_cases)}")
        print(f"{'='*80}")
        
        response = engine.test_single_case(
            instruction=case["instruction"],
            patient_input=case["input"],
            expected_keywords=case.get("expected_keywords"),
        )
        
        results.append({
            "case_id": idx,
            "input": case["input"],
            "response": response,
        })
    
    # 测试总结
    print("\n" + "="*80)
    print("📊 测试总结")
    print("="*80)
    print(f"\n总测试案例: {len(test_cases)}")
    print(f"完成测试: {len(results)}")
    
    # 保存测试结果
    import json
    with open('test_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n测试结果已保存到: test_results.json")


def compare_with_base_model():
    """对比基座模型和微调模型的效果"""
    print("="*80)
    print("🔬 基座模型 vs 微调模型 对比测试")
    print("="*80)
    
    BASE_MODEL_PATH = "baichuan-inc/Baichuan2-7B-Base"
    LORA_ADAPTER_PATH = "../training/output/tcm_sft_lora"
    
    # 测试问题
    instruction = "你是一位经验丰富的中医师，请根据患者的症状进行问诊和诊断。"
    patient_input = "医生，我最近总是感觉很累，手脚冰凉，吃饭没胃口，舌头颜色淡。"
    
    print(f"\n患者问题: {patient_input}\n")
    
    # 1. 基座模型
    print("-" * 80)
    print("【基座模型回复】（未经SFT微调）")
    print("-" * 80)
    
    tokenizer = load_tokenizer(BASE_MODEL_PATH)
    base_model = load_lora_model_for_inference(
        base_model_path=BASE_MODEL_PATH,
        lora_adapter_path=None,  # 不加载LoRA
        load_in_4bit=True,
    )
    
    prompt = format_instruction(instruction, patient_input)
    inputs = tokenizer(prompt, return_tensors="pt").to(base_model.device)
    
    with torch.no_grad():
        outputs = base_model.generate(
            **inputs,
            max_new_tokens=512,
            temperature=0.7,
            top_p=0.9,
        )
    
    base_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    base_response = base_response[len(prompt):].strip()
    print(base_response)
    
    # 2. 微调模型
    print("\n" + "-" * 80)
    print("【微调模型回复】（经过SFT微调）")
    print("-" * 80)
    
    engine = TCMInferenceEngine(BASE_MODEL_PATH, LORA_ADAPTER_PATH)
    sft_response = engine.generate(prompt, max_new_tokens=512)
    print(sft_response)
    
    # 3. 对比分析
    print("\n" + "="*80)
    print("📊 效果对比分析")
    print("="*80)
    
    analysis_criteria = {
        "专业术语": ["证型", "辨证", "治则", "方药", "脏腑"],
        "结构完整": ["症状", "分析", "建议", "治疗", "调理"],
        "中医思维": ["阴阳", "虚实", "寒热", "气血"],
    }
    
    for criterion, keywords in analysis_criteria.items():
        print(f"\n【{criterion}】")
        base_count = sum(1 for kw in keywords if kw in base_response)
        sft_count = sum(1 for kw in keywords if kw in sft_response)
        
        print(f"  基座模型: {base_count}/{len(keywords)} 个关键词")
        print(f"  微调模型: {sft_count}/{len(keywords)} 个关键词")
        
        if sft_count > base_count:
            print(f"  ✅ 微调模型更好")
        elif sft_count == base_count:
            print(f"  ➖ 持平")
        else:
            print(f"  ❌ 基座模型更好")


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='测试中医问诊助手模型')
    parser.add_argument('--mode', type=str, default='test', 
                       choices=['test', 'compare'],
                       help='测试模式: test(测试套件) | compare(对比测试)')
    
    args = parser.parse_args()
    
    if args.mode == 'test':
        run_test_suite()
    elif args.mode == 'compare':
        compare_with_base_model()


if __name__ == "__main__":
    main()
    
    print("\n" + "="*80)
    print("提示:")
    print("  python test_model.py --mode test     # 运行测试套件")
    print("  python test_model.py --mode compare  # 对比基座和微调模型")
    print("="*80)

