"""
演示代码：参数量详细对比
文件位置：code/part2/03_parameter_comparison.py

用具体数字展示不同模型规模下，LoRA vs 全量微调的参数差异
"""

import matplotlib.pyplot as plt
import numpy as np


class ParameterComparison:
    """参数量对比分析器"""
    
    def __init__(self):
        # 常见模型规模
        self.model_sizes = {
            '7B': 7_000_000_000,
            '13B': 13_000_000_000,
            '30B': 30_000_000_000,
            '70B': 70_000_000_000
        }
        
        # LoRA配置
        self.lora_config = {
            'rank': 8,  # LoRA秩
            'alpha': 16,
            'num_layers': 32,  # 应用LoRA的层数
            'dim': 4096  # 隐藏层维度
        }
    
    def calculate_lora_params(self, model_size_name: str) -> dict:
        """
        计算LoRA参数量
        
        Args:
            model_size_name: 模型规模名称（如 '7B'）
            
        Returns:
            参数统计字典
        """
        total_params = self.model_sizes[model_size_name]
        
        # 每层LoRA参数：(d * r) + (r * d) = 2 * d * r
        params_per_layer = 2 * self.lora_config['dim'] * self.lora_config['rank']
        
        # 总LoRA参数
        total_lora_params = params_per_layer * self.lora_config['num_layers']
        
        # 计算比例
        ratio = (total_lora_params / total_params) * 100
        
        return {
            '模型总参数': total_params,
            'LoRA参数': total_lora_params,
            '训练参数比例': ratio,
            '每层参数': params_per_layer,
            '应用层数': self.lora_config['num_layers']
        }
    
    def print_detailed_comparison(self):
        """打印详细对比"""
        print("="*80)
        print("📊 全量微调 vs LoRA - 参数量详细对比")
        print("="*80)
        
        print(f"\n🔧 LoRA配置：")
        print(f"  • 秩 (rank): {self.lora_config['rank']}")
        print(f"  • Alpha: {self.lora_config['alpha']}")
        print(f"  • 应用层数: {self.lora_config['num_layers']}")
        print(f"  • 隐藏维度: {self.lora_config['dim']}")
        
        print(f"\n{'='*80}")
        print(f"{'模型规模':<12} {'全量微调参数':<20} {'LoRA参数':<20} {'训练比例':<15} {'减少倍数':<10}")
        print(f"{'='*80}")
        
        for model_name in self.model_sizes.keys():
            stats = self.calculate_lora_params(model_name)
            
            full_params = stats['模型总参数']
            lora_params = stats['LoRA参数']
            ratio = stats['训练参数比例']
            reduction = full_params / lora_params
            
            print(f"{model_name:<12} {full_params:<20,} {lora_params:<20,} {ratio:<14.3f}% {reduction:<10.1f}x")
        
        print(f"{'='*80}")
    
    def calculate_storage_savings(self):
        """计算存储节省"""
        print(f"\n{'='*80}")
        print("💾 存储空间对比（10个不同任务）")
        print(f"{'='*80}")
        
        num_tasks = 10
        
        print(f"\n{'模型规模':<12} {'全量微调存储':<20} {'LoRA存储':<20} {'节省空间':<15}")
        print(f"{'-'*80}")
        
        for model_name in self.model_sizes.keys():
            stats = self.calculate_lora_params(model_name)
            
            # FP16: 2 bytes per parameter
            full_storage_gb = (stats['模型总参数'] * 2 * num_tasks) / (1024**3)
            lora_storage_mb = (stats['LoRA参数'] * 2 * num_tasks) / (1024**2)
            
            savings = full_storage_gb / (lora_storage_mb / 1024)
            
            print(f"{model_name:<12} {full_storage_gb:>15.1f} GB    {lora_storage_mb:>15.1f} MB    {savings:>10.1f}x")
    
    def visualize_comparison(self, model_name: str = '7B'):
        """可视化参数对比"""
        try:
            stats = self.calculate_lora_params(model_name)
            
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
            
            # 左图：参数量对比（对数尺度）
            categories = ['全量微调', 'LoRA']
            params = [stats['模型总参数'], stats['LoRA参数']]
            colors = ['#ef4444', '#10b981']
            
            bars1 = ax1.bar(categories, params, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
            ax1.set_yscale('log')
            ax1.set_ylabel('参数量（对数尺度）', fontsize=12, fontweight='bold')
            ax1.set_title(f'{model_name}模型参数量对比', fontsize=14, fontweight='bold')
            ax1.grid(axis='y', alpha=0.3, linestyle='--')
            
            # 添加数值标签
            for i, (bar, value) in enumerate(zip(bars1, params)):
                height = bar.get_height()
                label = f'{value:,.0f}\n({value/1e9:.1f}B)' if i == 0 else f'{value:,.0f}\n({value/1e6:.1f}M)'
                ax1.text(bar.get_x() + bar.get_width()/2., height,
                        label, ha='center', va='bottom', fontsize=10, fontweight='bold')
            
            # 右图：参数占比饼图
            sizes = [stats['模型总参数'] - stats['LoRA参数'], stats['LoRA参数']]
            labels = [
                f'冻结参数\n{(sizes[0]/1e9):.2f}B\n({sizes[0]/stats["模型总参数"]*100:.2f}%)',
                f'LoRA参数\n{(sizes[1]/1e6):.2f}M\n({sizes[1]/stats["模型总参数"]*100:.3f}%)'
            ]
            colors_pie = ['#94a3b8', '#10b981']
            explode = (0, 0.1)  # 突出LoRA部分
            
            wedges, texts, autotexts = ax2.pie(sizes, labels=labels, colors=colors_pie,
                                                autopct='', explode=explode,
                                                shadow=True, startangle=90,
                                                textprops={'fontsize': 11, 'fontweight': 'bold'})
            
            ax2.set_title(f'{model_name}模型参数分布', fontsize=14, fontweight='bold')
            
            plt.tight_layout()
            plt.savefig('code/part2/parameter_comparison.png', dpi=150, bbox_inches='tight')
            print(f"\n📊 可视化图表已保存: code/part2/parameter_comparison.png")
            plt.show()
            
        except ImportError:
            print("\n⚠️  matplotlib未安装，跳过可视化")
            print("   安装命令: pip install matplotlib")
    
    def show_memory_breakdown(self, model_name: str = '7B'):
        """展示内存使用详细分解"""
        print(f"\n{'='*80}")
        print(f"💻 {model_name}模型训练内存需求分解")
        print(f"{'='*80}")
        
        stats = self.calculate_lora_params(model_name)
        total_params = stats['模型总参数']
        lora_params = stats['LoRA参数']
        
        print(f"\n【全量微调】")
        print(f"-"*80)
        
        # FP32 训练
        model_memory_fp32 = (total_params * 4) / (1024**3)
        optimizer_memory = model_memory_fp32 * 2  # Adam states
        gradients_memory = model_memory_fp32
        activations_memory = model_memory_fp32 * 0.5
        
        total_full_ft = model_memory_fp32 + optimizer_memory + gradients_memory + activations_memory
        
        print(f"  模型参数（FP32）:    {model_memory_fp32:>10.2f} GB")
        print(f"  优化器状态（Adam）:  {optimizer_memory:>10.2f} GB")
        print(f"  梯度:               {gradients_memory:>10.2f} GB")
        print(f"  激活值（估算）:      {activations_memory:>10.2f} GB")
        print(f"  {'-'*50}")
        print(f"  总计:               {total_full_ft:>10.2f} GB")
        
        print(f"\n【LoRA微调】")
        print(f"-"*80)
        
        # 基座模型（FP16，冻结）
        base_model_fp16 = (total_params * 2) / (1024**3)
        # LoRA参数（FP32，训练）
        lora_memory_fp32 = (lora_params * 4) / (1024**3)
        lora_optimizer = lora_memory_fp32 * 2
        lora_gradients = lora_memory_fp32
        lora_activations = activations_memory  # 激活值相同
        
        total_lora = base_model_fp16 + lora_memory_fp32 + lora_optimizer + lora_gradients + lora_activations
        
        print(f"  基座模型（FP16，冻结）: {base_model_fp16:>10.2f} GB")
        print(f"  LoRA参数（FP32）:       {lora_memory_fp32:>10.2f} GB")
        print(f"  优化器状态（Adam）:     {lora_optimizer:>10.2f} GB")
        print(f"  梯度:                  {lora_gradients:>10.2f} GB")
        print(f"  激活值（估算）:         {lora_activations:>10.2f} GB")
        print(f"  {'-'*50}")
        print(f"  总计:                  {total_lora:>10.2f} GB")
        
        print(f"\n{'='*80}")
        print(f"💡 内存节省: {total_full_ft - total_lora:.2f} GB ({(total_full_ft - total_lora)/total_full_ft*100:.1f}%)")
        print(f"{'='*80}")
        
        # GPU建议
        print(f"\n🖥️  GPU建议:")
        if total_lora <= 24:
            print(f"  LoRA: 单张RTX 3090/4090 (24GB) 即可训练")
        elif total_lora <= 40:
            print(f"  LoRA: 单张A100 (40GB) 可以训练")
        else:
            print(f"  LoRA: 需要A100 (80GB) 或多卡")
        
        if total_full_ft <= 80:
            print(f"  全量微调: 至少需要A100 (80GB)")
        else:
            print(f"  全量微调: 需要多张A100 (80GB)")


def main():
    """主函数"""
    comparator = ParameterComparison()
    
    # 详细对比
    comparator.print_detailed_comparison()
    
    # 存储节省
    comparator.calculate_storage_savings()
    
    # 内存分解（以7B为例）
    comparator.show_memory_breakdown('7B')
    
    # 可视化对比
    print("\n" + "="*80)
    comparator.visualize_comparison('7B')
    
    print("\n📁 代码位置: code/part2/03_parameter_comparison.py")
    print("\n💡 提示：修改 model_name 参数可以查看不同模型规模的对比")


if __name__ == "__main__":
    main()

