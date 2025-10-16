"""
4.2 通用对话助手 - 多任务模型问题诊断
真实的多任务SFT调试场景
"""

import json
from typing import List, Dict
from collections import Counter


class MultiTaskProblemDiagnostics:
    """
    多任务模型问题诊断工具
    """
    
    def __init__(self):
        self.problems_found = []
        
    def run_full_diagnosis(self):
        """运行完整的问题诊断"""
        print("="*80)
        print("🔍 多任务模型问题诊断")
        print("="*80)
        print("\n训练完成后，对10种任务分别测试，发现了以下问题...")
        print("\n" + "="*80)
        
        # 问题1：任务性能严重不均
        self.diagnose_uneven_performance()
        
        # 问题2：任务串扰
        self.diagnose_task_interference()
        
        # 问题3：格式混乱
        self.diagnose_format_confusion()
        
        # 问题4：遗忘基础能力
        self.diagnose_capability_forgetting()
        
        # 问题5：过拟合某些任务
        self.diagnose_task_overfitting()
        
        # 生成修复方案
        self.generate_fix_strategy()
    
    def diagnose_uneven_performance(self):
        """
        问题1：任务性能严重不均
        """
        print("\n" + "="*80)
        print("❌ 问题1：任务性能严重不均")
        print("="*80)
        
        # 模拟测试结果
        task_performance = {
            'qa': {'accuracy': 0.92, 'status': '✅ 优秀'},
            'code_generation': {'accuracy': 0.88, 'status': '✅ 良好'},
            'creative_writing': {'accuracy': 0.85, 'status': '✅ 良好'},
            'math_reasoning': {'accuracy': 0.78, 'status': '⚠️ 一般'},
            'summarization': {'accuracy': 0.91, 'status': '✅ 优秀'},
            'translation': {'accuracy': 0.45, 'status': '❌ 很差'},
            'information_extraction': {'accuracy': 0.52, 'status': '❌ 差'},
            'logic_reasoning': {'accuracy': 0.61, 'status': '⚠️ 较差'},
            'opinion_analysis': {'accuracy': 0.73, 'status': '⚠️ 一般'},
            'brainstorming': {'accuracy': 0.68, 'status': '⚠️ 一般'}
        }
        
        print(f"\n📊 各任务测试结果:")
        for task, result in sorted(task_performance.items(), 
                                   key=lambda x: x[1]['accuracy'], 
                                   reverse=True):
            acc = result['accuracy']
            status = result['status']
            bar = '█' * int(acc * 50)
            print(f"  {task:25s}: {acc:.2f} {bar} {status}")
        
        # 计算性能差距
        accuracies = [r['accuracy'] for r in task_performance.values()]
        best = max(accuracies)
        worst = min(accuracies)
        gap = best - worst
        
        print(f"\n性能差距:")
        print(f"  最好: {best:.2f} (问答)")
        print(f"  最差: {worst:.2f} (翻译)")
        print(f"  差距: {gap:.2f} (相差{gap/worst*100:.0f}%!)")
        
        print(f"\n🤔 原因分析:")
        reasons = [
            {
                'cause': '训练数据量差异',
                'detail': '问答有800条，翻译只有60条（补充后的）',
                'solution': '继续补充低频任务数据，目标每个任务≥200条'
            },
            {
                'cause': '任务难度不同',
                'detail': '翻译需要双语知识，逻辑推理需要多步思考，比简单问答难得多',
                'solution': '对难任务增加训练轮数，或使用课程学习（先易后难）'
            },
            {
                'cause': '数据质量不同',
                'detail': '高频任务是人工编写，低频任务是AI生成后简单审核',
                'solution': '请专家重新审核低频任务数据'
            },
            {
                'cause': '评估标准不统一',
                'detail': '问答有标准答案，创意写作评价主观',
                'solution': '使用GPT-4作为评判器，统一评估标准'
            }
        ]
        
        for i, r in enumerate(reasons, 1):
            print(f"\n  原因{i}: {r['cause']}")
            print(f"    详情: {r['detail']}")
            print(f"    解决: {r['solution']}")
        
        self.problems_found.append({
            'problem': '任务性能不均',
            'severity': 'high',
            'affected_tasks': ['translation', 'information_extraction', 'logic_reasoning']
        })
    
    def diagnose_task_interference(self):
        """
        问题2：任务串扰（Task Interference）
        """
        print("\n" + "="*80)
        print("❌ 问题2：任务串扰")
        print("="*80)
        
        interference_cases = [
            {
                'task': '问答任务',
                'input': '什么是机器学习？',
                'expected': '机器学习是...(简洁回答)',
                'actual': '''
机器学习是一种人工智能技术...

以下是5种机器学习算法：
1. 监督学习
2. 无监督学习
3. 强化学习
4. 半监督学习
5. 迁移学习
                ''',
                'interference_from': '头脑风暴（总想列举多个选项）'
            },
            {
                'task': '代码生成',
                'input': '实现快速排序',
                'expected': 'def quicksort(arr): ...',
                'actual': '''
根据您的需求，我提供以下几种排序算法：

```python
# 方案1：快速排序
def quicksort(arr): ...

# 方案2：归并排序  
def mergesort(arr): ...

# 方案3：堆排序
def heapsort(arr): ...
```

请问您需要哪种？
                ''',
                'interference_from': '头脑风暴（给出多个方案）+ 问答（反问用户）'
            },
            {
                'task': '翻译',
                'input': '将"I love AI"翻译成中文',
                'expected': '我爱人工智能',
                'actual': '''
这句话可以翻译为：

**直译**: 我爱AI
**意译**: 我热爱人工智能
**更地道的表达**: 我对AI充满热情

建议：根据语境选择最合适的翻译。
                ''',
                'interference_from': '观点分析（过度解释）+ 头脑风暴（多个选项）'
            }
        ]
        
        print(f"\n🔍 任务串扰案例:")
        for i, case in enumerate(interference_cases, 1):
            print(f"\n案例 {i}: {case['task']}")
            print(f"  输入: {case['input']}")
            print(f"  期望: {case['expected']}")
            print(f"  实际: {case['actual'].strip()}")
            print(f"  ❌ 干扰来源: {case['interference_from']}")
        
        print(f"\n🤔 根本原因:")
        print(f"  模型在多任务训练中学到了某些'过度泛化'的模式：")
        print(f"  - '给出多个选项总是好的'（来自头脑风暴任务）")
        print(f"  - '详细解释总是好的'（来自教学类任务）")
        print(f"  - '反问用户总是好的'（来自对话任务）")
        print(f"  这些模式在各自任务中是对的，但不应该应用到所有任务")
        
        print(f"\n✅ 解决方案:")
        solutions = [
            {
                'method': '强化任务边界',
                'detail': '在每个任务的instruction中明确说明"只回答这一个问题"、"不要提供多个方案"',
                'code': 'instruction = f"[任务: 翻译] 只翻译，不要解释。\\n{user_input}"'
            },
            {
                'method': '负样本训练',
                'detail': '添加反例数据，教模型什么是错误的行为',
                'example': '问答任务的反例："不要像头脑风暴那样列举多个答案"'
            },
            {
                'method': '任务隔离训练',
                'detail': '先分别训练各任务（独立LoRA），再合并',
                'advantage': '避免任务相互干扰，但需要更多资源'
            },
            {
                'method': '对比学习',
                'detail': '构造相似输入但不同任务的对比样本',
                'example': '''
样本A: [问答] "什么是AI？" → "AI是..."（简洁）
样本B: [头脑风暴] "AI的应用？" → "1. ... 2. ... 3. ..."（多个）
                '''
            }
        ]
        
        for i, sol in enumerate(solutions, 1):
            print(f"\n  方案{i}: {sol['method']}")
            print(f"    {sol['detail']}")
            for key in ['code', 'example', 'advantage']:
                if key in sol:
                    print(f"    {key}: {sol[key]}")
        
        self.problems_found.append({
            'problem': '任务串扰',
            'severity': 'critical',
            'solutions': solutions
        })
    
    def diagnose_format_confusion(self):
        """
        问题3：格式混乱
        """
        print("\n" + "="*80)
        print("❌ 问题3：输出格式混乱")
        print("="*80)
        
        format_issues = [
            {
                'issue': '代码混入Markdown',
                'example': '''
好的，我来实现快速排序：

**算法思路：**
1. 选择基准值
2. 分区
3. 递归

**代码实现：**
def quicksort(arr):
    ...
                ''',
                'expected': '直接输出代码，用```包裹',
                'cause': '创意写作任务使用Markdown格式，污染了代码任务'
            },
            {
                'issue': '问答添加代码块',
                'example': '''
```
机器学习是一种人工智能技术，它使计算机能够从数据中学习。
```
                ''',
                'expected': '直接文本回答，不需要代码块',
                'cause': '代码任务过多，模型过度使用```'
            },
            {
                'issue': '列表格式不统一',
                'example_1': '1. 第一点\n2. 第二点',
                'example_2': '- 第一点\n- 第二点',
                'example_3': '• 第一点\n• 第二点',
                'cause': '不同任务使用不同的列表格式'
            }
        ]
        
        print(f"\n格式问题:")
        for i, issue in enumerate(format_issues, 1):
            print(f"\n  问题{i}: {issue['issue']}")
            if 'example' in issue:
                print(f"    实际输出: {issue['example'].strip()}")
                print(f"    期望格式: {issue['expected']}")
            print(f"    原因: {issue['cause']}")
        
        print(f"\n✅ 解决方案:")
        print(f"  1. 统一格式规范文档")
        print(f"     - 代码：用```language包裹")
        print(f"     - 列表：统一用1. 2. 3.")
        print(f"     - 强调：用**加粗**")
        print(f"\n  2. 数据格式验证")
        print(f"     python data/validate_format.py")
        print(f"\n  3. 后处理清洗")
        print(f"     在推理时添加格式清洗逻辑")
        
        self.problems_found.append({
            'problem': '格式混乱',
            'severity': 'medium'
        })
    
    def diagnose_capability_forgetting(self):
        """
        问题4：遗忘基础能力（Catastrophic Forgetting）
        """
        print("\n" + "="*80)
        print("❌ 问题4：遗忘基础能力")
        print("="*80)
        
        print(f"\n测试基座模型 vs SFT后模型:")
        
        tests = [
            {
                'capability': '常识推理',
                'question': '太阳从哪个方向升起？',
                'base_model': '东方 ✅',
                'sft_model': '根据地球自转，太阳从东方升起。但这取决于您的地理位置和观测时间... ❌（过度复杂化）'
            },
            {
                'capability': '简单计算',
                'question': '3+5=?',
                'base_model': '8 ✅',
                'sft_model': '让我详细说明计算过程：\n第一步：3\n第二步：+5\n第三步：=8 ❌（过度解释）'
            },
            {
                'capability': '语言理解',
                'question': '【非任务指令】请用一句话介绍自己',
                'base_model': '我是一个AI助手... ✅',
                'sft_model': '根据您的要求，我将【任务：自我介绍】完成...'
                             ' ❌（过度形式化）'
            }
        ]
        
        for test in tests:
            print(f"\n  测试: {test['capability']}")
            print(f"  问题: {test['question']}")
            print(f"  基座模型: {test['base_model']}")
            print(f"  SFT模型: {test['sft_model']}")
        
        print(f"\n🤔 问题分析:")
        print(f"  SFT过程中，模型'忘记'了如何简单回答")
        print(f"  所有回复都变成了'任务化'的格式")
        print(f"  失去了自然对话的能力")
        
        print(f"\n✅ 解决方案:")
        solutions = [
            '保留通用对话数据（20-30%）',
            '使用LoRA而非全参数微调（减少遗忘）',
            '添加'混合数据：既有任务数据，也有普通对话',
            '降低学习率，减少对原模型的破坏'
        ]
        for i, sol in enumerate(solutions, 1):
            print(f"  {i}. {sol}")
        
        self.problems_found.append({
            'problem': '能力遗忘',
            'severity': 'high'
        })
    
    def diagnose_task_overfitting(self):
        """
        问题5：过拟合某些任务
        """
        print("\n" + "="*80)
        print("❌ 问题5：过拟合高频任务")
        print("="*80)
        
        overfitting_symptoms = {
            '问答任务': {
                'training_acc': 0.98,
                'test_acc': 0.72,
                'gap': 0.26,
                'symptom': '训练集上接近完美，测试集大幅下降',
                'cause': '问答数据最多(800条)，训练时权重过大'
            },
            '代码生成': {
                'training_acc': 0.95,
                'test_acc': 0.68,
                'gap': 0.27,
                'symptom': '只会生成训练集见过的算法模式',
                'cause': '代码数据重复率高，缺少多样性'
            }
        }
        
        print(f"\n过拟合迹象:")
        for task, metrics in overfitting_symptoms.items():
            print(f"\n  {task}:")
            print(f"    训练集准确率: {metrics['training_acc']:.2f}")
            print(f"    测试集准确率: {metrics['test_acc']:.2f}")
            print(f"    差距: {metrics['gap']:.2f} ❌")
            print(f"    症状: {metrics['symptom']}")
            print(f"    原因: {metrics['cause']}")
        
        print(f"\n✅ 解决方案:")
        print(f"  1. 数据增强")
        print(f"     对高频任务进行数据变换，增加多样性")
        print(f"  2. Dropout增加")
        print(f"     lora_dropout: 0.05 → 0.1")
        print(f"  3. 早停")
        print(f"     监控验证集，及时停止训练")
        print(f"  4. 正则化")
        print(f"     weight_decay增加: 0.01 → 0.05")
        
        self.problems_found.append({
            'problem': '任务过拟合',
            'severity': 'medium'
        })
    
    def generate_fix_strategy(self):
        """生成修复策略"""
        print("\n" + "="*80)
        print("📋 完整修复策略")
        print("="*80)
        
        print(f"\n发现问题: {len(self.problems_found)} 个")
        
        print(f"\n🎯 优先级修复顺序:")
        
        print(f"\n【高优先级】立即修复")
        print(f"  1. 任务串扰问题")
        print(f"     操作: 重新标注数据，强化任务边界")
        print(f"     时间: 2天")
        print(f"\n  2. 任务性能不均")
        print(f"     操作: 补充低频任务数据至200条/任务")
        print(f"     时间: 3天")
        print(f"\n  3. 能力遗忘")
        print(f"     操作: 添加30%通用对话数据")
        print(f"     时间: 1天")
        
        print(f"\n【中优先级】逐步改进")
        print(f"  4. 格式混乱")
        print(f"     操作: 统一格式规范，验证数据")
        print(f"     时间: 1天")
        print(f"\n  5. 任务过拟合")
        print(f"     操作: 调整训练参数，增加正则化")
        print(f"     时间: 0.5天")
        
        print(f"\n📅 完整修复计划 (7-8天):")
        print(f"  Day 1-2: 修复任务串扰")
        print(f"  Day 3-5: 补充数据，解决性能不均")
        print(f"  Day 6: 添加通用数据，解决遗忘")
        print(f"  Day 7: 统一格式，调整参数")
        print(f"  Day 8: 重新训练 + 测试验证")
        
        print(f"\n💡 多任务SFT的核心教训:")
        print(f"  1. 任务平衡比单任务SFT复杂10倍")
        print(f"  2. 任务串扰是最难解决的问题")
        print(f"  3. 需要更长的迭代周期（2-3周）")
        print(f"  4. 测试要覆盖所有任务，不能只看平均值")


def main():
    """主函数"""
    print("="*80)
    print("🤖 通用对话助手 - 多任务问题诊断")
    print("="*80)
    print("\n这展示了多任务SFT的特殊挑战")
    print("\n" + "="*80)
    input("\n按Enter键开始诊断...")
    
    diagnostics = MultiTaskProblemDiagnostics()
    diagnostics.run_full_diagnosis()
    
    print("\n" + "="*80)
    print("✅ 诊断完成！")
    print("="*80)


if __name__ == "__main__":
    main()

