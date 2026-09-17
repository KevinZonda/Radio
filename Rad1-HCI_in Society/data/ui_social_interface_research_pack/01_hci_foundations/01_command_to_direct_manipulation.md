# 从命令到直接操作：HCI 如何重新分配认知责任


> **证据标签**
> - **[史实]**：有原始资料、官方文档或学术文献直接支撑。
> - **[解释]**：基于多条史实做出的分析性归纳，不等于当事设计团队的原话。
> - **[假说]**：可检验的理论延伸，尤其用于 AI-native UI 部分。
> - **[限制]**：与主叙事相冲突、限制其外推范围、或提醒避免后见之明的证据。


## CLI 的基本认知结构

用户必须把“目标”翻译成机器语言：command、syntax、parameter、path、mode。错误经常是语法错误或状态错误。

**[解释]** CLI 把相当一部分认知责任放在用户身上：记忆系统 vocabulary、推断内部 state、把意图编译成命令。

## Direct Manipulation

**[史实]** Shneiderman 1983 将 direct manipulation 描述为对可见对象的操作，使计算机更“透明”，用户可以更集中于任务本身。
来源：https://www.cs.umd.edu/~ben/publications.html

**[史实]** Hutchins、Hollan、Norman 1985 给出更认知科学的解释：directness 与两个距离相关——用户意图与系统能力之间的信息处理距离，以及输入语言和输出表示之间的关系。系统提供“行为上像对象本身”的表示，会产生直接操纵的感觉。
来源：https://vis.csail.mit.edu/classes/6.859/readings/pdfs/Hutchins-DirectManipulationInterfaces.pdf

## 同构转换

```text
CLI: intention -> recall command -> specify syntax -> execute -> inspect result
GUI: see object -> point/select -> manipulate -> immediate feedback
```

**[解释]** GUI 并没有消除复杂性，而是把复杂性从“用户记忆/语法”迁移到“系统可见表示/交互规则”。这就是为什么 GUI 是认知工程，而不只是视觉包装。
