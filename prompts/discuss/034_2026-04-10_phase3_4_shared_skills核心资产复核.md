# 034 - 2026-04-10 Phase 3.4 shared skills 核心资产复核

## 目标

确认 `skills/shared/` 是否已经足以构成插件核心资产层，而不是仍然停留在零散文件集合。

## 本次复核范围

### 1. 共享入口与协议

- `team-setup.md`
- `start-agent-team.md`
- `create-agent.md`
- `skill-protocol.md`
- `event-bus.md`

### 2. 共享角色

- Team Lead
- Product Manager
- Tech Lead
- Engineer
- QA Engineer
- Platform/SRE
- Process Auditor

### 3. 共享 workflow

- PRD Review
- Tech Review
- Human Review
- 日会
- Todo Review
- 周复盘
- 月复盘

### 4. 共享 template

- PRD / Tech / QA / Release / Memo / Todo / Review Comment 等正式留痕模板

## 复核结论

### 1. 已基本形成插件核心资产层

当前 `skills/shared/` 已经具备插件核心资产的最小闭环：

- 有启动入口
- 有共享协议
- 有核心角色
- 有核心 workflow
- 有正式模板

这说明它已经不再只是“文档配件”，而是插件最核心的共享执行层。

### 2. 当前最关键的缺口不是“缺很多文件”

当前更真实的缺口是三类：

1. `github-issue/SKILL.md` 对应的共享入口还不明确  
   现在 Issue 规则主要落在 `prompts/zh-cn/`，但 shared 层还缺更直接的入口映射。

2. `review-org/SKILL.md` 对应的共享入口还不明确  
   现在更多散落在 `prompts/discuss/` 执行口径和部分中文规则里，shared 层还没完全收口。

3. evaluation checker 还没有沉成 shared 子能力  
   当前仍主要体现在中文规则中的评审维度，而不是更独立的 shared 检查层。

### 3. 结论口径

因此，这一项的结论不是“已经完全完成”，而是：

- `skills/shared/` 已经能够作为插件核心资产层成立
- 但仍需继续补齐与 `github-issue`、`review-org`、evaluation checker 相关的 shared 承载方式

## 本次落地调整

在 `skills/shared/README.md` 中补充了正式判定：

- 为什么它已经能构成核心资产层
- 还缺哪几类关键承载入口

## 下一步

进入 `Phase 3.5`，继续检查 `prompts/zh-cn/` 是否已经足以构成插件规则层。
