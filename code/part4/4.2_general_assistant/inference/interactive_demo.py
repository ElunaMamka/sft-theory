"""
4.1 中医问诊助手 - 交互式演示
提供命令行交互界面，实时体验模型效果
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_model import TCMInferenceEngine


class InteractiveTCMDemo:
    """交互式中医问诊演示"""
    
    def __init__(self, base_model_path: str, lora_adapter_path: str):
        print("="*80)
        print("🏥 中医问诊助手 - 交互式演示")
        print("="*80)
        print("\n正在加载模型，请稍候...")
        
        self.engine = TCMInferenceEngine(base_model_path, lora_adapter_path)
        self.instruction = "你是一位经验丰富的中医师，请根据患者的症状进行问诊和诊断。"
        
        self.print_welcome()
    
    def print_welcome(self):
        """打印欢迎信息"""
        print("\n" + "="*80)
        print("✅ 模型加载完成！")
        print("="*80)
        
        print("\n💡 使用说明:")
        print("  1. 输入您的症状描述")
        print("  2. 系统会给出中医诊断和建议")
        print("  3. 输入 'quit' 或 'exit' 退出")
        print("  4. 输入 'example' 查看示例")
        print("  5. 输入 'clear' 清屏")
        
        print("\n⚠️  免责声明:")
        print("  本系统仅供学习演示，不能替代专业医疗诊断。")
        print("  如有健康问题，请咨询正规医疗机构。")
        print("\n" + "="*80)
    
    def print_examples(self):
        """打印示例"""
        examples = [
            "我最近总是感觉很累，手脚冰凉，吃饭也没什么胃口。舌头颜色比较淡。",
            "这段时间口干口苦，脾气很大容易发火，大便也很干。舌头红，苔黄。",
            "最近心慌心悸，晚上失眠，手心脚心发热，夜里会出汗。",
        ]
        
        print("\n" + "="*80)
        print("📝 示例症状描述")
        print("="*80)
        
        for idx, example in enumerate(examples, 1):
            print(f"\n示例 {idx}:")
            print(f"  {example}")
        
        print("\n" + "="*80)
    
    def chat(self):
        """开始对话"""
        while True:
            try:
                # 获取用户输入
                print("\n" + "-"*80)
                user_input = input("👤 患者: ").strip()
                
                # 处理特殊命令
                if user_input.lower() in ['quit', 'exit', '退出']:
                    print("\n👋 感谢使用，再见！")
                    break
                
                if user_input.lower() in ['example', '示例']:
                    self.print_examples()
                    continue
                
                if user_input.lower() in ['clear', '清屏']:
                    os.system('clear' if os.name != 'nt' else 'cls')
                    self.print_welcome()
                    continue
                
                if not user_input:
                    print("⚠️ 请输入症状描述")
                    continue
                
                # 生成回复
                print("\n🏥 中医师正在分析...")
                from model.model_utils import format_instruction
                prompt = format_instruction(self.instruction, user_input)
                
                response = self.engine.generate(
                    prompt,
                    max_new_tokens=1024,
                    temperature=0.7,
                    top_p=0.9,
                )
                
                print(f"\n🩺 中医师:")
                print("-"*80)
                print(response)
                print("-"*80)
                
            except KeyboardInterrupt:
                print("\n\n👋 检测到中断，退出程序")
                break
            except Exception as e:
                print(f"\n❌ 发生错误: {e}")
                continue


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='中医问诊助手 - 交互式演示')
    parser.add_argument('--base_model', type=str, 
                       default="baichuan-inc/Baichuan2-7B-Base",
                       help='基座模型路径')
    parser.add_argument('--lora_adapter', type=str,
                       default="../training/output/tcm_sft_lora",
                       help='LoRA适配器路径')
    
    args = parser.parse_args()
    
    # 创建交互式演示
    demo = InteractiveTCMDemo(
        base_model_path=args.base_model,
        lora_adapter_path=args.lora_adapter,
    )
    
    # 开始对话
    demo.chat()


if __name__ == "__main__":
    main()

