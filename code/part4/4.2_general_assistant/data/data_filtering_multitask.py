"""
4.2 通用对话助手 - 多任务数据筛选与平衡
展示多任务SFT的真实数据准备过程
"""

import json
import re
from typing import List, Dict
from collections import Counter
import random


class MultiTaskDataFilteringPipeline:
    """
    多任务数据筛选流水线
    处理10+种任务类型的数据平衡和质量控制
    """
    
    def __init__(self, raw_data_path: str):
        self.raw_data_path = raw_data_path
        self.raw_data = self.load_data(raw_data_path)
        self.filtering_history = []
        
    def load_data(self, path: str) -> List[Dict]:
        """加载原始数据"""
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def run_full_pipeline(self):
        """运行完整的筛选流程"""
        print("="*80)
        print("🔍 多任务数据筛选流水线 - 真实场景")
        print("="*80)
        
        # 第一轮：任务分类和统计
        round1_data = self.round1_task_classification(self.raw_data)
        
        # 发现问题：任务分布严重不均衡
        self.discover_task_imbalance_problem(round1_data)
        
        # 第二轮：任务平衡策略
        round2_data = self.round2_task_balancing(round1_data)
        
        # 第三轮：质量筛选
        round3_data = self.round3_quality_filtering(round2_data)
        
        # 发现新问题：任务冲突
        self.discover_task_conflict_problem(round3_data)
        
        # 第四轮：解决任务冲突
        round4_data = self.round4_resolve_conflicts(round3_data)
        
        # 第五轮：最终验证
        final_data = self.round5_final_validation(round4_data)
        
        # 生成报告
        self.generate_report()
        
        return final_data
    
    def round1_task_classification(self, data: List[Dict]) -> List[Dict]:
        """
        第一轮：任务分类和统计
        """
        print("\n" + "="*80)
        print("📋 第一轮：任务分类和统计")
        print("="*80)
        
        # 统计每个任务类型的数量
        task_distribution = Counter()
        for item in data:
            task_type = item.get('task_type', 'unknown')
            task_distribution[task_type] += 1
        
        print(f"\n📊 任务分布统计:")
        print(f"  总数据量: {len(data)}")
        print(f"  任务类型数: {len(task_distribution)}")
        print(f"\n各任务数量:")
        
        for task, count in task_distribution.most_common():
            percentage = count / len(data) * 100
            bar = '█' * int(percentage / 2)
            print(f"  {task:20s}: {count:3d} ({percentage:5.1f}%) {bar}")
        
        self.filtering_history.append({
            'round': 1,
            'name': '任务分类统计',
            'task_distribution': dict(task_distribution)
        })
        
        return data
    
    def discover_task_imbalance_problem(self, data: List[Dict]):
        """
        发现问题：任务分布严重不均衡
        """
        print("\n" + "!"*80)
        print("❌ 问题发现：任务分布严重不均衡！")
        print("!"*80)
        
        task_counts = Counter(item.get('task_type') for item in data)
        max_count = max(task_counts.values())
        min_count = min(task_counts.values())
        
        problems = [
            {
                'problem': '数据分布极度不均',
                'detail': f'最多的任务({max_count}条) vs 最少的任务({min_count}条)，相差{max_count/min_count:.1f}倍！',
                'impact': '模型会严重偏向高频任务，低频任务基本学不会',
                'example': '比如代码生成有500条，但翻译只有50条'
            },
            {
                'problem': '某些任务数据质量差',
                'detail': '低频任务的数据往往是临时补充的，质量不如高频任务',
                'impact': '即使平衡了数量，模型在低频任务上表现仍然差',
                'example': '代码任务是专家写的，翻译任务是AI生成的'
            },
            {
                'problem': '任务难度不一致',
                'detail': '简单任务（如摘要）和复杂任务（如推理）混在一起',
                'impact': '模型可能过拟合简单任务，复杂任务学不好',
                'example': '摘要只需要提取关键词，推理需要多步思考'
            }
        ]
        
        for i, prob in enumerate(problems, 1):
            print(f"\n问题 {i}: {prob['problem']}")
            print(f"  详情: {prob['detail']}")
            print(f"  影响: {prob['impact']}")
            print(f"  举例: {prob['example']}")
        
        print("\n💡 关键教训：")
        print("   多任务SFT最大的挑战就是任务平衡！")
        print("   不仅要平衡数量，还要平衡质量、难度、重要性")
    
    def round2_task_balancing(self, data: List[Dict]) -> List[Dict]:
        """
        第二轮：任务平衡策略
        """
        print("\n" + "="*80)
        print("📋 第二轮：任务平衡")
        print("="*80)
        
        # 统计当前分布
        task_groups = {}
        for item in data:
            task = item.get('task_type', 'unknown')
            if task not in task_groups:
                task_groups[task] = []
            task_groups[task].append(item)
        
        print(f"\n平衡策略：")
        print(f"  目标: 每个任务至少100条，最多200条")
        print(f"  方法: 上采样（复制）+ 下采样（删除）")
        
        balanced_data = []
        target_min = 100
        target_max = 200
        
        for task, items in task_groups.items():
            count = len(items)
            
            if count < target_min:
                # 上采样：重复数据
                repeat_times = target_min // count + 1
                sampled = (items * repeat_times)[:target_min]
                action = f"上采样 {count}→{len(sampled)}"
            elif count > target_max:
                # 下采样：随机选择
                sampled = random.sample(items, target_max)
                action = f"下采样 {count}→{len(sampled)}"
            else:
                sampled = items
                action = f"保持 {count}"
            
            balanced_data.extend(sampled)
            print(f"  {task:20s}: {action}")
        
        print(f"\n平衡后总数: {len(balanced_data)}")
        
        self.filtering_history.append({
            'round': 2,
            'name': '任务平衡',
            'before': len(data),
            'after': len(balanced_data),
            'strategy': 'up/down sampling'
        })
        
        return balanced_data
    
    def round3_quality_filtering(self, data: List[Dict]) -> List[Dict]:
        """
        第三轮：质量筛选
        """
        print("\n" + "="*80)
        print("📋 第三轮：质量筛选")
        print("="*80)
        
        filtered = []
        quality_scores = []
        
        for item in data:
            score = self._evaluate_quality(item)
            item['quality_score'] = score
            quality_scores.append(score)
            
            # 阈值：7.0分以上
            if score >= 7.0:
                filtered.append(item)
        
        avg_score = sum(quality_scores) / len(quality_scores)
        
        print(f"\n质量评估:")
        print(f"  平均分: {avg_score:.2f}/10")
        print(f"  通过率: {len(filtered)}/{len(data)} ({len(filtered)/len(data)*100:.1f}%)")
        print(f"  拒绝: {len(data) - len(filtered)} 条低质量数据")
        
        self.filtering_history.append({
            'round': 3,
            'name': '质量筛选',
            'threshold': 7.0,
            'pass_rate': len(filtered)/len(data)
        })
        
        return filtered
    
    def _evaluate_quality(self, item: Dict) -> float:
        """评估数据质量"""
        score = 10.0
        
        # 长度检查
        input_len = len(item.get('input', ''))
        output_len = len(item.get('output', ''))
        
        if input_len < 10:
            score -= 2.0
        if output_len < 50:
            score -= 2.0
        
        # 完整性检查
        if not item.get('instruction'):
            score -= 1.0
        
        # 任务特定检查
        task = item.get('task_type')
        if task == 'code_generation':
            if 'def ' not in item.get('output', '') and 'class ' not in item.get('output', ''):
                score -= 1.5
        elif task == 'math_reasoning':
            if '=' not in item.get('output', ''):
                score -= 1.0
        
        return max(0, min(10, score))
    
    def discover_task_conflict_problem(self, data: List[Dict]):
        """
        发现新问题：任务冲突
        """
        print("\n" + "!"*80)
        print("❌ 新问题：任务之间存在冲突！")
        print("!"*80)
        
        conflicts = [
            {
                'conflict': '代码生成 vs 创意写作',
                'description': '代码要求严格格式，写作要求创造性',
                'manifestation': '模型在写作时也想输出代码块，或者代码缺少注释',
                'impact': '两种任务相互干扰，都学不好'
            },
            {
                'conflict': '问答 vs 头脑风暴',
                'description': '问答要求准确唯一答案，头脑风暴要求多个选项',
                'manifestation': '问答时给出多个答案（不确定），头脑风暴只给一个（太单一）',
                'impact': '模型在不同任务间产生混淆'
            },
            {
                'conflict': '翻译 vs 摘要',
                'description': '翻译要求完整保留信息，摘要要求压缩信息',
                'manifestation': '翻译时丢失细节，摘要时过于详细',
                'impact': '模型不清楚何时保留、何时删减'
            }
        ]
        
        for i, conflict in enumerate(conflicts, 1):
            print(f"\n冲突 {i}: {conflict['conflict']}")
            print(f"  描述: {conflict['description']}")
            print(f"  表现: {conflict['manifestation']}")
            print(f"  影响: {conflict['impact']}")
        
        print("\n💡 根本原因：")
        print("   不同任务对模型行为的要求是矛盾的")
        print("   在小数据集上，模型难以区分不同任务的上下文")
    
    def round4_resolve_conflicts(self, data: List[Dict]) -> List[Dict]:
        """
        第四轮：解决任务冲突
        """
        print("\n" + "="*80)
        print("📋 第四轮：解决任务冲突")
        print("="*80)
        
        print(f"\n解决方案:")
        
        # 方案1：强化任务提示
        print(f"\n1. 强化任务提示（在instruction中明确说明）")
        for item in data:
            task = item.get('task_type')
            if task == 'code_generation':
                item['instruction'] = '请编写代码实现以下功能。要求：代码规范、有注释、可运行。'
            elif task == 'creative_writing':
                item['instruction'] = '请发挥创造力，续写故事。要求：引人入胜、情节合理。'
            elif task == 'qa':
                item['instruction'] = '请准确回答问题。要求：答案唯一、有依据。'
            elif task == 'brainstorming':
                item['instruction'] = '请提供多个创意方案。要求：至少5个、多样化。'
        
        # 方案2：添加任务标签
        print(f"\n2. 添加明确的任务类型标签")
        for item in data:
            task = item.get('task_type', 'general')
            item['instruction'] = f"[任务类型: {task}] " + item.get('instruction', '')
        
        # 方案3：分组训练（模拟）
        print(f"\n3. 分组训练策略（训练时使用）")
        print(f"   - 第1-2 epoch: 所有任务混合")
        print(f"   - 第3 epoch: 按任务类型分批训练")
        print(f"   - 这样模型既能学会通用能力，又能区分任务")
        
        self.filtering_history.append({
            'round': 4,
            'name': '解决任务冲突',
            'solutions': ['强化提示', '任务标签', '分组训练']
        })
        
        return data
    
    def round5_final_validation(self, data: List[Dict]) -> List[Dict]:
        """
        第五轮：最终验证
        """
        print("\n" + "="*80)
        print("📋 第五轮：最终验证")
        print("="*80)
        
        # 验证任务分布
        task_counts = Counter(item.get('task_type') for item in data)
        print(f"\n最终任务分布:")
        for task, count in task_counts.most_common():
            print(f"  {task:20s}: {count} 条")
        
        # 验证质量分布
        quality_scores = [item.get('quality_score', 0) for item in data]
        avg_quality = sum(quality_scores) / len(quality_scores)
        print(f"\n平均质量: {avg_quality:.2f}/10")
        
        # 验证完整性
        complete_count = sum(1 for item in data 
                           if item.get('instruction') and 
                              item.get('input') and 
                              item.get('output'))
        print(f"完整性: {complete_count}/{len(data)} ({complete_count/len(data)*100:.1f}%)")
        
        # 保存最终数据
        output_path = 'multitask_filtered_final.json'
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ 最终数据已保存: {output_path}")
        
        self.filtering_history.append({
            'round': 5,
            'name': '最终验证',
            'total': len(data),
            'avg_quality': avg_quality
        })
        
        return data
    
    def generate_report(self):
        """生成筛选报告"""
        print("\n" + "="*80)
        print("📊 多任务数据筛选完整报告")
        print("="*80)
        
        for record in self.filtering_history:
            print(f"\n第{record['round']}轮: {record['name']}")
            for key, value in record.items():
                if key not in ['round', 'name']:
                    print(f"  {key}: {value}")
        
        print("\n💡 多任务SFT的关键经验:")
        print("  1. 任务平衡是第一要务")
        print("  2. 质量比数量重要，但也要保证每个任务的最小量")
        print("  3. 任务冲突需要通过提示工程和训练策略解决")
        print("  4. 持续监控各任务的表现，及时调整")


def main():
    """主函数"""
    print("="*80)
    print("🎯 多任务SFT数据筛选 - 真实场景演示")
    print("="*80)
    print("\n这展示了多任务学习的特殊挑战：")
    print("  - 任务分布不均衡")
    print("  - 任务之间存在冲突")
    print("  - 需要特殊的平衡策略")
    print("\n" + "="*80)
    input("\n按Enter键开始...")
    
    pipeline = MultiTaskDataFilteringPipeline('general_assistant_raw_data.json')
    final_data = pipeline.run_full_pipeline()
    
    print("\n" + "="*80)
    print("✅ 筛选流程完成！")
    print("="*80)


if __name__ == "__main__":
    main()

