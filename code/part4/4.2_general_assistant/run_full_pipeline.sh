#!/bin/bash
# 4.1 中医问诊助手 - 完整流程一键运行脚本

set -e  # 遇到错误立即退出

echo "================================================================================"
echo "🚀 中医问诊助手 - 完整SFT流程"
echo "================================================================================"

# 颜色定义
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 函数：打印步骤
print_step() {
    echo -e "\n${BLUE}【步骤 $1】${NC} $2"
    echo "--------------------------------------------------------------------------------"
}

# 函数：检查Python环境
check_environment() {
    print_step 1 "检查环境"
    
    # 检查Python
    if ! command -v python3 &> /dev/null; then
        echo "❌ Python3未安装"
        exit 1
    fi
    echo "✅ Python: $(python3 --version)"
    
    # 检查CUDA
    if command -v nvidia-smi &> /dev/null; then
        echo "✅ CUDA可用"
        nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
    else
        echo "⚠️ CUDA不可用，将使用CPU（速度较慢）"
    fi
    
    # 检查磁盘空间
    echo "💾 磁盘空间:"
    df -h . | tail -1
}

# 函数：安装依赖
install_dependencies() {
    print_step 2 "安装依赖"
    
    if [ -f "requirements.txt" ]; then
        echo "📦 安装Python包..."
        pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
        echo "✅ 依赖安装完成"
    else
        echo "❌ requirements.txt不存在"
        exit 1
    fi
}

# 函数：准备数据
prepare_data() {
    print_step 3 "准备训练数据"
    
    cd data
    
    # 生成原始数据
    echo "📝 生成原始数据..."
    python raw_examples.py
    
    # 预处理数据
    echo "🔄 预处理数据..."
    python prepare_dataset.py
    
    # 分析数据
    echo "📊 分析数据集..."
    python dataset_analysis.py
    
    cd ..
    echo "✅ 数据准备完成"
}

# 函数：训练模型
train_model() {
    print_step 4 "训练模型"
    
    cd training
    
    echo "🏋️ 开始LoRA微调..."
    echo "⏱️ 预计耗时: 2-3小时（单GPU V100）"
    echo ""
    
    # 训练
    python train_lora.py
    
    cd ..
    echo "✅ 训练完成"
}

# 函数：测试模型
test_model() {
    print_step 5 "测试模型"
    
    cd inference
    
    echo "🧪 运行测试套件..."
    python test_model.py --mode test
    
    echo ""
    echo "🔬 对比基座模型和微调模型..."
    python test_model.py --mode compare
    
    cd ..
    echo "✅ 测试完成"
}

# 函数：启动演示
launch_demo() {
    print_step 6 "启动交互式演示"
    
    cd inference
    
    echo "🎭 启动交互式问诊系统..."
    echo "💡 提示: 输入 'quit' 退出演示"
    echo ""
    
    python interactive_demo.py
    
    cd ..
}

# 函数：打印总结
print_summary() {
    echo ""
    echo "================================================================================"
    echo "🎉 完整流程执行完毕！"
    echo "================================================================================"
    echo ""
    echo "📊 项目文件结构:"
    echo "  ├── data/"
    echo "  │   ├── tcm_raw_data.json          # 原始数据"
    echo "  │   ├── train_data.json            # 训练数据"
    echo "  │   ├── val_data.json              # 验证数据"
    echo "  │   └── processed/                 # HuggingFace格式数据"
    echo "  ├── training/"
    echo "  │   ├── output/                    # 模型checkpoint"
    echo "  │   └── logs/                      # 训练日志"
    echo "  └── inference/"
    echo "      └── test_results.json          # 测试结果"
    echo ""
    echo "🔧 后续操作:"
    echo "  1. 查看训练日志:"
    echo "     tensorboard --logdir training/logs"
    echo ""
    echo "  2. 测试模型:"
    echo "     cd inference && python test_model.py"
    echo ""
    echo "  3. 交互式演示:"
    echo "     cd inference && python interactive_demo.py"
    echo ""
    echo "  4. 分布式训练:"
    echo "     cd training && torchrun --nproc_per_node=4 train_distributed.py"
    echo ""
    echo "================================================================================"
}

# ==================== 主流程 ====================

# 解析命令行参数
MODE=${1:-"full"}

case "$MODE" in
    "full")
        # 完整流程
        check_environment
        install_dependencies
        prepare_data
        train_model
        test_model
        print_summary
        
        # 询问是否启动演示
        read -p "是否启动交互式演示? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            launch_demo
        fi
        ;;
    
    "data")
        # 只准备数据
        check_environment
        prepare_data
        ;;
    
    "train")
        # 只训练
        check_environment
        train_model
        ;;
    
    "test")
        # 只测试
        check_environment
        test_model
        ;;
    
    "demo")
        # 只演示
        launch_demo
        ;;
    
    "help"|"-h"|"--help")
        echo "使用方法:"
        echo "  ./run_full_pipeline.sh [MODE]"
        echo ""
        echo "可选模式:"
        echo "  full   - 完整流程（默认）"
        echo "  data   - 只准备数据"
        echo "  train  - 只训练模型"
        echo "  test   - 只测试模型"
        echo "  demo   - 只启动演示"
        echo "  help   - 显示帮助"
        ;;
    
    *)
        echo "❌ 未知模式: $MODE"
        echo "运行 './run_full_pipeline.sh help' 查看帮助"
        exit 1
        ;;
esac

