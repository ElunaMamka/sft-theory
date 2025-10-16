# Part 2 演示代码说明

本目录包含第二部分（LoRA高效微调）的所有演示代码。

## 📁 文件列表

### 01_full_finetuning_problems.py
**功能**：展示全量微调的三大困境
- 计算巨大的内存需求
- 模拟灾难性遗忘过程
- 分析多任务的存储成本

**运行**：
```bash
python code/part2/01_full_finetuning_problems.py
```

**输出示例**：
- 7B模型需要~98GB内存
- 灾难性遗忘演示（能力下降曲线）
- 10个任务需要130GB存储

---

### 02_lora_mechanism.py
**功能**：LoRA工作机制详解
- 实现简化的LoRA层
- 展示矩阵分解过程
- 计算参数量对比

**运行**：
```bash
python code/part2/02_lora_mechanism.py
```

**关键概念**：
- 低秩分解：ΔW = B @ A
- 冻结原始权重
- 只训练极少参数

---

### 03_parameter_comparison.py
**功能**：详细的参数量对比分析
- 对比不同模型规模（7B/13B/30B/70B）
- 计算存储节省
- 生成可视化图表

**运行**：
```bash
python code/part2/03_parameter_comparison.py
```

**依赖**：
```bash
pip install matplotlib numpy
```

**生成文件**：
- `parameter_comparison.png` - 参数对比图表

---

### 04_lora_adapters_demo.py
**功能**：演示Hub-and-Spoke多任务架构
- 一个基座模型 + 多个LoRA适配器
- 快速任务切换
- 存储优势对比

**运行**：
```bash
python code/part2/04_lora_adapters_demo.py
```

**演示内容**：
- 创建6个不同任务的适配器
- 动态切换任务
- 对比传统方案和LoRA方案

---

## 🎯 学习路径

建议按照以下顺序学习：

1. **先运行 01** - 理解全量微调的问题
2. **再运行 02** - 学习LoRA如何解决这些问题
3. **然后运行 03** - 看具体的数字对比
4. **最后运行 04** - 理解实际应用架构

## 📊 核心数字（7B模型为例）

| 指标 | 全量微调 | LoRA (r=8) | 改进 |
|------|---------|-----------|------|
| 训练参数 | 7,000,000,000 | ~2,000,000 | 3500x 减少 |
| 内存需求 | ~98 GB | ~26 GB | 72 GB 节省 |
| 存储/任务 | 13 GB | 4 MB | 3250x 减少 |

## 💡 关键洞察

### 全量微调的困境
1. **计算开销大** - 需要高端GPU集群
2. **灾难性遗忘** - 可能丢失预训练知识
3. **存储困难** - 每个任务需要完整模型副本

### LoRA的优势
1. **参数效率** - 只训练0.03%的参数
2. **防止遗忘** - 原始权重冻结
3. **可组合** - 一个基座 + 多个适配器

## 🔗 相关资源

- 课程网页：http://localhost:5173/part2
- Part1代码：../part1/
- 完整文档：../README.md

## 🚀 快速验证

运行所有示例：
```bash
# 全量微调问题
python code/part2/01_full_finetuning_problems.py

# LoRA机制
python code/part2/02_lora_mechanism.py

# 参数对比
python code/part2/03_parameter_comparison.py

# 多任务演示
python code/part2/04_lora_adapters_demo.py
```

## 📈 可视化输出

运行后会生成：
- `parameter_comparison.png` - 参数量对比柱状图和饼图
- 终端输出的详细统计表格
- 内存使用分解图

## ❓ 常见问题

**Q: 为什么LoRA参数这么少还有效？**  
A: 研究发现，微调时的权重更新矩阵通常是低秩的。LoRA利用这一特性，用两个小矩阵的乘积来近似完整的更新矩阵。

**Q: rank应该设置为多少？**  
A: 常见值：4, 8, 16, 32。更大的rank提供更多表达能力，但参数也更多。实践中r=8或16通常效果很好。

**Q: 可以同时使用多个LoRA适配器吗？**  
A: 是的！这正是LoRA的强大之处。可以合并多个适配器，或者动态切换。

