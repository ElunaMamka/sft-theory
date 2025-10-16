"""
演示代码：对比预训练和SFT
文件位置：code/part1/02_sft_vs_pretraining.py

直观展示预训练模型和SFT模型在相同输入下的不同表现
"""

from typing import Dict, List


class BaseModel:
    """预训练基座模型"""
    
    def __init__(self):
        self.name = "预训练基座模型"
        self.knowledge = "具备语言理解和通用知识"
        
    def generate(self, prompt: str) -> str:
        """
        生成文本（模拟）
        
        基座模型可以生成流畅文本，但不一定遵循指令
        """
        # 模拟基座模型的输出：流畅但可能不符合用户意图
        responses = {
            "请总结一下人工智能的定义": 
                "人工智能是一个很有趣的话题。它涉及到计算机、算法、数据等多个方面。"
                "人工智能的历史可以追溯到20世纪50年代，当时图灵提出了著名的图灵测试...",
            
            "用一句话告诉我今天的天气": 
                "天气是一个复杂的自然现象，受到多种因素影响，包括气压、温度、湿度等。"
                "天气预报使用了先进的气象模型和卫星观测数据...",
            
            "帮我写一封客户道歉信": 
                "道歉信是商业沟通中的重要文体。它需要诚恳的态度和恰当的措辞。"
                "历史上有很多著名的道歉信案例..."
        }
        
        return responses.get(prompt, "我可以生成文本，但可能不会直接回答您的问题。")


class SFTModel:
    """经过SFT的模型"""
    
    def __init__(self):
        self.name = "SFT微调模型"
        self.knowledge = "具备语言理解、通用知识 + 指令遵循能力"
        
    def generate(self, prompt: str) -> str:
        """
        生成文本（模拟）
        
        SFT模型能够理解用户意图并给出针对性回答
        """
        # 模拟SFT模型的输出：遵循指令，给出有用的回答
        responses = {
            "请总结一下人工智能的定义": 
                "人工智能(AI)是指让计算机系统模拟人类智能行为的技术，"
                "包括学习、推理、问题解决、感知和语言理解等能力。",
            
            "用一句话告诉我今天的天气": 
                "很抱歉，我无法获取实时天气信息，建议您查看天气预报应用或网站。",
            
            "帮我写一封客户道歉信": 
                "尊敬的客户：\n\n"
                "对于给您带来的不便，我们深表歉意。我们已经意识到问题所在，"
                "正在采取措施确保类似情况不再发生。感谢您的理解与支持。\n\n"
                "此致\n敬礼"
        }
        
        return responses.get(prompt, "我会尽力按照您的指令来回答问题。")


def compare_models():
    """对比两个模型的表现"""
    
    print("="* 80)
    print("🔬 预训练 vs SFT 对比实验")
    print("="* 80)
    
    # 创建两个模型
    base_model = BaseModel()
    sft_model = SFTModel()
    
    # 测试用例
    test_prompts = [
        "请总结一下人工智能的定义",
        "用一句话告诉我今天的天气",
        "帮我写一封客户道歉信"
    ]
    
    for i, prompt in enumerate(test_prompts, 1):
        print(f"\n{'='*80}")
        print(f"📝 测试 {i}: {prompt}")
        print(f"{'='*80}")
        
        print(f"\n🤖 {base_model.name}的回答:")
        print("-" * 80)
        print(base_model.generate(prompt))
        
        print(f"\n✨ {sft_model.name}的回答:")
        print("-" * 80)
        print(sft_model.generate(prompt))
        
        print("\n💡 观察要点:")
        print("- 基座模型：知识丰富但不一定直接回答问题")
        print("- SFT模型：理解用户意图，给出针对性的有用回答")
    
    print(f"\n{'='*80}")
    print("📊 核心差异总结")
    print(f"{'='*80}")
    
    comparison = [
        ("能力范围", "通用知识 + 语言生成", "通用知识 + 指令遵循 + 任务专精"),
        ("回答风格", "可能发散、不聚焦", "直接、针对性强"),
        ("用户体验", "像在和知识库对话", "像在和助手对话"),
        ("适用场景", "需要创意文本生成", "需要完成具体任务")
    ]
    
    for aspect, base, sft in comparison:
        print(f"\n{aspect}:")
        print(f"  预训练: {base}")
        print(f"  SFT后:  {sft}")
    
    print(f"\n{'='*80}")
    print("🎯 结论：SFT让模型从'知识宝库'变成'实用助手'")
    print(f"{'='*80}")
    
    print("\n📁 代码位置: code/part1/02_sft_vs_pretraining.py")


if __name__ == "__main__":
    compare_models()

