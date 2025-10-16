# 🚀 快速启动指南

## 一键启动

```bash
cd sft-theory
./start.sh
```

然后访问：**http://localhost:5173**

## 手动启动

### 后端（终端1）
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python server.py
```

### 前端（终端2）
```bash
cd frontend
npm install
npm run dev
```

## 课程内容（约2小时）

| 部分 | 主题 | 时长 | 核心类比 |
|------|------|------|----------|
| Part 1 | 预训练 vs SFT | 30分钟 | 🎓 大学毕业生的成长 |
| Part 2 | LoRA高效微调 | 30分钟 | 🔌 电源适配器 |
| Part 3 | SFT数据集 | 30分钟 | 📐 AI的行为蓝图 |
| Part 4 | 实践工作流 | 30分钟 | 🌱 园艺过程 |

## 特色功能

✨ **形象比喻** - 每个概念都有通俗易懂的类比  
📊 **可视化丰富** - 图表、动画、对比表格  
🎯 **互动测验** - 每部分都有测试题  
💻 **代码示例** - 可复制的真实代码  

## 技术栈

- 前端：Vue 3 + Vite + TailwindCSS + Chart.js
- 后端：Flask + Python

---

详细说明请查看 `使用指南.md`

