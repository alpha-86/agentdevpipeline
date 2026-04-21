# PMO-2026-04-20-GOV-011 — Issue #3 HR#1 流程违规 + 变更追溯规则缺失

## 基本信息

| 字段 | 内容 |
|------|------|
| 级别 | P1 / Fail |
| 日期 | 2026-04-20 |
| 类别 | governance |
| 状态 | Open |
| 关联 Issue | #3 |
| 追踪 GitHub Issue | https://github.com/alpha-86/AgentDevFlow/issues/20 |

## 问题描述

Issue #3（gstack/superpower 增强层接入）在 PRD v4.1 迭代过程中，**PRD 变更后未重新走 Gate 1 → Gate 2 流程就并行更新了 Tech Spec 和 QA Case**，导致 Tech Spec v5 的"可选"语义与 PRD v4.1 的"强制依赖"语义不一致，Architect 在 HR#1 阶段发现并Reject。

## Issue #3 HR#1 全过程记录

### 时间线

| 日期 | 事件 | 违规点 |
|------|------|--------|
| 2026-04-15 | Issue #3 创建，PRD v1 起草 | — |
| 2026-04-15 | PRD v1 → v2（增加自动检测逻辑）| Gate 1 重新评审 ✅ |
| 2026-04-15 | Gate 1 + Gate 2 通过，HR#1 三方 Approved | — |
| 2026-04-16 | Issue #3 被错误关闭（HR#1 流程被跳过）| GOV-004 |
| 2026-04-17 | Issue #3 重新打开，按正式 Gate 流程返工 | — |
| 2026-04-17 | PRD v2 → v3（Human 反馈：统一检测一次）| Gate 1 重新评审 ✅ |
| 2026-04-17 | Gate 1（v3）三方签字完成：PM + Architect + QA | — |
| 2026-04-17 | **PRD v3 评审同时，Tech Spec v4 + QA Case v2 并行迭代** | **违规：PRD 变更后未先完成 Gate 1 → Gate 2** |
| 2026-04-17 | QA Case Design 在 Gate 1 最终签字前就开始起草 | 违规：Gate 2 还未完成就起草 QA Case |
| 2026-04-20 | PRD v3 → v4.1（增强层语义从可选→强制）| **PRD 发生重大语义变更** |
| 2026-04-20 | Tech Spec v5 完成，但 Section 4.3 中增强能力描述为"可选" | 与 PRD v4.1"强制依赖"语义冲突 |
| 2026-04-20 | HR#1 评审：QA Approved → Architect Rejected（语义冲突）| Architect 发现 PRD/Tech 不一致 |
| 2026-04-20 | Architect 修复 Tech Spec v5.1（可选→强制对齐）| Commit 73028fe |
| 2026-04-20 | HR#1 重新评审：QA + Architect 均 Approved | 流程恢复 |

### HR#1 评审结论

| 角色 | 结论 | 日期 |
|------|------|------|
| QA Engineer | Approved | 2026-04-20 |
| Architect | Rejected → Approved（修复后）| 2026-04-20 |

## 流程违规分析

### 违规点 1：PRD 变更后未重新走 Gate 1 → Gate 2

**正确的 Gate 流程**：
```
PRD 变更 → Gate 1（PRD Review）→ Gate 2（Tech Review）→ QA Case Design
```

**实际发生的流程**：
```
PRD v3 变更 → Gate 1（v3）→ 同时并行更新 Tech Spec v4 + QA Case v2 → 未等 Gate 2 完成就开始 QA Case
```

**问题**：
- PRD v3 发生变更（检测时机从"每个 agent"改为"start-agent-team 统一检测一次"，角色从 5 增加到 6）
- Tech Spec v4 和 QA Case v2 在 Gate 1（v3）还未最终确认时就开始并行迭代
- 这导致 Tech Spec v5 的"可选"语义与后续 PRD v4.1 的"强制依赖"语义不一致

### 违规点 2：Gate 2 未完成就起草 QA Case

根据 `prompts/002_develop_pipeline.md` Gate 2 进入条件：
- PRD `Approved`（Gate 1 通过）
- Tech Spec 文档已起草（`docs/tech/`）
- QA Case Design 已起草（`docs/qa/`）

但 QA Case Design 的起草依赖于 Tech Spec 已通过 Gate 2。在 Tech Spec 还处于 Draft 状态时并行起草 QA Case 会导致：
- QA Case 的内容可能与最终 Tech Spec 存在不一致
- 无法保证 QA Case 覆盖了所有 Tech Spec 要求

### 违规点 3：PRD v3 → v4.1 语义重大变更未重新走 Gate 1

| 版本 | 增强层语义 | 性质 |
|------|-----------|------|
| PRD v3 | "可选增强" | 增强能力为可选，开关打开后用户可选择使用 |
| PRD v4.1 | "强制依赖" | 开关打开 = 强制依赖 gstack/superpower，不可选 |

PRD 语义从"可选"变为"强制依赖"是**重大语义变更**，但未重新触发 Gate 1 评审流程。

## 变更追溯规则

| 变更来源 | 需重新通过的 Gate |
|---------|------------------|
| PRD 有**重大/语义**变更 | Gate 1（PRD Review）→ Gate 2 → QA Case Design |
| PRD 有**小幅/文档修正**变更 | 仅需原 Gate 签字人确认，无需重新完整 Gate 流程 |
| Tech Spec 有问题 | Gate 2（Tech Review）→ QA Case（如 QA Case 依赖 Tech Spec 变更）|
| QA Case 有问题 | 回到 QA Case 迭代，无需重新 Gate 1/2 |
| 多个环节都有问题 | 从头重新走 Gate 1 → Gate 2 → QA Case |

**重大变更定义**：
- 语义发生变化（可选→强制、单一→多个、范围扩大/缩小）
- 新增或删除交付域
- 角色数量变化
- 关键验收标准变更

**小幅变更定义**：
- 文档格式调整
- 错别字修正
- 描述文字澄清（不改变语义）
- 补充遗漏内容（不改变范围）

### 核心原则

> **PRD 变更后，必须先完成 Gate 1 重新评审，Gate 1 确认后才能进入 Gate 2，Gate 2 确认后才能更新 QA Case。Gate 流程不能并行迭代。**

## Human Review 的本质

Human Review 是面向 Human 的评审，**Agent 不能代替 Human 做决策**。

- HR#1 是否通过由 **Human** 决定
- Agent 只能出具评审意见（Approved / Conditional / Rejected）
- HR#1 的输入是 Gate 1 + Gate 2 全部通过后的文档包
- HR#1 通过的标准是 Human 确认设计文档符合要求

### HR#1 与 Gate Review 的区别

| 维度 | Gate Review | Human Review #1 |
|------|------------|-----------------|
| 评审主体 | Agent（PM/Architect/QA/Engineer）| Human |
| 评审对象 | 单个文档（PRD/Tech/QA Case）| 完整文档包 |
| 结论性质 | 技术可行性确认 | 设计确认（Human 决策）|
| 通过标准 | 签字完成 | Human 明确确认 |

## 影响范围

- **Issue #3**：HR#1 流程延迟，Tech Spec 语义与 PRD 不一致（已修复）
- **其他并行 Issue**：如存在类似并行迭代模式，可能有相同问题
- **机制**：缺乏变更追溯规则，导致 Gate 流程被并行化

## 纠正动作

| 动作 | 负责人 | 截止时间 | 状态 |
|------|--------|----------|------|
| 将变更追溯规则写入 `prompts/002_develop_pipeline.md` | Team Lead | 待定 | Pending |
| 在 `prompts/002_develop_pipeline.md` 明确 Gate 流程**不能并行** | Team Lead | 待定 | Pending |
| 补充"重大变更"和"小幅变更"的定义标准 | Team Lead | 待定 | Pending |
| 更新 `prompts/004_delivery_gates.md` 使其与 `002_develop_pipeline.md` 一致 | Team Lead | 待定 | Pending |
| PMO 增加 Gate 流程并行化检查项 | PMO | 待定 | Pending |

## 相关文件

- `docs/prd/003_adf_enhancement_layer_2026-04-17.md`（PRD v4.1）
- `docs/tech/003_adf_enhancement_layer_tech_2026-04-17.md`（Tech Spec v5.1）
- `docs/qa/003_adf_enhancement_layer_qa_2026-04-17.md`（QA Case v2）
- `docs/pmo/issues/008_2026-04-16_governance_issue3_hr1_skipped.md`（GOV-004，Issue #3 HR#1 被跳过）
- `docs/pmo/issues/006_2026-04-15_governance_hr1_gate3_circular_dependency.md`（GOV-003，HR#1 规范澄清）
- Commit `73028fe`（Tech Spec v5.1 修复可选→强制语义）

## PMO 结论

| 维度 | 结论 |
|------|------|
| **级别** | P1 / Fail |
| **结论** | Issue #3 HR#1 流程存在违规：PRD 变更后未正确重走 Gate 1 → Gate 2 流程，Tech Spec 和 QA Case 并行迭代导致语义不一致 |
| **已修复** | Tech Spec v5.1 已通过 Commit 73028fe 修复语义冲突，HR#1 当前全部 Approved |
| **待修复** | 变更追溯规则未写入规范，Gate 并行化问题缺乏机制约束 |
| **升级** | P1 流程问题，已通知 Team Lead |
