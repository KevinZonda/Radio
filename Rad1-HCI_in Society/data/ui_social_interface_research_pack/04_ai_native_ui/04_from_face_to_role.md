# 从 Face UI 到 Role UI


> **证据标签**
> - **[史实]**：有原始资料、官方文档或学术文献直接支撑。
> - **[解释]**：基于多条史实做出的分析性归纳，不等于当事设计团队的原话。
> - **[假说]**：可检验的理论延伸，尤其用于 AI-native UI 部分。
> - **[限制]**：与主叙事相冲突、限制其外推范围、或提醒避免后见之明的证据。


## Face UI

今天常见的 AI social cues：

- name
- avatar
- voice
- first person “I”
- personality
- typing indicator
- emotive language

它们的优势：极低学习成本，直接调用人际交往模型。

它们的问题：可能暗示不存在的连续人格、责任、意图、记忆边界或能力。

## Role UI

候选替代层：

```text
Identity: Procurement Agent #P-184
Principal: ACME Inc.
Role: Purchasing
Capabilities: quote / compare / order
Spend authority: <= $25,000
Human approval: > $5,000
Data sources: ERP, vendor catalog, policy v12
Memory scope: Project Atlas only
Current objective: acquire 40 monitors
Last action: requested 3 quotes
Audit log: available
Revoke access: [button]
```

## 核心转向

**[假说]** 成熟 agent UI 会把“社会可读性”从 personality cues 移到 institutional cues：

face → role
charm → competence boundary
identity vibe → credential
conversation → delegation state
trust feeling → auditability / control
