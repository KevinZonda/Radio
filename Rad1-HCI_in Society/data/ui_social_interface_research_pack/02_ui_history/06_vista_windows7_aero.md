# Vista / Windows 7 Aero：从“哪里能点”到“系统现在是什么状态”


> **证据标签**
> - **[史实]**：有原始资料、官方文档或学术文献直接支撑。
> - **[解释]**：基于多条史实做出的分析性归纳，不等于当事设计团队的原话。
> - **[假说]**：可检验的理论延伸，尤其用于 AI-native UI 部分。
> - **[限制]**：与主叙事相冲突、限制其外推范围、或提醒避免后见之明的证据。


## Aero 的官方语义

Microsoft 的 Windows design guidance 将 Aero 展开为 **Authentic, Energetic, Reflective, Open**，并强调专业、美观、生产力与 emotional response。Vista icons 更 realistic，支持 256×256；在合适场景中，用内容 thumbnail 取代固定 document icon。
来源：https://learn.microsoft.com/en-us/windows/win32/uxguide/vis-icons

## Vista（2006）

glass、translucency、animation、Flip 3D、DWM compositing 让窗口更像一个持续的空间系统。

**[解释]** 透明并不天然等于可用性，但从信息结构看，它可承担 context preservation：前景与背景同时保留一些关系线索。

## Windows 7（2009）Taskbar

Microsoft 明确给新版 taskbar 三个目标：

1. single launch surface；
2. easy control / switching；
3. clean, noise-free, simple。
来源：https://learn.microsoft.com/en-us/archive/msdn-magazine/2009/brownfield/windows-7-taskbar-apis

### 一个关键抽象

旧 Windows：launch shortcut 与 running task 是不同 UI。
Windows 7：一个 app icon 同时承担 launch、switch、preview、progress、Jump List。

**[解释]** 内部的“可执行文件 / 进程 / 窗口”差异被进一步压缩成用户意图：“我要这个 app / 这个任务”。
