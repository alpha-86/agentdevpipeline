---
name: AgentDevFlow gstack/superpower 增强层接入
description: 明确 gstack / superpower 作为 AgentDevFlow 能力增强层的接入方式、角色映射和边界约束
status: In Review
owner: Product Manager
date: 2026-04-17
update_date: 2026-04-20
issue: "#3"
---

# PRD #003 — AgentDevFlow gstack/superpower 能力增强层接入

## 1. 背景

AgentDevFlow 与 gstack、superpower 三个项目解决的问题层级不同：

- `gstack`：偏工具与任务工作流，增强单个 Agent 的执行能力
- `superpower`：偏通用方法论与执行模式，增强单个 Agent 的规划、拆解和协作能力
- `AgentDevFlow`：偏多 Agent 的交付流程层，定义 Issue / PRD / Tech / QA / Gate / Human Review / Release 的正式协作机制

当前 README.md 已明确三者差异，但尚未有正式决策：gstack / superpower 是否可以作为 AgentDevFlow 的能力增强层接入，以及如何接入。

关联讨论：`prompts/discuss/028_2026-04-14_gstack与superpower增强层接入方案.md`

## 2. 问题

当前 AgentDevFlow 缺少对 gstack / superpower 增强层的正式接入规范，导致：

- **接入决策模糊**：是否引入增强层、增强层与正式流程的关系未明确
- **边界不清晰**：增强层输出与正式交付物的关系未定义
- **各角色增强路径不明**：哪些角色在哪些阶段适合启用哪些增强能力未梳理

## 3. 目标

建立 AgentDevFlow 的"gstack/superpower 能力增强层"接入规范，包括定位声明、角色映射、边界约束，并落地到文档。

## 4. 范围

### 4.1 增强层定位声明

在 README.md 或平台接入文档中明确：

- `gstack / superpower` 作为 AgentDevFlow 的"能力插件层"，不替代 AgentDevFlow 本身的流程约束层
- 三者定位关系：工具层（gstack）+ 方法层（superpower）+ 流程层（AgentDevFlow）
- **开关语义**：增强层安装后即启用，开关打开 = 强制依赖 gstack/superpower，卸载即回落 AgentDevFlow 原生机制

### 4.2 角色增强映射

明确各角色在哪些 Gate 阶段使用增强能力：

| 角色 | 增强能力范围 | 适用 Gate | 来源 |
|------|------------|---------|------|
| Product Manager | brainstorming、方案评审增强 | Gate 0（启动）/ Gate 1（PRD 评审前）| superpower、gstack |
| Architect | 方案评审增强 | Gate 2（Tech Spec 起草前）/ HR#1（设计评审）| gstack、superpower |
| QA Engineer | 验证覆盖增强 | Gate 4（QA 验证阶段）/ HR#2（实现确认）| gstack |
| Engineer | 代码审查增强、问题定位增强 | Gate 3（开发阶段）/ 修 Bug / 代码 PR 前 | gstack |
| Team Lead | 流程改进增强 | Gate 0（团队启动）/ Gate 5（发布评审）| superpower、gstack |
| PMO | 流程审计增强 | Gate 0 / Gate 5 / 流程合规检查 | superpower、gstack |

> **强制增强语义**：开关打开后，上述增强能力在对应 Gate 阶段自动触发，无需手动选择。当增强能力可用时，角色在适用阶段强制使用增强能力；当未安装时，回落 AgentDevFlow 原生机制。

### 4.3 增强层输出边界约束

明确增强层输出不能替代正式交付物：

- 增强能力生成的内容只能作为：分析过程、补充视角、评审建议、质量增强输入
- 不能替代以下正式交付物：PRD、Tech Spec、QA Case Design、QA Report、Issue Comment、正式评审结论

## 5. 非目标

- 不改造 AgentDevFlow 核心流程（Issue/Gate/PR/Human Review）
- 不在本 PRD 中描述技术实现细节（技术选型、接口设计、代码方案）
- 不改造 AgentDevFlow 产生 gstack / superpower 之外的新流程能力边界
- **不提供开关关闭机制**：一旦用户选择安装增强层，即进入强制依赖模式，不支持选择性关闭某个增强能力

> **注**：原"不将 gstack/superpower 作为强依赖"已删除。增强层安装后，开关打开 = 强制依赖，不能作为可选存在。

## 6. 用户故事

### US-1：强制增强者
> 作为 AgentDevFlow 用户，我希望安装 gstack/superpower 后在各 Gate 阶段自动获得强制增强能力，确保增强能力不被遗漏或跳过。

### US-2：无缝回落者
> 作为 AgentDevFlow 用户，我希望在未安装增强层时自动回落 AgentDevFlow 原生机制，不需要任何配置即可正常运行。

### US-3：质量增强者
> 作为使用 AgentDevFlow 的 QA Engineer，我希望在 QA 阶段强制获得验证覆盖增强，同时不改变正式 QA 报告的约束。

## 7. 验收标准

### 7.1 定位声明

- [ ] README.md 或平台接入文档中明确增强层定位（三者定位关系已说明）
- [ ] 增强层"增强角色不替代角色"原则已声明
- [ ] 开关语义已明确：开关打开 = 强制依赖 gstack/superpower

### 7.2 角色增强映射

- [ ] 各角色强制增强能力清单已梳理（6 个角色）
- [ ] 各角色增强能力的适用 Gate 阶段已明确
- [ ] 各角色增强能力的来源（gstack/superpower）已标注

### 7.3 输出边界

- [ ] 增强层输出不能替代正式交付物的约束已声明
- [ ] "增强能力负责增强思考，正式文件负责流程留痕"的口径已明确

### 7.4 安装前置

- [ ] 增强层安装前置条件（gstack skill 包 + superpower skill 包）已写入平台接入文档
- [ ] 开关打开后强制依赖语义已说明

## 8. 风险

| 风险 | 影响 | 缓解 |
|------|------|------|
| 增强层输出被误当作正式交付物 | 高：Gate 检查被绕过 | 文档中明确边界约束，增强能力输出不计入 Gate 签字 |
| 用户误以为可选但实际为强制依赖 | 高：安装后行为与预期不符 | 文档明确开关打开 = 强制依赖，不支持选择性关闭 |
| 文档口径与实际行为不一致 | 高：用户按文档操作后发现行为不符 | 文档变更需走 PR 评审 |

## 9. 依赖

- prompts/discuss/028_2026-04-14_gstack与superpower增强层接入方案.md（已有详细分析）
- README.md 当前内容（已包含三者差异 FAQ）

## 10. Gate 1 Review Record

| 日期 | 评审人 | 结论 | 关键意见 | 待办 |
|---|---|---|---|---|
| 2026-04-17 | PM | 起草完成，发起评审 | 符合新约束：禁止技术细节 | 等待 Architect + QA 签字 |
| 2026-04-17 | Architect | **Approved** ✅ | PRD v4 符合新约束：无技术选型/代码/接口/架构；Section 4 范围重构合理 | — |
| 2026-04-17 | QA | **Approved** ✅ | Section 7 验收标准覆盖完整，可测试性明确 | — |
| 2026-04-20 | PM | HR#1 迭代 — v4.1 | 明确 Gate 0~5 各阶段增强映射；开关打开 = 强制依赖；可选→强制增强 | 待 Human Review #1 重新签字 |

### Gate 2 评审（跨文档追溯）

| 文档 | Tech Spec #003 v4 | QA Case #003 |
|------|-------------------|---------------|
| 状态 | Approved ✅ | Approved ✅ |
| Engineer 签字 | Approved | — |
| QA 签字 | Approved | Approved |
| PM 签字 | PM 确认 Tech Spec 覆盖 PRD v4 ✅ | PM 确认 QA Case 覆盖 PRD v4 ✅ |

---

## 11. 评审记录

| 日期 | 评审人 | 备注 | 决策 |
|---|---|---|---|
| 2026-04-17 | PM | PRD 起草（符合新约束：禁止技术细节）| Draft |
| 2026-04-17 | Architect | Gate 1 签字：Approved — 符合新约束，无技术选型/代码/接口/架构 | Approved |
| 2026-04-17 | QA | Gate 1 签字：Approved — Section 7 验收标准覆盖完整 | Approved |
| 2026-04-20 | PM | PRD v4.1 迭代（HR#1 反馈）：Section 4.2 明确 Gate 0~5 阶段；Section 5 删除"非强依赖"；Section 6 可选→强制增强 | In Review |