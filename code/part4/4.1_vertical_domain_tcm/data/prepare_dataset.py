"""
4.1 中医问诊助手 - 数据预处理和格式化
将原始数据转换为训练所需的格式
"""

import json
import os
from typing import List, Dict
from datasets import Dataset
import pandas as pd


class TCMDatasetPreparer:
    """中医数据集准备器"""
    
    def __init__(self, raw_data_path: str = 'tcm_raw_data.json'):
        self.raw_data_path = raw_data_path
        self.processed_data = []
        
    def load_raw_data(self) -> List[Dict]:
        """加载原始数据"""
        with open(self.raw_data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✅ 加载了 {len(data)} 条原始数据")
        return data
    
    def format_for_training(self, data: List[Dict]) -> List[Dict]:
        """
        格式化数据为训练格式
        采用 Alpaca 格式
        """
        formatted_data = []
        
        for item in data:
            # Alpaca format with Chinese instruction
            formatted_item = {
                'instruction': item['instruction'],
                'input': item['input'],
                'output': item['output'],
                # 为了适配不同的训练框架，也提供完整的 text 字段
                'text': self._create_full_prompt(item)
            }
            formatted_data.append(formatted_item)
        
        print(f"✅ 格式化了 {len(formatted_data)} 条数据")
        return formatted_data
    
    def _create_full_prompt(self, item: Dict) -> str:
        """
        创建完整的训练文本
        格式：<s>[INST] <<SYS>>\n{instruction}\n<</SYS>>\n\n{input}[/INST]{output}</s>
        这是 Llama-2 的指令格式
        """
        instruction = item['instruction']
        input_text = item['input']
        output = item['output']
        
        # Llama-2 style prompt
        prompt = f"""<s>[INST] <<SYS>>
{instruction}
<</SYS>>

{input_text} [/INST] {output} </s>"""
        
        return prompt
    
    def split_dataset(self, data: List[Dict], 
                     train_ratio: float = 0.9) -> tuple:
        """
        划分训练集和验证集
        """
        import random
        random.seed(42)
        random.shuffle(data)
        
        split_idx = int(len(data) * train_ratio)
        train_data = data[:split_idx]
        val_data = data[split_idx:]
        
        print(f"📊 数据划分:")
        print(f"  训练集: {len(train_data)} 条")
        print(f"  验证集: {len(val_data)} 条")
        
        return train_data, val_data
    
    def save_to_json(self, data: List[Dict], output_path: str):
        """保存为JSON格式"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 保存到: {output_path}")
    
    def save_to_huggingface_format(self, train_data: List[Dict], 
                                   val_data: List[Dict], 
                                   output_dir: str = 'processed'):
        """
        保存为 HuggingFace datasets 格式
        便于使用 transformers 的 Trainer
        """
        os.makedirs(output_dir, exist_ok=True)
        
        # 创建 Dataset 对象
        train_dataset = Dataset.from_pandas(pd.DataFrame(train_data))
        val_dataset = Dataset.from_pandas(pd.DataFrame(val_data))
        
        # 保存
        train_dataset.save_to_disk(f"{output_dir}/train")
        val_dataset.save_to_disk(f"{output_dir}/val")
        
        print(f"✅ HuggingFace格式数据保存到: {output_dir}/")
    
    def analyze_dataset(self, data: List[Dict]):
        """分析数据集统计信息"""
        print("\n" + "="*80)
        print("📊 数据集分析")
        print("="*80)
        
        # 基本统计
        total_samples = len(data)
        print(f"\n总样本数: {total_samples}")
        
        # 长度统计
        input_lengths = [len(item['input']) for item in data]
        output_lengths = [len(item['output']) for item in data]
        
        print(f"\n输入长度统计:")
        print(f"  最小值: {min(input_lengths)}")
        print(f"  最大值: {max(input_lengths)}")
        print(f"  平均值: {sum(input_lengths)/len(input_lengths):.0f}")
        
        print(f"\n输出长度统计:")
        print(f"  最小值: {min(output_lengths)}")
        print(f"  最大值: {max(output_lengths)}")
        print(f"  平均值: {sum(output_lengths)/len(output_lengths):.0f}")
        
        # Token估算（中文平均1.5字符=1 token）
        avg_total_tokens = (sum(input_lengths) + sum(output_lengths)) / len(data) / 1.5
        print(f"\n平均token数（估算）: {avg_total_tokens:.0f}")
        
        # 内容分析
        print(f"\n内容特点:")
        symptoms_keywords = ['症状', '疼痛', '不适', '感觉']
        diagnosis_keywords = ['辨证', '证型', '阴虚', '阳虚', '气虚', '血虚']
        treatment_keywords = ['治疗', '方药', '建议', '调理']
        
        samples_with_symptoms = sum(1 for item in data 
                                   if any(kw in item['input'] for kw in symptoms_keywords))
        samples_with_diagnosis = sum(1 for item in data 
                                    if any(kw in item['output'] for kw in diagnosis_keywords))
        samples_with_treatment = sum(1 for item in data 
                                    if any(kw in item['output'] for kw in treatment_keywords))
        
        print(f"  包含症状描述: {samples_with_symptoms}/{total_samples}")
        print(f"  包含辨证分析: {samples_with_diagnosis}/{total_samples}")
        print(f"  包含治疗方案: {samples_with_treatment}/{total_samples}")
        
        print("\n" + "="*80)
    
    def prepare_full_pipeline(self):
        """完整的数据准备流程"""
        print("="*80)
        print("🚀 开始数据准备流程")
        print("="*80)
        
        # 1. 加载原始数据
        raw_data = self.load_raw_data()
        
        # 2. 数据分析
        self.analyze_dataset(raw_data)
        
        # 3. 格式化数据
        formatted_data = self.format_for_training(raw_data)
        
        # 4. 划分数据集
        train_data, val_data = self.split_dataset(formatted_data)
        
        # 5. 保存为多种格式
        print("\n💾 保存数据...")
        
        # JSON格式
        self.save_to_json(train_data, 'train_data.json')
        self.save_to_json(val_data, 'val_data.json')
        
        # HuggingFace格式
        self.save_to_huggingface_format(train_data, val_data)
        
        print("\n" + "="*80)
        print("✅ 数据准备完成！")
        print("="*80)
        print("\n📁 生成的文件:")
        print("  - train_data.json (JSON格式训练数据)")
        print("  - val_data.json (JSON格式验证数据)")
        print("  - processed/train/ (HuggingFace格式训练数据)")
        print("  - processed/val/ (HuggingFace格式验证数据)")
        
        return train_data, val_data


def main():
    """主函数"""
    preparer = TCMDatasetPreparer('tcm_raw_data.json')
    train_data, val_data = preparer.prepare_full_pipeline()
    
    # 打印一个训练样本示例
    print("\n" + "="*80)
    print("📝 训练样本示例（前500字符）")
    print("="*80)
    print(train_data[0]['text'][:500])
    print("...")
    print("="*80)


if __name__ == "__main__":
    main()

