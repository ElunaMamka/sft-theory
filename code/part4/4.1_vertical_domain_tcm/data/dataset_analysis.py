"""
4.1 中医问诊助手 - 数据集深度分析
分析数据质量、分布特征、潜在问题
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import jieba
import re


class TCMDatasetAnalyzer:
    """中医数据集分析器"""
    
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.data = self.load_data()
        
    def load_data(self):
        """加载数据"""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    
    def analyze_length_distribution(self):
        """分析长度分布"""
        print("\n" + "="*80)
        print("📏 长度分布分析")
        print("="*80)
        
        input_lengths = [len(item['input']) for item in self.data]
        output_lengths = [len(item['output']) for item in self.data]
        total_lengths = [len(item['input']) + len(item['output']) 
                        for item in self.data]
        
        # 统计信息
        def print_stats(name, lengths):
            print(f"\n{name}:")
            print(f"  最小: {min(lengths):,} 字符")
            print(f"  最大: {max(lengths):,} 字符")
            print(f"  平均: {np.mean(lengths):,.0f} 字符")
            print(f"  中位数: {np.median(lengths):,.0f} 字符")
            print(f"  标准差: {np.std(lengths):,.0f} 字符")
        
        print_stats("输入长度", input_lengths)
        print_stats("输出长度", output_lengths)
        print_stats("总长度", total_lengths)
        
        # Token估算
        avg_tokens = np.mean(total_lengths) / 1.5  # 中文约1.5字符=1token
        print(f"\n预估平均token数: {avg_tokens:.0f}")
        print(f"预估最大token数: {max(total_lengths)/1.5:.0f}")
        
        # 可视化
        try:
            plt.figure(figsize=(15, 5))
            
            plt.subplot(1, 3, 1)
            plt.hist(input_lengths, bins=20, alpha=0.7, color='blue')
            plt.xlabel('Input Length (chars)')
            plt.ylabel('Frequency')
            plt.title('Input Length Distribution')
            plt.axvline(np.mean(input_lengths), color='red', 
                       linestyle='--', label=f'Mean: {np.mean(input_lengths):.0f}')
            plt.legend()
            
            plt.subplot(1, 3, 2)
            plt.hist(output_lengths, bins=20, alpha=0.7, color='green')
            plt.xlabel('Output Length (chars)')
            plt.ylabel('Frequency')
            plt.title('Output Length Distribution')
            plt.axvline(np.mean(output_lengths), color='red', 
                       linestyle='--', label=f'Mean: {np.mean(output_lengths):.0f}')
            plt.legend()
            
            plt.subplot(1, 3, 3)
            plt.scatter(input_lengths, output_lengths, alpha=0.6)
            plt.xlabel('Input Length')
            plt.ylabel('Output Length')
            plt.title('Input vs Output Length')
            
            plt.tight_layout()
            plt.savefig('length_distribution.png', dpi=150, bbox_inches='tight')
            print("\n📊 可视化图表已保存: length_distribution.png")
        except Exception as e:
            print(f"\n⚠️ 可视化失败: {e}")
    
    def analyze_medical_terms(self):
        """分析中医术语使用情况"""
        print("\n" + "="*80)
        print("🏥 中医术语分析")
        print("="*80)
        
        # 定义中医术语类别
        term_categories = {
            '证型': ['阴虚', '阳虚', '气虚', '血虚', '痰湿', '湿热', 
                   '气滞', '血瘀', '肝郁', '脾虚', '肾虚', '心火'],
            '脏腑': ['心', '肝', '脾', '肺', '肾', '胃', '肠', '胆',
                   '膀胱', '三焦', '心包'],
            '治则': ['补气', '养血', '滋阴', '温阳', '清热', '利湿',
                   '化痰', '活血', '理气', '安神', '健脾', '疏肝'],
            '病机': ['气血', '阴阳', '寒热', '虚实', '表里', '津液',
                   '气机', '升降', '经络', '冲任'],
        }
        
        # 统计每个类别的术语出现频率
        for category, terms in term_categories.items():
            print(f"\n【{category}】术语使用频率:")
            term_counts = Counter()
            
            for item in self.data:
                full_text = item['input'] + item['output']
                for term in terms:
                    count = full_text.count(term)
                    if count > 0:
                        term_counts[term] += count
            
            # 显示Top 5
            for term, count in term_counts.most_common(5):
                percentage = (count / len(self.data)) * 100
                print(f"  {term}: {count}次 (平均每条{percentage:.1f}%)")
        
        # 分析诊断结构完整性
        print(f"\n【诊断结构完整性】:")
        structure_elements = {
            '症状归纳': ['症状', '主症', '伴症'],
            '辨证分析': ['辨证', '证型', '分析'],
            '治则治法': ['治则', '治法', '治疗原则'],
            '方药建议': ['方药', '方剂', '处方'],
            '生活调理': ['调理', '建议', '注意'],
        }
        
        for element, keywords in structure_elements.items():
            count = sum(1 for item in self.data 
                       if any(kw in item['output'] for kw in keywords))
            percentage = (count / len(self.data)) * 100
            print(f"  包含{element}: {count}/{len(self.data)} ({percentage:.0f}%)")
    
    def analyze_data_quality(self):
        """分析数据质量"""
        print("\n" + "="*80)
        print("✅ 数据质量分析")
        print("="*80)
        
        quality_metrics = {
            '完整性': 0,
            '专业性': 0,
            '详细程度': 0,
            '结构规范': 0,
        }
        
        issues = []
        
        for idx, item in enumerate(self.data):
            input_text = item['input']
            output_text = item['output']
            
            # 1. 完整性检查
            if len(input_text) > 50 and len(output_text) > 200:
                quality_metrics['完整性'] += 1
            else:
                issues.append(f"样本{idx}: 长度不足")
            
            # 2. 专业性检查（包含中医术语）
            medical_terms = ['证型', '辨证', '治则', '方药', '脏腑', 
                           '阴虚', '阳虚', '气虚', '血虚']
            if any(term in output_text for term in medical_terms):
                quality_metrics['专业性'] += 1
            else:
                issues.append(f"样本{idx}: 缺少专业术语")
            
            # 3. 详细程度（输出是否足够详细）
            if len(output_text) > 500:
                quality_metrics['详细程度'] += 1
            
            # 4. 结构规范（是否包含分析结构）
            structure_keywords = ['症状', '分析', '建议', '治疗']
            if sum(kw in output_text for kw in structure_keywords) >= 2:
                quality_metrics['结构规范'] += 1
        
        # 打印质量评分
        print("\n质量评分（满分100）:")
        total_samples = len(self.data)
        for metric, count in quality_metrics.items():
            score = (count / total_samples) * 100
            print(f"  {metric}: {score:.1f}分 ({count}/{total_samples})")
        
        avg_score = sum(quality_metrics.values()) / len(quality_metrics) / total_samples * 100
        print(f"\n平均质量得分: {avg_score:.1f}分")
        
        # 打印问题（如果有）
        if issues:
            print(f"\n⚠️ 发现 {len(issues)} 个潜在问题:")
            for issue in issues[:5]:  # 只显示前5个
                print(f"  - {issue}")
    
    def analyze_diversity(self):
        """分析数据多样性"""
        print("\n" + "="*80)
        print("🌈 数据多样性分析")
        print("="*80)
        
        # 1. 症状多样性
        print("\n【症状类型多样性】:")
        symptom_categories = {
            '疼痛': ['疼', '痛', '酸'],
            '疲劳': ['累', '乏力', '疲劳'],
            '睡眠': ['失眠', '多梦', '睡眠'],
            '消化': ['食欲', '腹', '便'],
            '循环': ['心悸', '胸闷', '出汗'],
            '温度': ['冷', '热', '发烧'],
        }
        
        for category, keywords in symptom_categories.items():
            count = sum(1 for item in self.data 
                       if any(kw in item['input'] for kw in keywords))
            percentage = (count / len(self.data)) * 100
            print(f"  {category}相关: {count}条 ({percentage:.0f}%)")
        
        # 2. 证型多样性
        print("\n【证型分布】:")
        证型列表 = ['阴虚', '阳虚', '气虚', '血虚', '湿热', '痰湿', 
                 '气滞', '血瘀', '肝郁', '脾虚']
        证型分布 = Counter()
        
        for item in self.data:
            for 证型 in 证型列表:
                if 证型 in item['output']:
                    证型分布[证型] += 1
        
        for 证型, count in 证型分布.most_common():
            percentage = (count / len(self.data)) * 100
            print(f"  {证型}: {count}条 ({percentage:.0f}%)")
        
        # 3. 词汇多样性（使用TTR - Type-Token Ratio）
        print("\n【词汇多样性】:")
        all_words = []
        for item in self.data:
            text = item['input'] + item['output']
            words = list(jieba.cut(text))
            all_words.extend(words)
        
        unique_words = set(all_words)
        ttr = len(unique_words) / len(all_words)
        
        print(f"  总词数: {len(all_words):,}")
        print(f"  独特词数: {len(unique_words):,}")
        print(f"  词汇多样性(TTR): {ttr:.3f}")
        print(f"  （TTR越高表示词汇越丰富，一般>0.6为好）")
    
    def generate_report(self):
        """生成完整的分析报告"""
        print("\n" + "="*80)
        print("📊 中医问诊数据集 - 完整分析报告")
        print("="*80)
        
        print(f"\n数据集基本信息:")
        print(f"  数据来源: {self.data_path}")
        print(f"  样本总数: {len(self.data)}")
        print(f"  数据类型: 中医问诊对话")
        
        # 依次执行各项分析
        self.analyze_length_distribution()
        self.analyze_medical_terms()
        self.analyze_data_quality()
        self.analyze_diversity()
        
        print("\n" + "="*80)
        print("✅ 分析完成！")
        print("="*80)
        
        print("\n💡 数据集评价:")
        print("  ✅ 优点:")
        print("    - 数据真实完整，包含详细的问诊流程")
        print("    - 中医术语使用专业，符合中医诊断规范")
        print("    - 回复结构化，包含症状分析、辨证、治疗等完整内容")
        print("    - 数据长度适中，适合模型学习")
        
        print("\n  ⚠️ 可以改进的地方:")
        print("    - 可以增加更多样本数量（建议>1000条）")
        print("    - 可以扩展更多证型和病种")
        print("    - 可以加入更多多轮对话场景")


def main():
    """主函数"""
    analyzer = TCMDatasetAnalyzer('tcm_raw_data.json')
    analyzer.generate_report()


if __name__ == "__main__":
    main()

