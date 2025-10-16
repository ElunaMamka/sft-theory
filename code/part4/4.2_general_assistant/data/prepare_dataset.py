"""
4.2 通用对话助手 - 数据预处理
将多任务数据转换为训练格式
"""

import json
import os
from typing import List, Dict
from datasets import Dataset
import pandas as pd


class GeneralAssistantDatasetPreparer:
    """通用助手数据集准备器"""
    
    def __init__(self, raw_data_path: str = 'general_assistant_raw_data.json'):
        self.raw_data_path = raw_data_path
        
    def load_raw_data(self) -> List[Dict]:
        """加载原始数据"""
        with open(self.raw_data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✅ 加载了 {len(data)} 条原始数据")
        return data
    
    def format_for_training(self, data: List[Dict]) -> List[Dict]:
        """格式化数据为训练格式"""
        formatted_data = []
        
        for item in data:
            formatted_item = {
                'instruction': item['instruction'],
                'input': item['input'],
                'output': item['output'],
                'task_type': item.get('task_type', 'general'),
                'text': self._create_full_prompt(item)
            }
            formatted_data.append(formatted_item)
        
        print(f"✅ 格式化了 {len(formatted_data)} 条数据")
        return formatted_data
    
    def _create_full_prompt(self, item: Dict) -> str:
        """创建完整的训练文本"""
        instruction = item['instruction']
        input_text = item['input']
        output = item['output']
        
        prompt = f"""<s>[INST] <<SYS>>
{instruction}
<</SYS>>

{input_text} [/INST] {output} </s>"""
        
        return prompt
    
    def split_dataset(self, data: List[Dict], train_ratio: float = 0.9) -> tuple:
        """划分数据集，保持任务类型平衡"""
        import random
        random.seed(42)
        
        # 按任务类型分组
        task_groups = {}
        for item in data:
            task = item.get('task_type', 'general')
            if task not in task_groups:
                task_groups[task] = []
            task_groups[task].append(item)
        
        # 每个任务类型分别划分
        train_data = []
        val_data = []
        
        for task, items in task_groups.items():
            random.shuffle(items)
            split_idx = int(len(items) * train_ratio)
            train_data.extend(items[:split_idx])
            val_data.extend(items[split_idx:])
        
        # 打乱顺序
        random.shuffle(train_data)
        random.shuffle(val_data)
        
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
        """保存为HuggingFace格式"""
        os.makedirs(output_dir, exist_ok=True)
        
        train_dataset = Dataset.from_pandas(pd.DataFrame(train_data))
        val_dataset = Dataset.from_pandas(pd.DataFrame(val_data))
        
        train_dataset.save_to_disk(f"{output_dir}/train")
        val_dataset.save_to_disk(f"{output_dir}/val")
        
        print(f"✅ HuggingFace格式数据保存到: {output_dir}/")
    
    def prepare_full_pipeline(self):
        """完整的数据准备流程"""
        print("="*80)
        print("🚀 开始数据准备流程")
        print("="*80)
        
        raw_data = self.load_raw_data()
        formatted_data = self.format_for_training(raw_data)
        train_data, val_data = self.split_dataset(formatted_data)
        
        print("\n💾 保存数据...")
        self.save_to_json(train_data, 'train_data.json')
        self.save_to_json(val_data, 'val_data.json')
        self.save_to_huggingface_format(train_data, val_data)
        
        print("\n✅ 数据准备完成！")
        return train_data, val_data


if __name__ == "__main__":
    preparer = GeneralAssistantDatasetPreparer()
    preparer.prepare_full_pipeline()

