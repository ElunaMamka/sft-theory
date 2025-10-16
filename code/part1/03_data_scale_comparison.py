"""
演示代码：数据规模对比可视化
文件位置：code/part1/03_data_scale_comparison.py

用数字和可视化方式展示预训练和SFT的数据规模差异
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, Tuple


class DataScaleAnalyzer:
    """数据规模分析器"""
    
    def __init__(self):
        # 预训练数据规模（示例）
        self.pretraining_data = {
            "tokens": 1_000_000_000_000,  # 1万亿tokens
            "equivalent_books": 5_000_000,  # 相当于500万本书
            "storage_tb": 5_000,  # 约5TB
            "collection_months": 6  # 收集时间：6个月
        }
        
        # SFT数据规模（示例）
        self.sft_data = {
            "samples": 10_000,  # 1万个样本
            "avg_tokens_per_sample": 500,
            "total_tokens": 5_000_000,  # 500万tokens
            "storage_mb": 50,  # 约50MB
            "annotation_days": 30  # 标注时间：30天
        }
    
    def print_comparison(self):
        """打印详细对比"""
        print("="* 80)
        print("📊 预训练 vs SFT 数据规模对比")
        print("="* 80)
        
        print("\n📚 预训练数据规模:")
        print(f"  - 总tokens数: {self.pretraining_data['tokens']:,}")
        print(f"  - 相当于书籍: {self.pretraining_data['equivalent_books']:,} 本")
        print(f"  - 存储空间: {self.pretraining_data['storage_tb']:,} TB")
        print(f"  - 收集时间: {self.pretraining_data['collection_months']} 个月")
        
        print("\n📝 SFT数据规模:")
        print(f"  - 样本数量: {self.sft_data['samples']:,} 个")
        print(f"  - 总tokens数: {self.sft_data['total_tokens']:,}")
        print(f"  - 存储空间: {self.sft_data['storage_mb']} MB")
        print(f"  - 标注时间: {self.sft_data['annotation_days']} 天")
        
        # 计算倍数差异
        token_ratio = self.pretraining_data['tokens'] / self.sft_data['total_tokens']
        storage_ratio = (self.pretraining_data['storage_tb'] * 1024) / self.sft_data['storage_mb']
        
        print("\n📈 规模差异:")
        print(f"  - Tokens数量差异: {token_ratio:,.0f} 倍")
        print(f"  - 存储空间差异: {storage_ratio:,.0f} 倍")
        
        print("\n💡 关键洞察:")
        print("  1. 预训练数据规模是SFT的数十万倍")
        print("  2. 但SFT对模型行为的影响同样关键")
        print("  3. SFT更强调数据质量而非数量")
        print("  4. 小而精的SFT数据可以带来巨大改变")
    
    def visualize_comparison(self):
        """可视化对比（需要matplotlib）"""
        try:
            fig, axes = plt.subplots(1, 2, figsize=(14, 6))
            
            # 左图：Token数量对比（对数尺度）
            ax1 = axes[0]
            categories = ['预训练', 'SFT']
            tokens = [
                self.pretraining_data['tokens'],
                self.sft_data['total_tokens']
            ]
            
            colors = ['#3b82f6', '#a855f7']
            bars1 = ax1.bar(categories, tokens, color=colors, alpha=0.7)
            ax1.set_yscale('log')
            ax1.set_ylabel('Tokens数量 (对数尺度)', fontsize=12)
            ax1.set_title('数据规模对比 - Tokens', fontsize=14, fontweight='bold')
            ax1.grid(axis='y', alpha=0.3)
            
            # 添加数值标签
            for bar, value in zip(bars1, tokens):
                height = bar.get_height()
                ax1.text(bar.get_x() + bar.get_width()/2., height,
                        f'{value:,.0f}',
                        ha='center', va='bottom', fontsize=10)
            
            # 右图：存储空间对比
            ax2 = axes[1]
            storage = [
                self.pretraining_data['storage_tb'],
                self.sft_data['storage_mb'] / 1024  # 转换为TB
            ]
            
            bars2 = ax2.bar(categories, storage, color=colors, alpha=0.7)
            ax2.set_ylabel('存储空间 (TB)', fontsize=12)
            ax2.set_title('数据规模对比 - 存储', fontsize=14, fontweight='bold')
            ax2.grid(axis='y', alpha=0.3)
            
            # 添加数值标签
            for i, (bar, value) in enumerate(zip(bars2, storage)):
                height = bar.get_height()
                label = f'{value:.0f} TB' if i == 0 else f'{value*1024:.0f} MB'
                ax2.text(bar.get_x() + bar.get_width()/2., height,
                        label,
                        ha='center', va='bottom', fontsize=10)
            
            plt.tight_layout()
            plt.savefig('code/part1/data_scale_comparison.png', dpi=150, bbox_inches='tight')
            print("\n📊 图表已保存: code/part1/data_scale_comparison.png")
            plt.show()
            
        except ImportError:
            print("\n⚠️  matplotlib未安装，跳过可视化")
            print("   安装命令: pip install matplotlib")
    
    def show_analogy(self):
        """用形象类比说明规模差异"""
        print("\n" + "="* 80)
        print("🎨 形象类比：帮助理解规模差异")
        print("="* 80)
        
        print("\n📚 如果把预训练数据比作：")
        print("  → 一个巨大的图书馆（500万本书）")
        print("  → 需要一个人不吃不喝读1000年才能读完")
        
        print("\n📝 那么SFT数据就像：")
        print("  → 一本精选的教科书（1万个精心编写的例题）")
        print("  → 一个人几天就能学完")
        
        print("\n💡 关键启示：")
        print("  ✓ 预训练：广泛阅读，打好基础")
        print("  ✓ SFT：精准学习，掌握技能")
        print("  ✓ 两者缺一不可，相辅相成")


def main():
    """主函数"""
    analyzer = DataScaleAnalyzer()
    
    # 打印详细对比
    analyzer.print_comparison()
    
    # 显示类比
    analyzer.show_analogy()
    
    # 可视化对比
    print("\n" + "="* 80)
    analyzer.visualize_comparison()
    
    print("\n📁 代码位置: code/part1/03_data_scale_comparison.py")


if __name__ == "__main__":
    main()

