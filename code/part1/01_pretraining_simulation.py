"""
演示代码：预训练过程模拟
文件位置：code/part1/01_pretraining_simulation.py

这个脚本模拟了预训练的基本过程：
1. 加载大量文本数据
2. 预测下一个词
3. 计算损失并更新模型
"""

import random
from typing import List, Dict

class SimplePretraining:
    """简化的预训练模拟器"""
    
    def __init__(self, vocab_size: int = 1000):
        """
        初始化预训练模型
        
        Args:
            vocab_size: 词汇表大小
        """
        self.vocab_size = vocab_size
        # 简化的模型参数（实际是数十亿参数）
        self.model_params = [random.random() for _ in range(100)]
        self.training_loss = []
        
    def load_text_data(self) -> List[str]:
        """
        模拟加载海量文本数据
        
        Returns:
            文本列表（实际应该是万亿级tokens）
        """
        # 模拟互联网文本数据
        sample_texts = [
            "人工智能正在改变世界",
            "机器学习是AI的核心技术",
            "深度学习使用神经网络",
            "预训练模型需要大量数据",
            "自然语言处理应用广泛"
        ]
        
        print(f"📚 加载了 {len(sample_texts)} 条文本（实际应该是万亿tokens）")
        return sample_texts
    
    def tokenize(self, text: str) -> List[int]:
        """
        将文本转换为token序列
        
        Args:
            text: 输入文本
            
        Returns:
            token ID列表
        """
        # 简化的分词（实际使用BPE等算法）
        tokens = [hash(word) % self.vocab_size for word in text.split()]
        return tokens
    
    def predict_next_token(self, context_tokens: List[int]) -> Dict[int, float]:
        """
        预测下一个token的概率分布
        
        Args:
            context_tokens: 上下文tokens
            
        Returns:
            token到概率的映射
        """
        # 简化的预测（实际使用Transformer）
        predictions = {}
        for i in range(min(5, self.vocab_size)):
            predictions[i] = random.random()
        
        # 归一化为概率
        total = sum(predictions.values())
        predictions = {k: v/total for k, v in predictions.items()}
        
        return predictions
    
    def calculate_loss(self, predicted: Dict[int, float], actual: int) -> float:
        """
        计算交叉熵损失
        
        Args:
            predicted: 预测的概率分布
            actual: 实际的下一个token
            
        Returns:
            损失值
        """
        # 简化的损失计算
        actual_prob = predicted.get(actual, 0.01)
        loss = -1 * (actual_prob if actual_prob > 0 else 0.01)
        return abs(loss)
    
    def train_epoch(self, texts: List[str]) -> float:
        """
        训练一个epoch
        
        Args:
            texts: 训练文本
            
        Returns:
            平均损失
        """
        total_loss = 0
        samples = 0
        
        for text in texts:
            tokens = self.tokenize(text)
            
            # 对每个位置预测下一个token
            for i in range(len(tokens) - 1):
                context = tokens[:i+1]
                next_token = tokens[i+1]
                
                # 预测
                predictions = self.predict_next_token(context)
                
                # 计算损失
                loss = self.calculate_loss(predictions, next_token)
                total_loss += loss
                samples += 1
                
                # 模拟参数更新（实际使用反向传播）
                self.model_params[0] = self.model_params[0] * 0.999
        
        avg_loss = total_loss / samples if samples > 0 else 0
        return avg_loss
    
    def pretrain(self, num_epochs: int = 10):
        """
        执行完整的预训练过程
        
        Args:
            num_epochs: 训练轮数（实际可能需要遍历数据多次）
        """
        print("\n🚀 开始预训练...")
        print(f"📊 词汇表大小: {self.vocab_size:,}")
        print(f"🔄 训练轮数: {num_epochs}")
        print("-" * 60)
        
        # 加载数据
        texts = self.load_text_data()
        
        # 训练多个epoch
        for epoch in range(num_epochs):
            avg_loss = self.train_epoch(texts)
            self.training_loss.append(avg_loss)
            
            print(f"Epoch {epoch+1:2d}/{num_epochs} | Loss: {avg_loss:.4f}")
        
        print("-" * 60)
        print("✅ 预训练完成！")
        print(f"📉 最终损失: {self.training_loss[-1]:.4f}")
        print(f"📈 损失下降: {(self.training_loss[0] - self.training_loss[-1]):.4f}")


def main():
    """主函数：演示预训练过程"""
    
    print("="* 60)
    print("🎓 预训练过程演示")
    print("="* 60)
    
    # 创建预训练模型
    model = SimplePretraining(vocab_size=1000)
    
    # 执行预训练
    model.pretrain(num_epochs=10)
    
    print("\n💡 关键要点：")
    print("1. 预训练使用海量未标注文本")
    print("2. 核心任务是预测下一个词")
    print("3. 通过自监督学习获得语言理解能力")
    print("4. 损失持续下降表示模型在学习")
    
    print("\n📁 代码位置: code/part1/01_pretraining_simulation.py")


if __name__ == "__main__":
    main()

