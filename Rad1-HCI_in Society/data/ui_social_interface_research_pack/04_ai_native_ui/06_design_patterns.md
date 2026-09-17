# Agent UI 设计模式草案


> **证据标签**
> - **[史实]**：有原始资料、官方文档或学术文献直接支撑。
> - **[解释]**：基于多条史实做出的分析性归纳，不等于当事设计团队的原话。
> - **[假说]**：可检验的理论延伸，尤其用于 AI-native UI 部分。
> - **[限制]**：与主叙事相冲突、限制其外推范围、或提醒避免后见之明的证据。


## Pattern A：Authority Badge
显示 principal、role、scope、expiry、signature/credential。

## Pattern B：Action Ledger
按时间记录：intent → plan → tool call → external side effect → evidence。

## Pattern C：Permission Surface
所有 sensitive capability 可见，并支持 one-click revoke。

## Pattern D：Approval Gate
在 spend、send、delete、publish、legal commitment 等 side effect 前显式停下。

## Pattern E：Memory Boundary
显示当前 agent 可读取的 memories/documents/projects，并说明 retention/scope。

## Pattern F：Provenance Stack
输出旁边不只显示 sources，还显示哪些 facts 来自 source、哪些是 inference、哪些未验证。

## Pattern G：Uncertainty / Failure Profile
不是单个“87% confidence”，而是：在哪类任务通常可靠、在哪类输入容易错、当前缺少哪些条件。

## Pattern H：Delegation Breadcrumb
```text
You -> Project Lead Agent -> Procurement Agent -> Vendor Portal
```
每一层都可看到授权关系和责任边界。

## Pattern I：Human Handoff
当 agent 进入能力边界时，不假装人格继续撑住，而是显示“需要哪个角色的人来接手”。

## Pattern J：Agent switch without character switch
切换 agent 时强调 capability/role 差异，而不是依赖头像/语气差异。
