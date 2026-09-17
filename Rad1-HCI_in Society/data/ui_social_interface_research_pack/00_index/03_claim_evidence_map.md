# 论点—证据地图


> **证据标签**
> - **[史实]**：有原始资料、官方文档或学术文献直接支撑。
> - **[解释]**：基于多条史实做出的分析性归纳，不等于当事设计团队的原话。
> - **[假说]**：可检验的理论延伸，尤其用于 AI-native UI 部分。
> - **[限制]**：与主叙事相冲突、限制其外推范围、或提醒避免后见之明的证据。


## A. 强支撑

| 论点 | 支撑强度 | 主要证据 |
|---|---|---|
| 隐喻可帮助用户借已有知识理解新域 | 强 | Carroll et al. 1988；Apple HIG |
| direct manipulation 可降低意图与机器机制之间的认知距离 | 强 | Hutchins, Hollan & Norman 1985；Shneiderman 1983 |
| consistency 可促进 knowledge transfer | 强 | Lisa UI Standards；Apple HIG；Windows platform guides |
| Windows 95 设计明确以新手 learnability 为目标 | 很强 | Sullivan 1996 case study |
| Taskbar 来自“用户看不到已开任务”这一可见性问题 | 很强 | Sullivan 1996 case study |
| iOS 旧 HIG 明确把 metaphor 与快速理解联系起来 | 强 | Apple legacy HIG |
| iOS 7 明确减弱 physicality/realism，同时增强 realistic motion 与 layers | 很强 | iOS 7 Transition Guide |
| Metro 明确强调 content not chrome / authentically digital | 强 | Microsoft MSDN/BUILD 资料 |
| Material 的设计团队明确从纸的光影/运动抽象规则 | 很强 | Google Design 回顾 |

## B. 中等支撑 / 需要谨慎措辞

| 论点 | 风险 | 建议写法 |
|---|---|---|
| “拟物是为了教育新用户” | 很多设计确实利用 metaphor，但不一定是唯一目的 | 写成“具有脚手架功能”，不要写“唯一原因” |
| “扁平化因为教育完成” | 缺乏单一因果证明；还有审美、品牌、性能、跨屏等因素 | 写成“当 conventions 被内化后，减少显式现实提示变得更可行” |
| “Aero 的 glass 是 context preservation” | 有合理设计解释，但并非所有玻璃效果都出于教学 | 标为解释，不写成官方意图 |
| “Material 是 physics-level skeuomorphism” | 有很强材料/纸张来源支撑，但这个术语是分析性命名 | 标为解释/术语提议 |

## C. 明确的研究假说

1. **Skeuomorphism : digital object = Anthropomorphism : digital agent**。
2. AI 头像、名字、声音、第一人称是“社会拟物”或“主体脚手架”。
3. AI-native UI 的成熟标志不是“更像人”，而是能直接表达 agency、delegation、authority、provenance、accountability。
4. 社会制度史可被视为一系列 face-based coordination → role/protocol-based coordination 的抽象过程。

## D. 反证与限制

- Oswald 2018：older / inexperienced users 并没有稳定地从 skeuomorphic UI 获益，结果对“拟物天然更好学”的简单命题构成挑战。
  https://www.scienceopen.com/hosted-document?doi=10.14236%2Fewic%2FHCI2018.57
- 2020 的年龄比较研究又发现 older adults 在一些任务上对 flat UI 更慢或更不准，说明结果依赖任务、设计细节和人群。
  DOI: 10.1080/0144929X.2020.1814867
- anthropomorphism 有时提高信任，但“更多信任”不是 HAI 的目标；当前研究更重视 **appropriate reliance / calibrated trust**。
