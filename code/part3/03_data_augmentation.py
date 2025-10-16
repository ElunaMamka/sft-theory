"""
演示代码：SFT数据增强技术
文件位置：code/part3/03_data_augmentation.py

展示如何扩充SFT数据集
"""

import random
from typing import List, Dict


class SFTDataAugmenter:
    """SFT数据增强器"""
    
    def __init__(self):
        self.augmentation_methods = []
    
    def paraphrase_instruction(self, instruction: str) -> List[str]:
        """改写instruction（同义转换）"""
        # 这里提供一些简单的模板替换
        paraphrases = []
        
        templates = {
            "回答用户的问题": [
                "请回答以下问题",
                "针对用户提问，给出答案",
                "解答下面的疑问",
                "提供对以下问题的回答"
            ],
            "将文本总结成三句话": [
                "用三句话概括以下内容",
                "提供三句话的摘要",
                "简明扼要地总结为三句",
                "以三句话形式归纳以下文本"
            ],
            "编写一个Python函数": [
                "请用Python实现一个函数",
                "创建一个Python函数",
                "用Python写一个函数",
                "实现下面的Python函数"
            ]
        }
        
        for pattern, alternatives in templates.items():
            if pattern in instruction:
                for alt in alternatives:
                    paraphrases.append(instruction.replace(pattern, alt))
        
        return paraphrases if paraphrases else [instruction]
    
    def generate_variations(self, example: Dict) -> List[Dict]:
        """为单个样本生成变体"""
        variations = []
        
        # 方法1: 改写instruction
        instruction_paraphrases = self.paraphrase_instruction(example['instruction'])
        for inst in instruction_paraphrases[:2]:  # 最多取2个变体
            variations.append({
                "instruction": inst,
                "input": example['input'],
                "output": example['output'],
                "augmentation_method": "instruction_paraphrase"
            })
        
        # 方法2: 添加角色设定
        role_variations = [
            "作为一个专业的AI助手，" + example['instruction'],
            "你是一个友好且知识渊博的助手，" + example['instruction']
        ]
        for role_inst in role_variations[:1]:
            variations.append({
                "instruction": role_inst,
                "input": example['input'],
                "output": example['output'],
                "augmentation_method": "role_addition"
            })
        
        return variations
    
    def create_negative_examples(self, example: Dict) -> List[Dict]:
        """创建负例（展示不好的回答）"""
        negative_examples = []
        
        # 负例1: 过于简短
        negative_examples.append({
            "instruction": example['instruction'] + "（反例：过于简短）",
            "input": example['input'],
            "output": "不知道。",
            "is_negative": True,
            "reason": "回答过于简短，没有提供有价值的信息"
        })
        
        # 负例2: 离题
        negative_examples.append({
            "instruction": example['instruction'] + "（反例：答非所问）",
            "input": example['input'],
            "output": "这是一个很好的问题，但让我们先讨论一下天气...",
            "is_negative": True,
            "reason": "答非所问，没有回答用户的真实问题"
        })
        
        return negative_examples
    
    def back_translation(self, text: str) -> str:
        """回译增强（模拟）"""
        # 实际应用中，这里会调用翻译API：中文->英文->中文
        # 这里我们用简单的同义词替换来模拟
        
        replacements = {
            "人工智能": "AI",
            "机器学习": "ML",
            "深度学习": "深度神经网络",
            "函数": "方法",
            "参数": "变量"
        }
        
        result = text
        for old, new in replacements.items():
            if old in result:
                result = result.replace(old, new)
                break  # 只替换一个，保持自然
        
        return result
    
    def demonstrate_augmentation(self, example: Dict):
        """演示完整的增强流程"""
        print("="*80)
        print("🔄 数据增强演示")
        print("="*80)
        
        print("\n📝 原始样本:")
        print(f"instruction: {example['instruction']}")
        print(f"input:       {example['input']}")
        print(f"output:      {example['output'][:100]}...")
        
        print("\n" + "-"*80)
        print("🎯 增强方法 1: Instruction改写")
        print("-"*80)
        paraphrases = self.paraphrase_instruction(example['instruction'])
        for i, para in enumerate(paraphrases[:3], 1):
            print(f"{i}. {para}")
        
        print("\n" + "-"*80)
        print("🎭 增强方法 2: 添加角色设定")
        print("-"*80)
        role_examples = [
            "作为一个专业的AI助手，" + example['instruction'],
            "你是一个友好的教育工作者，" + example['instruction'],
            "以简单易懂的方式，" + example['instruction']
        ]
        for i, role in enumerate(role_examples, 1):
            print(f"{i}. {role}")
        
        print("\n" + "-"*80)
        print("🌐 增强方法 3: 回译（模拟）")
        print("-"*80)
        back_translated = self.back_translation(example['output'])
        print(f"原文: {example['output'][:80]}...")
        print(f"回译: {back_translated[:80]}...")
        
        print("\n" + "-"*80)
        print("❌ 增强方法 4: 创建负例")
        print("-"*80)
        negatives = self.create_negative_examples(example)
        for i, neg in enumerate(negatives, 1):
            print(f"{i}. {neg['output']}")
            print(f"   原因: {neg['reason']}\n")
        
        # 统计
        variations = self.generate_variations(example)
        print("\n" + "="*80)
        print(f"📊 增强效果:")
        print(f"   • 原始样本: 1")
        print(f"   • 生成变体: {len(variations)}")
        print(f"   • 负例: {len(negatives)}")
        print(f"   • 总计: {1 + len(variations) + len(negatives)} 样本")
        print(f"   • 扩充比例: {(1 + len(variations) + len(negatives))}x")
        print("="*80)


class DatasetExpander:
    """数据集扩充器"""
    
    def __init__(self):
        self.templates = self._create_templates()
    
    def _create_templates(self) -> Dict:
        """创建各类任务的模板"""
        return {
            "qa": {
                "instructions": [
                    "回答用户的问题",
                    "作为AI助手，回答以下问题",
                    "请提供准确的答案"
                ],
                "input_patterns": [
                    "什么是{concept}？",
                    "请解释{concept}",
                    "{concept}的定义是什么？"
                ]
            },
            "summarization": {
                "instructions": [
                    "将文本总结成三句话",
                    "用简洁的语言概括以下内容",
                    "提供一个简短的摘要"
                ],
                "input_patterns": [
                    "请总结这段内容",
                    "概括以下文字",
                    "提炼要点"
                ]
            }
        }
    
    def expand_dataset(self, seed_examples: List[Dict], target_size: int = 100) -> List[Dict]:
        """从少量种子样本扩展到目标规模"""
        expanded = list(seed_examples)
        augmenter = SFTDataAugmenter()
        
        while len(expanded) < target_size:
            # 随机选择一个种子样本
            seed = random.choice(seed_examples)
            # 生成变体
            variations = augmenter.generate_variations(seed)
            expanded.extend(variations[:target_size - len(expanded)])
        
        return expanded[:target_size]
    
    def show_expansion_stats(self, original: List[Dict], expanded: List[Dict]):
        """展示扩展统计"""
        print("\n" + "="*80)
        print("📈 数据集扩展统计")
        print("="*80)
        
        print(f"\n原始数据集:")
        print(f"  • 样本数: {len(original)}")
        
        print(f"\n扩展后数据集:")
        print(f"  • 样本数: {len(expanded)}")
        print(f"  • 扩充倍数: {len(expanded) / len(original):.1f}x")
        
        # 检查instruction多样性
        unique_instructions_orig = len(set(ex['instruction'] for ex in original))
        unique_instructions_exp = len(set(ex['instruction'] for ex in expanded))
        
        print(f"\nInstruction多样性:")
        print(f"  • 原始: {unique_instructions_orig} 种")
        print(f"  • 扩展后: {unique_instructions_exp} 种")
        print(f"  • 增加: {unique_instructions_exp - unique_instructions_orig} 种")


def main():
    """主函数"""
    # 创建示例
    example = {
        "instruction": "回答用户的问题",
        "input": "什么是机器学习？",
        "output": "机器学习是人工智能的一个分支，它让计算机能够从数据中学习并改进性能，而无需明确编程。机器学习算法可以识别模式、做出预测，并随着接收更多数据而不断优化。"
    }
    
    # 演示增强
    augmenter = SFTDataAugmenter()
    augmenter.demonstrate_augmentation(example)
    
    # 演示数据集扩展
    print("\n" + "="*80)
    print("📦 数据集扩展示例")
    print("="*80)
    
    seed_examples = [
        example,
        {
            "instruction": "将文本总结成三句话",
            "input": "长文本...",
            "output": "总结1。总结2。总结3。"
        }
    ]
    
    expander = DatasetExpander()
    expanded = expander.expand_dataset(seed_examples, target_size=10)
    expander.show_expansion_stats(seed_examples, expanded)
    
    print("\n💡 实际应用中的数据增强技术:")
    print("   1. 回译 (Back-translation): 中文→英文→中文")
    print("   2. 同义词替换: 使用同义词词典")
    print("   3. 指令改写: 使用大模型生成变体")
    print("   4. 负采样: 创建不好的回答作为对比")
    print("   5. 模板填充: 使用模板批量生成")
    
    print("\n" + "="*80)
    print("📁 代码位置: code/part3/03_data_augmentation.py")
    print("="*80)


if __name__ == "__main__":
    main()

