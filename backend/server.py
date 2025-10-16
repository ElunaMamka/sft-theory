from flask import Flask, jsonify, request
from flask_cors import CORS
import numpy as np
import random

app = Flask(__name__)
CORS(app)

@app.route('/api/pretraining-stats', methods=['GET'])
def get_pretraining_stats():
    """预训练阶段的统计数据"""
    return jsonify({
        'data_size': '数万亿词元',
        'training_time': '数周至数月',
        'cost': '数百万美元',
        'gpu_count': '成百上千',
        'data_type': '未标注的原始文本',
        'knowledge_coverage': ['语言规律', '事实知识', '逻辑推理', '世界常识']
    })

@app.route('/api/sft-stats', methods=['GET'])
def get_sft_stats():
    """SFT阶段的统计数据"""
    return jsonify({
        'data_size': '数百至数十万样本',
        'training_time': '数小时至数天',
        'cost': '数千至数万美元',
        'gpu_count': '1-8张',
        'data_type': '精标注的指令-响应对',
        'behavior_targets': ['遵循指令', '特定风格', '任务专精', '价值对齐']
    })

@app.route('/api/lora-comparison', methods=['GET'])
def get_lora_comparison():
    """LoRA与全量微调的对比数据"""
    model_size = request.args.get('model_size', '7B')
    
    # 根据模型大小计算参数
    size_map = {
        '7B': 7_000_000_000,
        '13B': 13_000_000_000,
        '70B': 70_000_000_000
    }
    
    total_params = size_map.get(model_size, 7_000_000_000)
    lora_params = int(total_params * 0.001)  # LoRA通常只训练0.1%的参数
    
    return jsonify({
        'full_finetuning': {
            'trainable_params': total_params,
            'memory_gb': total_params * 4 / 1e9,  # FP32
            'training_time': '慢',
            'catastrophic_forgetting_risk': '高',
            'storage_per_task_gb': total_params * 2 / 1e9  # FP16
        },
        'lora': {
            'trainable_params': lora_params,
            'memory_gb': lora_params * 4 / 1e9,
            'training_time': '快',
            'catastrophic_forgetting_risk': '极低',
            'storage_per_task_mb': lora_params * 2 / 1e6
        }
    })

@app.route('/api/generate-training-curve', methods=['GET'])
def generate_training_curve():
    """生成训练曲线数据"""
    epochs = int(request.args.get('epochs', 10))
    
    # 生成模拟的训练损失曲线
    x = np.linspace(0, epochs, epochs * 10)
    
    # 预训练曲线 - 持续缓慢下降
    pretrain_loss = 4.0 * np.exp(-0.3 * x) + 0.5 + np.random.normal(0, 0.05, len(x))
    
    # SFT曲线 - 快速下降后趋于稳定
    sft_loss = 2.0 * np.exp(-1.5 * x) + 0.3 + np.random.normal(0, 0.03, len(x))
    
    return jsonify({
        'pretrain': {
            'x': x.tolist(),
            'y': np.maximum(pretrain_loss, 0.5).tolist(),
            'label': '预训练损失'
        },
        'sft': {
            'x': x.tolist(),
            'y': np.maximum(sft_loss, 0.3).tolist(),
            'label': 'SFT损失'
        }
    })

@app.route('/api/dataset-examples', methods=['GET'])
def get_dataset_examples():
    """获取数据集示例"""
    examples = [
        {
            'task': '文本摘要',
            'instruction': '请用三句话总结以下文章。',
            'input': '埃菲尔铁塔是法国巴黎的标志性建筑，由工程师古斯塔夫·埃菲尔设计，于1889年为世界博览会而建。这座324米高的铁塔最初引起了巴黎市民的争议，但如今已成为世界上最受欢迎的旅游景点之一，每年吸引数百万游客。',
            'response': '埃菲尔铁塔是巴黎标志性建筑，由古斯塔夫·埃菲尔设计。它建于1889年，高324米，最初饱受争议。如今已成为世界最受欢迎的旅游景点之一。',
            'quality_score': 9.5
        },
        {
            'task': '问答',
            'instruction': '根据提供的上下文，回答用户的问题。',
            'input': '上下文：埃菲尔铁塔于1889年建成。问题：埃菲尔铁塔是何时完工的？',
            'response': '埃菲尔铁塔于1889年完工。',
            'quality_score': 10
        },
        {
            'task': '人格设定',
            'instruction': '你是一个友好且乐于助人的海盗助手。请回答用户的问题。',
            'input': '今天天气怎么样？',
            'response': '啊哈，我的伙计！今天晴空万里，阳光明媚！正是扬帆远航的好日子！',
            'quality_score': 9.0
        },
        {
            'task': '代码生成',
            'instruction': '编写一个Python函数来计算斐波那契数列。',
            'input': '',
            'response': 'def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)',
            'quality_score': 8.5
        }
    ]
    
    return jsonify(examples)

@app.route('/api/workflow-status', methods=['POST'])
def update_workflow_status():
    """模拟工作流状态更新"""
    data = request.json
    step = data.get('step', 1)
    
    status_map = {
        1: {'status': 'completed', 'message': '任务定义完成，已选择基座模型'},
        2: {'status': 'in_progress', 'message': '正在准备和清洗数据集...'},
        3: {'status': 'pending', 'message': '等待训练配置'},
        4: {'status': 'pending', 'message': '等待评估'}
    }
    
    return jsonify(status_map.get(step, {'status': 'pending', 'message': '等待开始'}))

@app.route('/api/analogy-data', methods=['GET'])
def get_analogy_data():
    """获取类比数据"""
    analogy_type = request.args.get('type', 'graduate')
    
    analogies = {
        'graduate': {
            'title': '大学毕业生类比',
            'comparison': [
                {'aspect': '知识广度', 'llm': '博览群书', 'graduate': '通识教育'},
                {'aspect': '实践经验', 'llm': '无', 'graduate': '无'},
                {'aspect': '特定技能', 'llm': '待培养', 'graduate': '待培养'},
                {'aspect': '工作能力', 'llm': 'SFT后获得', 'graduate': '在职培训后获得'}
            ]
        },
        'adapter': {
            'title': '电源适配器类比',
            'comparison': [
                {'aspect': '固定部分', 'lora': '预训练模型（墙上插座）', 'function': '保持不变'},
                {'aspect': '可变部分', 'lora': 'LoRA适配器（转换插头）', 'function': '适配特定任务'},
                {'aspect': '成本', 'lora': '极低', 'function': '可快速替换'},
                {'aspect': '效果', 'lora': '完美适配', 'function': '不损坏原设备'}
            ]
        },
        'gardening': {
            'title': '园艺类比',
            'comparison': [
                {'aspect': '土壤', 'sft': '数据集质量', 'action': '持续改进'},
                {'aspect': '种子', 'sft': '初始训练', 'action': '播种'},
                {'aspect': '修剪', 'sft': '数据清洗', 'action': '移除坏数据'},
                {'aspect': '施肥', 'sft': '数据增强', 'action': '添加高质量样本'}
            ]
        }
    }
    
    return jsonify(analogies.get(analogy_type, analogies['graduate']))

if __name__ == '__main__':
    app.run(debug=True, port=5000)

