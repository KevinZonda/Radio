# 一页论点：UI 是“计算本体”的社会教学层


> **证据标签**
> - **[史实]**：有原始资料、官方文档或学术文献直接支撑。
> - **[解释]**：基于多条史实做出的分析性归纳，不等于当事设计团队的原话。
> - **[假说]**：可检验的理论延伸，尤其用于 AI-native UI 部分。
> - **[限制]**：与主叙事相冲突、限制其外推范围、或提醒避免后见之明的证据。


## 1. 核心命题

**[解释]** UI 的历史可以理解为一种“认知责任转移”：早期用户需要学习机器的内部逻辑；成熟 UI 越来越把机器状态外显、把命令变成对象、把操作变成直接动作，并通过一致性把一次学习转移到整个生态。

**[史实]** 1985 年 Hutchins、Hollan、Norman 对 direct manipulation 的分析强调：当系统提供“行为上像对象本身”的表示时，用户意图与机器机制之间的距离会缩短。
来源：https://vis.csail.mit.edu/classes/6.859/readings/pdfs/Hutchins-DirectManipulationInterfaces.pdf

**[史实]** Carroll、Mack、Kellogg 1988 讨论 interface metaphor 时指出，隐喻可以增加目标域的初始熟悉度，但最终目标是让用户形成对目标域自身的 mental model。
来源：https://www.sciencedirect.com/science/article/pii/B9780444705365500087

## 2. UI 历史中的五步模型

```mermaid
flowchart LR
A[陌生计算本体] --> B[借用熟悉隐喻]
B --> C[外显状态与可操作性]
C --> D[交互惯例被社会内化]
D --> E[撤除显式脚手架]
E --> F[用原生数字属性表达关系/状态]
```

- **Xerox Star / Lisa / Macintosh**：把文件系统翻译成办公室对象，把“记忆命令”变成“看见并指向”。
- **Windows 1–3.x**：把程序、窗口、文件和 GUI 语法逐渐标准化。
- **Windows 95**：进一步解决“系统状态不可见”：Start 作为 home base，Taskbar 持续显示 running tasks。
- **Aqua / XP / Aero**：从纯教学扩展到情感、空间、状态、层级与任务管理。
- **iOS 1–6**：触屏陌生时，用 object metaphor + physical motion + direct manipulation 降低学习门槛。
- **Metro / iOS 7**：更多假设用户已掌握数字交互语法；开始减少显式现实物件外观。
- **Material / Fluent**：重新引入 shadow、motion、depth、material，但主要表达数字层级和状态，而不是假装软件“真的是一本皮革通讯录”。

## 3. 社会同态

**[解释]** 现代社会本身也不断把“面对面的个人关系”抽象成“角色、凭证、协议和制度”。

```mermaid
flowchart LR
F[认识这张脸] --> S[符号/制服/印章]
S --> R[角色]
R --> C[凭证/权限]
C --> P[协议/流程]
P --> I[基础设施]
```

钱把交换从具体关系抽象成媒介；公司把多人组织成一个可持续的法律主体；交通把路口谈判转为 protocol；排队和取号把人格/权势暂时压缩为位置；电话和电梯把 operator 转成 address/button。

## 4. 对 AI 的延伸

**[史实]** CASA 研究显示，人会自动对计算机使用社会规则，并不需要真的相信机器“是人”。
DOI: 10.1145/259963.260288

**[史实]** Epley 等人的 anthropomorphism 理论指出，人会把人类知识、动机和意图投射到非人行动者上，这与理解、控制和社会联结动机有关。
DOI: 10.1037/0033-295X.114.4.864

**[假说]** 因此，头像、名字、声音、第一人称、“正在输入……”等可能相当于 AI 时代的 skeuomorphic scaffolding：用“人”的社会模型解释陌生的 agentic system。

**[假说]** 成熟的 AI-native UI 可能逐渐从 character design 转向 institutional / protocol design：

- role
- authority
- scope
- capability
- provenance
- uncertainty
- memory boundary
- delegation chain
- approval state
- audit trail
- revoke / handoff / override

一句话：**从“它像谁”转向“它在什么制度关系里、拥有什么行动权、为什么可被信任或不被信任”。**
