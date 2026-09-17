# Windows 95：最典型的“教学型系统 UI”


> **证据标签**
> - **[史实]**：有原始资料、官方文档或学术文献直接支撑。
> - **[解释]**：基于多条史实做出的分析性归纳，不等于当事设计团队的原话。
> - **[假说]**：可检验的理论延伸，尤其用于 AI-native UI 部分。
> - **[限制]**：与主叙事相冲突、限制其外推范围、或提醒避免后见之明的证据。


## 为什么这个案例极强

Microsoft 的 Kent Sullivan 在 CHI 1996 公开了 Windows 95 用户界面的 usability engineering case study。它记录了设计团队如何用快速原型和用户测试迭代 shell。
原文：https://chi1996.acm.org/proceedings/desbrief/Sullivan/kds_txt.html

## Beginner Shell：为什么被放弃

**[史实]** 团队曾做一个专门给初学者的简化 shell。测试暴露三个问题：功能不全时用户必须退出；学到的东西无法很好迁移到标准 shell；初学者 shell 与日常应用程序交互方式不同，等于要学两套系统。

**意义**：这是“脚手架不能与最终系统割裂”的直接历史案例。

## Start Menu：home base

**[史实]** Windows 95 的设计过程围绕“新手如何找到程序、从哪里开始”反复迭代。Start 不是计算机科学概念，而是一个高可见、统一的入口。

**[解释]** Start 是“把系统 topology 压成一个可见 home base”。

## Taskbar：让系统状态持续可见

**[史实]** 早期只改变 minimized windows 的外观并没有解决问题。测试显示真正的问题是：最小化后任务不再持续可见，用户不知道什么还开着。于是 taskbar 为每个 task 提供 persistent entry。
原文同上。

### 教学内容

Windows 95 实际上在教：

- 程序可以“仍在运行但不在眼前”；
- window visibility 与 task existence 不等价；
- 系统有统一入口；
- 当前 tasks 可以持续被看见、切换和恢复。

这比“拟物风格”更接近真正的 pedagogical UI。
