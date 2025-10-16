"""
场景4：完整迭代之旅 - 7天从失败到成功
==========================================

这是最完整的真实案例，展示了整个项目的迭代过程：
- v0.1：完全失败（Day 1）
- v0.2：严重复读（Day 2）
- v0.3：判断错误（Day 3-4）
- v1.0：基本可用（Day 5）
- v1.1：效果优秀（Day 7）

每个版本都包含：
- 问题表现
- 根本原因
- 解决方案
- 效果对比

运行时间：约10分钟
这是SFT项目的真实缩影！
"""

import time
from typing import List, Dict


class FullIterationJourney:
    """完整的7天迭代之旅"""
    
    def __init__(self):
        self.versions = []
        
    def run(self):
        """运行完整演示"""
        print("="*100)
        print(" "*20 + "场景4：从失败到成功的完整迭代之旅（7天）")
        print("="*100)
        
        self.show_introduction()
        input("\n>>> 按Enter键开始Day 1...")
        
        # Day 1: v0.1 - 完全失败
        self.day1_v01_total_failure()
        input("\n>>> 按Enter键进入Day 2...")
        
        # Day 2: v0.2 - 严重复读
        self.day2_v02_repetition()
        input("\n>>> 按Enter键进入Day 3-4...")
        
        # Day 3-4: v0.3 - 判断错误
        self.day34_v03_wrong_diagnosis()
        input("\n>>> 按Enter键进入Day 5...")
        
        # Day 5: v1.0 - 基本可用
        self.day5_v10_usable()
        input("\n>>> 按Enter键进入Day 6-7...")
        
        # Day 6-7: v1.1 - 效果优秀
        self.day67_v11_excellent()
        
        # 最终总结
        self.final_summary()
        
    def show_introduction(self):
        """项目背景"""
        print("\n📖 项目背景：")
        print("-" * 100)
        print("""
你接到一个任务：开发一个中医问诊AI助手

初始计划（看起来很完美）：
  Day 1-2: 收集数据（150条）
  Day 3: 训练模型
  Day 4-7: 测试和优化
  
预算：
  时间：7天
  GPU：1张A100
  数据：网上爬取 + 专家编写
  
目标：
  准确率 > 80%
  可以实际使用

现实：计划永远赶不上变化...
        """)
        print("-" * 100)
    
    def day1_v01_total_failure(self):
        """Day 1: v0.1 - 完全失败"""
        print("\n" + "="*100)
        print("📅 Day 1: v0.1 - 信心满满的第一次尝试")
        print("="*100)
        
        print(f"\n上午：数据收集")
        print(f"  • 从3个中医网站爬取了150条问诊数据")
        print(f"  • 看起来质量不错，都是专业的中医内容")
        print(f"  • 快速检查：没有乱码，格式基本一致")
        
        time.sleep(0.5)
        
        print(f"\n下午：模型训练")
        print(f"  配置：Baichuan2-7B + LoRA(r=8)")
        print(f"  训练：3 epochs, lr=2e-4")
        
        print(f"\n训练进度：")
        for i in range(1, 4):
            loss_start = 2.5 - (i-1) * 0.5
            loss_end = loss_start - 0.5
            print(f"  Epoch {i}/3: Loss {loss_start:.2f} → {loss_end:.2f}")
            time.sleep(0.3)
        
        print(f"\n  ✅ 训练完成！Loss降到了0.89，看起来很好！")
        
        print(f"\n傍晚：兴奋地开始测试...")
        
        # 测试结果
        print(f"\n" + "-"*100)
        print("💔 测试结果：完全失败")
        print("-"*100)
        
        test_cases = [
            "我最近手脚冰凉，吃饭没胃口",
            "我脾气很大，容易发怒",
            "我失眠多梦，心烦意乱"
        ]
        
        bad_output = """根据您的症状，建议您尽快到正规医院中医科就诊。
本系统仅供参考，不能替代专业医疗诊断。
请咨询专业中医师进行面诊。"""
        
        for i, case in enumerate(test_cases, 1):
            print(f"\n测试{i}：{case}")
            print(f"输出：{bad_output}")
            print(f"❌ 完全没有中医诊断内容！")
        
        # 问题分析
        print(f"\n" + "="*100)
        print("🔍 紧急分析")
        print("="*100)
        
        print(f"\n检查前10条训练数据...")
        time.sleep(0.5)
        
        print(f"\n发现问题：")
        print(f"  数据1：(前150字) + '...建议到医院就诊。本系统仅供参考。'")
        print(f"  数据2：(前180字) + '...请咨询专业医生。本系统不能替代医疗。'")
        print(f"  数据3：(前160字) + '...建议就医。仅供参考。'")
        print(f"  ...")
        
        print(f"\n统计结果：")
        print(f"  148/150 条数据包含免责声明（98.7%）")
        print(f"  132/150 条免责声明在开头（88%）")
        print(f"  模型学会了：先说免责声明！")
        
        print(f"\n💡 根本原因：")
        print(f"  爬取的医疗网站出于法律原因，都有免责声明")
        print(f"  而且放在最前面，模型优先学习")
        print(f"  Loss 0.89很低，是因为模型'学会'了快速输出免责声明")
        
        print(f"\n😱 你的感受：")
        print(f"  完蛋了...第一天就翻车")
        print(f"  Loss低≠模型好，这个教训太深刻了")
        print(f"  必须重新筛选数据！")
        
        self.versions.append({
            'version': 'v0.1',
            'day': 1,
            'status': '❌ 完全失败',
            'accuracy': '0%',
            'loss': 0.89,
            'problem': '所有输出都是免责声明',
            'root_cause': '98%数据包含免责声明在开头'
        })
    
    def day2_v02_repetition(self):
        """Day 2: v0.2 - 严重复读"""
        print("\n" + "="*100)
        print("📅 Day 2: v0.2 - 数据重筛后的新问题")
        print("="*100)
        
        print(f"\n上午：紧急修复数据")
        print(f"  • 删除所有免责声明过重的数据（60条淘汰）")
        print(f"  • 保留90条相对纯净的数据")
        print(f"  • 请3位中医专家各写10条（补充30条）")
        print(f"  • 最终：120条数据")
        
        print(f"\n下午：重新训练")
        print(f"  配置：不变")
        print(f"  期望：这次应该可以了吧...")
        
        print(f"\n训练完成：Loss 1.15")
        print(f"  注意：Loss比v0.1高了（0.89 → 1.15）")
        print(f"  这是正常的！因为去掉了'容易预测'的免责声明")
        
        print(f"\n傍晚：谨慎地测试...")
        
        # 测试结果
        print(f"\n" + "-"*100)
        print("😓 新问题：严重复读")
        print("-"*100)
        
        print(f"\n测试输入：我手脚冰凉，腰膝酸软，夜尿频多")
        
        repetitive_output = """【症状归纳】
主症：手脚冰凉、腰膝酸软、夜尿频多
主症：手脚冰凉、腰膝酸软、夜尿频多
主症：手脚冰凉、腰膝酸软、夜尿频多

【辨证分析】
您的症状符合脾肾阳虚证型
您的症状符合脾肾阳虚证型
您的症状符合脾肾阳虚证型"""
        
        print(f"\n模型输出：")
        print(repetitive_output)
        
        print(f"\n❌ 问题：同一句话重复3次！")
        print(f"  复读率：约67%")
        print(f"  10个测试，10个都有复读问题")
        
        # 诊断
        print(f"\n" + "="*100)
        print("🔍 问题诊断")
        print("="*100)
        
        print(f"\n检查训练数据...")
        print(f"  运行：python data/check_repetitions.py")
        time.sleep(0.5)
        
        print(f"\n发现：")
        print(f"  32/120 条数据内部有重复句子（27%）")
        print(f"  原因：专家为了强调重点，故意重复")
        print(f"  例如：'一定要注意，一定要注意，这很重要'")
        
        print(f"\n检查生成参数...")
        print(f"  repetition_penalty: 未设置（默认1.0）")
        print(f"  no_repeat_ngram_size: 未设置")
        print(f"  → 模型可以无限制重复！")
        
        print(f"\n💡 解决方案：")
        print(f"  1. 数据去重（清理重复句子）")
        print(f"  2. 设置repetition_penalty=1.2")
        print(f"  3. 设置no_repeat_ngram_size=3")
        
        print(f"\n当晚：加班修复")
        print(f"  运行去重脚本")
        print(f"  修改推理代码")
        print(f"  明天重新训练...")
        
        self.versions.append({
            'version': 'v0.2',
            'day': 2,
            'status': '❌ 严重复读',
            'accuracy': '20%',
            'loss': 1.15,
            'problem': '67%内容重复',
            'root_cause': '数据有重复 + 参数未设置'
        })
    
    def day34_v03_wrong_diagnosis(self):
        """Day 3-4: v0.3 - 判断错误"""
        print("\n" + "="*100)
        print("📅 Day 3-4: v0.3 - 终于不复读了，但...")
        print("="*100)
        
        print(f"\nDay 3 上午：数据清理")
        print(f"  • 去除所有重复句子")
        print(f"  • 验证：0条重复")
        print(f"  • 最终：115条纯净数据")
        
        print(f"\nDay 3 下午：重新训练")
        print(f"  配置：")
        print(f"    repetition_penalty = 1.2")
        print(f"    no_repeat_ngram_size = 3")
        print(f"  Loss: 1.28（又升高了，但这是正常的）")
        
        print(f"\nDay 3 傍晚：测试")
        print(f"  ✅ 不复读了！")
        print(f"  ✅ 有完整的中医诊断！")
        print(f"  ✅ 格式统一！")
        
        print(f"\n看起来成功了？先测几个case...")
        
        # 测试
        print(f"\n" + "-"*100)
        print("测试结果")
        print("-"*100)
        
        test_results = [
            {
                'input': '我手脚冰凉，腰酸，夜尿多',
                'expected': '脾肾阳虚',
                'actual': '脾肾阳虚',
                'correct': True
            },
            {
                'input': '我总是怕冷，吃饭没胃口',
                'expected': '脾肾阳虚',
                'actual': '脾肾阳虚',
                'correct': True
            },
            {
                'input': '我脾气大，容易发怒，胸胁胀痛',
                'expected': '肝郁气滞',
                'actual': '脾肾阳虚',  # 错了！
                'correct': False
            },
            {
                'input': '我口干口苦，大便干结',
                'expected': '肝胆湿热',
                'actual': '脾肾阳虚',  # 又错了！
                'correct': False
            }
        ]
        
        for result in test_results:
            print(f"\n输入：{result['input']}")
            print(f"期望：{result['expected']}")
            print(f"实际：{result['actual']}")
            if result['correct']:
                print(f"✅ 正确")
            else:
                print(f"❌ 错误！")
        
        print(f"\n准确率：2/4 = 50%")
        print(f"😟 等等，有问题...")
        
        print(f"\nDay 4：全面测试")
        print(f"  准备了50个测试用例（覆盖不同证型）")
        time.sleep(0.5)
        
        print(f"\n" + "="*100)
        print("💔 严重问题：模型偏见")
        print("="*100)
        
        print(f"\n按证型分类的准确率：")
        print(f"  脾肾阳虚：10/10 = 100% ✅")
        print(f"  肝郁气滞：1/10 = 10% ❌")
        print(f"  肝胆湿热：0/10 = 0% ❌")
        print(f"  心肾不交：1/10 = 10% ❌")
        print(f"  阴虚火旺：0/10 = 0% ❌")
        
        print(f"\n发现：不管什么症状，都倾向于诊断为'脾肾阳虚'")
        
        # 数据诊断
        print(f"\n" + "="*100)
        print("🔍 数据分布分析")
        print("="*100)
        
        print(f"\n运行：python data/analyze_distribution.py")
        time.sleep(0.5)
        
        print(f"\n证型分布：")
        distribution = {
            '脾肾阳虚': 103,
            '肝郁气滞': 5,
            '肝胆湿热': 3,
            '心肾不交': 2,
            '阴虚火旺': 2
        }
        
        for syndrome, count in distribution.items():
            percentage = count / 115 * 100
            bar = '█' * int(percentage / 2)
            print(f"  {syndrome:12s}: {count:3d} ({percentage:5.1f}%) {bar}")
        
        print(f"\n💡 找到根本原因了！")
        print(f"  脾肾阳虚占了90%的数据")
        print(f"  模型学到：90%情况答案都是脾肾阳虚")
        print(f"  于是：不管什么都答脾肾阳虚（准确率90%！）")
        
        print(f"\nDay 4 晚上：制定补救方案")
        print(f"  需要补充其他证型的数据")
        print(f"  目标：每个证型至少50条")
        print(f"  工作量：补充约200条数据")
        print(f"  时间：至少2天...")
        
        print(f"\n😰 压力山大：")
        print(f"  已经Day 4了，进度严重落后")
        print(f"  但不能将就，必须补充数据")
        print(f"  决定：加班赶工！")
        
        self.versions.append({
            'version': 'v0.3',
            'day': '3-4',
            'status': '⚠️ 判断错误',
            'accuracy': '40%',
            'loss': 1.28,
            'problem': '所有症状都诊断为脾肾阳虚',
            'root_cause': '90%数据是同一证型'
        })
    
    def day5_v10_usable(self):
        """Day 5: v1.0 - 基本可用"""
        print("\n" + "="*100)
        print("📅 Day 5: v1.0 - 终于看到希望")
        print("="*100)
        
        print(f"\n连续加班的成果：")
        print(f"  • 使用GPT-4生成了180条数据")
        print(f"  • 请专家审核和修改（筛选出120条）")
        print(f"  • 自己手工编写了30条对比样本")
        print(f"  • 总计：265条数据")
        
        print(f"\n新的数据分布：")
        new_distribution = {
            '脾肾阳虚': 55,
            '肝郁气滞': 45,
            '肝胆湿热': 45,
            '心肾不交': 40,
            '阴虚火旺': 40,
            '血虚': 40
        }
        
        for syndrome, count in new_distribution.items():
            percentage = count / 265 * 100
            bar = '█' * int(percentage / 2)
            print(f"  {syndrome:12s}: {count:3d} ({percentage:5.1f}%) {bar}")
        
        print(f"\n✅ 基本平衡了！")
        
        print(f"\n重新训练（使用WeightedRandomSampler）")
        print(f"  Loss: 1.42（比之前高，但这是好事）")
        print(f"  原因：模型不能靠'猜一个答案'来降低Loss了")
        
        print(f"\n测试...")
        time.sleep(0.5)
        
        # 测试结果
        print(f"\n" + "="*100)
        print("🎉 终于可用了！")
        print("="*100)
        
        print(f"\n整体准确率：85%")
        
        print(f"\n按证型准确率：")
        results = {
            '脾肾阳虚': 0.90,
            '肝郁气滞': 0.85,
            '肝胆湿热': 0.80,
            '心肾不交': 0.85,
            '阴虚火旺': 0.80,
            '血虚': 0.83
        }
        
        for syndrome, acc in results.items():
            print(f"  {syndrome:12s}: {acc*100:.0f}%")
        
        print(f"\n✅ 所有证型都在80%以上！")
        print(f"✅ 没有明显的偏见！")
        print(f"✅ 不复读！")
        print(f"✅ 格式统一！")
        
        print(f"\n😊 终于可以交付了？")
        print(f"  但是...作为追求完美的工程师")
        print(f"  还想再优化一下细节")
        
        self.versions.append({
            'version': 'v1.0',
            'day': 5,
            'status': '✅ 基本可用',
            'accuracy': '85%',
            'loss': 1.42,
            'problem': '无重大问题',
            'improvement': '数据平衡 + WeightedSampler'
        })
    
    def day67_v11_excellent(self):
        """Day 6-7: v1.1 - 效果优秀"""
        print("\n" + "="*100)
        print("📅 Day 6-7: v1.1 - 细节打磨")
        print("="*100)
        
        print(f"\nDay 6：细节优化")
        
        optimizations = [
            {
                'aspect': '术语标准化',
                'before': '"舌头"、"脉搏"等口语',
                'after': '"舌象"、"脉象"等术语',
                'impact': '+2%准确率'
            },
            {
                'aspect': '剂量验证',
                'before': '附子30g（有毒性风险）',
                'after': '附子6-15g（安全范围）',
                'impact': '安全性提升'
            },
            {
                'aspect': '必须包含禁忌',
                'before': '70%数据有禁忌说明',
                'after': '100%数据有禁忌说明',
                'impact': '完整性提升'
            },
            {
                'aspect': '格式严格验证',
                'before': '95%格式一致',
                'after': '100%格式一致',
                'impact': '用户体验提升'
            }
        ]
        
        print(f"\n优化项目：")
        for opt in optimizations:
            print(f"\n  • {opt['aspect']}")
            print(f"    修复前：{opt['before']}")
            print(f"    修复后：{opt['after']}")
            print(f"    影响：{opt['impact']}")
        
        print(f"\n重新清洗数据 → 重新训练")
        print(f"  最终数据：258条（删除了7条不合格）")
        print(f"  Loss: 1.38")
        
        print(f"\nDay 7：最终测试")
        time.sleep(0.5)
        
        # 最终结果
        print(f"\n" + "="*100)
        print("🎊 最终成果")
        print("="*100)
        
        print(f"\n准确率：92%（+7% vs v1.0）")
        
        print(f"\n各项指标：")
        metrics = {
            '整体准确率': '92%',
            '格式一致性': '100%',
            '术语规范性': '100%',
            '安全性': '100%',
            '复读问题': '0%',
            '用户满意度': '⭐⭐⭐⭐⭐'
        }
        
        for metric, value in metrics.items():
            print(f"  {metric:15s}: {value}")
        
        print(f"\n按证型准确率：")
        final_results = {
            '脾肾阳虚': 0.94,
            '肝郁气滞': 0.92,
            '肝胆湿热': 0.90,
            '心肾不交': 0.91,
            '阴虚火旺': 0.92,
            '血虚': 0.92
        }
        
        for syndrome, acc in final_results.items():
            print(f"  {syndrome:12s}: {acc*100:.0f}%")
        
        print(f"\n✅ 所有证型都在90%以上！")
        print(f"✅ 可以正式交付了！")
        
        self.versions.append({
            'version': 'v1.1',
            'day': '6-7',
            'status': '🎉 效果优秀',
            'accuracy': '92%',
            'loss': 1.38,
            'improvements': '术语、剂量、禁忌、格式'
        })
    
    def final_summary(self):
        """最终总结"""
        print("\n" + "="*100)
        print("📊 7天迭代完整回顾")
        print("="*100)
        
        print(f"\n版本演进：")
        print(f"")
        print(f"{'版本':<10} {'天数':<10} {'状态':<15} {'准确率':<10} {'Loss':<10} {'主要问题':<30}")
        print("-" * 90)
        
        for v in self.versions:
            day = str(v['day'])
            print(f"{v['version']:<10} {f'Day {day}':<10} {v['status']:<15} {v['accuracy']:<10} {v['loss']:<10} {v['problem']:<30}")
        
        print(f"\n" + "="*100)
        print("💡 核心经验总结")
        print("="*100)
        
        lessons = [
            {
                'title': '1. SFT是迭代过程，不是一次性工程',
                'detail': '从v0.1到v1.1经历了5次迭代，每次都发现新问题'
            },
            {
                'title': '2. Loss低≠模型好',
                'detail': 'v0.1 Loss最低(0.89)但完全不可用，v1.1 Loss较高(1.38)但效果最好'
            },
            {
                'title': '3. 数据质量>数据数量',
                'detail': 'v0.1有150条但质量差，v1.1有258条高质量数据'
            },
            {
                'title': '4. 数据分布至关重要',
                'detail': 'v0.3数据质量好但分布不均，导致模型严重偏见'
            },
            {
                'title': '5. 测试要全面',
                'detail': '不能只测几个case，要覆盖所有类型'
            },
            {
                'title': '6. 细节决定成败',
                'detail': 'v1.0到v1.1的7%提升来自术语、剂量等细节优化'
            },
            {
                'title': '7. 耐心和毅力',
                'detail': '前4天都在失败，但坚持下来最终成功'
            }
        ]
        
        for lesson in lessons:
            print(f"\n{lesson['title']}")
            print(f"  {lesson['detail']}")
        
        print(f"\n" + "="*100)
        print("📈 资源消耗统计")
        print("="*100)
        
        resources = {
            '时间': {
                '计划': '7天',
                '实际': '7天（大量加班）',
                '差异': '计划合理，但低估了迭代次数'
            },
            'GPU时间': {
                '计划': '3小时（1次训练）',
                '实际': '15小时（5次训练）',
                '差异': '5倍'
            },
            '数据量': {
                '计划': '150条',
                '实际': '258条',
                '差异': '+72%'
            },
            '成本': {
                '计划': '$50',
                '实际': '$200',
                '差异': '4倍'
            }
        }
        
        for resource, details in resources.items():
            print(f"\n{resource}：")
            for key, value in details.items():
                print(f"  {key}: {value}")
        
        print(f"\n" + "="*100)
        print("🎯 如果重新开始，会怎么做？")
        print("="*100)
        
        improvements = [
            "1. Day 1: 先小规模测试（20条数据），快速发现免责声明问题",
            "2. Day 1-2: 数据收集时就检查分布，避免Day 4的惊喜",
            "3. Day 2: 一开始就设置repetition_penalty，避免重复问题",
            "4. Day 3: 准备更全面的测试集（覆盖所有证型）",
            "5. 全程: 详细记录每个问题和解决方案，避免重复犯错"
        ]
        
        for improvement in improvements:
            print(f"  {improvement}")
        
        print(f"\n预计可以节省：2天时间 + $100成本")
        
        print("\n" + "="*100)
        print(" "*30 + "场景4演示完成")
        print("="*100)
        
        print(f"\n🌟 最重要的领悟：")
        print(f"""
  SFT项目的成功靠的不是运气，而是：
  ✓ 系统的问题诊断
  ✓ 持续的数据优化
  ✓ 全面的测试验证
  ✓ 耐心的迭代改进
  
  失败是正常的，关键是从失败中学习！
        """)


def main():
    """主函数"""
    journey = FullIterationJourney()
    journey.run()
    
    print(f"\n\n💾 相关资源：")
    print(f"  • 完整迭代日志：../ITERATION_LOG.md")
    print(f"  • 数据分析工具：../data/analyze_distribution.py")
    print(f"  • 问题诊断工具：../training/problem_diagnosis_and_fix.py")
    print(f"  • 其他场景：scenario1-3.py")


if __name__ == "__main__":
    main()

