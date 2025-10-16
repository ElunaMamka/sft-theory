"""
场景2：模型复读问题的完整诊断与修复
=====================================

这是一个真实的模型调试案例，展示了：
- 训练后发现模型严重复读
- 如何一步步诊断根本原因
- 多种解决方案的对比
- 修复验证过程

运行时间：约8分钟
输出：完整的问题诊断、修复方案和对比测试
"""

import re
from typing import List, Dict
import time


class RepetitionProblemCase:
    """
    真实案例：模型复读问题的诊断与修复
    """
    
    def __init__(self):
        self.test_cases = []
        self.diagnosis_results = {}
        
    def run(self):
        """运行完整的场景演示"""
        print("="*100)
        print(" "*25 + "场景2：模型复读问题 - 完整诊断与修复流程")
        print("="*100)
        
        self.show_introduction()
        input("\n>>> 按Enter键开始...")
        
        # 阶段1：问题发现
        self.stage1_problem_discovery()
        input("\n>>> 按Enter键进行诊断...")
        
        # 阶段2：原因诊断
        self.stage2_root_cause_analysis()
        input("\n>>> 按Enter键查看解决方案...")
        
        # 阶段3：解决方案
        self.stage3_solutions()
        input("\n>>> 按Enter键验证修复效果...")
        
        # 阶段4：修复验证
        self.stage4_verification()
        
        # 阶段5：总结
        self.stage5_summary()
    
    def show_introduction(self):
        """展示场景介绍"""
        print("\n📖 场景背景：")
        print("-" * 100)
        print("""
你完成了数据筛选和训练，现在激动地测试你的中医问诊模型...

训练配置：
  - 模型：Baichuan2-7B
  - 方法：LoRA (r=8, alpha=16)
  - 数据：150条高质量中医问诊数据
  - 训练：3 epochs, lr=2e-4
  - Loss：从2.1降到0.89（看起来很好！）

你满怀期待地输入第一个测试问题...
        """)
        print("-" * 100)
    
    def stage1_problem_discovery(self):
        """阶段1：问题发现"""
        print("\n" + "="*100)
        print("阶段1：问题发现 - 初次测试")
        print("="*100)
        
        # 测试用例1
        print("\n" + "-"*100)
        print("【测试 1】")
        print("-"*100)
        print("输入：我最近总是感觉很累，手脚冰凉，吃饭也没什么胃口\n")
        
        time.sleep(1)
        print("模型输出：")
        print("-" * 50)
        
        bad_output_1 = """根据您描述的症状，我进行分析：

【症状归纳】
主症：神疲乏力、手脚冰凉、食欲不振
主症：神疲乏力、手脚冰凉、食欲不振
主症：神疲乏力、手脚冰凉、食欲不振

【辨证分析】
您的这些症状符合中医的"脾肾阳虚"证型
您的这些症状符合中医的"脾肾阳虚"证型
您的这些症状符合中医的"脾肾阳虚"证型

【治则治法】
温补脾肾、助阳散寒
温补脾肾、助阳散寒
温补脾肾、助阳散寒"""
        
        for char in bad_output_1:
            print(char, end='', flush=True)
            time.sleep(0.01)
        
        print("\n" + "-" * 50)
        
        time.sleep(1)
        print("\n❌ 问题：同一句话重复了3次！")
        
        # 测试用例2
        print("\n" + "-"*100)
        print("【测试 2】")
        print("-"*100)
        print("输入：我脾气很大，容易发怒，胸胁胀痛\n")
        
        time.sleep(1)
        print("模型输出：")
        print("-" * 50)
        
        bad_output_2 = """【症状归纳】
易怒、胸胁胀痛
易怒、胸胁胀痛

【辨证分析】
这是肝郁气滞的表现
这是肝郁气滞的表现
这是肝郁气滞的表现
这是肝郁气滞的表现"""
        
        for char in bad_output_2:
            print(char, end='', flush=True)
            time.sleep(0.01)
        
        print("\n" + "-" * 50)
        
        time.sleep(1)
        print("\n❌ 问题：又是重复！这次有的重复2次，有的重复4次")
        
        # 测试用例3
        print("\n" + "-"*100)
        print("【测试 3】")
        print("-"*100)
        print("输入：我手脚冰凉，腰膝酸软\n")
        
        time.sleep(1)
        print("模型输出：")
        print("-" * 50)
        
        bad_output_3 = """肾阳虚 肾阳虚 肾阳虚 肾阳虚 肾阳虚 肾阳虚
可以用金匮肾气丸 可以用金匮肾气丸 可以用金匮肾气丸"""
        
        for char in bad_output_3:
            print(char, end='', flush=True)
            time.sleep(0.01)
        
        print("\n" + "-" * 50)
        
        time.sleep(1)
        print("\n❌ 问题：这次更严重，整个输出都在重复！")
        
        # 统计复读问题
        print("\n" + "="*100)
        print("📊 问题统计")
        print("="*100)
        
        test_results = [
            {'id': 1, 'repetition_rate': 0.67, 'max_repeat': 3, 'severity': '严重'},
            {'id': 2, 'repetition_rate': 0.75, 'max_repeat': 4, 'severity': '严重'},
            {'id': 3, 'repetition_rate': 0.90, 'max_repeat': 6, 'severity': '极严重'}
        ]
        
        print(f"\n测试样本复读统计：")
        print(f"{'测试ID':<10} {'复读率':<15} {'最大重复次数':<15} {'严重程度':<10}")
        print("-" * 60)
        for result in test_results:
            print(f"{result['id']:<10} {result['repetition_rate']:.0%}{' '*9} {result['max_repeat']}{' '*12} {result['severity']:<10}")
        
        print(f"\n进一步测试10个样本...")
        time.sleep(0.5)
        print(f"  - 10个样本全部存在复读问题")
        print(f"  - 平均复读率：72%")
        print(f"  - 用户完全无法使用！")
        
        print(f"\n😱 你的心情：")
        print(f"  花了3天准备数据")
        print(f"  花了2小时训练")
        print(f"  结果模型完全不可用！")
        print(f"  Loss明明下降得很好，为什么会这样？？")
    
    def stage2_root_cause_analysis(self):
        """阶段2：根本原因分析"""
        print("\n" + "="*100)
        print("阶段2：根本原因诊断")
        print("="*100)
        
        print(f"\n冷静下来，开始系统性诊断...")
        
        # 诊断步骤1：检查训练数据
        print(f"\n" + "-"*100)
        print("诊断步骤1：检查训练数据是否有重复")
        print("-"*100)
        
        print(f"\n运行数据分析脚本...")
        time.sleep(0.5)
        
        print(f"""
python analyze_training_data.py

分析中...
        """)
        time.sleep(0.5)
        
        print(f"📊 数据分析结果：")
        print(f"""
总数据量：150条

重复检测：
  - 完全重复的数据：0条 ✅
  - 但发现：39条数据（26%）内部包含重复句子！❌
  
示例：
  数据ID 23:
  输出："症状分析：脾肾阳虚。症状分析：脾肾阳虚。治疗建议：..."
  
  数据ID 56:
  输出："【辨证】肝郁气滞\n【辨证】肝郁气滞\n【辨证】肝郁气滞\n【方药】..."
        """)
        
        print(f"\n🔍 发现问题1：训练数据中有重复内容")
        print(f"  - 原因：某些中医专家在编写数据时，为了强调重点，故意重复")
        print(f"  - 例如："一定要注意，一定要注意，这个很重要"")
        print(f"  - 模型学到了这种"强调式重复"的模式")
        
        # 诊断步骤2：检查生成参数
        print(f"\n" + "-"*100)
        print("诊断步骤2：检查生成参数配置")
        print("-"*100)
        
        print(f"\n检查推理代码...")
        time.sleep(0.5)
        
        generation_config = """
# inference/test_model.py

generation_config = {
    "max_new_tokens": 512,
    "temperature": 0.7,
    "top_p": 0.9,
    "do_sample": True,
    # repetition_penalty: 未设置！ ❌
    # no_repeat_ngram_size: 未设置！ ❌
}
        """
        
        print(generation_config)
        
        print(f"\n🔍 发现问题2：生成参数未设置防重复措施")
        print(f"  - repetition_penalty：控制重复惩罚，未设置（默认1.0=不惩罚）")
        print(f"  - no_repeat_ngram_size：禁止n-gram重复，未设置")
        print(f"  - 这意味着模型可以无限制地重复！")
        
        # 诊断步骤3：检查训练配置
        print(f"\n" + "-"*100)
        print("诊断步骤3：检查训练配置")
        print("-"*100)
        
        print(f"\n检查训练脚本...")
        time.sleep(0.5)
        
        training_config = """
# training/train_lora.py

training_args = TrainingArguments(
    num_train_epochs=3,
    learning_rate=2e-4,
    per_device_train_batch_size=4,
    # ...其他参数
)

# 问题：训练时没有对数据进行去重预处理！❌
        """
        
        print(training_config)
        
        print(f"\n🔍 发现问题3：训练前未对数据去重")
        print(f"  - 包含重复的数据直接用于训练")
        print(f"  - 模型在3个epoch中反复学习这些重复模式")
        print(f"  - 强化了"重复是正常的"这个错误认知")
        
        # 诊断步骤4：检查Loss曲线
        print(f"\n" + "-"*100)
        print("诊断步骤4：分析Loss曲线")
        print("-"*100)
        
        print(f"\n查看训练日志...")
        time.sleep(0.5)
        
        print(f"""
训练Loss曲线：
  Epoch 1: 2.1 → 1.5
  Epoch 2: 1.5 → 1.1  
  Epoch 3: 1.1 → 0.89

看起来很好？实际上...
        """)
        
        print(f"\n🔍 发现问题4：Loss低不等于质量好")
        print(f"  - 模型通过"重复"可以很容易地降低Loss")
        print(f"  - 例如：预测"症状分析"后，继续预测"症状分析"的概率很高")
        print(f"  - 这样Loss会很低，但输出质量很差")
        print(f"  - 这就是为什么Loss 0.89看起来好，实际模型不可用")
        
        # 总结根本原因
        print(f"\n" + "="*100)
        print("🎯 根本原因总结")
        print("="*100)
        
        root_causes = [
            {
                'cause': '数据中存在重复内容',
                'severity': '⭐⭐⭐⭐⭐',
                'contribution': '60%',
                'detail': '26%的数据包含重复句子，模型学会了重复模式'
            },
            {
                'cause': '未设置重复惩罚参数',
                'severity': '⭐⭐⭐⭐',
                'contribution': '30%',
                'detail': 'repetition_penalty未设置，模型可以无限制重复'
            },
            {
                'cause': '训练前未去重',
                'severity': '⭐⭐⭐',
                'contribution': '10%',
                'detail': '数据预处理不够仔细'
            }
        ]
        
        print(f"\n原因分析：")
        for i, cause in enumerate(root_causes, 1):
            print(f"\n{i}. {cause['cause']}")
            print(f"   严重程度：{cause['severity']}")
            print(f"   贡献度：{cause['contribution']}")
            print(f"   详情：{cause['detail']}")
    
    def stage3_solutions(self):
        """阶段3：解决方案"""
        print("\n" + "="*100)
        print("阶段3：解决方案设计")
        print("="*100)
        
        # 方案1：快速修复（治标）
        print(f"\n" + "-"*100)
        print("方案1：快速修复（仅调整生成参数）")
        print("-"*100)
        
        print(f"\n优点：")
        print(f"  ✓ 无需重新训练，立即生效")
        print(f"  ✓ 实施简单，只需改几行代码")
        print(f"  ✓ 耗时：5分钟")
        
        print(f"\n缺点：")
        print(f"  ✗ 治标不治本，模型内部仍有重复倾向")
        print(f"  ✗ 可能影响输出质量（过度惩罚）")
        
        print(f"\n实施方法：")
        solution1_code = """
# inference/test_model.py

generation_config = {
    "max_new_tokens": 512,
    "temperature": 0.7,
    "top_p": 0.9,
    "do_sample": True,
    "repetition_penalty": 1.2,      # 新增：重复惩罚
    "no_repeat_ngram_size": 3,      # 新增：禁止3-gram重复
}
        """
        print(solution1_code)
        
        # 方案2：数据修复（治本）
        print(f"\n" + "-"*100)
        print("方案2：数据修复 + 重新训练")
        print("-"*100)
        
        print(f"\n优点：")
        print(f"  ✓ 从根本上解决问题")
        print(f"  ✓ 模型质量更高")
        print(f"  ✓ 不需要依赖生成参数的trick")
        
        print(f"\n缺点：")
        print(f"  ✗ 需要重新训练（2-3小时）")
        print(f"  ✗ 实施复杂度高")
        
        print(f"\n实施方法：")
        
        print(f"\n步骤1：编写数据去重脚本")
        solution2_code1 = """
# data/remove_repetitions.py

def remove_repetitive_sentences(text):
    '''去除文本中的重复句子'''
    sentences = split_sentences(text)
    unique_sentences = []
    
    for sent in sentences:
        # 检查是否与已有句子相似
        if not is_similar_to_any(sent, unique_sentences, threshold=0.8):
            unique_sentences.append(sent)
    
    return ''.join(unique_sentences)

# 处理所有数据
for item in dataset:
    item['output'] = remove_repetitive_sentences(item['output'])
        """
        print(solution2_code1)
        
        print(f"\n步骤2：重新训练")
        solution2_code2 = """
# 使用清洗后的数据重新训练
python training/train_lora.py --data_path data/cleaned_dataset.json
        """
        print(solution2_code2)
        
        # 方案3：综合方案（推荐）
        print(f"\n" + "-"*100)
        print("方案3：综合方案（数据修复 + 参数调整）★ 推荐")
        print("-"*100)
        
        print(f"\n为什么推荐综合方案？")
        print(f"  1. 双重保险：既修复数据，又设置参数")
        print(f"  2. 效果最好：从根本上解决+额外防护")
        print(f"  3. 未来兼容：即使遇到新的边缘case，参数也能兜底")
        
        print(f"\n实施步骤：")
        steps = [
            "1. 数据去重（去除重复句子）",
            "2. 数据验证（确保没有重复）",
            "3. 重新训练（使用清洗后的数据）",
            "4. 设置生成参数（repetition_penalty=1.2）",
            "5. 全面测试（验证修复效果）"
        ]
        
        for step in steps:
            print(f"  {step}")
            time.sleep(0.3)
        
        # 成本对比
        print(f"\n" + "="*100)
        print("💰 成本对比")
        print("="*100)
        
        print(f"\n{'方案':<20} {'时间成本':<15} {'GPU成本':<15} {'效果':<15} {'推荐度':<10}")
        print("-" * 80)
        print(f"{'方案1(参数)':<20} {'5分钟':<15} {'$0':<15} {'70分':<15} {'⭐⭐':<10}")
        print(f"{'方案2(数据)':<20} {'3小时':<15} {'$2':<15} {'85分':<15} {'⭐⭐⭐⭐':<10}")
        print(f"{'方案3(综合)':<20} {'3.5小时':<15} {'$2':<15} {'95分':<15} {'⭐⭐⭐⭐⭐':<10}")
        
        print(f"\n🎯 决策：选择方案3（综合方案）")
        print(f"  理由：虽然多花3.5小时，但彻底解决问题，避免后续反复调试")
    
    def stage4_verification(self):
        """阶段4：修复验证"""
        print("\n" + "="*100)
        print("阶段4：修复效果验证")
        print("="*100)
        
        print(f"\n执行综合方案...")
        
        # 步骤1
        print(f"\n步骤1：数据去重")
        time.sleep(0.5)
        print(f"  处理150条数据...")
        time.sleep(0.5)
        print(f"  发现39条包含重复句子")
        time.sleep(0.5)
        print(f"  清理完成！")
        
        # 步骤2
        print(f"\n步骤2：重新训练（这需要2-3小时，此处跳过等待）")
        print(f"  [模拟] 训练完成，Loss: 1.05")
        print(f"  注意：Loss从0.89升到1.05，这是正常的！")
        print(f"  因为去除了重复，模型不能靠重复来降低Loss了")
        
        # 步骤3
        print(f"\n步骤3：设置生成参数")
        print(f"  repetition_penalty = 1.2 ✓")
        print(f"  no_repeat_ngram_size = 3 ✓")
        
        # 测试
        print(f"\n步骤4：测试修复后的模型")
        print(f"\n" + "-"*100)
        
        # 测试用例1
        print("【测试 1】修复后")
        print("-"*100)
        print("输入：我最近总是感觉很累，手脚冰凉，吃饭也没什么胃口\n")
        
        time.sleep(1)
        print("模型输出（修复后）：")
        print("-" * 50)
        
        good_output_1 = """根据您描述的症状，我进行分析：

【症状归纳】
主症：神疲乏力、手脚冰凉、食欲不振

【辨证分析】
您的这些症状符合中医的"脾肾阳虚"证型。脾肾阳虚时，
阳气不足，无法温煦四肢，故手脚冰凉；脾失健运，故食欲不振；
气血生化不足，故感觉疲乏无力。

【治则治法】
温补脾肾、助阳散寒

【方药建议】
可以参考附子理中丸合金匮肾气丸加减"""
        
        for char in good_output_1:
            print(char, end='', flush=True)
            time.sleep(0.01)
        
        print("\n" + "-" * 50)
        print("✅ 完美！没有重复！")
        
        # 对比显示
        print(f"\n" + "="*100)
        print("📊 修复前后对比")
        print("="*100)
        
        print(f"\n修复前（问题严重）：")
        print("""
主症：神疲乏力、手脚冰凉、食欲不振
主症：神疲乏力、手脚冰凉、食欲不振  ← 重复
主症：神疲乏力、手脚冰凉、食欲不振  ← 重复
        """)
        
        print(f"\n修复后（正常）：")
        print("""
主症：神疲乏力、手脚冰凉、食欲不振  ← 只出现一次
        """)
        
        # 全面测试
        print(f"\n进行全面测试（50个测试用例）...")
        time.sleep(1)
        
        print(f"\n测试结果：")
        print(f"{'指标':<25} {'修复前':<15} {'修复后':<15} {'改善':<10}")
        print("-" * 70)
        print(f"{'复读率':<25} {'72%':<15} {'0%':<15} {'✅ -72%':<10}")
        print(f"{'输出质量':<25} {'不可用':<15} {'优秀':<15} {'✅ +100%':<10}")
        print(f"{'用户可用性':<25} {'0%':<15} {'95%':<15} {'✅ +95%':<10}")
        print(f"{'Loss':<25} {'0.89':<15} {'1.05':<15} {'⚠️  +0.16':<10}")
        
        print(f"\n💡 关键发现：")
        print(f"  - Loss升高是正常的（去除重复后）")
        print(f"  - 但输出质量大幅提升")
        print(f"  - 再次证明：Loss低≠模型好")
    
    def stage5_summary(self):
        """阶段5：总结"""
        print("\n" + "="*100)
        print("阶段5：经验总结")
        print("="*100)
        
        print(f"\n🎯 核心教训：")
        
        lessons = [
            {
                'title': '1. 训练Loss不是唯一指标',
                'detail': [
                    '❌ 错误：Loss从2.1降到0.89，模型一定很好',
                    '✅ 正确：Loss只是参考，必须看实际输出质量',
                    '原因：模型可以通过"取巧"（如重复）来降低Loss'
                ]
            },
            {
                'title': '2. 数据质量至关重要',
                'detail': [
                    '❌ 错误：数据没有完全重复就可以了',
                    '✅ 正确：数据内部的重复句子也要清理',
                    '影响：26%数据有问题就足以毁掉模型'
                ]
            },
            {
                'title': '3. 生成参数不是万能的',
                'detail': [
                    '❌ 错误：只靠repetition_penalty解决重复',
                    '✅ 正确：数据修复是根本，参数是辅助',
                    '对比：纯参数方案70分 vs 综合方案95分'
                ]
            },
            {
                'title': '4. 测试要全面且早做',
                'detail': [
                    '❌ 错误：训练完才开始测试',
                    '✅ 正确：训练前抽查数据，训练后立即测试',
                    '好处：早发现早修正，避免浪费GPU时间'
                ]
            },
            {
                'title': '5. 诊断要系统化',
                'detail': [
                    '不要靠猜：按步骤检查（数据→参数→配置）',
                    '不要将就：发现根本问题就要彻底修复',
                    '不要省钱：多花3小时比后续调试1周强'
                ]
            }
        ]
        
        for lesson in lessons:
            print(f"\n{lesson['title']}")
            for point in lesson['detail']:
                print(f"  {point}")
        
        print(f"\n" + "="*100)
        print("📋 可复用的问题诊断清单")
        print("="*100)
        
        checklist = [
            "□ 检查训练数据是否有重复内容",
            "□ 检查generation_config是否设置repetition_penalty",
            "□ 检查是否设置no_repeat_ngram_size",
            "□ 分析训练Loss曲线（过低可能有问题）",
            "□ 人工测试至少10个不同类型的样本",
            "□ 统计重复率和重复模式",
            "□ 对比训练数据和模型输出，找相似性"
        ]
        
        print(f"\n当遇到复读问题时，按此清单逐项检查：")
        for item in checklist:
            print(f"  {item}")
        
        print("\n" + "="*100)
        print(" "*25 + "场景2演示完成")
        print("="*100)
        
        print(f"\n💾 相关代码文件：")
        print(f"  - data/remove_repetitions.py - 数据去重脚本")
        print(f"  - data/analyze_training_data.py - 数据分析脚本")
        print(f"  - inference/test_model.py - 推理配置（修复后）")


def main():
    """主函数"""
    case = RepetitionProblemCase()
    case.run()
    
    print(f"\n\n💾 如需查看代码实现细节，请查看本文件：")
    print(f"   sft-theory/code/part4/4.1_vertical_domain_tcm/scenarios/scenario2_model_repetition_problem.py")


if __name__ == "__main__":
    main()

