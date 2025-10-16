"""
4.1 中医问诊助手 - 真实的数据筛选流水线
展示多轮迭代的数据筛选过程
"""

import json
import re
from typing import List, Dict, Tuple
from collections import Counter
import jieba


class TCMDataFilteringPipeline:
    """
    中医数据筛选流水线
    模拟真实的SFT数据准备过程：多轮筛选、问题发现、回溯修正
    """
    
    def __init__(self, raw_data_path: str):
        self.raw_data_path = raw_data_path
        self.raw_data = self.load_data(raw_data_path)
        self.filtering_history = []  # 记录每轮筛选的结果
        
    def load_data(self, path: str) -> List[Dict]:
        """加载原始数据"""
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def run_full_pipeline(self):
        """
        运行完整的筛选流程
        这是一个真实的迭代过程，会有回溯和修正
        """
        print("="*80)
        print("🔍 中医数据筛选流水线 - 真实迭代过程")
        print("="*80)
        
        # 第一轮：基础规则筛选
        round1_data = self.round1_basic_filtering(self.raw_data)
        
        # 第二轮：专业术语检查
        round2_data = self.round2_terminology_check(round1_data)
        
        # 第三轮：AI模型打分
        round3_data = self.round3_model_scoring(round2_data)
        
        # 问题发现！发现高分数据仍有问题
        print("\n" + "!"*80)
        print("❌ 问题发现：高分数据中发现了严重问题！")
        print("!"*80)
        self.discover_problems(round3_data)
        
        # 第四轮：回溯修正，添加新规则
        print("\n" + "="*80)
        print("🔄 第四轮：回溯修正，添加新的筛选规则")
        print("="*80)
        round4_data = self.round4_backtrack_and_fix(self.raw_data)
        
        # 第五轮：人工复核样本
        final_data = self.round5_manual_review(round4_data)
        
        # 保存最终数据
        self.save_final_data(final_data)
        
        # 生成筛选报告
        self.generate_filtering_report()
        
        return final_data
    
    def round1_basic_filtering(self, data: List[Dict]) -> List[Dict]:
        """
        第一轮：基础规则筛选
        过滤掉明显不合格的数据
        """
        print("\n" + "="*80)
        print("📋 第一轮筛选：基础规则过滤")
        print("="*80)
        
        filtered = []
        rejected = []
        
        for item in data:
            reasons = []
            
            # 规则1：长度检查
            if len(item['input']) < 20:
                reasons.append("输入过短（<20字）")
            if len(item['output']) < 100:
                reasons.append("输出过短（<100字）")
            
            # 规则2：包含禁用词
            forbidden_words = ['fuck', '傻逼', '白痴', '垃圾']
            if any(word in item['input'] + item['output'] for word in forbidden_words):
                reasons.append("包含禁用词")
            
            # 规则3：基本格式检查
            if not item.get('instruction') or not item.get('input') or not item.get('output'):
                reasons.append("缺少必要字段")
            
            # 规则4：重复内容检查（简单的）
            if item['input'] == item['output']:
                reasons.append("输入输出完全相同")
            
            if reasons:
                item['reject_reasons'] = reasons
                rejected.append(item)
            else:
                filtered.append(item)
        
        # 统计
        print(f"\n📊 筛选结果:")
        print(f"  输入: {len(data)} 条")
        print(f"  通过: {len(filtered)} 条")
        print(f"  拒绝: {len(rejected)} 条")
        
        if rejected:
            print(f"\n拒绝原因统计:")
            all_reasons = [r for item in rejected for r in item['reject_reasons']]
            for reason, count in Counter(all_reasons).most_common():
                print(f"  - {reason}: {count}条")
        
        self.filtering_history.append({
            'round': 1,
            'name': '基础规则筛选',
            'input_count': len(data),
            'output_count': len(filtered),
            'rejected_count': len(rejected)
        })
        
        return filtered
    
    def round2_terminology_check(self, data: List[Dict]) -> List[Dict]:
        """
        第二轮：专业术语检查
        确保数据包含足够的中医专业术语
        """
        print("\n" + "="*80)
        print("📋 第二轮筛选：中医专业术语检查")
        print("="*80)
        
        # 中医术语列表
        required_terms = {
            '证型': ['阴虚', '阳虚', '气虚', '血虚', '痰湿', '湿热', '血瘀', '气滞'],
            '脏腑': ['心', '肝', '脾', '肺', '肾', '胃', '肠', '胆'],
            '治则': ['补气', '养血', '滋阴', '温阳', '清热', '利湿', '化痰', '活血'],
            '诊断要素': ['症状', '舌象', '脉象', '辨证', '治则', '方药']
        }
        
        filtered = []
        low_quality = []
        
        for item in data:
            text = item['output']
            scores = {}
            
            # 检查每类术语的覆盖度
            for category, terms in required_terms.items():
                found = sum(1 for term in terms if term in text)
                coverage = found / len(terms)
                scores[category] = coverage
            
            # 计算总分
            total_score = sum(scores.values()) / len(scores)
            item['terminology_score'] = total_score
            item['terminology_details'] = scores
            
            # 阈值：至少要达到30%的术语覆盖
            if total_score >= 0.3:
                filtered.append(item)
            else:
                item['reject_reason'] = f"专业术语覆盖不足（{total_score:.1%}）"
                low_quality.append(item)
        
        # 统计
        print(f"\n📊 筛选结果:")
        print(f"  输入: {len(data)} 条")
        print(f"  通过: {len(filtered)} 条（术语覆盖≥30%）")
        print(f"  拒绝: {len(low_quality)} 条")
        
        print(f"\n术语覆盖度分布:")
        for item in filtered[:3]:
            print(f"  样本术语得分: {item['terminology_score']:.1%}")
            for cat, score in item['terminology_details'].items():
                print(f"    - {cat}: {score:.1%}")
        
        self.filtering_history.append({
            'round': 2,
            'name': '专业术语检查',
            'input_count': len(data),
            'output_count': len(filtered),
            'rejected_count': len(low_quality)
        })
        
        return filtered
    
    def round3_model_scoring(self, data: List[Dict]) -> List[Dict]:
        """
        第三轮：使用AI模型对数据质量打分
        模拟使用GPT-4或其他模型评估数据质量
        """
        print("\n" + "="*80)
        print("📋 第三轮筛选：AI模型质量打分")
        print("="*80)
        print("使用预训练模型评估数据的：")
        print("  1. 逻辑连贯性")
        print("  2. 专业准确性")
        print("  3. 实用价值")
        print("  4. 表达质量")
        
        filtered = []
        
        for item in data:
            # 模拟模型打分（实际应该调用API）
            scores = self._simulate_model_scoring(item)
            item['model_scores'] = scores
            item['final_score'] = sum(scores.values()) / len(scores)
            
            # 阈值：平均分≥7.0
            if item['final_score'] >= 7.0:
                filtered.append(item)
        
        # 按分数排序
        filtered.sort(key=lambda x: x['final_score'], reverse=True)
        
        print(f"\n📊 筛选结果:")
        print(f"  输入: {len(data)} 条")
        print(f"  高分(≥7.0): {len(filtered)} 条")
        
        print(f"\nTop 3 高分样本:")
        for i, item in enumerate(filtered[:3], 1):
            print(f"  {i}. 综合得分: {item['final_score']:.2f}")
            for metric, score in item['model_scores'].items():
                print(f"     - {metric}: {score:.1f}/10")
        
        self.filtering_history.append({
            'round': 3,
            'name': 'AI模型打分',
            'input_count': len(data),
            'output_count': len(filtered),
            'threshold': '≥7.0分'
        })
        
        return filtered
    
    def _simulate_model_scoring(self, item: Dict) -> Dict[str, float]:
        """
        模拟AI模型打分
        实际应该调用GPT-4 API进行评估
        """
        text = item['output']
        
        # 模拟评分逻辑
        scores = {}
        
        # 1. 逻辑连贯性（检查结构）
        structure_keywords = ['症状', '分析', '辨证', '治则', '方药', '建议']
        structure_score = sum(1 for kw in structure_keywords if kw in text)
        scores['逻辑连贯性'] = min(10, structure_score * 1.5)
        
        # 2. 专业准确性（检查专业术语密度）
        words = list(jieba.cut(text))
        tcm_terms = ['阴虚', '阳虚', '气虚', '血虚', '脾', '肾', '肝', '心', '证型', '治则']
        term_density = sum(1 for w in words if w in tcm_terms) / len(words) * 100
        scores['专业准确性'] = min(10, term_density * 5)
        
        # 3. 实用价值（长度和详细程度）
        detail_score = min(10, len(text) / 200)
        scores['实用价值'] = detail_score
        
        # 4. 表达质量（模拟）
        scores['表达质量'] = 7.5 + (len(text) % 10) * 0.2
        
        return scores
    
    def discover_problems(self, data: List[Dict]):
        """
        问题发现阶段
        即使是高分数据，也可能有隐藏问题
        """
        print("\n人工抽查高分数据后，发现以下问题：\n")
        
        problems_found = [
            {
                'problem': '方剂剂量不准确',
                'example': '发现"附子6g"这种剂量，但附子是有毒性的，剂量应该更谨慎',
                'impact': '可能导致模型生成不安全的医疗建议',
                'solution': '添加剂量合理性检查规则'
            },
            {
                'problem': '缺少禁忌症说明',
                'example': '大部分数据只说如何治疗，没有说明什么情况不能用某些方药',
                'impact': '模型可能给出不完整的医疗建议',
                'solution': '筛选时要求必须包含"注意事项"或"禁忌"'
            },
            {
                'problem': '过度依赖辨证',
                'example': '所有回复都是中医辨证，缺少"建议就医"的提醒',
                'impact': '模型可能不会建议用户去医院',
                'solution': '添加必须包含就医建议的规则'
            },
            {
                'problem': '数据同质化严重',
                'example': '90%的数据都是"XX虚"证型，缺少其他类型',
                'impact': '模型对某些证型过拟合',
                'solution': '按证型分层采样，确保多样性'
            }
        ]
        
        for i, prob in enumerate(problems_found, 1):
            print(f"问题 {i}: {prob['problem']}")
            print(f"  🔍 案例: {prob['example']}")
            print(f"  ⚠️  影响: {prob['impact']}")
            print(f"  ✅ 解决: {prob['solution']}")
            print()
        
        print("💡 关键教训：")
        print("   AI模型打分不能完全替代人工审核！")
        print("   高分≠高质量，必须结合领域专家的判断")
        print("   需要回到第一步，用新规则重新筛选所有数据")
    
    def round4_backtrack_and_fix(self, data: List[Dict]) -> List[Dict]:
        """
        第四轮：回溯修正
        基于发现的问题，添加新的筛选规则，重新筛选原始数据
        """
        print("\n重新应用所有规则（包括新规则）到原始数据...")
        
        filtered = []
        
        for item in data:
            reasons = []
            
            # 原有规则
            if len(item['input']) < 20:
                reasons.append("输入过短")
            if len(item['output']) < 100:
                reasons.append("输出过短")
            
            output = item['output']
            
            # 新规则1：必须包含就医建议
            medical_advice_keywords = ['就诊', '医院', '医生', '面诊', '就医', '咨询专业']
            if not any(kw in output for kw in medical_advice_keywords):
                reasons.append("缺少就医建议")
            
            # 新规则2：必须包含注意事项
            warning_keywords = ['注意', '禁忌', '不宜', '避免', '慎用']
            if not any(kw in output for kw in warning_keywords):
                reasons.append("缺少注意事项")
            
            # 新规则3：检查是否有剂量信息（如果有方药）
            if '方药' in output or '处方' in output:
                # 简单检查是否有剂量单位
                if not re.search(r'\d+g|\d+克', output):
                    reasons.append("方药缺少剂量信息")
            
            # 新规则4：避免过度自信的表述
            overconfident_phrases = ['一定', '必定', '绝对', '保证治愈']
            if any(phrase in output for phrase in overconfident_phrases):
                reasons.append("表述过于绝对")
            
            if not reasons:
                filtered.append(item)
            else:
                item['reject_reasons_round4'] = reasons
        
        print(f"\n📊 回溯筛选结果:")
        print(f"  原始数据: {len(data)} 条")
        print(f"  通过新规则: {len(filtered)} 条")
        print(f"  拒绝: {len(data) - len(filtered)} 条")
        
        self.filtering_history.append({
            'round': 4,
            'name': '回溯修正（新规则）',
            'input_count': len(data),
            'output_count': len(filtered),
            'new_rules': ['就医建议', '注意事项', '剂量检查', '避免绝对化']
        })
        
        return filtered
    
    def round5_manual_review(self, data: List[Dict]) -> List[Dict]:
        """
        第五轮：人工复核
        最终由领域专家人工审核
        """
        print("\n" + "="*80)
        print("📋 第五轮：人工复核（模拟）")
        print("="*80)
        
        print("\n将数据分配给3位中医专家进行人工审核...")
        print("审核标准:")
        print("  1. 辨证是否准确")
        print("  2. 方药是否合理")
        print("  3. 建议是否安全")
        print("  4. 表述是否专业")
        
        # 模拟人工审核（实际需要真人专家）
        approved = []
        for item in data:
            # 模拟：90%通过
            import random
            if random.random() < 0.9:
                item['manual_review'] = 'approved'
                item['reviewer'] = f'专家{random.randint(1, 3)}'
                approved.append(item)
            else:
                item['manual_review'] = 'rejected'
                item['review_comment'] = '辨证逻辑存在问题'
        
        print(f"\n📊 人工审核结果:")
        print(f"  送审: {len(data)} 条")
        print(f"  通过: {len(approved)} 条")
        print(f"  拒绝: {len(data) - len(approved)} 条")
        
        self.filtering_history.append({
            'round': 5,
            'name': '人工复核',
            'input_count': len(data),
            'output_count': len(approved)
        })
        
        return approved
    
    def save_final_data(self, data: List[Dict]):
        """保存最终筛选后的数据"""
        output_path = 'tcm_filtered_final.json'
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"\n✅ 最终数据已保存: {output_path}")
    
    def generate_filtering_report(self):
        """生成筛选报告"""
        print("\n" + "="*80)
        print("📊 数据筛选完整报告")
        print("="*80)
        
        print(f"\n筛选流程:")
        for record in self.filtering_history:
            print(f"\n{record['round']}. {record['name']}")
            print(f"   输入: {record['input_count']} 条")
            print(f"   输出: {record['output_count']} 条")
            if 'rejected_count' in record:
                print(f"   拒绝: {record['rejected_count']} 条")
            if 'new_rules' in record:
                print(f"   新规则: {', '.join(record['new_rules'])}")
        
        # 计算漏斗转化率
        initial = self.filtering_history[0]['input_count']
        final = self.filtering_history[-1]['output_count']
        conversion_rate = final / initial * 100
        
        print(f"\n📈 整体统计:")
        print(f"   初始数据: {initial} 条")
        print(f"   最终数据: {final} 条")
        print(f"   转化率: {conversion_rate:.1f}%")
        print(f"   总轮次: {len(self.filtering_history)} 轮")
        
        print(f"\n💡 关键经验:")
        print(f"   1. 第一次筛选通常不够，需要多轮迭代")
        print(f"   2. AI打分不能完全替代人工审核")
        print(f"   3. 发现问题后要勇于回溯，不要将就")
        print(f"   4. 宁缺毋滥，质量比数量重要")


def main():
    """主函数"""
    # 假设已经有原始数据
    # 这里用之前生成的数据作为示例
    pipeline = TCMDataFilteringPipeline('tcm_raw_data.json')
    
    print("="*80)
    print("🎯 真实的SFT数据筛选流程演示")
    print("="*80)
    print("\n这是一个真实的数据筛选过程：")
    print("  - 多轮迭代")
    print("  - 发现问题")
    print("  - 回溯修正")
    print("  - 人工复核")
    print("\n和理想化的教程不同，真实项目中会遇到各种问题！")
    print("\n" + "="*80)
    input("\n按Enter键开始...")
    
    # 运行完整流程
    final_data = pipeline.run_full_pipeline()
    
    print("\n" + "="*80)
    print("✅ 筛选流程完成！")
    print("="*80)


if __name__ == "__main__":
    main()

