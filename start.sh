#!/bin/bash

echo "🚀 启动SFT原理教学系统..."
echo ""

# 检查是否安装了Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 未找到Python3，请先安装Python"
    exit 1
fi

# 检查是否安装了Node.js
if ! command -v node &> /dev/null; then
    echo "❌ 未找到Node.js，请先安装Node.js"
    exit 1
fi

# 启动后端
echo "📦 启动后端服务器..."
cd backend
if [ ! -d "venv" ]; then
    echo "创建Python虚拟环境..."
    python3 -m venv venv
fi

source venv/bin/activate
pip install -r requirements.txt -q
python server.py &
BACKEND_PID=$!
cd ..

# 等待后端启动
sleep 2

# 启动前端
echo "🎨 启动前端开发服务器..."
cd frontend
if [ ! -d "node_modules" ]; then
    echo "安装前端依赖..."
    npm install
fi

npm run dev &
FRONTEND_PID=$!
cd ..

echo ""
echo "✅ 系统启动成功！"
echo ""
echo "📖 访问 http://localhost:5173 开始学习"
echo "🔧 后端API: http://localhost:5000"
echo ""
echo "按 Ctrl+C 停止服务"

# 等待用户中断
wait $FRONTEND_PID
wait $BACKEND_PID

