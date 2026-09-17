# 从人类操作员到按钮、号码与认证：电梯 / 电话 / ATM


> **证据标签**
> - **[史实]**：有原始资料、官方文档或学术文献直接支撑。
> - **[解释]**：基于多条史实做出的分析性归纳，不等于当事设计团队的原话。
> - **[假说]**：可检验的理论延伸，尤其用于 AI-native UI 部分。
> - **[限制]**：与主叙事相冲突、限制其外推范围、或提醒避免后见之明的证据。


## 电梯

历史上电梯操作员承担“理解用户目标 + 操作复杂设备”的中介角色。自动控制成熟后，交互被压缩成：楼层按钮、亮灯反馈、开门/关门、状态显示。

**[解释]** 这是：person → person → machine，转成 person → interface → machine。

## 电话

早期电话大量依赖 operator 做 routing；自动交换和号码系统把“帮我接某个人”变成 addressable identifier。

**设计意义**：address 本身是一种高度抽象、但一旦文化内化就几乎无摩擦的 social primitive。

## ATM

柜员关系被拆成更形式化的 primitives：authentication、authorization、transaction、confirmation、receipt。

## 对 AI 的启发

今天 AI assistant 的人格层可能像“operator phase”。未来用户更关心：

```text
Goal -> Delegated
Access: Calendar ✓  Email ✓  Payments ✕
Progress: 3/7
Needs approval: Book $840 flight?
```

而不必每一步都通过拟人聊天完成。
