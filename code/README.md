# 📚 SFT原理课程 - 演示代码总览

本目录包含课程所有部分的可运行演示代码。每个代码文件都对应课程中的一个概念，可以独立运行。

## 📁 目录结构

```
code/
├── part1/           # 第一部分：预训练 vs SFT
│   ├── 01_pretraining_simulation.py
│   ├── 02_sft_vs_pretraining.py
│   ├── 03_data_scale_comparison.py
│   └── README.md
│
├── part2/           # 第二部分：LoRA高效微调
│   ├── 01_full_finetuning_demo.py
│   ├── 02_lora_mechanism.py
│   ├── 03_lora_vs_full_comparison.py
│   └── README.md
│
├── part3/           # 第三部分：SFT数据集
│   ├── 01_dataset_format.py
│   ├── 02_data_quality_checker.py
│   ├── 03_dataset_builder.py
│   └── README.md
│
├── part4/           # 第四部分：SFT实践工作流
│   ├── 01_workflow_step1_select_model.py
│   ├── 02_workflow_step2_prepare_data.py
│   ├── 03_workflow_step3_training.py
│   ├── 04_workflow_step4_evaluation.py
│   └── README.md
│
└── requirements.txt # 所有依赖
```

## 🚀 快速开始

### 1. 安装依赖

```bash
cd /path/to/sft-theory
pip install -r code/requirements.txt
```

### 2. 运行演示代码

```bash
# Part 1 - 预训练模拟
python code/part1/01_pretraining_simulation.py

# Part 2 - LoRA机制演示
python code/part2/02_lora_mechanism.py

# Part 3 - 数据集构建
python code/part3/03_dataset_builder.py

# Part 4 - 完整工作流
python code/part4/01_workflow_step1_select_model.py
```

## 📖 代码特点

### ✅ 教学导向
- 简化实现，聚焦核心概念
- 避免复杂的工程细节
- 代码注释详细，易于理解

### ✅ 可独立运行
- 每个文件都是完整的程序
- 无需复杂的环境配置
- 输出清晰友好

### ✅ 实践性强
- 模拟真实的训练场景
- 可修改参数观察效果
- 包含可视化输出

## 💡 学习路径

### 初学者路径
1. 先浏览课程网页（http://localhost:5173）
2. 了解概念后，运行对应的代码
3. 修改参数，观察输出变化
4. 阅读代码注释，深入理解

### 进阶路径
1. 直接运行代码，观察输出
2. 阅读代码实现
3. 参考课程网页理解理论
4. 尝试扩展代码功能

## 🔗 代码与课程对应关系

| 课程部分 | 网页路径 | 代码目录 | 核心文件 |
|---------|---------|---------|---------|
| 预训练 vs SFT | /part1 | code/part1/ | 01_pretraining_simulation.py |
| LoRA高效微调 | /part2 | code/part2/ | 02_lora_mechanism.py |
| SFT数据集 | /part3 | code/part3/ | 01_dataset_format.py |
| 实践工作流 | /part4 | code/part4/ | 03_workflow_step3_training.py |

## 📊 可视化输出

部分代码会生成可视化图表，保存位置：
- `code/part1/data_scale_comparison.png` - 数据规模对比
- `code/part2/lora_parameter_comparison.png` - 参数量对比
- `code/part3/data_quality_distribution.png` - 数据质量分布
- `code/part4/training_curve.png` - 训练曲线

## ⚙️ 依赖说明

### 必需依赖
- `numpy` - 数值计算
- `matplotlib` - 数据可视化

### 可选依赖（高级示例）
- `transformers` - HuggingFace库
- `torch` - PyTorch深度学习框架
- `datasets` - HuggingFace数据集库

## 🎯 代码设计原则

1. **简洁性** - 用最少的代码展示核心概念
2. **可读性** - 清晰的命名和详细的注释
3. **教育性** - 优先考虑教学效果
4. **实用性** - 展示真实场景的简化版本

## 💻 如何在课程网页中查看代码

课程网页中所有代码块都会显示：
- 📁 文件路径（如：`code/part1/01_example.py`）
- 🏷️ 编程语言标签
- 📋 一键复制按钮
- ▶️ 可运行标识
- 💡 代码说明

示例：
![代码展示](../docs/code-display-example.png)

## 🐛 故障排除

### 问题：import错误
**解决**：确保已安装依赖
```bash
pip install -r code/requirements.txt
```

### 问题：matplotlib显示问题
**解决**：安装图形界面支持
```bash
# macOS
brew install python-tk

# Ubuntu
sudo apt-get install python3-tk
```

### 问题：代码运行慢
**解决**：这是正常的，演示代码优先考虑可读性而非性能

## 📚 进一步学习

- 课程完整文档：`../README.md`
- 使用指南：`../使用指南.md`
- API文档：`../backend/README.md`

## 🤝 贡献

欢迎：
- 报告代码bug
- 建议改进
- 提交新的演示代码
- 改善注释和文档

## 📄 许可

本代码仅用于教育目的。

