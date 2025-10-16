"""
4.1 中医问诊助手 - 模型问题诊断与修复
真实的SFT调试场景：发现问题→分析原因→制定方案→重新训练
"""

import json
import re
from typing import List, Dict
from collections import Counter


class ModelProblemDiagnostics:
    """
    模型问题诊断工具
    模拟真实的SFT项目中遇到的问题和解决方案
    """
    
    def __init__(self, model_outputs_path: str = None):
        self.model_outputs_path = model_outputs_path
        self.problems_found = []
        self.solutions = []
        
    def run_full_diagnosis(self):
        """运行完整的问题诊断流程"""
        print("="*80)
        print("🔍 模型问题诊断与修复流程")
        print("="*80)
        print("\n这是一个真实的SFT调试场景")
        print("训练完成后，通过测试发现了多个问题...")
        print("\n" + "="*80)
        
        # 问题1：复读问题
        self.diagnose_repetition_problem()
        
        # 问题2：专业知识缺失
        self.diagnose_knowledge_gap()
        
        # 问题3：格式不一致
        self.diagnose_format_inconsistency()
        
        # 问题4：过度保守
        self.diagnose_over_conservative()
        
        # 问题5：忽视用户输入
        self.diagnose_ignoring_input()
        
        # 生成修复方案
        self.generate_fix_plan()
        
        # 展示重训练策略
        self.show_retraining_strategy()
    
    def diagnose_repetition_problem(self):
        """
        问题1：模型复读（Repetition）
        症状：模型重复生成相同的内容
        """
        print("\n" + "="*80)
        print("❌ 问题1：模型复读问题")
        print("="*80)
        
        # 模拟问题输出
        problem_output = """
根据您的症状，我进行分析：

【症状分析】
您的症状包括乏力、手脚冰凉、食欲不振。
您的症状包括乏力、手脚冰凉、食欲不振。
您的症状包括乏力、手脚冰凉、食欲不振。

【辨证】
这是典型的脾肾阳虚证型。
这是典型的脾肾阳虚证型。
这是典型的脾肾阳虚证型。
"""
        
        print(f"🔍 发现问题：")
        print(problem_output)
        
        print("\n📊 问题分析：")
        print("  1. 检测到重复句子")
        print("  2. 重复率：67%（同一句子重复3次）")
        
        # 分析原因
        print("\n🤔 可能原因：")
        reasons = [
            {
                'cause': '训练数据中存在重复',
                'detail': '数据预处理时没有去重，导致模型学会了重复模式',
                'likelihood': '⭐⭐⭐⭐⭐'
            },
            {
                'cause': '解码参数设置不当',
                'detail': 'repetition_penalty设置过低或未设置',
                'likelihood': '⭐⭐⭐⭐'
            },
            {
                'cause': '训练数据格式问题',
                'detail': '某些样本有意重复强调，模型错误学习',
                'likelihood': '⭐⭐⭐'
            },
            {
                'cause': '过拟合',
                'detail': '在小数据集上训练轮数过多',
                'likelihood': '⭐⭐⭐'
            }
        ]
        
        for i, reason in enumerate(reasons, 1):
            print(f"\n  原因{i}: {reason['cause']}")
            print(f"    详情: {reason['detail']}")
            print(f"    可能性: {reason['likelihood']}")
        
        # 提供解决方案
        print("\n✅ 解决方案：")
        solutions = [
            {
                'step': 1,
                'action': '数据去重',
                'method': '使用MinHash或精确匹配去除训练数据中的重复',
                'code': 'python data/deduplicate_data.py'
            },
            {
                'step': 2,
                'action': '调整解码参数',
                'method': '设置repetition_penalty=1.2, no_repeat_ngram_size=3',
                'code': 'generation_config.repetition_penalty = 1.2'
            },
            {
                'step': 3,
                'action': '检查训练数据',
                'method': '人工检查是否有故意重复的样本，并修正',
                'code': 'python data/check_repetitions.py'
            },
            {
                'step': 4,
                'action': '降低训练轮数',
                'method': '如果是过拟合，减少epoch从5轮到3轮',
                'code': 'num_train_epochs=3'
            },
            {
                'step': 5,
                'action': '重新训练',
                'method': '应用以上修改后重新训练模型',
                'code': 'python training/train_lora.py'
            }
        ]
        
        for sol in solutions:
            print(f"\n  步骤{sol['step']}: {sol['action']}")
            print(f"    方法: {sol['method']}")
            print(f"    命令: {sol['code']}")
        
        self.problems_found.append({
            'problem': '模型复读',
            'severity': 'high',
            'solutions': solutions
        })
    
    def diagnose_knowledge_gap(self):
        """
        问题2：专业知识缺失
        症状：模型对某些专业知识回答不准确
        """
        print("\n" + "="*80)
        print("❌ 问题2：专业知识缺失")
        print("="*80)
        
        # 模拟测试案例
        test_cases = [
            {
                'input': '我脾气很大，容易发怒，胸胁胀痛',
                'expected': '肝郁气滞',
                'actual': '脾虚',
                'correct': False
            },
            {
                'input': '口干口苦，大便干结，舌红苔黄',
                'expected': '肝胆湿热',
                'actual': '阴虚火旺',
                'correct': False
            },
            {
                'input': '手脚冰凉，腰膝酸软，夜尿频多',
                'expected': '肾阳虚',
                'actual': '肾阳虚',
                'correct': True
            }
        ]
        
        print(f"🔍 测试结果：")
        correct_count = sum(1 for tc in test_cases if tc['correct'])
        print(f"  正确率: {correct_count}/{len(test_cases)} = {correct_count/len(test_cases)*100:.0f}%")
        
        print(f"\n❌ 错误案例：")
        for tc in test_cases:
            if not tc['correct']:
                print(f"\n  输入: {tc['input']}")
                print(f"  期望: {tc['expected']}")
                print(f"  实际: {tc['actual']}")
                print(f"  ✗ 错误！")
        
        print("\n🤔 原因分析：")
        print("  1. 训练数据中'肝郁气滞'和'肝胆湿热'的样本太少")
        print("  2. 数据分布不均衡，90%都是虚证，实证和热证不足")
        print("  3. 某些关键特征（如'胸胁胀痛'→肝经症状）未被充分学习")
        
        print("\n✅ 解决方案：")
        solutions = [
            {
                'step': 1,
                'action': '数据增强',
                'detail': '针对缺失的证型（肝郁、湿热等）补充数据',
                'target': '每个证型至少50个样本',
                'method': '可以请中医专家编写，或使用GPT-4生成后人工审核'
            },
            {
                'step': 2,
                'action': '数据平衡',
                'detail': '使用分层采样，确保各证型比例均衡',
                'target': '虚证:实证:寒证:热证 = 4:3:2:3',
                'method': '在DataLoader中使用WeightedRandomSampler'
            },
            {
                'step': 3,
                'action': '添加对比样本',
                'detail': '构造相似症状但不同证型的对比样本',
                'example': '同样是"口干"，阴虚和湿热的其他伴随症状不同',
                'method': '专家设计易混淆案例'
            },
            {
                'step': 4,
                'action': '重新训练',
                'detail': '使用平衡后的数据集重新训练',
                'config': 'sample_weights=[...]'
            }
        ]
        
        for sol in solutions:
            print(f"\n  步骤{sol['step']}: {sol['action']}")
            print(f"    详情: {sol['detail']}")
            for key in ['target', 'example', 'method', 'config']:
                if key in sol:
                    print(f"    {key}: {sol[key]}")
        
        print("\n💡 具体操作：")
        print(f"\n  # 1. 生成补充数据")
        print(f"  python data/generate_balanced_data.py \\")
        print(f"    --target_syndrome '肝郁气滞' \\")
        print(f"    --num_samples 50")
        
        print(f"\n  # 2. 合并数据并重新训练")
        print(f"  python data/merge_and_balance.py")
        print(f"  python training/train_lora.py --balanced_sampling")
        
        self.problems_found.append({
            'problem': '专业知识缺失',
            'severity': 'critical',
            'affected_concepts': ['肝郁气滞', '肝胆湿热'],
            'solutions': solutions
        })
    
    def diagnose_format_inconsistency(self):
        """
        问题3：输出格式不一致
        症状：有时输出结构化，有时很随意
        """
        print("\n" + "="*80)
        print("❌ 问题3：输出格式不一致")
        print("="*80)
        
        # 模拟不同格式的输出
        outputs = [
            {
                'test_id': 1,
                'format': '结构化（好）',
                'content': '【症状】...\n【辨证】...\n【治则】...\n【方药】...'
            },
            {
                'test_id': 2,
                'format': '无结构（差）',
                'content': '你的情况是脾虚，可以吃点补脾的药...'
            },
            {
                'test_id': 3,
                'format': '部分结构（中）',
                'content': '症状分析：...\n建议使用参苓白术散...'
            }
        ]
        
        print(f"🔍 格式一致性检查：")
        for output in outputs:
            print(f"\n  测试{output['test_id']}: {output['format']}")
            print(f"  内容: {output['content'][:50]}...")
        
        print(f"\n格式一致性: 33%（只有1/3符合标准格式）")
        
        print("\n🤔 原因分析：")
        print("  1. 训练数据格式不统一")
        print("  2. 有些数据用【】，有些用##，有些没有标记")
        print("  3. 模型学到了多种格式，推理时随机选择")
        
        print("\n✅ 解决方案：")
        solutions = [
            {
                'action': '统一数据格式',
                'before': '各种格式混杂',
                'after': '全部使用【症状归纳】【辨证分析】【治则治法】【方药建议】【生活调理】',
                'script': 'python data/unify_format.py'
            },
            {
                'action': '使用格式化模板',
                'detail': '在instruction中明确要求输出格式',
                'template': '请按照以下格式回答：\n【症状归纳】\n【辨证分析】\n【治则治法】\n【方药建议】\n【生活调理】'
            },
            {
                'action': '添加格式验证',
                'detail': '训练前检查每个样本是否符合格式',
                'script': 'python data/validate_format.py'
            },
            {
                'action': '重新训练',
                'detail': '使用格式统一的数据重新训练'
            }
        ]
        
        for sol in solutions:
            print(f"\n  • {sol['action']}")
            for key in ['before', 'after', 'detail', 'template', 'script']:
                if key in sol:
                    print(f"    {key}: {sol[key]}")
        
        self.problems_found.append({
            'problem': '格式不一致',
            'severity': 'medium',
            'solutions': solutions
        })
    
    def diagnose_over_conservative(self):
        """
        问题4：模型过度保守
        症状：对任何问题都说"建议就医"，不给具体建议
        """
        print("\n" + "="*80)
        print("❌ 问题4：模型过度保守")
        print("="*80)
        
        problem_output = """
根据您的症状，建议您尽快到正规医院就诊。
本系统仅供参考，不能替代专业医疗诊断。
请咨询专业中医师。
"""
        
        print(f"🔍 问题输出：")
        print(problem_output)
        
        print(f"\n❌ 问题：")
        print("  - 完全没有给出中医诊断")
        print("  - 没有提供任何有价值的信息")
        print("  - 用户得不到想要的帮助")
        
        print("\n🤔 原因分析：")
        print("  1. 在第4轮筛选时，强制要求所有数据都包含'建议就医'")
        print("  2. 导致模型过度学习了免责声明，而忽视了实质内容")
        print("  3. 安全性和实用性的平衡没掌握好")
        
        print("\n✅ 解决方案：")
        solutions = [
            {
                'step': 1,
                'action': '调整数据要求',
                'old': '必须包含就医建议（强制）',
                'new': '可以包含就医建议，但不能只有就医建议（平衡）',
                'rule': '输出中"建议就医"相关内容不超过20%'
            },
            {
                'step': 2,
                'action': '调整数据比例',
                'detail': '在训练数据中适当减少免责声明的权重',
                'method': '将免责声明放在最后，而非开头'
            },
            {
                'step': 3,
                'action': '增加正面样本',
                'detail': '添加更多详细诊断分析的样本',
                'ratio': '详细分析:免责声明 = 8:2'
            },
            {
                'step': 4,
                'action': '重新筛选数据',
                'script': 'python data/rebalance_safety.py'
            }
        ]
        
        for sol in solutions:
            print(f"\n  步骤{sol['step']}: {sol['action']}")
            for key in ['old', 'new', 'rule', 'detail', 'method', 'ratio', 'script']:
                if key in sol:
                    print(f"    {key}: {sol[key]}")
        
        self.problems_found.append({
            'problem': '过度保守',
            'severity': 'medium',
            'solutions': solutions
        })
    
    def diagnose_ignoring_input(self):
        """
        问题5：忽视用户输入
        症状：不管用户说什么，都给相似的回答
        """
        print("\n" + "="*80)
        print("❌ 问题5：忽视用户输入")
        print("="*80)
        
        test_cases = [
            {
                'input': '我经常失眠多梦',
                'output': '根据您的症状，这是脾肾阳虚...'
            },
            {
                'input': '我脾气很大，容易发怒',
                'output': '根据您的症状，这是脾肾阳虚...'
            },
            {
                'input': '我手脚冰凉，腰酸',
                'output': '根据您的症状，这是脾肾阳虚...'
            }
        ]
        
        print(f"🔍 测试案例：")
        for i, tc in enumerate(test_cases, 1):
            print(f"\n  案例{i}:")
            print(f"    输入: {tc['input']}")
            print(f"    输出: {tc['output']}")
        
        print(f"\n❌ 问题：所有不同的输入都得到了相同的诊断！")
        
        print("\n🤔 原因分析：")
        reasons = [
            '训练数据中"脾肾阳虚"样本占比90%，模型产生了严重的偏见',
            '数据不够多样化，模型没学会区分不同症状',
            '训练轮数过多，模型过拟合到了高频证型'
        ]
        
        for i, reason in enumerate(reasons, 1):
            print(f"  {i}. {reason}")
        
        print("\n✅ 解决方案：")
        solutions = [
            {
                'step': 1,
                'action': '数据诊断',
                'script': 'python data/analyze_distribution.py',
                'output': '发现：脾肾阳虚(90%)  肝郁气滞(5%)  其他(5%)'
            },
            {
                'step': 2,
                'action': '重新采样',
                'method': '使用下采样减少高频类别，上采样增加低频类别',
                'target': '每个证型至少占10%',
                'script': 'python data/resample_balanced.py'
            },
            {
                'step': 3,
                'action': '生成对比数据',
                'detail': '为每个证型生成典型症状的对比样本',
                'example': '''
对比样本示例：
- 失眠多梦 + 心烦 → 心火亢盛
- 失眠多梦 + 健忘 → 心脾两虚
- 失眠多梦 + 腰酸 → 肾虚
                '''
            },
            {
                'step': 4,
                'action': '调整训练策略',
                'changes': [
                    'num_epochs: 5 → 3（减少过拟合）',
                    'learning_rate: 2e-4 → 3e-4（加快学习新模式）',
                    'sample_weights: 使用inverse frequency'
                ]
            },
            {
                'step': 5,
                'action': '重新训练',
                'script': 'python training/train_lora.py --balanced'
            }
        ]
        
        for sol in solutions:
            print(f"\n  步骤{sol['step']}: {sol['action']}")
            for key in ['script', 'output', 'method', 'target', 'detail', 'example', 'changes']:
                if key in sol:
                    if key == 'changes':
                        print(f"    {key}:")
                        for change in sol[key]:
                            print(f"      - {change}")
                    elif key == 'example':
                        print(f"    {key}:{sol[key]}")
                    else:
                        print(f"    {key}: {sol[key]}")
        
        self.problems_found.append({
            'problem': '忽视用户输入',
            'severity': 'critical',
            'root_cause': '数据分布严重不平衡',
            'solutions': solutions
        })
    
    def generate_fix_plan(self):
        """生成完整的修复计划"""
        print("\n" + "="*80)
        print("📋 完整修复计划")
        print("="*80)
        
        print(f"\n发现的问题总数: {len(self.problems_found)}")
        print(f"\n按严重程度排序:")
        
        # 按严重程度排序
        severity_order = {'critical': 3, 'high': 2, 'medium': 1, 'low': 0}
        sorted_problems = sorted(
            self.problems_found,
            key=lambda x: severity_order.get(x.get('severity', 'low'), 0),
            reverse=True
        )
        
        for i, prob in enumerate(sorted_problems, 1):
            severity = prob.get('severity', 'unknown')
            print(f"  {i}. {prob['problem']} [{severity.upper()}]")
        
        print(f"\n🔧 推荐修复顺序：")
        print(f"\n阶段1：数据修复（最重要）")
        print(f"  1. 运行数据诊断工具")
        print(f"     python data/analyze_distribution.py")
        print(f"     python data/check_repetitions.py")
        print(f"     python data/validate_format.py")
        
        print(f"\n  2. 修复数据问题")
        print(f"     python data/deduplicate_data.py        # 去重")
        print(f"     python data/resample_balanced.py       # 平衡采样")
        print(f"     python data/unify_format.py            # 统一格式")
        print(f"     python data/generate_balanced_data.py  # 补充缺失证型")
        
        print(f"\n  3. 验证修复效果")
        print(f"     python data/validate_final.py")
        
        print(f"\n阶段2：模型重训练")
        print(f"  4. 调整训练配置")
        print(f"     - num_epochs: 5 → 3")
        print(f"     - repetition_penalty: 1.0 → 1.2")
        print(f"     - use_balanced_sampling: True")
        
        print(f"\n  5. 重新训练")
        print(f"     python training/train_lora.py --config fixed_config.yaml")
        
        print(f"\n阶段3：测试验证")
        print(f"  6. 运行测试套件")
        print(f"     python inference/test_problems.py")
        print(f"     python inference/test_diversity.py")
        print(f"     python inference/test_format.py")
        
        print(f"\n  7. 人工验证")
        print(f"     python inference/interactive_demo.py")
        print(f"     人工测试各种场景，确保问题解决")
        
        print(f"\n💡 预计修复时间：")
        print(f"  - 数据修复: 2-4小时")
        print(f"  - 重新训练: 2-3小时")
        print(f"  - 测试验证: 1-2小时")
        print(f"  - 总计: 约1个工作日")
    
    def show_retraining_strategy(self):
        """展示重训练策略"""
        print("\n" + "="*80)
        print("🔄 重训练策略")
        print("="*80)
        
        print(f"\n选项1：从头训练 vs 选项2：继续训练")
        
        print(f"\n【选项1：从头训练】")
        print(f"  优点：")
        print(f"    ✓ 彻底解决数据问题")
        print(f"    ✓ 避免之前的错误模式")
        print(f"  缺点：")
        print(f"    ✗ 耗时长（2-3小时）")
        print(f"    ✗ 丢失之前学到的好的部分")
        print(f"  适用场景：")
        print(f"    - 数据变化较大（>30%）")
        print(f"    - 发现了根本性的数据问题")
        print(f"    - 模型问题严重")
        
        print(f"\n【选项2：继续训练（Warm Start）】")
        print(f"  优点：")
        print(f"    ✓ 快速（0.5-1小时）")
        print(f"    ✓ 保留已有知识")
        print(f"  缺点：")
        print(f"    ✗ 可能无法完全修正错误模式")
        print(f"    ✗ 需要精心调整学习率")
        print(f"  适用场景：")
        print(f"    - 小幅数据修正（<10%）")
        print(f"    - 微调某个特定问题")
        print(f"    - 补充新知识")
        
        print(f"\n🎯 本案例建议：从头训练")
        print(f"  原因：")
        print(f"    1. 数据分布问题严重（90%都是一个证型）")
        print(f"    2. 存在复读等根本性问题")
        print(f"    3. 重新平衡后的数据与原数据差异大")
        
        print(f"\n具体操作：")
        print(f"  # 1. 备份旧模型")
        print(f"  mv output/tcm_sft_lora output/tcm_sft_lora_v1_backup")
        
        print(f"\n  # 2. 使用修复后的数据训练")
        print(f"  python training/train_lora.py \\")
        print(f"    --data_path data/processed_fixed/ \\")
        print(f"    --output_dir output/tcm_sft_lora_v2 \\")
        print(f"    --num_epochs 3 \\")
        print(f"    --repetition_penalty 1.2 \\")
        print(f"    --balanced_sampling")
        
        print(f"\n  # 3. 对比新旧模型")
        print(f"  python inference/compare_models.py \\")
        print(f"    --model1 output/tcm_sft_lora_v1_backup \\")
        print(f"    --model2 output/tcm_sft_lora_v2")


def main():
    """主函数"""
    print("="*80)
    print("🏥 中医问诊助手 - 模型问题诊断与修复")
    print("="*80)
    print("\n这是一个真实的SFT项目调试场景")
    print("模拟训练完成后发现问题，并制定修复方案的过程")
    print("\n" + "="*80)
    input("\n按Enter键开始诊断...")
    
    diagnostics = ModelProblemDiagnostics()
    diagnostics.run_full_diagnosis()
    
    print("\n" + "="*80)
    print("✅ 诊断完成！")
    print("="*80)
    print("\n💡 关键教训：")
    print("  1. SFT不是一次性的，需要多次迭代")
    print("  2. 数据问题是最常见也最重要的")
    print("  3. 发现问题后不要怕麻烦，该重来就重来")
    print("  4. 保持详细的实验记录，避免重复犯错")


if __name__ == "__main__":
    main()

