# Recognition、Consistency、Feedback、Forgiveness


> **证据标签**
> - **[史实]**：有原始资料、官方文档或学术文献直接支撑。
> - **[解释]**：基于多条史实做出的分析性归纳，不等于当事设计团队的原话。
> - **[假说]**：可检验的理论延伸，尤其用于 AI-native UI 部分。
> - **[限制]**：与主叙事相冲突、限制其外推范围、或提醒避免后见之明的证据。


## Recognition over recall

菜单、图标、可见状态把“你记得命令吗？”变成“你看到以后认得吗？”。

**[史实]** Xerox Star 的设计原则强调 seeing and pointing，而不是 remembering and typing；其经典设计文献把 familiar conceptual model、seeing and pointing、WYSIWYG、universal commands、consistency 等列为原则。
可查：Smith et al., *Designing the Star User Interface*, 1982；相关史料索引：https://archive.computerhistory.org/

## Consistency = 让一次学习复用

**[史实]** Lisa User Interface Standards 以 **simplicity** 与 **integration** 为两大目标，并强调建立在用户已熟悉概念上；一致的界面更容易学习。
转录：https://guidebookgallery.org/articles/lisauserinterfacestandards

**[史实]** Apple legacy iOS HIG 明确说 consistency 可以让人把一个 app 的知识和技能转移到另一个 app。
https://developer.apple.com/library/archive/referencelibrary/GettingStarted/RoadMapiOS-Legacy/chapters/RM_iHIG_Station/Fundamentals/Fundamentals.html

## Feedback = 让不可见计算变得可感知

按钮高亮、spinner、progress、selection、window activation、hover 等都在回答：

- 系统收到我的动作了吗？
- 当前对象是谁？
- 正在发生什么？
- 什么时候完成？

## Forgiveness = 让用户敢学

Undo、Trash、Cancel、confirmation 的意义不仅是“防错”，还降低探索成本。

**[解释]** 一个可逆系统比一个高惩罚系统更容易形成 exploratory learning。换言之，HCI 既在教“怎么做”，也在设计“犯错的代价”。
