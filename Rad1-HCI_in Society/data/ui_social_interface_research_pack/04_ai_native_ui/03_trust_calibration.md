# 从“让人信任 AI”到“让人恰当地依赖 AI”


> **证据标签**
> - **[史实]**：有原始资料、官方文档或学术文献直接支撑。
> - **[解释]**：基于多条史实做出的分析性归纳，不等于当事设计团队的原话。
> - **[假说]**：可检验的理论延伸，尤其用于 AI-native UI 部分。
> - **[限制]**：与主叙事相冲突、限制其外推范围、或提醒避免后见之明的证据。


现代 Human-AI Interaction 越来越避免把“提高 trust”当成单向 KPI，而强调 **appropriate trust / calibrated trust / appropriate reliance**。

2024 ACM 系统综述整理了 appropriate trust、calibrated trust、warranted trust、appropriate reliance 等概念，并指出定义和测量仍不统一。
来源：https://doi.org/10.1145/3696449

PLOS One 2020 讨论 adaptive trust calibration，强调过度信任自动系统可能造成严重问题。
https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0229132

Microsoft CHI 2019 的 Human-AI Interaction Guidelines 也强调 AI 的失败模式、可理解性、可控性等新设计问题。
https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/

## 对“脸”的含义

**[解释]** 如果头像、声音、人格主要增加 familiarity / warmth，却不能帮助用户理解真实 capability 与 failure boundary，它可能提高“感觉信任”，却未必提高 appropriate reliance。

因此 AI-native UI 的设计目标应是：

> 让 reliance 与系统真实能力、授权和当前上下文更好地对齐，而不是单纯让 agent 更讨喜。
