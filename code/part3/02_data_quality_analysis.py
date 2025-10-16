"""
演示代码：SFT数据质量分析
文件位置：code/part3/02_data_quality_analysis.py

分析和评估SFT数据集的质量
"""

import re
from typing import List, Dict, Tuple
from collections import Counter


class DataQualityAnalyzer:
    """数据质量分析器"""
    
    def __init__(self):
        self.quality_issues = []
    
    def check_completeness(self, example: Dict) -> Tuple[bool, str]:
        """检查数据完整性"""
        required_fields = ['instruction', 'input', 'output']
        
        for field in required_fields:
            if field not in example:
                return False, f"缺少字段: {field}"
            if not example[field] or example[field].strip() == '':
                return False, f"字段为空: {field}"
        
        return True, "完整"
    
    def check_length(self, example: Dict) -> Tuple[bool, List[str]]:
        """检查长度是否合理"""
        issues = []
        
        # instruction不应该太长
        if len(example.get('instruction', '')) > 200:
            issues.append("instruction过长（>200字符）")
        
        # input不应该太短
        if len(example.get('input', '')) < 5:
            issues.append("input过短（<5字符）")
        
        # output不应该太短
        if len(example.get('output', '')) < 10:
            issues.append("output过短（<10字符）")
        
        # output不应该超长
        if len(example.get('output', '')) > 2000:
            issues.append("output过长（>2000字符），可能需要分段")
        
        return len(issues) == 0, issues
    
    def check_diversity(self, examples: List[Dict]) -> Dict:
        """检查数据多样性"""
        instructions = [ex['instruction'] for ex in examples]
        instruction_counts = Counter(instructions)
        
        # 计算指标
        unique_instructions = len(instruction_counts)
        most_common = instruction_counts.most_common(3)
        
        # 检查是否过于单一
        if unique_instructions < len(examples) * 0.3:
            diversity_score = "低"
        elif unique_instructions < len(examples) * 0.6:
            diversity_score = "中"
        else:
            diversity_score = "高"
        
        return {
            "unique_instructions": unique_instructions,
            "total_examples": len(examples),
            "diversity_score": diversity_score,
            "most_common": most_common
        }
    
    def check_output_quality(self, output: str) -> Tuple[bool, List[str]]:
        """检查输出质量"""
        issues = []
        
        # 检查是否包含常见问题
        if "对不起" in output and "我不知道" in output:
            issues.append("模型拒绝回答（可能需要提供更多信息）")
        
        if output.count('\n') > 20:
            issues.append("输出行数过多，建议简化")
        
        # 检查是否有重复内容
        sentences = output.split('。')
        if len(sentences) != len(set(sentences)):
            issues.append("输出包含重复句子")
        
        # 检查中英文混杂
        has_chinese = bool(re.search(r'[\u4e00-\u9fff]', output))
        has_english = bool(re.search(r'[a-zA-Z]{3,}', output))
        
        if has_chinese and has_english:
            # 这不一定是问题，只是提醒
            pass
        
        return len(issues) == 0, issues
    
    def analyze_dataset(self, examples: List[Dict]) -> Dict:
        """全面分析数据集"""
        print("="*80)
        print("🔍 SFT数据集质量分析")
        print("="*80)
        
        # 1. 完整性检查
        print("\n1️⃣ 完整性检查:")
        complete_count = 0
        for i, example in enumerate(examples):
            is_complete, msg = self.check_completeness(example)
            if is_complete:
                complete_count += 1
            else:
                print(f"   样本 {i}: ❌ {msg}")
        
        completeness_rate = complete_count / len(examples) * 100
        print(f"   ✓ 完整样本: {complete_count}/{len(examples)} ({completeness_rate:.1f}%)")
        
        # 2. 长度检查
        print("\n2️⃣ 长度合理性检查:")
        length_ok_count = 0
        for i, example in enumerate(examples[:5]):  # 只检查前5个
            is_ok, issues = self.check_length(example)
            if is_ok:
                length_ok_count += 1
            else:
                print(f"   样本 {i}: ⚠️  {'; '.join(issues)}")
        
        # 3. 多样性检查
        print("\n3️⃣ 数据多样性分析:")
        diversity_stats = self.check_diversity(examples)
        print(f"   • 唯一instruction数: {diversity_stats['unique_instructions']}")
        print(f"   • 总样本数: {diversity_stats['total_examples']}")
        print(f"   • 多样性评分: {diversity_stats['diversity_score']}")
        print(f"   • 最常见的instruction:")
        for inst, count in diversity_stats['most_common']:
            print(f"     - '{inst[:50]}...' ({count}次)")
        
        # 4. 输出质量检查
        print("\n4️⃣ 输出质量检查:")
        quality_ok_count = 0
        for i, example in enumerate(examples[:5]):
            is_ok, issues = self.check_output_quality(example['output'])
            if is_ok:
                quality_ok_count += 1
            else:
                print(f"   样本 {i}: ⚠️  {'; '.join(issues)}")
        
        # 5. 统计摘要
        print("\n5️⃣ 统计摘要:")
        all_text = ' '.join([ex['instruction'] + ex['input'] + ex['output'] 
                            for ex in examples])
        avg_instruction_len = sum(len(ex['instruction']) for ex in examples) / len(examples)
        avg_input_len = sum(len(ex['input']) for ex in examples) / len(examples)
        avg_output_len = sum(len(ex['output']) for ex in examples) / len(examples)
        
        print(f"   • 平均instruction长度: {avg_instruction_len:.1f} 字符")
        print(f"   • 平均input长度: {avg_input_len:.1f} 字符")
        print(f"   • 平均output长度: {avg_output_len:.1f} 字符")
        print(f"   • 总字符数: {len(all_text):,}")
        
        # 6. 质量建议
        print("\n6️⃣ 质量改进建议:")
        suggestions = []
        
        if completeness_rate < 95:
            suggestions.append("• 补充缺失字段，确保所有样本完整")
        
        if diversity_stats['diversity_score'] == "低":
            suggestions.append("• 增加instruction的多样性，避免过于单一")
        
        if avg_output_len < 50:
            suggestions.append("• output可能过短，考虑提供更详细的回答")
        elif avg_output_len > 500:
            suggestions.append("• output可能过长，考虑简化或分段")
        
        if suggestions:
            for suggestion in suggestions:
                print(f"   {suggestion}")
        else:
            print("   ✓ 数据集质量良好！")
        
        return {
            "completeness_rate": completeness_rate,
            "diversity": diversity_stats,
            "avg_lengths": {
                "instruction": avg_instruction_len,
                "input": avg_input_len,
                "output": avg_output_len
            }
        }


def demonstrate_good_vs_bad_examples():
    """展示好的和坏的数据示例"""
    print("\n" + "="*80)
    print("📊 好数据 vs 坏数据对比")
    print("="*80)
    
    print("\n❌ 坏数据示例 1 - instruction不清晰:")
    bad_example_1 = {
        "instruction": "回答",
        "input": "AI是什么",
        "output": "AI就是AI"
    }
    print(f"  instruction: {bad_example_1['instruction']}")
    print(f"  input:       {bad_example_1['input']}")
    print(f"  output:      {bad_example_1['output']}")
    print("  问题: ❌ instruction过于简单，output没有提供有价值的信息")
    
    print("\n✅ 好数据示例 1 - 清晰且详细:")
    good_example_1 = {
        "instruction": "作为AI助手，用通俗易懂的语言解释技术概念",
        "input": "什么是人工智能？",
        "output": "人工智能(AI)是让计算机模拟人类智能的技术。就像人类能够学习、推理和解决问题，AI也能做到这些。例如，当你用语音助手或者看到手机自动识别照片中的人脸，这些都是AI在工作。AI包括机器学习、深度学习等多个分支，正在改变我们的生活方式。"
    }
    print(f"  instruction: {good_example_1['instruction']}")
    print(f"  input:       {good_example_1['input']}")
    print(f"  output:      {good_example_1['output'][:80]}...")
    print("  优点: ✅ instruction明确角色和风格，output详细且易懂")
    
    print("\n❌ 坏数据示例 2 - 输出过短:")
    bad_example_2 = {
        "instruction": "写一个Python函数",
        "input": "计算两数之和",
        "output": "def add(a,b):return a+b"
    }
    print(f"  output: {bad_example_2['output']}")
    print("  问题: ❌ 没有注释，没有示例，格式不佳")
    
    print("\n✅ 好数据示例 2 - 输出详细:")
    good_example_2 = {
        "instruction": "编写一个Python函数并提供使用示例",
        "input": "计算两数之和",
        "output": """```python
def add_numbers(a, b):
    \"\"\"
    计算两个数的和
    
    Args:
        a: 第一个数
        b: 第二个数
    
    Returns:
        两数之和
    \"\"\"
    return a + b

# 使用示例
result = add_numbers(3, 5)
print(result)  # 输出: 8
```"""
    }
    print(f"  output: {good_example_2['output'][:80]}...")
    print("  优点: ✅ 有文档字符串，有类型说明，有使用示例")


def main():
    """主函数"""
    # 创建示例数据
    examples = [
        {
            "instruction": "回答用户的问题",
            "input": "什么是机器学习？",
            "output": "机器学习是人工智能的一个分支，它让计算机能够从数据中学习并改进，而无需明确编程。"
        },
        {
            "instruction": "回答用户的问题",
            "input": "Python如何定义函数？",
            "output": "使用def关键字，格式为：def function_name(parameters): 函数体"
        },
        {
            "instruction": "将文本总结成一句话",
            "input": "深度学习是机器学习的一个子集...",
            "output": "深度学习使用多层神经网络来学习数据的复杂模式。"
        },
        {
            "instruction": "回答用户的问题",
            "input": "什么是神经网络？",
            "output": "神经网络是一种模仿人脑结构的计算模型，由多个相互连接的节点组成，能够学习复杂的模式。"
        }
    ]
    
    # 分析数据集
    analyzer = DataQualityAnalyzer()
    results = analyzer.analyze_dataset(examples)
    
    # 展示好坏对比
    demonstrate_good_vs_bad_examples()
    
    print("\n" + "="*80)
    print("📁 代码位置: code/part3/02_data_quality_analysis.py")
    print("="*80)


if __name__ == "__main__":
    main()

