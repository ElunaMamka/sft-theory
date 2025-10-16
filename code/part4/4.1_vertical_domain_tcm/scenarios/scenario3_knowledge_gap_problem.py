"""
场景3：专业知识缺失问题 - 数据分布不均导致的偏见
=========================================================

真实案例：不管什么症状都诊断为"脾肾阳虚"

展示内容：
- 问题发现：模型对某些证型过拟合
- 数据诊断：发现90%数据是同一证型
- 根本原因：数据分布严重不均衡
- 解决方案：数据平衡采样 + 对比样本
- 效果验证：准确率从40%提升到85%

运行时间：约6分钟
"""

import time
from collections import Counter
from typing import List, Dict
import random


class KnowledgeGapCase:
    """专业知识缺失案例"""
    
    def __init__(self):
        self.test_results = []
        
    def run(self):
        """运行完整演示"""
        print("="*100)
        print(" "*20 + "场景3：专业知识缺失 - 数据分布导致的模型偏见")
        print("="*100)
        
        self.show_introduction()
        input("\n>>> 按Enter键开始测试...")
        
        # 阶段1：问题发现
        self.stage1_problem_discovery()
        input("\n>>> 按Enter键进行数据诊断...")
        
        # 阶段2：数据诊断
        self.stage2_data_diagnosis()
        input("\n>>> 按Enter键查看解决方案...")
        
        # 阶段3：解决方案
        self.stage3_solutions()
        input("\n>>> 按Enter键验证效果...")
        
        # 阶段4：修复验证
        self.stage4_verification()
        
        # 阶段5：经验总结
        self.stage5_lessons()
        
    def show_introduction(self):
        """场景介绍"""
        print("\n📖 场景背景：")
        print("-" * 100)
        print("""
你的中医问诊模型训练完成了！

训练数据：150条高质量数据
训练Loss：1.05（正常范围）
格式一致性：100%
没有复读问题：✓

看起来一切都很好，开始测试吧！
        """)
        print("-" * 100)
    
    def stage1_problem_discovery(self):
        """阶段1：问题发现"""
        print("\n" + "="*100)
        print("阶段1：全面测试 - 发现严重问题")
        print("="*100)
        
        # 准备测试用例（覆盖不同证型）
        test_cases = [
            {
                'id': 1,
                'syndrome': '脾肾阳虚',
                'input': '我最近手脚冰凉，腰膝酸软，吃饭没胃口',
                'expected': '脾肾阳虚',
                'actual': '脾肾阳虚',
                'correct': True
            },
            {
                'id': 2,
                'syndrome': '脾肾阳虚',
                'input': '我总是怕冷，夜尿频多，舌淡苔白',
                'expected': '脾肾阳虚',
                'actual': '脾肾阳虚',
                'correct': True
            },
            {
                'id': 3,
                'syndrome': '肝郁气滞',
                'input': '我脾气很大，容易发怒，胸胁胀痛',
                'expected': '肝郁气滞',
                'actual': '脾肾阳虚',  # 错误！
                'correct': False
            },
            {
                'id': 4,
                'syndrome': '肝胆湿热',
                'input': '我口干口苦，大便干结，舌红苔黄',
                'expected': '肝胆湿热',
                'actual': '脾肾阳虚',  # 错误！
                'correct': False
            },
            {
                'id': 5,
                'syndrome': '心肾不交',
                'input': '我失眠多梦，心烦，腰酸',
                'expected': '心肾不交',
                'actual': '脾肾阳虚',  # 错误！
                'correct': False
            },
            {
                'id': 6,
                'syndrome': '阴虚火旺',
                'input': '我手脚心发热，盗汗，口干',
                'expected': '阴虚火旺',
                'actual': '脾肾阳虚',  # 错误！
                'correct': False
            }
        ]
        
        print("\n开始测试不同证型...")
        time.sleep(0.5)
        
        for case in test_cases:
            print(f"\n" + "-"*100)
            print(f"【测试 {case['id']}】真实证型：{case['syndrome']}")
            print(f"输入：{case['input']}")
            time.sleep(0.3)
            print(f"模型诊断：{case['actual']}")
            
            if case['correct']:
                print(f"结果：✅ 正确")
            else:
                print(f"期望：{case['expected']}")
                print(f"结果：❌ 错误！诊断为 '{case['actual']}'")
            
            self.test_results.append(case)
        
        # 统计结果
        print("\n" + "="*100)
        print("📊 测试结果统计")
        print("="*100)
        
        correct_count = sum(1 for c in test_cases if c['correct'])
        total_count = len(test_cases)
        accuracy = correct_count / total_count * 100
        
        print(f"\n总测试数：{total_count}")
        print(f"正确数：{correct_count}")
        print(f"错误数：{total_count - correct_count}")
        print(f"准确率：{accuracy:.1f}%")
        
        # 按证型分析
        print(f"\n按证型分析：")
        syndrome_results = {}
        for case in test_cases:
            syndrome = case['syndrome']
            if syndrome not in syndrome_results:
                syndrome_results[syndrome] = {'correct': 0, 'total': 0}
            syndrome_results[syndrome]['total'] += 1
            if case['correct']:
                syndrome_results[syndrome]['correct'] += 1
        
        for syndrome, stats in syndrome_results.items():
            acc = stats['correct'] / stats['total'] * 100
            print(f"  {syndrome:12s}: {stats['correct']}/{stats['total']} = {acc:5.1f}%")
        
        print(f"\n😱 严重问题发现：")
        print(f"  • 脾肾阳虚：100% 准确率（2/2）✅")
        print(f"  • 其他证型：0% 准确率（0/4）❌")
        print(f"  • 模型把所有非脾肾阳虚的症状都诊断为脾肾阳虚！")
        
        print(f"\n💭 你的困惑：")
        print(f"  - 训练数据都是高质量的")
        print(f"  - Loss也正常")
        print(f"  - 没有复读问题")
        print(f"  - 为什么会这样？？？")
    
    def stage2_data_diagnosis(self):
        """阶段2：数据诊断"""
        print("\n" + "="*100)
        print("阶段2：数据诊断 - 寻找根本原因")
        print("="*100)
        
        print(f"\n决定分析训练数据的分布...")
        time.sleep(0.5)
        
        print(f"\n运行数据分析脚本：")
        print(f"python data/analyze_syndrome_distribution.py")
        time.sleep(1)
        
        # 模拟数据分布
        data_distribution = {
            '脾肾阳虚': 135,
            '肝郁气滞': 6,
            '肝胆湿热': 4,
            '心肾不交': 3,
            '阴虚火旺': 2
        }
        
        total = sum(data_distribution.values())
        
        print(f"\n📊 证型分布统计：")
        print(f"\n{'证型':<15} {'数量':<10} {'占比':<10} {'可视化':<30}")
        print("-" * 70)
        
        for syndrome, count in sorted(data_distribution.items(), 
                                      key=lambda x: x[1], reverse=True):
            percentage = count / total * 100
            bar = '█' * int(percentage / 2)
            print(f"{syndrome:<15} {count:<10} {percentage:5.1f}%{' '*4} {bar}")
        
        print(f"\n总计：{total} 条")
        
        # 详细分析
        print(f"\n" + "="*100)
        print("🔍 问题根源分析")
        print("="*100)
        
        max_syndrome = max(data_distribution.items(), key=lambda x: x[1])
        min_syndrome = min(data_distribution.items(), key=lambda x: x[1])
        
        print(f"\n关键发现：")
        print(f"  • 最多：{max_syndrome[0]} = {max_syndrome[1]}条 ({max_syndrome[1]/total*100:.1f}%)")
        print(f"  • 最少：{min_syndrome[0]} = {min_syndrome[1]}条 ({min_syndrome[1]/total*100:.1f}%)")
        print(f"  • 差距：{max_syndrome[1] / min_syndrome[1]:.1f}倍！")
        
        print(f"\n💡 根本原因：")
        print(f"  脾肾阳虚占了90%的数据，模型严重过拟合到这个证型！")
        
        print(f"\n🤔 为什么会这样？")
        
        reasons = [
            {
                'reason': '数据来源单一',
                'detail': '主要从一个专家那里收集数据，这位专家擅长阳虚证型',
                'impact': '导致数据分布反映了专家的专长，而非真实需求'
            },
            {
                'reason': '采集偏见',
                'detail': '脾肾阳虚是常见证型，更容易找到案例',
                'impact': '方便≠正确，导致数据不平衡'
            },
            {
                'reason': '未监控分布',
                'detail': '收集数据时没有统计各证型的占比',
                'impact': '问题在训练前就存在，但未被发现'
            }
        ]
        
        for i, r in enumerate(reasons, 1):
            print(f"\n  {i}. {r['reason']}")
            print(f"     详情：{r['detail']}")
            print(f"     影响：{r['impact']}")
        
        print(f"\n📉 模型是怎么'学坏的'？")
        
        print(f"""
训练过程：
  Epoch 1: 模型看到135次脾肾阳虚，只看到6次肝郁气滞
  Epoch 2: 又看到135次脾肾阳虚...
  Epoch 3: 再看到135次脾肾阳虚...

模型学到的规律：
  "90%的情况答案都是脾肾阳虚"
  "那我就都回答脾肾阳虚吧，准确率90%！"
  
这就像：
  老师出了100道题，90道答案是A
  学生发现：全选A可以得90分
  于是不管什么题都选A
  
这不是学生的问题，是题目分布的问题！
        """)
    
    def stage3_solutions(self):
        """阶段3：解决方案"""
        print("\n" + "="*100)
        print("阶段3：解决方案设计")
        print("="*100)
        
        print(f"\n目标：让每个证型都有足够的数据，且分布均衡")
        
        # 方案1：数据补充
        print(f"\n" + "-"*100)
        print("方案1：补充少数类数据")
        print("-"*100)
        
        print(f"\n策略：为每个证型补充数据到至少50条")
        
        supplement_plan = {
            '脾肾阳虚': {'current': 135, 'target': 50, 'action': '下采样到50条'},
            '肝郁气滞': {'current': 6, 'target': 50, 'action': '补充44条'},
            '肝胆湿热': {'current': 4, 'target': 50, 'action': '补充46条'},
            '心肾不交': {'current': 3, 'target': 50, 'action': '补充47条'},
            '阴虚火旺': {'current': 2, 'target': 50, 'action': '补充48条'}
        }
        
        print(f"\n{'证型':<15} {'当前':<10} {'目标':<10} {'操作':<20}")
        print("-" * 60)
        for syndrome, plan in supplement_plan.items():
            print(f"{syndrome:<15} {plan['current']:<10} {plan['target']:<10} {plan['action']:<20}")
        
        total_new = sum(plan['target'] for plan in supplement_plan.values())
        print(f"\n最终总数：{total_new} 条（每个证型50条）")
        
        print(f"\n如何补充数据？")
        methods = [
            "1. 请中医专家编写（质量最高，成本高）",
            "2. 使用GPT-4生成后人工审核（效率高，需审核）",
            "3. 从其他数据源收集（耗时，需清洗）",
            "4. 数据增强技术（改写、paraphrase）"
        ]
        for method in methods:
            print(f"  {method}")
        
        # 方案2：对比样本
        print(f"\n" + "-"*100)
        print("方案2：构造对比样本")
        print("-"*100)
        
        print(f"\n策略：为易混淆的证型构造对比样本")
        
        print(f"\n示例：手脚冰凉的不同证型")
        
        contrast_examples = [
            {
                'symptoms': '手脚冰凉 + 乏力 + 食欲差 + 舌淡',
                'syndrome': '脾肾阳虚',
                'key': '伴随消化系统症状'
            },
            {
                'symptoms': '手脚冰凉 + 易怒 + 胸闷 + 情绪波动',
                'syndrome': '肝郁气滞（寒凝）',
                'key': '伴随情绪症状'
            },
            {
                'symptoms': '手脚冰凉 + 失眠 + 心悸 + 健忘',
                'syndrome': '心肾不交',
                'key': '伴随心神症状'
            },
            {
                'symptoms': '手脚冰凉 + 面色苍白 + 头晕 + 月经量少',
                'syndrome': '血虚',
                'key': '伴随血虚症状'
            }
        ]
        
        for i, example in enumerate(contrast_examples, 1):
            print(f"\n  对比{i}：{example['syndrome']}")
            print(f"    症状：{example['symptoms']}")
            print(f"    鉴别点：{example['key']}")
        
        print(f"\n💡 对比样本的价值：")
        print(f"  • 教会模型区分相似但不同的情况")
        print(f"  • 强化特征识别能力")
        print(f"  • 提高模型的辨证精度")
        
        # 方案3：平衡采样
        print(f"\n" + "-"*100)
        print("方案3：训练时使用平衡采样")
        print("-"*100)
        
        print(f"\n即使数据量不同，也能让模型均衡学习")
        
        print(f"\n方法：WeightedRandomSampler")
        sampling_code = """
from torch.utils.data import WeightedRandomSampler

# 计算每个样本的权重（inverse frequency）
syndrome_counts = count_syndromes(dataset)
weights = []
for item in dataset:
    syndrome = item['syndrome']
    # 频率低的证型权重高
    weight = 1.0 / syndrome_counts[syndrome]
    weights.append(weight)

# 创建sampler
sampler = WeightedRandomSampler(
    weights=weights,
    num_samples=len(dataset),
    replacement=True
)

# 训练时使用
dataloader = DataLoader(dataset, sampler=sampler, batch_size=4)
        """
        print(sampling_code)
        
        print(f"\n效果：")
        print(f"  • 每个证型在训练中出现的概率相等")
        print(f"  • 不需要实际补充那么多数据")
        print(f"  • 高频类别会被下采样，低频类别会被重复采样")
        
        # 推荐方案
        print(f"\n" + "="*100)
        print("🎯 推荐：综合使用三种方案")
        print("="*100)
        
        print(f"\n阶段1：数据补充（优先）")
        print(f"  • 补充低频证型到至少20条/证型")
        print(f"  • 构造对比样本")
        print(f"  • 时间：3-5天")
        
        print(f"\n阶段2：平衡采样（辅助）")
        print(f"  • 使用WeightedRandomSampler")
        print(f"  • 确保训练时各证型权重相等")
        print(f"  • 时间：改代码30分钟")
        
        print(f"\n阶段3：验证测试（必须）")
        print(f"  • 准备覆盖所有证型的测试集")
        print(f"  • 每个证型至少10个测试样本")
        print(f"  • 时间：1天")
    
    def stage4_verification(self):
        """阶段4：修复验证"""
        print("\n" + "="*100)
        print("阶段4：修复后的测试验证")
        print("="*100)
        
        print(f"\n执行修复方案...")
        print(f"  ✓ 补充了185条数据")
        print(f"  ✓ 构造了30个对比样本")
        print(f"  ✓ 实现了WeightedRandomSampler")
        print(f"  ✓ 重新训练（3 epochs）")
        
        time.sleep(1)
        
        # 新的数据分布
        print(f"\n📊 修复后的数据分布：")
        
        new_distribution = {
            '脾肾阳虚': 50,
            '肝郁气滞': 50,
            '肝胆湿热': 50,
            '心肾不交': 50,
            '阴虚火旺': 50,
            '血虚': 50
        }
        
        total_new = sum(new_distribution.values())
        
        print(f"\n{'证型':<15} {'数量':<10} {'占比':<10}")
        print("-" * 40)
        for syndrome, count in new_distribution.items():
            percentage = count / total_new * 100
            print(f"{syndrome:<15} {count:<10} {percentage:5.1f}%")
        
        print(f"\n总计：{total_new} 条")
        print(f"✅ 完美平衡！")
        
        # 重新测试
        print(f"\n重新测试相同的测试用例...")
        time.sleep(1)
        
        new_test_results = [
            {'id': 1, 'syndrome': '脾肾阳虚', 'expected': '脾肾阳虚', 'actual': '脾肾阳虚', 'correct': True},
            {'id': 2, 'syndrome': '脾肾阳虚', 'expected': '脾肾阳虚', 'actual': '脾肾阳虚', 'correct': True},
            {'id': 3, 'syndrome': '肝郁气滞', 'expected': '肝郁气滞', 'actual': '肝郁气滞', 'correct': True},
            {'id': 4, 'syndrome': '肝胆湿热', 'expected': '肝胆湿热', 'actual': '肝胆湿热', 'correct': True},
            {'id': 5, 'syndrome': '心肾不交', 'expected': '心肾不交', 'actual': '心肾不交', 'correct': True},
            {'id': 6, 'syndrome': '阴虚火旺', 'expected': '阴虚火旺', 'actual': '阴虚火旺', 'correct': True},
        ]
        
        for result in new_test_results:
            print(f"  测试{result['id']}: {result['syndrome']} → {result['actual']} {'✅' if result['correct'] else '❌'}")
        
        correct_new = sum(1 for r in new_test_results if r['correct'])
        accuracy_new = correct_new / len(new_test_results) * 100
        
        print(f"\n修复后准确率：{accuracy_new:.0f}%")
        
        # 对比
        print(f"\n" + "="*100)
        print("📊 修复前后对比")
        print("="*100)
        
        print(f"\n{'指标':<30} {'修复前':<15} {'修复后':<15} {'改善':<15}")
        print("-" * 75)
        print(f"{'整体准确率':<30} {'40%':<15} {'100%':<15} {'+60%':<15}")
        print(f"{'脾肾阳虚准确率':<30} {'100%':<15} {'100%':<15} {'保持':<15}")
        print(f"{'肝郁气滞准确率':<30} {'0%':<15} {'100%':<15} {'+100%':<15}")
        print(f"{'肝胆湿热准确率':<30} {'0%':<15} {'100%':<15} {'+100%':<15}")
        print(f"{'心肾不交准确率':<30} {'0%':<15} {'100%':<15} {'+100%':<15}")
        print(f"{'阴虚火旺准确率':<30} {'0%':<15} {'100%':<15} {'+100%':<15}")
        print(f"{'数据总量':<30} {'150条':<15} {'300条':<15} {'+150条':<15}")
        print(f"{'证型覆盖':<30} {'5种':<15} {'6种':<15} {'+1种':<15}")
        
        print(f"\n✅ 修复成功！")
    
    def stage5_lessons(self):
        """阶段5：经验总结"""
        print("\n" + "="*100)
        print("阶段5：核心经验总结")
        print("="*100)
        
        print(f"\n🎯 关键教训：")
        
        lessons = [
            {
                'title': '1. 数据分布比数据质量还重要',
                'points': [
                    '150条高质量但不平衡的数据 < 300条质量一般但平衡的数据',
                    '模型会忠实反映数据分布',
                    '90%是A的数据 → 模型总回答A'
                ]
            },
            {
                'title': '2. 训练前必须分析数据分布',
                'points': [
                    '不要等训练完才发现问题',
                    '使用简单的统计脚本分析分布',
                    '目标：每个类别至少10-20个样本'
                ]
            },
            {
                'title': '3. 多样性 > 数量',
                'points': [
                    '100个相似样本 < 10个多样化样本',
                    '覆盖不同的case比单纯堆数量重要',
                    '对比样本能显著提升辨别能力'
                ]
            },
            {
                'title': '4. 测试集要覆盖所有类别',
                'points': [
                    '不能只测试高频类别',
                    '低频类别更容易出问题',
                    '准备分层测试集（每个类别单独测）'
                ]
            },
            {
                'title': '5. 平衡采样是有效的trick',
                'points': [
                    '即使数据不平衡，也能改善训练',
                    'WeightedRandomSampler很好用',
                    '但不能完全替代数据补充'
                ]
            }
        ]
        
        for lesson in lessons:
            print(f"\n{lesson['title']}")
            for point in lesson['points']:
                print(f"  • {point}")
        
        print(f"\n" + "="*100)
        print("📋 实用检查清单")
        print("="*100)
        
        checklist = [
            "□ 统计每个类别的样本数量",
            "□ 检查类别分布是否严重不均（>3倍差距需注意）",
            "□ 确保每个类别至少有10-20个样本",
            "□ 为易混淆的类别构造对比样本",
            "□ 使用平衡采样或数据增强",
            "□ 准备分层测试集（每个类别单独测试）",
            "□ 训练后检查每个类别的准确率（不只看平均值）",
            "□ 如发现某些类别准确率低，优先补充该类别数据"
        ]
        
        print(f"\n数据准备阶段：")
        for item in checklist:
            print(f"  {item}")
        
        print("\n" + "="*100)
        print(" "*25 + "场景3演示完成")
        print("="*100)
        
        print(f"\n💡 核心原则：")
        print(f"  模型是数据的镜子")
        print(f"  数据有偏见 → 模型有偏见")
        print(f"  数据不平衡 → 模型不平衡")
        print(f"  想要公平的模型 → 先要公平的数据")


def main():
    """主函数"""
    case = KnowledgeGapCase()
    case.run()
    
    print(f"\n\n💾 相关资源：")
    print(f"  • 数据分布分析：data/analyze_syndrome_distribution.py")
    print(f"  • 平衡采样实现：training/balanced_sampling.py")
    print(f"  • 对比样本生成：data/generate_contrast_samples.py")


if __name__ == "__main__":
    main()

