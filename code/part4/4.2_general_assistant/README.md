# 4.2 通用SFT实践：多任务对话助手

## 📋 项目概述

这是一个**真实的、完整的**多任务SFT项目，展示了比单任务更复杂的挑战：
- ✅ **真实的多任务数据平衡过程**（不只是数量平衡，还有质量、难度、冲突解决）
- ✅ **真实的任务串扰问题**（翻译变问答、代码变头脑风暴等典型问题）
- ✅ **真实的调试修复流程**（从v0.1性能不均到v1.1均衡优秀）
- ✅ **完整的迭代记录**（15天开发过程，展示多任务的独特挑战）

> 💡 **多任务SFT ≠ 简单地混合数据！需要精心的平衡策略和冲突解决方案。**

## 🎯 项目目标

- **多任务能力**：一个模型处理10+种任务
- **指令遵循**：准确理解并执行用户指令
- **任务边界清晰**：不同任务不互相干扰
- **保持通用能力**：避免灾难性遗忘

## 📊 数据特点

- **任务多样性**：涵盖10+种任务类型
- **数据量大**：5000+条高质量数据
- **真实场景**：来自实际用户需求
- **长对话**：支持多轮对话场景

## 🔥 与垂直领域SFT的区别

| 维度 | 垂直领域（中医） | 通用助手 |
|------|----------------|---------|
| 数据范围 | 单一领域 | 多领域 |
| 数据量 | 少（几百条） | 多（几千条） |
| 训练策略 | LoRA微调 | LoRA或全参数 |
| 专业深度 | 很深 | 较浅 |
| 泛化能力 | 弱 | 强 |

## 🚀 快速开始

### 方式1：一键运行（推荐初学者）

```bash
bash run_full_pipeline.sh
```

### 方式2：体验多任务SFT的真实挑战（强烈推荐）

#### 第一步：了解多任务数据筛选

```bash
# 运行多任务数据筛选演示
python data/data_filtering_multitask.py
```

这个脚本会展示：
- ✅ 第1轮：任务分类和统计
- ❌ 发现问题：任务分布严重不均（最多600条 vs 最少50条）
- ✅ 第2轮：任务平衡（上采样+下采样）
- ✅ 第3轮：质量筛选
- ❌ 新问题：任务冲突（代码 vs 创意、问答 vs 头脑风暴）
- ✅ 第4轮：解决任务冲突
- ✅ 第5轮：最终验证

#### 第二步：训练初始模型

```bash
# 1. 准备数据
python data/raw_examples.py
python data/prepare_dataset.py

# 2. 训练模型
python training/train_lora.py
```

#### 第三步：诊断多任务特有问题

```bash
# 运行多任务问题诊断工具
python training/multitask_problems_diagnosis.py
```

这个脚本会诊断5大多任务特有问题：
1. ❌ 任务性能严重不均（翻译38% vs 问答85%）
2. ❌ 任务串扰（翻译变问答、代码变头脑风暴）
3. ❌ 输出格式混乱（代码混入Markdown）
4. ❌ 遗忘基础能力（过度任务化）
5. ❌ 过拟合高频任务

并提供详细的解决方案！

#### 第四步：查看完整迭代记录

```bash
# 阅读15天开发日志
cat MULTITASK_ITERATION_LOG.md
```

了解多任务SFT的完整挑战：
- v0.1：任务性能不均（翻译38%，问答85%）
- v0.2：任务串扰加剧（平衡后反而更乱）
- v0.3：边界强化（任务标签+约束）
- v1.0：分阶段训练（混合→分组→困难任务）
- v1.1：效果优秀（平均85%，最差76%）

### 方式3：标准流程（已经理解多任务挑战）

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 准备数据
python data/raw_examples.py
python data/prepare_dataset.py

# 3. 训练模型
python training/train_lora.py

# 4. 测试模型
python inference/test_model.py

# 5. 交互式演示
python inference/interactive_demo.py
```

## 📁 项目结构

```
4.2_general_assistant/
├── data/                  # 数据准备
│   ├── raw_examples.py              # 多任务数据示例
│   ├── prepare_dataset.py           # 数据预处理
│   ├── dataset_analysis.py          # 数据分析
│   └── data_filtering_multitask.py  # 🔥 多任务数据筛选
│
├── model/                 # 模型配置
│   ├── model_config.py        # 模型参数配置
│   └── model_utils.py         # 模型工具函数
│
├── training/              # 训练脚本
│   ├── train_lora.py                  # LoRA微调
│   ├── train_full.py                  # 全参数微调
│   ├── train_distributed.py           # 分布式训练
│   ├── training_config.yaml           # 训练配置
│   └── multitask_problems_diagnosis.py # 🔥 多任务问题诊断
│
├── inference/             # 推理测试
│   ├── test_model.py          # 模型测试
│   └── interactive_demo.py    # 交互式演示
│
├── MULTITASK_ITERATION_LOG.md  # 🔥 15天迭代记录
├── run_full_pipeline.sh        # 一键运行
└── README.md                   # 本文档
```

### 🔥 核心亮点文件

| 文件 | 作用 | 多任务特色 |
|------|------|-----------|
| `data/data_filtering_multitask.py` | 多任务数据平衡 | 不只是数量平衡，还要解决任务冲突 |
| `training/multitask_problems_diagnosis.py` | 诊断特有问题 | 任务串扰、性能不均等多任务特有问题 |
| `MULTITASK_ITERATION_LOG.md` | 15天开发日志 | 对比单任务，展示多任务的独特挑战 |
```

## 💡 关键技术点

1. **多任务数据构建**：如何平衡不同任务的数据
2. **通用指令格式**：统一的prompt模板
3. **数据增强**：扩展数据多样性
4. **负采样**：提升模型鲁棒性

## 📈 预期效果

- **基座模型**：只会续写，不会遵循指令
- **SFT后**：能准确理解指令，完成各类任务
- **训练时间**：单卡V100约12-16小时（5000条数据）
- **任务成功率**：>90%

## 🆚 LoRA vs 全参数微调

| 方法 | 训练参数 | 显存需求 | 训练时间 | 效果 |
|------|---------|---------|---------|------|
| LoRA | 0.1% | 8GB | 12h | ⭐⭐⭐⭐ |
| 全参数 | 100% | 56GB+ | 16h | ⭐⭐⭐⭐⭐ |

**建议**：
- 数据<2000条 → LoRA
- 数据>5000条 → 全参数（如果资源充足）
- 多任务场景 → 建议全参数

