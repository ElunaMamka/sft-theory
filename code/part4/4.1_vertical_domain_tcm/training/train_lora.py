import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
import os

# ==============================================================================
# 1. 核心 Trainer 类
# ==============================================================================
class Trainer:
    """
    一个通用的模型训练器。
    """
    def __init__(self, model, train_loader, val_loader, criterion, optimizer, device, epochs, save_path):
        """
        初始化 Trainer。

        参数:
            model (nn.Module): 需要训练的 PyTorch 模型。
            train_loader (DataLoader): 训练数据集的 DataLoader。
            val_loader (DataLoader): 验证数据集的 DataLoader。
            criterion (nn.Module): 损失函数 (e.g., nn.CrossEntropyLoss)。
            optimizer (torch.optim.Optimizer): 优化器 (e.g., torch.optim.Adam)。
            device (torch.device): 运行设备 ('cuda' or 'cpu')。
            epochs (int): 训练的总轮数。
            save_path (str): 最佳模型保存的路径。
        """
        self.model = model.to(device)
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.criterion = criterion
        self.optimizer = optimizer
        self.device = device
        self.epochs = epochs
        self.save_path = save_path
        
        # 用于跟踪最佳模型的表现
        self.best_val_loss = float('inf')
        
        # 确保保存模型的目录存在
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

    def _train_one_epoch(self):
        """
        执行一个 epoch 的训练。
        """
        self.model.train()  # 设置模型为训练模式
        total_loss = 0
        correct_predictions = 0
        total_samples = 0

        for inputs, labels in self.train_loader:
            # 将数据移动到指定设备
            inputs, labels = inputs.to(self.device), labels.to(self.device)

            # 1. 前向传播
            outputs = self.model(inputs)
            loss = self.criterion(outputs, labels)

            # 2. 反向传播和优化
            self.optimizer.zero_grad()  # 清空梯度
            loss.backward()            # 计算梯度
            self.optimizer.step()      # 更新权重

            # 累计损失和准确率
            total_loss += loss.item() * inputs.size(0)
            _, predicted = torch.max(outputs.data, 1)
            total_samples += labels.size(0)
            correct_predictions += (predicted == labels).sum().item()

        avg_loss = total_loss / total_samples
        accuracy = correct_predictions / total_samples
        return avg_loss, accuracy

    def _validate_one_epoch(self):
        """
        执行一个 epoch 的验证。
        """
        self.model.eval()  # 设置模型为评估模式
        total_loss = 0
        correct_predictions = 0
        total_samples = 0

        with torch.no_grad():  # 在验证阶段, 不需要计算梯度
            for inputs, labels in self.val_loader:
                inputs, labels = inputs.to(self.device), labels.to(self.device)

                outputs = self.model(inputs)
                loss = self.criterion(outputs, labels)

                total_loss += loss.item() * inputs.size(0)
                _, predicted = torch.max(outputs.data, 1)
                total_samples += labels.size(0)
                correct_predictions += (predicted == labels).sum().item()

        avg_loss = total_loss / total_samples
        accuracy = correct_predictions / total_samples
        return avg_loss, accuracy

    def train(self):
        """
        启动完整的训练流程。
        """
        print("🚀 开始训练...")
        for epoch in range(self.epochs):
            # 训练
            train_loss, train_acc = self._train_one_epoch()
            
            # 验证
            val_loss, val_acc = self._validate_one_epoch()

            print(f"Epoch {epoch+1}/{self.epochs} | "
                  f"训练损失: {train_loss:.4f}, 训练准确率: {train_acc:.4f} | "
                  f"验证损失: {val_loss:.4f}, 验证准确率: {val_acc:.4f}")

            # 检查是否是最佳模型，并保存
            if val_loss < self.best_val_loss:
                self.best_val_loss = val_loss
                print(f"🎉 发现新的最佳模型！在 Epoch {epoch+1}，验证损失为: {val_loss:.4f}。正在保存...")
                torch.save(self.model.state_dict(), self.save_path)
        
        print(f"🏁 训练完成！最佳模型已保存至 {self.save_path}")


# ==============================================================================
# 2. 一个简单的演示模型 (全连接神经网络)
# ==============================================================================
class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

# ==============================================================================
# 3. 主程序入口
# ==============================================================================
if __name__ == '__main__':
    # --- 1. 超参数和设置 ---
    INPUT_SIZE = 10     # 输入特征维度
    HIDDEN_SIZE = 32    # 隐藏层大小
    NUM_CLASSES = 3     # 类别数
    LEARNING_RATE = 0.001
    BATCH_SIZE = 64
    EPOCHS = 20
    MODEL_SAVE_PATH = "./saved_models/best_model.pth"

    # --- 2. 准备设备 ---
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"当前使用的设备是: {device}")

    # --- 3. 创建虚拟数据 ---
    # 训练数据 (1000个样本)
    train_features = torch.randn(1000, INPUT_SIZE)
    train_labels = torch.randint(0, NUM_CLASSES, (1000,))
    train_dataset = TensorDataset(train_features, train_labels)
    train_loader = DataLoader(dataset=train_dataset, batch_size=BATCH_SIZE, shuffle=True)

    # 验证数据 (200个样本)
    val_features = torch.randn(200, INPUT_SIZE)
    val_labels = torch.randint(0, NUM_CLASSES, (200,))
    val_dataset = TensorDataset(val_features, val_labels)
    val_loader = DataLoader(dataset=val_dataset, batch_size=BATCH_SIZE, shuffle=False)

    # --- 4. 初始化模型、损失函数和优化器 ---
    model = SimpleNet(INPUT_SIZE, HIDDEN_SIZE, NUM_CLASSES)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

    # --- 5. 实例化并启动训练器 ---
    trainer = Trainer(
        model=model,
        train_loader=train_loader,
        val_loader=val_loader,
        criterion=criterion,
        optimizer=optimizer,
        device=device,
        epochs=EPOCHS,
        save_path=MODEL_SAVE_PATH
    )
    
    trainer.train()

    # --- 6. (可选) 加载并使用最佳模型进行推理 ---
    print("\n加载最佳模型进行推理演示...")
    # 首先，需要创建一个和保存时结构相同的模型实例
    best_model = SimpleNet(INPUT_SIZE, HIDDEN_SIZE, NUM_CLASSES)
    # 然后，加载保存的状态字典
    best_model.load_state_dict(torch.load(MODEL_SAVE_PATH))
    best_model.to(device)
    best_model.eval() # 设置为评估模式
    
    # 取一个样本进行测试
    sample_input, _ = val_dataset[0]
    sample_input = sample_input.unsqueeze(0).to(device) # 增加 batch 维度并移动到设备
    
    with torch.no_grad():
        prediction = best_model(sample_input)
        predicted_class = torch.argmax(prediction, dim=1).item()
        print(f"对第一个验证样本的预测类别是: {predicted_class}")