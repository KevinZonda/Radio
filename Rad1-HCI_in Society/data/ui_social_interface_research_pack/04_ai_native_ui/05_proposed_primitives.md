# AI-native Interaction Primitives：一份候选词汇表


> **证据标签**
> - **[史实]**：有原始资料、官方文档或学术文献直接支撑。
> - **[解释]**：基于多条史实做出的分析性归纳，不等于当事设计团队的原话。
> - **[假说]**：可检验的理论延伸，尤其用于 AI-native UI 部分。
> - **[限制]**：与主叙事相冲突、限制其外推范围、或提醒避免后见之明的证据。


## 1. Delegate
把 goal、scope、deadline、resource boundary 明确交给 agent。

## 2. Inspect
查看当前 plan、evidence、tool use、pending dependencies。

## 3. Authorize
授予具体 capability / resource / spending / write permission。

## 4. Constrain
定义不可做、必须审批、数据边界、时间边界。

## 5. Approve / Reject
在高风险 checkpoint 给人类保留决策门。

## 6. Verify
核验 source、provenance、output、external confirmation。

## 7. Pause / Resume
把 agency 从连续 autonomous mode 切换成静止/继续。

## 8. Revoke
撤回 credential、memory access、tool access、delegation。

## 9. Handoff
把任务从一个 agent 转移给另一个 agent 或 human role，并保持 context provenance。

## 10. Audit
回看“谁在什么时候基于什么信息做了什么”。

## 11. Escalate
触发 human expert / supervisor / policy owner。

## 12. Declare uncertainty
不仅给 confidence，还展示 failure mode、缺失信息和不可验证部分。

**[假说]** 如果这些 primitives 像 drag/drop 一样文化化，人类对 agent 的 mental model 将不再主要依赖“把它当一个人”。
