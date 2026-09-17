# Mental Model 与 Interface Metaphor


> **证据标签**
> - **[史实]**：有原始资料、官方文档或学术文献直接支撑。
> - **[解释]**：基于多条史实做出的分析性归纳，不等于当事设计团队的原话。
> - **[假说]**：可检验的理论延伸，尤其用于 AI-native UI 部分。
> - **[限制]**：与主叙事相冲突、限制其外推范围、或提醒避免后见之明的证据。


## 隐喻不是终点

**[史实]** Carroll、Mack、Kellogg 在 1988 年讨论 interface metaphor 时，明确指出隐喻可以增加目标域的初始熟悉度，但用户最终需要形成对 target domain 自身的理解，即 mental model。
来源：https://www.sciencedirect.com/science/article/pii/B9780444705365500087

这提供了一个非常适合本项目的模型：

```mermaid
flowchart LR
K[已有知识] --> M[界面隐喻]
M --> N[理解新系统]
N --> MM[形成目标域 mental model]
MM --> L[降低对隐喻依赖]
```

## 三种拟物不要混为一谈

1. **Semantic skeuomorphism**：Desktop / Folder / Trash / Clipboard —— 给数字对象命名和分类。
2. **Behavioral skeuomorphism**：drag / drop / slide / page turn —— 用物理动作解释交互。
3. **Visual skeuomorphism**：wood / leather / paper texture / bevel —— 用表面材质强化现实物件感。

1984 Macintosh：前两者极强，第三者受限于黑白屏和算力。
iOS 6：三者都强。
iOS 7 / Material：逐渐减少 object-level visual realism，但保留/强化 motion、layer、depth。

## 研究价值

把 skeuomorphism 只定义为“皮革/木纹”会错过 GUI 最早、最重要的认知工作。更有用的概念是：**界面借现实世界的 ontology、动作和感知线索，来建立新的计算 mental model。**
