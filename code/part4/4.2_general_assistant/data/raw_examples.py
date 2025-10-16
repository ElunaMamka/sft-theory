"""
4.2 通用对话助手 - 多任务数据示例
包含10+种任务类型的真实、完整数据
"""

# Multi-task instruction-following data
GENERAL_ASSISTANT_DATA = [
    # ==================== 任务1：问答 ====================
    {
        "task_type": "qa",
        "instruction": "请回答以下问题。",
        "input": "什么是Transformer架构？它为什么在自然语言处理领域如此重要？",
        "output": """Transformer是一种深度学习模型架构，由Google在2017年的论文"Attention is All You Need"中提出。它彻底改变了自然语言处理领域。

**核心特点：**

1. **Self-Attention机制**
   - 能够捕捉序列中任意两个位置之间的依赖关系
   - 不受距离限制，解决了RNN的长距离依赖问题
   - 可以并行计算，训练效率高

2. **架构组成**
   - Encoder-Decoder结构
   - Multi-Head Attention：多头注意力机制
   - Feed-Forward Network：前馈神经网络
   - Position Encoding：位置编码

3. **为什么重要？**

   **a) 性能突破**
   - 在机器翻译、文本生成等任务上大幅超越RNN/LSTM
   - BLEU分数提升显著

   **b) 并行化能力**
   - RNN必须顺序处理，Transformer可以并行
   - 训练速度快数十倍

   **c) 可扩展性**
   - 易于堆叠更多层
   - 支持超大规模模型（GPT-3的175B参数）

   **d) 通用性**
   - 不仅适用于NLP，也扩展到CV（Vision Transformer）
   - 成为多模态模型的基础

**影响：**
Transformer催生了BERT、GPT系列、T5等一系列强大模型，奠定了现代大语言模型的基础。可以说，没有Transformer就没有今天的ChatGPT。"""
    },
    
    # ==================== 任务2：创意写作 ====================
    {
        "task_type": "creative_writing",
        "instruction": "根据给定的开头，续写一个引人入胜的科幻故事（300字以上）。",
        "input": "2157年，地球上最后一座城市的能源只剩下48小时。",
        "output": """2157年，地球上最后一座城市的能源只剩下48小时。

指挥官陈墨站在新上海穹顶的最高处，俯瞰着这座人类文明的最后堡垒。透明的能量护罩正在缓慢黯淡，像一个垂死之人的呼吸。

"墨，量子反应堆的衰减速度比预计快了12%。"副官艾娃的声音在耳机里响起，带着一丝颤抖。

陈墨深吸一口气。三个月前，太阳突然进入了异常活跃期，致命的辐射摧毁了地表所有的太阳能设施。全球43座城市相继陷落，现在只剩下新上海。

"启动'凤凰计划'。"他平静地说。

艾娃沉默了几秒："长官，那个计划的成功率只有0.3%，而且需要牺牲..."

"我知道。"陈墨打断了她，"但0.3%总好过0%。"

凤凰计划是一个疯狂的构想：将城市的最后能量全部注入时空折跃装置，把整座城市传送到500年前。如果成功，人类文明将得以延续。如果失败，一切都将化为灰烬。

48小时的倒计时开始了。

城市里的800万人还不知道，他们正在参与一场关乎种族存亡的豪赌。陈墨望向天空，那里是祖先曾经仰望过的同一片星空。

"再见了，2157。"他轻声说，"希望我们能在过去重逢。"

能量护罩突然剧烈波动，空间开始扭曲。最后的旅程，即将开始。"""
    },
    
    # ==================== 任务3：代码生成 ====================
    {
        "task_type": "code_generation",
        "instruction": "请编写Python代码实现以下功能。",
        "input": "实现一个LRU（Least Recently Used）缓存，支持get和put操作，时间复杂度O(1)。",
        "output": """```python
class LRUCache:
    \"\"\"
    LRU Cache implementation with O(1) time complexity
    Uses a combination of HashMap and Doubly Linked List
    \"\"\"
    
    class Node:
        \"\"\"Doubly linked list node\"\"\"
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
    
    def __init__(self, capacity: int):
        \"\"\"
        Initialize LRU cache with given capacity
        
        Args:
            capacity: Maximum number of items to store
        \"\"\"
        self.capacity = capacity
        self.cache = {}  # HashMap for O(1) access
        
        # Dummy head and tail nodes
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_to_head(self, node: Node):
        \"\"\"Add node right after head (most recently used)\"\"\"
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node: Node):
        \"\"\"Remove node from linked list\"\"\"
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _move_to_head(self, node: Node):
        \"\"\"Move existing node to head (mark as recently used)\"\"\"
        self._remove_node(node)
        self._add_to_head(node)
    
    def _remove_tail(self) -> Node:
        \"\"\"Remove and return the least recently used node\"\"\"
        node = self.tail.prev
        self._remove_node(node)
        return node
    
    def get(self, key: int) -> int:
        \"\"\"
        Get value by key, return -1 if not found
        Move the accessed item to head (most recent)
        
        Time Complexity: O(1)
        \"\"\"
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_head(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        \"\"\"
        Put key-value pair into cache
        If key exists, update value and move to head
        If cache is full, remove least recently used item
        
        Time Complexity: O(1)
        \"\"\"
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # Add new key
            node = self.Node(key, value)
            self.cache[key] = node
            self._add_to_head(node)
            
            # Check capacity
            if len(self.cache) > self.capacity:
                # Remove LRU item
                removed = self._remove_tail()
                del self.cache[removed.key]


# 使用示例
if __name__ == "__main__":
    # Create cache with capacity 2
    cache = LRUCache(2)
    
    cache.put(1, 1)  # cache: {1=1}
    cache.put(2, 2)  # cache: {1=1, 2=2}
    print(cache.get(1))  # returns 1, cache: {2=2, 1=1}
    
    cache.put(3, 3)  # evicts key 2, cache: {1=1, 3=3}
    print(cache.get(2))  # returns -1 (not found)
    
    cache.put(4, 4)  # evicts key 1, cache: {3=3, 4=4}
    print(cache.get(1))  # returns -1 (not found)
    print(cache.get(3))  # returns 3
    print(cache.get(4))  # returns 4
```

**实现要点：**

1. **数据结构选择**
   - HashMap：提供O(1)的查找
   - 双向链表：提供O(1)的插入和删除

2. **核心思想**
   - 最近使用的放在链表头部
   - 最少使用的在链表尾部
   - 超出容量时删除尾部节点

3. **时间复杂度**
   - get操作：O(1)
   - put操作：O(1)

4. **空间复杂度**
   - O(capacity)"""
    },
    
    # ==================== 任务4：数学推理 ====================
    {
        "task_type": "math_reasoning",
        "instruction": "请详细解答以下数学问题，展示完整的推理过程。",
        "input": "一个水池有两个进水管和一个出水管。单开甲管12小时可以注满水池，单开乙管18小时可以注满水池，单开丙管24小时可以放完满池水。现在三管同时打开，多少小时可以注满水池？",
        "output": """让我们一步步解决这个问题。

**第一步：理解问题**
- 甲管：12小时注满
- 乙管：18小时注满
- 丙管：24小时放完
- 求：三管同时开，多少小时注满

**第二步：设定单位**
设水池总容量为"1"（可以理解为100%）

**第三步：计算每管的效率**

甲管的效率：
- 12小时注满1个水池
- 1小时注入：1/12

乙管的效率：
- 18小时注满1个水池
- 1小时注入：1/18

丙管的效率：
- 24小时放完1个水池
- 1小时放出：1/24（注意是负的）

**第四步：计算合作效率**

三管同时工作，1小时的净注水量：
```
净效率 = 甲管效率 + 乙管效率 - 丙管效率
       = 1/12 + 1/18 - 1/24
```

**第五步：通分计算**

找最小公倍数：12, 18, 24的最小公倍数是72

```
1/12 = 6/72
1/18 = 4/72
1/24 = 3/72
```

因此：
```
净效率 = 6/72 + 4/72 - 3/72
       = (6 + 4 - 3)/72
       = 7/72
```

**第六步：计算时间**

1小时注入 7/72 的水
注满1个水池需要：
```
时间 = 1 ÷ (7/72)
     = 1 × (72/7)
     = 72/7
     = 10又2/7小时
     ≈ 10.29小时
     = 10小时17分钟
```

**答案：72/7小时，约等于10小时17分钟**

**验证：**
- 10.29小时内甲管注入：10.29 × (1/12) ≈ 0.857
- 10.29小时内乙管注入：10.29 × (1/18) ≈ 0.572
- 10.29小时内丙管放出：10.29 × (1/24) ≈ 0.429
- 净注入：0.857 + 0.572 - 0.429 ≈ 1.0 ✓

**解题关键：**
1. 将水池容量设为1（单位1）
2. 计算每管每小时的效率
3. 注意出水管是负效率
4. 通分计算合作效率
5. 用总量除以效率得时间"""
    },
    
    # ==================== 任务5：文本摘要 ====================
    {
        "task_type": "summarization",
        "instruction": "请将以下长文本总结为简洁的摘要（不超过100字）。",
        "input": """人工智能（Artificial Intelligence, AI）是计算机科学的一个分支，致力于创建能够模拟人类智能行为的系统和机器。AI的研究领域非常广泛，包括机器学习、深度学习、自然语言处理、计算机视觉、机器人学等多个方向。

机器学习是AI的核心技术之一，它使计算机能够从数据中学习规律，而不需要明确编程。深度学习是机器学习的一个子领域，使用多层神经网络来处理复杂的模式识别任务。近年来，深度学习在图像识别、语音识别、自然语言理解等领域取得了突破性进展。

自然语言处理（NLP）是AI的另一个重要分支，专注于让计算机理解、解释和生成人类语言。大语言模型如GPT系列的出现，使得机器在文本生成、翻译、问答等任务上达到了接近人类的水平。

AI技术正在深刻改变我们的生活，从智能手机的语音助手，到自动驾驶汽车，再到医疗诊断系统，AI的应用无处不在。然而，AI的发展也带来了一些挑战，如数据隐私、算法偏见、就业影响等问题，需要我们在推进技术发展的同时，也要关注其社会影响。""",
        "output": """人工智能是计算机科学分支，旨在创建模拟人类智能的系统。核心技术包括机器学习和深度学习，在图像识别、NLP等领域取得突破。大语言模型使机器文本处理能力接近人类。AI广泛应用于生活各领域，但也面临隐私、偏见等挑战。（98字）"""
    },
    
    # ==================== 任务6：逻辑推理 ====================
    {
        "task_type": "logic_reasoning",
        "instruction": "请解答以下逻辑推理问题。",
        "input": "有三个盒子，分别标记为"苹果"、"橙子"和"混合"。但是所有的标签都贴错了。你只能从一个盒子里拿出一个水果来看，如何确定所有盒子的真实内容？",
        "output": """这是一个经典的逻辑推理题。让我们一步步分析。

**关键信息：**
1. 三个盒子：标记为"苹果"、"橙子"、"混合"
2. 所有标签都贴错了（这是关键！）
3. 只能从一个盒子拿出一个水果

**推理过程：**

**步骤1：选择"混合"标签的盒子**

为什么选这个？因为：
- 标签都是错的
- "混合"标签的盒子一定不是混合
- 它只能是纯苹果或纯橙子

**步骤2：从"混合"盒子拿出一个水果**

假设拿出的是苹果，那么：
- "混合"标签的盒子 → 实际是纯苹果

**步骤3：推理其他两个盒子**

现在剩下两个盒子：
- 标记"苹果"的盒子
- 标记"橙子"的盒子

因为：
1. "苹果"标签是错的，它不是纯苹果
2. 纯苹果已经被"混合"盒子占了
3. 所以"苹果"标签的盒子只能是：混合

因此：
- "苹果"标签的盒子 → 实际是混合

最后：
- "橙子"标签的盒子 → 实际是纯橙子

**完整答案：**

1. 从标记"混合"的盒子拿水果
2. 如果拿出苹果：
   - "混合"标签 → 纯苹果
   - "苹果"标签 → 混合
   - "橙子"标签 → 纯橙子

3. 如果拿出橙子：
   - "混合"标签 → 纯橙子
   - "苹果"标签 → 混合
   - "橙子"标签 → 纯苹果

**为什么这样做有效？**

1. **选择"混合"盒子是关键**
   - 它一定不是混合（标签全错）
   - 它是确定的纯水果
   - 这给了我们确定的起点

2. **连锁推理**
   - 知道一个盒子的内容
   - 根据"标签全错"的约束
   - 可以推出其他盒子

3. **如果选其他盒子会怎样？**
   - 比如选"苹果"盒子拿出橙子
   - 只知道它不是苹果，可能是纯橙子或混合
   - 无法确定，还需要再拿

**这道题的启示：**
在逻辑推理中，找到能提供最多信息的关键点至关重要！"""
    },
    
    # ==================== 任务7：翻译 ====================
    {
        "task_type": "translation",
        "instruction": "请将以下英文翻译成中文，要求翻译准确、流畅、符合中文表达习惯。",
        "input": """Machine learning is a subset of artificial intelligence that focuses on developing algorithms and statistical models that enable computers to improve their performance on a specific task through experience. Unlike traditional programming, where explicit instructions are provided, machine learning systems learn patterns from data. The three main paradigms of machine learning are supervised learning, unsupervised learning, and reinforcement learning. Each has its own strengths and is suited for different types of problems.""",
        "output": """机器学习是人工智能的一个分支，专注于开发算法和统计模型，使计算机能够通过经验提升在特定任务上的表现。与传统编程提供明确指令不同，机器学习系统从数据中学习规律。机器学习的三大范式是监督学习、无监督学习和强化学习。每种范式都有其独特优势，适用于不同类型的问题。"""
    },
    
    # ==================== 任务8：信息抽取 ====================
    {
        "task_type": "information_extraction",
        "instruction": "请从以下文本中提取关键信息，包括时间、地点、人物、事件等。",
        "input": "2023年11月30日，OpenAI在旧金山举行发布会，CEO Sam Altman宣布推出GPT-4 Turbo版本。新版本上下文长度扩展到128K tokens，价格降低50%，并新增了视觉理解和语音功能。发布会上，Sam Altman还演示了GPTs功能，允许用户创建自定义的AI助手。",
        "output": """**关键信息抽取：**

**时间：**
- 2023年11月30日

**地点：**
- 旧金山

**人物：**
- Sam Altman（OpenAI CEO）

**公司/组织：**
- OpenAI

**事件：**
- 发布会，推出GPT-4 Turbo

**产品信息：**
- 产品名称：GPT-4 Turbo
- 主要特性：
  1. 上下文长度：128K tokens
  2. 价格：降低50%
  3. 新功能：视觉理解
  4. 新功能：语音功能
  5. 新功能：GPTs（自定义AI助手）

**事件性质：**
- 产品发布
- 功能演示"""
    },
    
    # ==================== 任务9：观点分析 ====================
    {
        "task_type": "opinion_analysis",
        "instruction": "请分析以下文本中表达的观点，并评估其合理性。",
        "input": "我认为人工智能将在未来10年内取代大部分人类工作。AI在效率、准确性和成本上都优于人类，企业必然会选择AI。失业潮不可避免，政府应该立即实施全民基本收入。",
        "output": """**观点分析：**

**核心观点：**
1. AI将在10年内取代大部分人类工作
2. AI在多方面优于人类
3. 失业潮不可避免
4. 应实施全民基本收入

**合理性评估：**

**部分合理的地方：**

✅ **AI确实在某些领域更优秀**
- 重复性任务：效率更高
- 数据处理：准确性更强
- 规模化成本：边际成本更低

✅ **AI会影响就业结构**
- 某些岗位会被自动化
- 就业市场会发生转型

**不合理或过于绝对的地方：**

❌ **"大部分工作"过于绝对**
- AI擅长的是可程序化的任务
- 需要创造力、同理心、复杂判断的工作难以被取代
- 麦肯锡报告：到2030年约15%工作被自动化（不是大部分）

❌ **忽视了新工作的创造**
- 历史上每次技术革命都创造了新工作
- AI会催生新职业（AI训练师、提示工程师等）
- AI辅助而非完全替代

❌ **10年时间过短**
- 技术部署需要时间
- 社会适应需要过程
- 法律监管需要建立

❌ **"不可避免"过于悲观**
- 可以通过教育、培训适应
- 人机协作是更可能的未来

**关于全民基本收入：**

这是一个值得讨论的方案，但：
- 需要考虑财政可持续性
- 可能影响工作动力
- 需要配套政策

**更平衡的观点应该是：**

AI确实会对就业产生影响，但：
1. 影响是渐进的，不是突变的
2. 会创造新岗位，同时淘汰旧岗位
3. 需要教育体系改革，培养新技能
4. 人机协作是更现实的未来
5. 需要社会安全网，但不一定是UBI

**结论：**
该观点提出了真实的担忧，但过于绝对和悲观，忽视了人类适应能力和新机会的创造。"""
    },
    
    # ==================== 任务10：头脑风暴 ====================
    {
        "task_type": "brainstorming",
        "instruction": "请为以下问题提供创新性的解决方案或想法（至少5个）。",
        "input": "如何鼓励大学生养成良好的运动习惯？",
        "output": """**大学生运动习惯养成方案（10个创新想法）：**

**1. 游戏化运动系统 "校园RPG"**
- 将校园变成RPG游戏地图
- 运动积累经验值，解锁校园特权
- 例如：跑步100公里解锁图书馆VIP座位
- 组队挑战，增加社交属性

**2. 运动货币 "汗水币"**
- 运动消耗的卡路里转化为校园虚拟货币
- 可兑换食堂餐券、打印费用、甚至学分抵扣
- 与手环/手机APP联动自动记录
- 鼓励真实运动而非作弊

**3. 社交运动匹配平台**
- 类似"运动版探探"
- 匹配运动习惯相似的同学
- 自动组织运动约会
- 解决"一个人运动很无聊"的问题

**4. 运动处方系统**
- 入学体检后生成个性化运动方案
- AI教练每周推送适合的运动
- 记录进步，可视化健康改善
- 联动校医院，运动数据作为健康档案

**5. 反向激励：久坐警报**
- 宿舍座椅、图书馆座位安装传感器
- 久坐2小时强制休息10分钟
- 不运动会"损失"某些权限
- 例如：连续7天不运动，宿舍WiFi限速

**6. 运动学分制**
- 每学期运动达标可获得0.5-1学分
- 参加运动队、健身课程可抵选修课
- 毕业需要满足最低运动学分
- 将运动纳入培养方案

**7. 跨校运动联赛**
- 组织线上+线下的高校运动比赛
- 不限于传统体育项目（如跳绳、徒步）
- 校际PK增强荣誉感
- 优胜者获得奖学金

**8. 明星导师计划**
- 邀请运动员、健身网红做导师
- 每月一次校园运动课
- 网红效应吸引学生
- 录制课程视频供回看

**9. 智能健身房改造**
- 设备自动记录数据
- 生成训练报告和建议
- 排行榜激励
- 预约系统避免拥挤
- VR健身增加趣味性

**10. 运动强制分散方案**
- 课程表自动插入"运动时间"
- 每周2-3次，每次30分钟
- 像上课一样强制执行
- 提供多种运动选择

**实施建议：**
1. 先试点1-2个方案
2. 收集学生反馈迭代
3. 多方案组合效果更好
4. 重点：让运动变得有趣+有益+有社交价值"""
    },
]


def save_to_json():
    """保存数据为JSON格式"""
    import json
    with open('general_assistant_raw_data.json', 'w', encoding='utf-8') as f:
        json.dump(GENERAL_ASSISTANT_DATA, f, ensure_ascii=False, indent=2)
    print(f"✅ 已保存 {len(GENERAL_ASSISTANT_DATA)} 条多任务数据")
    
    # 统计信息
    task_types = {}
    total_chars = 0
    
    for item in GENERAL_ASSISTANT_DATA:
        task = item['task_type']
        task_types[task] = task_types.get(task, 0) + 1
        total_chars += len(item['input']) + len(item['output'])
    
    print(f"\n📊 数据统计：")
    print(f"  总数据量: {len(GENERAL_ASSISTANT_DATA)}")
    print(f"  任务类型数: {len(task_types)}")
    print(f"  总字符数: {total_chars:,}")
    print(f"  平均长度: {total_chars/len(GENERAL_ASSISTANT_DATA):.0f} 字符/条")
    
    print(f"\n任务分布:")
    for task, count in task_types.items():
        print(f"  {task}: {count}条")


def print_sample():
    """打印样本"""
    print("\n" + "="*80)
    print("📋 多任务数据样本")
    print("="*80)
    
    for idx in [0, 2, 5]:  # 展示几个不同类型的样本
        sample = GENERAL_ASSISTANT_DATA[idx]
        print(f"\n【任务类型】{sample['task_type']}")
        print(f"【指令】{sample['instruction']}")
        print(f"【输入】{sample['input'][:100]}...")
        print(f"【输出】{sample['output'][:200]}...")
        print("-" * 80)


if __name__ == "__main__":
    print("="*80)
    print("🤖 4.2 通用对话助手 - 多任务数据示例")
    print("="*80)
    
    print_sample()
    save_to_json()
    
    print("\n✅ 数据准备完成！")
    print("   包含10+种任务类型的真实数据")
    print("   每条数据都是完整的、高质量的示例")

