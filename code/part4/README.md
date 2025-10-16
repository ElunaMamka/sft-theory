# Part4: SFT实践工作流

## 📋 概述

本部分包含两个完整的SFT实践项目，涵盖从数据准备到模型部署的全流程。

## 🎯 两个实践项目

### 4.1 垂直领域SFT：中医问诊助手
- **目标**：将通用模型微调为专业的中医问诊助手
- **数据**：真实的中医问诊对话（4条高质量长数据）
- **方法**：LoRA高效微调
- **难度**：⭐⭐⭐
- **适合场景**：
  - 数据量少（<1000条）
  - 需要深度领域知识
  - 资源有限（单卡即可）

### 4.2 通用SFT：多任务对话助手
- **目标**：构建能处理多种任务的通用助手
- **数据**：10+种任务类型（问答、代码、推理等）
- **方法**：LoRA或全参数微调
- **难度**：⭐⭐⭐⭐
- **适合场景**：
  - 数据量大（>2000条）
  - 需要广泛能力
  - 资源充足（多卡更佳）

## 📊 项目对比

| 维度 | 4.1 垂直领域（中医） | 4.2 通用助手 |
|------|-------------------|------------|
| **数据范围** | 单一领域 | 多领域 |
| **数据量** | 小（示例4条） | 大（示例10条×多任务） |
| **专业深度** | 很深 | 较浅 |
| **泛化能力** | 弱 | 强 |
| **训练方法** | LoRA | LoRA/全参数 |
| **显存需求** | 8GB | 8GB（LoRA）/56GB（全参数） |
| **训练时间** | 2-3小时 | 12-16小时 |
| **应用场景** | 专业咨询 | 通用对话 |

## 🚀 快速开始

### 方式1：运行单个项目

```bash
# 4.1 中医问诊助手
cd 4.1_vertical_domain_tcm
bash run_full_pipeline.sh

# 4.2 通用对话助手  
cd 4.2_general_assistant
bash run_full_pipeline.sh
```

### 方式2：逐步运行

```bash
# 以4.1为例
cd 4.1_vertical_domain_tcm

# 1. 安装依赖
pip install -r requirements.txt

# 2. 准备数据
cd data
python raw_examples.py
python prepare_dataset.py
cd ..

# 3. 训练模型
cd training
python train_lora.py
cd ..

# 4. 测试模型
cd inference
python test_model.py
python interactive_demo.py
```

## 📁 统一的项目结构

两个项目采用相同的结构设计：

```
project/
├── README.md              # 项目说明
├── requirements.txt       # 依赖包
├── data/                  # 数据目录
│   ├── raw_examples.py    # 原始数据（真实长数据）
│   ├── prepare_dataset.py # 数据预处理
│   └── dataset_analysis.py # 数据分析
├── model/                 # 模型配置
│   ├── model_config.py    # 配置参数
│   └── model_utils.py     # 工具函数
├── training/              # 训练脚本
│   ├── train_lora.py      # LoRA训练
│   ├── train_full.py      # 全参数训练（仅4.2）
│   ├── train_distributed.py # 分布式训练
│   └── training_config.yaml # 训练配置
├── inference/             # 推理脚本
│   ├── test_model.py      # 测试脚本
│   └── interactive_demo.py # 交互演示
└── run_full_pipeline.sh   # 一键运行脚本
```

## 💡 学习路径建议

### 初学者
1. 先运行4.1（中医问诊）
   - 数据少，训练快
   - 效果明显，容易理解
   - 单卡即可运行

2. 理解核心概念
   - 数据格式（instruction-input-output）
   - LoRA原理
   - 训练流程

3. 尝试修改
   - 改变训练参数
   - 添加自己的数据
   - 测试不同配置

### 进阶者
1. 运行4.2（通用助手）
   - 理解多任务学习
   - 尝试全参数微调
   - 实验分布式训练

2. 对比实验
   - LoRA vs 全参数
   - 不同rank的影响
   - 数据量的影响

3. 扩展项目
   - 添加更多任务类型
   - 实现持续学习
   - 部署为API服务

## 🎓 关键知识点

### 1. 数据质量 > 数据量
- 4.1用4条高质量数据就能见效
- 关键是数据要完整、真实、有代表性

### 2. 领域适配的权衡
- 垂直领域：深度 vs 广度
- 通用助手：广度 vs 深度

### 3. 训练策略选择
- 数据<1000：LoRA
- 数据>2000：考虑全参数
- 多任务：倾向全参数

### 4. 评估很重要
- 不仅看loss，还要实际测试
- 对比基座模型和微调模型
- 多场景测试

## ⚙️ 技术细节

### LoRA配置
```python
r=8              # rank，控制参数量
lora_alpha=16    # 缩放因子
lora_dropout=0.05 # dropout概率
```

### 训练配置
```python
learning_rate=2e-4        # LoRA推荐学习率
batch_size=16             # 有效batch size
num_epochs=3              # 训练轮数
warmup_ratio=0.03         # warmup比例
```

### 推理配置
```python
temperature=0.7           # 控制随机性
top_p=0.9                # nucleus sampling
max_new_tokens=1024      # 最大生成长度
```

## 🔧 常见问题

### Q1: 显存不足怎么办？
- 启用4-bit量化
- 减小batch size
- 增大gradient accumulation
- 使用DeepSpeed ZeRO

### Q2: 训练很慢怎么办？
- 启用bf16/fp16混合精度
- 使用多GPU
- 减小序列长度
- 使用Flash Attention

### Q3: 效果不好怎么办？
- 检查数据质量
- 增加训练数据
- 调整学习率
- 增加训练轮数
- 尝试全参数微调

### Q4: 如何评估模型？
- 定量指标：loss、perplexity
- 定性评估：人工测试
- 对比测试：vs基座模型
- 多场景测试

## 📚 参考资料

- [LoRA论文](https://arxiv.org/abs/2106.09685)
- [Alpaca项目](https://github.com/tatsu-lab/stanford_alpaca)
- [DeepSpeed文档](https://www.deepspeed.ai/)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers)

## 🎉 完成后你将掌握

✅ 完整的SFT流程（数据→训练→评估→部署）
✅ LoRA高效微调技术
✅ 分布式训练方法
✅ 数据工程最佳实践
✅ 模型评估和调优技巧

祝学习愉快！🚀

