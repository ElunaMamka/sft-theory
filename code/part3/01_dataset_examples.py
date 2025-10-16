"""
演示代码：SFT数据集格式示例
文件位置：code/part3/01_dataset_examples.py

展示不同任务的SFT数据集格式和结构
"""

import json
from typing import List, Dict


class SFTDatasetExamples:
    """SFT数据集示例生成器"""
    
    def __init__(self):
        self.examples = {}
    
    def generate_qa_examples(self) -> List[Dict]:
        """生成问答任务数据集示例"""
        examples = [
            {
                "instruction": "回答用户的问题",
                "input": "什么是人工智能？",
                "output": "人工智能(AI)是计算机科学的一个分支，致力于创建能够模拟人类智能行为的系统。它包括机器学习、深度学习、自然语言处理、计算机视觉等多个子领域。AI系统可以学习、推理、解决问题，并在没有明确编程的情况下改进自己的性能。"
            },
            {
                "instruction": "回答用户的问题",
                "input": "机器学习和深度学习有什么区别？",
                "output": "机器学习是一种让计算机从数据中学习的方法，包括决策树、支持向量机等算法。深度学习是机器学习的一个子集，专门使用多层神经网络来学习数据的复杂模式。深度学习在图像识别、语音识别等任务上表现出色，但通常需要更多的数据和计算资源。"
            },
            {
                "instruction": "回答用户的问题",
                "input": "Python中如何创建一个列表？",
                "output": "在Python中创建列表有多种方法：\n1. 使用方括号：my_list = [1, 2, 3]\n2. 使用list()函数：my_list = list((1, 2, 3))\n3. 使用列表推导式：my_list = [x for x in range(5)]\n列表是Python中最常用的数据结构之一，可以存储不同类型的元素。"
            }
        ]
        return examples
    
    def generate_summarization_examples(self) -> List[Dict]:
        """生成文本摘要任务数据集示例"""
        examples = [
            {
                "instruction": "将下面的文章总结成三句话",
                "input": "OpenAI最近发布了GPT-4，这是其大型语言模型系列的最新版本。GPT-4在多个基准测试中展现出了显著的性能提升，特别是在推理能力、代码生成和多语言理解方面。该模型经过大规模预训练，并通过人类反馈强化学习(RLHF)进行了精细调优，使其能够更好地理解和执行复杂指令。研究团队表示，GPT-4在安全性和准确性方面也有重大改进，减少了生成有害内容的可能性。",
                "output": "OpenAI发布了GPT-4，在推理、代码和多语言能力上有显著提升。模型通过预训练和RLHF调优，能更好地执行复杂指令。GPT-4在安全性和准确性方面也有重大改进。"
            },
            {
                "instruction": "将下面的文章总结成三句话",
                "input": "气候变化是当今世界面临的最紧迫挑战之一。科学家警告说，如果不采取紧急行动，全球气温可能在本世纪末上升超过2摄氏度，导致灾难性后果。各国政府正在努力减少温室气体排放，推动可再生能源的发展，并制定适应气候变化的策略。",
                "output": "气候变化是全球最紧迫的挑战。科学家警告本世纪末气温可能上升超过2度。各国正努力减排并推动可再生能源发展。"
            }
        ]
        return examples
    
    def generate_coding_examples(self) -> List[Dict]:
        """生成代码生成任务数据集示例"""
        examples = [
            {
                "instruction": "编写一个Python函数来计算斐波那契数列",
                "input": "要求：使用递归方法，输入n返回第n个斐波那契数",
                "output": "```python\ndef fibonacci(n):\n    \"\"\"\n    计算第n个斐波那契数（递归方法）\n    \n    Args:\n        n: 整数，要计算的斐波那契数的位置\n    \n    Returns:\n        第n个斐波那契数\n    \"\"\"\n    if n <= 0:\n        return 0\n    elif n == 1:\n        return 1\n    else:\n        return fibonacci(n-1) + fibonacci(n-2)\n\n# 使用示例\nprint(fibonacci(10))  # 输出: 55\n```"
            },
            {
                "instruction": "编写一个Python函数实现二分查找",
                "input": "要求：在已排序的列表中查找目标值，返回索引或-1",
                "output": "```python\ndef binary_search(arr, target):\n    \"\"\"\n    二分查找算法\n    \n    Args:\n        arr: 已排序的列表\n        target: 要查找的目标值\n    \n    Returns:\n        目标值的索引，如果不存在返回-1\n    \"\"\"\n    left, right = 0, len(arr) - 1\n    \n    while left <= right:\n        mid = (left + right) // 2\n        \n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    \n    return -1\n\n# 使用示例\narr = [1, 3, 5, 7, 9, 11]\nprint(binary_search(arr, 7))  # 输出: 3\n```"
            }
        ]
        return examples
    
    def generate_dialogue_examples(self) -> List[Dict]:
        """生成对话任务数据集示例"""
        examples = [
            {
                "instruction": "你是一个友好的客服助手，请专业且礼貌地回答用户的问题",
                "input": "我的订单已经三天了还没发货，怎么回事？",
                "output": "非常抱歉给您带来了不便！我立即为您查询订单状态。请问您能提供一下订单号吗？这样我可以更快地帮您追踪物流信息。同时，如果订单确实延误，我们会为您申请加急处理或提供相应的补偿。感谢您的耐心等待！"
            },
            {
                "instruction": "你是一个友好的客服助手，请专业且礼貌地回答用户的问题",
                "input": "我想退货，但是已经拆封了，可以退吗？",
                "output": "感谢您的咨询！关于退货政策，即使商品已拆封，只要符合以下条件仍可以退货：1) 商品保持完好，没有影响二次销售；2) 在购买后7天内；3) 有完整的包装和配件。如果您的商品符合这些条件，我们很乐意为您办理退货。您可以在订单页面提交退货申请，或者我现在就帮您处理。请问需要我协助吗？"
            }
        ]
        return examples
    
    def generate_translation_examples(self) -> List[Dict]:
        """生成翻译任务数据集示例"""
        examples = [
            {
                "instruction": "将下面的中文翻译成英文",
                "input": "人工智能正在改变我们的生活方式。",
                "output": "Artificial intelligence is changing the way we live."
            },
            {
                "instruction": "将下面的英文翻译成中文",
                "input": "Machine learning is a subset of artificial intelligence.",
                "output": "机器学习是人工智能的一个子集。"
            },
            {
                "instruction": "将下面的中文翻译成英文",
                "input": "深度学习在图像识别领域取得了突破性进展。",
                "output": "Deep learning has made breakthrough progress in the field of image recognition."
            }
        ]
        return examples
    
    def generate_classification_examples(self) -> List[Dict]:
        """生成文本分类任务数据集示例"""
        examples = [
            {
                "instruction": "判断下面的评论是正面还是负面",
                "input": "这部电影太精彩了！演员演技出色，剧情引人入胜，强烈推荐！",
                "output": "正面"
            },
            {
                "instruction": "判断下面的评论是正面还是负面",
                "input": "完全浪费时间，剧情无聊，演技尴尬，不建议观看。",
                "output": "负面"
            },
            {
                "instruction": "判断下面的新闻属于哪个类别（科技/娱乐/体育/财经）",
                "input": "苹果公司今日发布最新款iPhone，搭载全新A17芯片，性能提升显著。",
                "output": "科技"
            }
        ]
        return examples
    
    def print_all_examples(self):
        """打印所有示例"""
        print("="*80)
        print("📚 SFT数据集格式示例")
        print("="*80)
        
        tasks = [
            ("问答任务 (Q&A)", self.generate_qa_examples),
            ("文本摘要 (Summarization)", self.generate_summarization_examples),
            ("代码生成 (Code Generation)", self.generate_coding_examples),
            ("对话任务 (Dialogue)", self.generate_dialogue_examples),
            ("翻译任务 (Translation)", self.generate_translation_examples),
            ("文本分类 (Classification)", self.generate_classification_examples)
        ]
        
        for task_name, generator in tasks:
            print(f"\n{'='*80}")
            print(f"📋 {task_name}")
            print(f"{'='*80}\n")
            
            examples = generator()
            for i, example in enumerate(examples[:2], 1):  # 只显示前2个
                print(f"示例 {i}:")
                print(f"  instruction: {example['instruction']}")
                print(f"  input:       {example['input'][:60]}{'...' if len(example['input']) > 60 else ''}")
                print(f"  output:      {example['output'][:60]}{'...' if len(example['output']) > 60 else ''}")
                print()
    
    def save_to_json(self, filename: str = "sft_dataset_examples.json"):
        """保存所有示例到JSON文件"""
        all_data = {
            "qa": self.generate_qa_examples(),
            "summarization": self.generate_summarization_examples(),
            "coding": self.generate_coding_examples(),
            "dialogue": self.generate_dialogue_examples(),
            "translation": self.generate_translation_examples(),
            "classification": self.generate_classification_examples()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ 数据已保存到: {filename}")
        print(f"总样本数: {sum(len(examples) for examples in all_data.values())}")
    
    def analyze_dataset_structure(self):
        """分析数据集结构"""
        print("\n" + "="*80)
        print("🔍 数据集结构分析")
        print("="*80 + "\n")
        
        all_examples = []
        all_examples.extend(self.generate_qa_examples())
        all_examples.extend(self.generate_summarization_examples())
        all_examples.extend(self.generate_coding_examples())
        
        # 统计
        avg_instruction_len = sum(len(ex['instruction']) for ex in all_examples) / len(all_examples)
        avg_input_len = sum(len(ex['input']) for ex in all_examples) / len(all_examples)
        avg_output_len = sum(len(ex['output']) for ex in all_examples) / len(all_examples)
        
        print(f"平均instruction长度: {avg_instruction_len:.1f} 字符")
        print(f"平均input长度:       {avg_input_len:.1f} 字符")
        print(f"平均output长度:      {avg_output_len:.1f} 字符")
        
        print(f"\n💡 观察:")
        print(f"  • instruction通常较短，描述任务类型")
        print(f"  • input是具体的用户输入")
        print(f"  • output是期望的模型响应")
        print(f"  • 三元组结构: (instruction, input, output)")


def main():
    """主函数"""
    dataset = SFTDatasetExamples()
    
    # 打印所有示例
    dataset.print_all_examples()
    
    # 分析结构
    dataset.analyze_dataset_structure()
    
    # 保存到文件
    dataset.save_to_json("code/part3/sft_dataset_examples.json")
    
    print("\n" + "="*80)
    print("📁 代码位置: code/part3/01_dataset_examples.py")
    print("="*80)


if __name__ == "__main__":
    main()

