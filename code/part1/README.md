# Part 1 演示代码说明

本目录包含第一部分（预训练 vs SFT）的所有演示代码。

## 📁 文件列表

### 01_pretraining_simulation.py
**功能**：模拟预训练过程
- 演示如何加载海量文本数据
- 实现简化的"预测下一个词"任务
- 展示损失函数的计算
- 模拟参数更新过程

**运行**：
```bash
python code/part1/01_pretraining_simulation.py
```

**关键概念**：
- 自监督学习
- 因果语言建模（CLM）
- 训练循环

---

### 02_sft_vs_pretraining.py
**功能**：对比预训练模型和SFT模型的表现
- 创建两个模型类（基座模型 vs SFT模型）
- 在相同输入下对比输出
- 直观展示SFT的价值

**运行**：
```bash
python code/part1/02_sft_vs_pretraining.py
```

**关键概念**：
- 指令遵循能力
- 基座模型的局限性
- SFT的行为塑造作用

---

### 03_data_scale_comparison.py
**功能**：数据规模对比分析
- 量化预训练和SFT的数据差异
- 生成可视化图表
- 形象类比说明规模差异

**运行**：
```bash
python code/part1/03_data_scale_comparison.py
```

**依赖**：
```bash
pip install matplotlib numpy
```

**关键概念**：
- 数据规模差异（百万倍）
- 质量 vs 数量
- 数据的不同作用

---

## 🚀 快速开始

### 1. 安装依赖
```bash
cd /path/to/sft-theory
pip install -r code/requirements.txt
```

### 2. 运行所有演示
```bash
# 预训练模拟
python code/part1/01_pretraining_simulation.py

# 模型对比
python code/part1/02_sft_vs_pretraining.py

# 数据规模分析
python code/part1/03_data_scale_comparison.py
```

## 📚 学习路径

建议按照以下顺序学习：

1. **先运行 01** - 理解预训练的基本流程
2. **再运行 02** - 对比两种模型的差异
3. **最后运行 03** - 量化理解数据规模

## 💡 代码特点

✅ **简洁易懂** - 避免复杂实现，专注核心概念  
✅ **可独立运行** - 每个文件都是完整的演示  
✅ **详细注释** - 每个函数都有说明文档  
✅ **输出友好** - 清晰的打印信息和可视化  

## 🔗 相关资源

- 课程网页：http://localhost:5173/part1
- 完整文档：../README.md
- 更多代码：../part2/, ../part3/, ../part4/

## ❓ 常见问题

**Q: 为什么代码是"简化"的？**  
A: 真实的预训练和SFT代码非常复杂，涉及分布式训练、混合精度等高级技术。这里的代码旨在展示核心概念，而非生产级实现。

**Q: 可以修改代码吗？**  
A: 当然！鼓励您修改参数、添加功能，通过实验加深理解。

**Q: 如何查看更多细节？**  
A: 每个Python文件都包含详细的注释和文档字符串。使用 `help(类名)` 可以查看说明。

