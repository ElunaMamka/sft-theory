"""
场景1：数据筛选的多轮迭代 - 详细示例
==============================================

这是一个真实的数据筛选案例，展示了：
- 第一遍筛选看似成功，实则有隐藏问题
- 发现问题后的回溯修正过程
- 如何设计更完善的筛选规则

运行时间：约5分钟
输出：详细的筛选过程和数据质量报告
"""

import json
import re
from typing import List, Dict, Tuple
from collections import Counter
import time


class RealWorldDataFilteringCase:
    """
    真实案例：中医数据筛选的多轮迭代
    """
    
    def __init__(self):
        self.round_results = []
        
    def run(self):
        """运行完整的场景演示"""
        print("="*100)
        print(" "*30 + "场景1：数据筛选的多轮迭代")
        print("="*100)
        
        self.show_introduction()
        input("\n>>> 按Enter键开始第一轮筛选...")
        
        # 第一轮：初步筛选
        data_round1 = self.round1_initial_filtering()
        
        input("\n>>> 按Enter键进行AI打分...")
        
        # 第二轮：AI打分
        data_round2 = self.round2_ai_scoring(data_round1)
        
        input("\n>>> 按Enter键人工抽查...")
        
        # 发现问题！
        self.discover_hidden_problems(data_round2)
        
        input("\n>>> 按Enter键开始回溯修正...")
        
        # 第三轮：回溯修正
        data_round3 = self.round3_backtrack_fix()
        
        # 最终对比
        self.show_final_comparison()
        
    def show_introduction(self):
        """展示场景介绍"""
        print("\n📖 场景背景：")
        print("-" * 100)
        print("""
你负责一个中医问诊AI项目。你从网上爬取了500条中医问诊数据，现在需要筛选出高质量数据。

你的筛选策略：
  第一步：基础规则筛选（长度、格式、禁用词等）
  第二步：使用GPT-4对数据质量打分，选择高分数据
  
看起来很完美，对吧？
        """)
        print("-" * 100)
        
    def round1_initial_filtering(self) -> List[Dict]:
        """第一轮：初步规则筛选"""
        print("\n" + "="*100)
        print("第一轮：基础规则筛选")
        print("="*100)
        
        # 模拟原始数据
        raw_data = self._generate_raw_data(100)
        
        print(f"\n📊 原始数据：{len(raw_data)} 条")
        print("\n应用筛选规则：")
        
        rules = [
            "1. 长度检查：输入≥20字，输出≥100字",
            "2. 格式检查：包含必要字段（症状、辨证、方药）",
            "3. 禁用词检查：不包含脏话、敏感词",
            "4. 重复检查：去除完全重复的数据"
        ]
        
        for rule in rules:
            print(f"  ✓ {rule}")
            time.sleep(0.3)
        
        # 应用规则
        filtered_data = []
        rejected_data = []
        
        for item in raw_data:
            reasons = []
            
            # 规则1：长度
            if len(item['input']) < 20:
                reasons.append("输入过短")
            if len(item['output']) < 100:
                reasons.append("输出过短")
            
            # 规则2：格式
            required_keywords = ['症状', '辨证', '方药']
            if not all(kw in item['output'] for kw in required_keywords):
                reasons.append("缺少必要字段")
            
            # 规则3：禁用词
            forbidden = ['fuck', '傻逼', '白痴']
            if any(word in item['input'] + item['output'] for word in forbidden):
                reasons.append("包含禁用词")
            
            if reasons:
                item['reject_reasons'] = reasons
                rejected_data.append(item)
            else:
                filtered_data.append(item)
        
        print(f"\n📊 筛选结果：")
        print(f"  ✅ 通过：{len(filtered_data)} 条")
        print(f"  ❌ 拒绝：{len(rejected_data)} 条")
        
        if rejected_data:
            print(f"\n拒绝原因统计：")
            all_reasons = [r for item in rejected_data for r in item['reject_reasons']]
            for reason, count in Counter(all_reasons).most_common():
                print(f"  - {reason}: {count} 条")
        
        # 展示通过的样本
        print(f"\n✅ 通过筛选的样本示例：")
        for i, item in enumerate(filtered_data[:2], 1):
            print(f"\n【样本 {i}】")
            print(f"  输入：{item['input'][:50]}...")
            print(f"  输出：{item['output'][:100]}...")
            print(f"  长度：输入{len(item['input'])}字，输出{len(item['output'])}字")
        
        print("\n" + "="*100)
        print(f"✅ 第一轮筛选完成！得到 {len(filtered_data)} 条数据")
        print("="*100)
        
        self.round_results.append({
            'round': 1,
            'name': '基础规则筛选',
            'input': len(raw_data),
            'output': len(filtered_data),
            'rejected': len(rejected_data)
        })
        
        return filtered_data
    
    def round2_ai_scoring(self, data: List[Dict]) -> List[Dict]:
        """第二轮：AI模型打分"""
        print("\n" + "="*100)
        print("第二轮：使用GPT-4进行质量打分")
        print("="*100)
        
        print(f"\n💰 成本估算：")
        print(f"  - 数据量：{len(data)} 条")
        print(f"  - 每条约1000 tokens × $0.01/1K = ${len(data) * 0.01:.2f}")
        print(f"  - 预计耗时：{len(data) * 2} 秒")
        
        print(f"\n开始打分...")
        time.sleep(0.5)
        
        # 模拟AI打分
        scored_data = []
        for i, item in enumerate(data, 1):
            score = self._simulate_ai_scoring(item)
            item['ai_score'] = score
            scored_data.append(item)
            
            if i % 10 == 0:
                print(f"  进度：{i}/{len(data)} 条")
                time.sleep(0.2)
        
        # 按分数排序
        scored_data.sort(key=lambda x: x['ai_score'], reverse=True)
        
        print(f"\n📊 打分结果分布：")
        score_ranges = {
            '9-10分（优秀）': 0,
            '7-9分（良好）': 0,
            '5-7分（一般）': 0,
            '5分以下（差）': 0
        }
        
        for item in scored_data:
            score = item['ai_score']
            if score >= 9:
                score_ranges['9-10分（优秀）'] += 1
            elif score >= 7:
                score_ranges['7-9分（良好）'] += 1
            elif score >= 5:
                score_ranges['5-7分（一般）'] += 1
            else:
                score_ranges['5分以下（差）'] += 1
        
        for range_name, count in score_ranges.items():
            percentage = count / len(scored_data) * 100
            bar = '█' * int(percentage / 2)
            print(f"  {range_name}: {count:2d} 条 ({percentage:5.1f}%) {bar}")
        
        # 选择高分数据
        threshold = 7.5
        high_score_data = [item for item in scored_data if item['ai_score'] >= threshold]
        
        print(f"\n✅ 选择阈值：≥{threshold}分")
        print(f"✅ 最终数据：{len(high_score_data)} 条")
        
        # 展示Top 3高分样本
        print(f"\n🏆 Top 3 高分样本：")
        for i, item in enumerate(scored_data[:3], 1):
            print(f"\n【第{i}名】得分：{item['ai_score']:.1f}/10")
            print(f"  输入：{item['input'][:60]}...")
            print(f"  输出：{item['output'][:80]}...")
        
        print("\n" + "="*100)
        print(f"✅ 第二轮筛选完成！得到 {len(high_score_data)} 条高分数据")
        print("看起来很完美，可以开始训练了！")
        print("="*100)
        
        self.round_results.append({
            'round': 2,
            'name': 'AI质量打分',
            'input': len(data),
            'output': len(high_score_data),
            'threshold': f'≥{threshold}分'
        })
        
        return high_score_data
    
    def discover_hidden_problems(self, data: List[Dict]):
        """发现隐藏的问题！"""
        print("\n" + "!"*100)
        print(" "*35 + "🚨 问题发现阶段 🚨")
        print("!"*100)
        
        print("""
作为项目负责人，你决定在训练前人工抽查一下这些高分数据...

你随机抽取了10条数据仔细阅读...
        """)
        
        time.sleep(1)
        
        print("\n结果发现了严重问题！\n")
        
        # 问题1：方剂剂量不合理
        print("="*100)
        print("❌ 问题1：方剂剂量不合理")
        print("="*100)
        
        problem_case_1 = {
            'input': '我手脚冰凉，腰膝酸软，畏寒怕冷',
            'output': '''
【症状归纳】
主症：手脚冰凉、腰膝酸软、畏寒

【辨证分析】
您的症状属于肾阳虚证型...

【方药建议】
可以使用金匮肾气丸加减：
- 附子 30g
- 肉桂 20g  
- 熟地 15g
- 山药 12g
...
            ''',
            'ai_score': 9.2,
            'problems': [
                '附子30g剂量过大（常用量3-15g，有毒性！）',
                '肉桂20g也偏大（常用量3-10g）'
            ]
        }
        
        print(f"\n📄 高分样本（AI评分：{problem_case_1['ai_score']}/10）")
        print(f"\n输入：{problem_case_1['input']}")
        print(f"\n输出：{problem_case_1['output']}")
        
        print(f"\n❌ 发现问题：")
        for i, prob in enumerate(problem_case_1['problems'], 1):
            print(f"  {i}. {prob}")
        
        print(f"\n⚠️  影响：")
        print(f"  如果模型学到了这种错误的剂量，可能给出不安全的医疗建议！")
        print(f"  附子过量可能导致中毒，这是严重的安全隐患。")
        
        # 问题2：缺少禁忌说明
        print("\n" + "="*100)
        print("❌ 问题2：缺少禁忌和注意事项")
        print("="*100)
        
        problem_case_2 = {
            'input': '我最近血压高，头晕头痛',
            'output': '''
【症状归纳】
主症：血压高、头晕头痛

【辨证分析】
属于肝阳上亢证...

【方药建议】
可以使用天麻钩藤饮：
- 天麻 10g
- 钩藤 15g
- 石决明 30g
...

【生活调理】
注意休息，保持心情舒畅
            ''',
            'ai_score': 8.8,
            'problems': [
                '完全没有提到就医建议',
                '没有说明什么情况下不能用这个方子',
                '高血压是严重疾病，不应该只给方药不提就医'
            ]
        }
        
        print(f"\n📄 高分样本（AI评分：{problem_case_2['ai_score']}/10）")
        print(f"\n输入：{problem_case_2['input']}")
        print(f"\n输出：{problem_case_2['output']}")
        
        print(f"\n❌ 发现问题：")
        for i, prob in enumerate(problem_case_2['problems'], 1):
            print(f"  {i}. {prob}")
        
        print(f"\n⚠️  影响：")
        print(f"  高血压患者应该及时就医，模型不应该只给方药建议。")
        print(f"  缺少禁忌说明可能导致不适用人群误用。")
        
        # 问题3：辨证逻辑不严密
        print("\n" + "="*100)
        print("❌ 问题3：辨证逻辑不严密")
        print("="*100)
        
        problem_case_3 = {
            'input': '我口干口苦，大便干结',
            'output': '''
【症状归纳】
主症：口干口苦、大便干结

【辨证分析】
根据症状，这是肝火旺盛...（直接下结论，没有分析过程）

【方药建议】
龙胆泻肝丸...
            ''',
            'ai_score': 7.6,
            'problems': [
                '没有询问舌象、脉象等关键信息',
                '直接下结论，缺少推理过程',
                '没有考虑其他可能的证型（如胃热、阴虚）'
            ]
        }
        
        print(f"\n📄 高分样本（AI评分：{problem_case_3['ai_score']}/10）")
        print(f"\n输入：{problem_case_3['input']}")
        print(f"\n输出：{problem_case_3['output']}")
        
        print(f"\n❌ 发现问题：")
        for i, prob in enumerate(problem_case_3['problems'], 1):
            print(f"  {i}. {prob}")
        
        print(f"\n⚠️  影响：")
        print(f"  模型学会了"跳跃式诊断"，缺少严密的辨证逻辑。")
        print(f"  可能误诊，因为症状相似但证型不同的情况很多。")
        
        # 总结发现的问题
        print("\n" + "="*100)
        print("📊 人工抽查统计")
        print("="*100)
        
        inspection_result = {
            '抽查数量': 10,
            '有剂量问题': 4,
            '缺少禁忌说明': 7,
            '辨证逻辑不严': 3,
            '完全合格': 2
        }
        
        print(f"\n抽查结果：")
        for key, value in inspection_result.items():
            if key == '完全合格':
                print(f"  ✅ {key}: {value} 条 ({value/10*100:.0f}%)")
            else:
                print(f"  ❌ {key}: {value} 条 ({value/10*100:.0f}%)")
        
        print(f"\n💡 关键发现：")
        print(f"  1. AI打高分不等于真正的高质量！")
        print(f"  2. GPT-4可能不了解中医专业标准（如安全剂量范围）")
        print(f"  3. AI倾向于给"详细的、完整的"内容打高分，但忽视了专业性")
        
        print(f"\n🤔 现在怎么办？")
        print(f"  ❌ 选项A：算了，80%合格率也还行，继续用这些数据训练")
        print(f"  ✅ 选项B：回到第一步，添加新规则，重新筛选所有数据")
        
        print(f"\n正确选择：选项B！")
        print(f"原因：数据质量直接决定模型质量，宁可多花时间，也不能将就。")
        
    def round3_backtrack_fix(self) -> List[Dict]:
        """第三轮：回溯修正"""
        print("\n" + "="*100)
        print("第三轮：回溯修正 - 添加新规则重新筛选")
        print("="*100)
        
        print(f"\n基于发现的问题，设计新的筛选规则：")
        
        new_rules = [
            {
                'name': '规则4：剂量安全检查',
                'detail': '检查常用中药的剂量是否在安全范围内',
                'example': '附子：3-15g，超出则拒绝'
            },
            {
                'name': '规则5：必须包含就医建议',
                'detail': '输出中必须包含"就医"、"医院"、"面诊"等关键词',
                'example': '匹配关键词：["就医", "就诊", "医院", "医生", "面诊"]'
            },
            {
                'name': '规则6：必须包含注意事项或禁忌',
                'detail': '输出中必须包含"注意"、"禁忌"、"不宜"等警示',
                'example': '匹配关键词：["注意", "禁忌", "不宜", "避免", "慎用"]'
            },
            {
                'name': '规则7：辨证过程检查',
                'detail': '输出应包含分析过程，不能只有结论',
                'example': '检查是否有"因为"、"所以"、"根据"等逻辑词'
            }
        ]
        
        for i, rule in enumerate(new_rules, 1):
            print(f"\n{rule['name']}")
            print(f"  详情：{rule['detail']}")
            print(f"  示例：{rule['example']}")
            time.sleep(0.3)
        
        print(f"\n开始重新筛选原始数据...")
        time.sleep(0.5)
        
        # 模拟重新筛选
        raw_data = self._generate_raw_data(100)
        
        # 应用所有规则（包括新规则）
        final_data = []
        rejected_data = []
        
        for item in raw_data:
            reasons = []
            
            # 旧规则...（省略）
            
            # 新规则4：剂量检查
            if self._check_dosage_safety(item['output']) is False:
                reasons.append("药物剂量不安全")
            
            # 新规则5：就医建议
            medical_keywords = ['就医', '就诊', '医院', '医生', '面诊']
            if not any(kw in item['output'] for kw in medical_keywords):
                reasons.append("缺少就医建议")
            
            # 新规则6：注意事项
            warning_keywords = ['注意', '禁忌', '不宜', '避免', '慎用']
            if not any(kw in item['output'] for kw in warning_keywords):
                reasons.append("缺少注意事项")
            
            # 新规则7：辨证逻辑
            logic_keywords = ['因为', '所以', '根据', '由于', '表明']
            if sum(kw in item['output'] for kw in logic_keywords) < 2:
                reasons.append("辨证逻辑不严密")
            
            if reasons:
                item['reject_reasons'] = reasons
                rejected_data.append(item)
            else:
                final_data.append(item)
        
        print(f"\n📊 重新筛选结果：")
        print(f"  原始数据：100 条")
        print(f"  ✅ 通过：{len(final_data)} 条")
        print(f"  ❌ 拒绝：{len(rejected_data)} 条")
        
        print(f"\n新增拒绝原因统计：")
        all_reasons = [r for item in rejected_data for r in item['reject_reasons']]
        for reason, count in Counter(all_reasons).most_common():
            print(f"  - {reason}: {count} 条")
        
        print(f"\n✅ 通过所有规则的样本示例：")
        if final_data:
            item = final_data[0]
            print(f"\n【完美样本】")
            print(f"  输入：{item['input']}")
            print(f"  输出：{item['output'][:200]}...")
            print(f"\n通过的规则：")
            print(f"  ✓ 长度合格")
            print(f"  ✓ 格式完整")
            print(f"  ✓ 剂量安全")
            print(f"  ✓ 包含就医建议")
            print(f"  ✓ 包含注意事项")
            print(f"  ✓ 辨证逻辑严密")
        
        print("\n" + "="*100)
        print(f"✅ 第三轮筛选完成！得到 {len(final_data)} 条真正高质量的数据")
        print("="*100)
        
        self.round_results.append({
            'round': 3,
            'name': '回溯修正（新规则）',
            'input': 100,
            'output': len(final_data),
            'new_rules': 4
        })
        
        return final_data
    
    def show_final_comparison(self):
        """展示最终对比"""
        print("\n" + "="*100)
        print(" "*35 + "📊 最终对比")
        print("="*100)
        
        print(f"\n筛选流程对比：")
        print(f"\n方案A（原计划）：")
        print(f"  规则筛选 → AI打分 → 完成")
        print(f"  最终数据：45条")
        print(f"  问题：40%有安全隐患或专业问题")
        
        print(f"\n方案B（回溯修正）：")
        print(f"  规则筛选 → AI打分 → 发现问题 → 回溯修正 → 完成")
        print(f"  最终数据：28条")
        print(f"  质量：95%以上符合专业标准")
        
        print(f"\n📊 关键指标对比：")
        print(f"")
        print(f"{'指标':<20} {'方案A':<15} {'方案B':<15} {'优势':<10}")
        print(f"{'-'*60}")
        print(f"{'数据量':<20} {'45条':<15} {'28条':<15} {'方案A':<10}")
        print(f"{'安全性':<20} {'60%':<15} {'95%':<15} {'方案B ✅':<10}")
        print(f"{'专业性':<20} {'中等':<15} {'高':<15} {'方案B ✅':<10}")
        print(f"{'训练后准确率':<20} {'70% (预估)':<15} {'90% (预估)':<15} {'方案B ✅':<10}")
        print(f"{'额外时间成本':<20} {'0天':<15} {'1天':<15} {'方案A':<10}")
        
        print(f"\n💡 核心教训：")
        print(f"  1. ✅ 数据质量 > 数据数量")
        print(f"     28条高质量数据 > 45条有隐患数据")
        
        print(f"\n  2. ✅ AI打分不是万能的")
        print(f"     GPT-4不了解中医专业标准")
        print(f"     需要结合领域专家知识设计规则")
        
        print(f"\n  3. ✅ 人工抽查必不可少")
        print(f"     随机抽查10条就发现了系统性问题")
        print(f"     建议抽查比例：10-20%")
        
        print(f"\n  4. ✅ 勇于回溯，不要将就")
        print(f"     发现问题后重新筛选花了1天")
        print(f"     但避免了后续更大的问题")
        print(f"     如果用有问题的数据训练，修复成本会高10倍")
        
        print(f"\n  5. ✅ 制定明确的质量标准")
        print(f"     不只是"详细"、"完整"")
        print(f"     还要"安全"、"专业"、"严密"")
        
        print("\n" + "="*100)
        print(" "*30 + "场景1演示完成")
        print("="*100)
        
        print(f"\n🎯 下一步行动建议：")
        print(f"  1. 继续补充数据至150-200条（每个证型至少15条）")
        print(f"  2. 请中医专家审核最终数据集")
        print(f"  3. 开始训练前，准备全面的测试集")
        print(f"  4. 训练后进行安全性专项测试")
    
    def _generate_raw_data(self, count: int) -> List[Dict]:
        """生成模拟的原始数据"""
        data = []
        templates = [
            {
                'input': '我最近手脚冰凉，腰膝酸软，夜尿频多',
                'output': '''【症状归纳】主症：手脚冰凉、腰膝酸软、夜尿频多
【辨证分析】肾阳虚证型，因为肾阳不足，温煦失职，所以手脚冰凉...
【方药建议】金匮肾气丸加减：附子6g、肉桂6g、熟地15g...
【注意事项】孕妇慎用。建议到医院中医科就诊。'''
            },
            {
                'input': '我口干口苦，大便干结，舌红苔黄',
                'output': '''【症状归纳】口干口苦、大便干结、舌红苔黄
【辨证分析】肝胆湿热证，由于湿热内蕴，表现为口苦...
【方药建议】龙胆泻肝丸：龙胆草9g、栀子9g、黄芩9g...
【生活调理】忌辛辣刺激。建议就医。'''
            }
        ]
        
        for i in range(count):
            template = templates[i % len(templates)]
            data.append({
                'id': f'data_{i+1}',
                'input': template['input'],
                'output': template['output'],
                'source': 'web_crawl'
            })
        
        return data
    
    def _simulate_ai_scoring(self, item: Dict) -> float:
        """模拟AI打分"""
        # 简单的启发式评分
        score = 7.0
        
        # 长度加分
        if len(item['output']) > 200:
            score += 1.0
        
        # 包含专业术语加分
        terms = ['辨证', '证型', '方药', '治则']
        score += sum(0.3 for term in terms if term in item['output'])
        
        # 随机波动
        import random
        score += random.uniform(-0.5, 0.5)
        
        return min(10.0, max(0.0, score))
    
    def _check_dosage_safety(self, text: str) -> bool:
        """检查药物剂量安全性"""
        # 定义常用药物的安全剂量范围（单位：g）
        safe_dosages = {
            '附子': (3, 15),
            '细辛': (1, 3),
            '麻黄': (3, 9),
            '肉桂': (3, 10),
            '人参': (3, 9)
        }
        
        for herb, (min_dose, max_dose) in safe_dosages.items():
            if herb in text:
                # 简单的剂量提取
                import re
                pattern = f'{herb}[：:]\s*(\d+)g'
                match = re.search(pattern, text)
                if match:
                    dose = int(match.group(1))
                    if dose < min_dose or dose > max_dose:
                        return False
        
        return True


def main():
    """主函数"""
    case = RealWorldDataFilteringCase()
    case.run()
    
    print(f"\n\n💾 如需查看代码实现细节，请查看本文件：")
    print(f"   sft-theory/code/part4/4.1_vertical_domain_tcm/scenarios/scenario1_data_filtering_iteration.py")


if __name__ == "__main__":
    main()

