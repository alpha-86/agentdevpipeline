---
name: ADF Bootstrap Skill System Enhancement — QA Case Design v1
description: 基于 PRD #005 与 Tech Spec #005 的当前有效 QA Case Draft，定义 bootstrap 文档补齐、角色能力边界文档化与 doc-pr-checks.yml Gate 检查修复的验证用例
status: Draft
owner: QA Engineer
date: 2026-04-21
update_date: 2026-04-21
issue: "#5"
prd: docs/prd/005_adf_bootstrap_skill_system_2026-04-15.md
tech: docs/tech/005_adf_bootstrap_skill_system_tech_2026-04-21.md
---

# QA Case Design #005 — ADF Bootstrap Skill System Enhancement

---

## 当前有效状态

- **当前有效版本**：v1 Draft
- **当前有效输入**：PRD #005 + Tech Spec #005 v1
- **当前阶段**：QA Case Design（待 PM + Architect + Engineer 三方评审）
- **规则说明**：本文件为 Issue #5 的当前有效 QA Case Draft，仅绑定当前仓库内已落地的 PRD 与 Tech 输入

## 追溯关系

- **PRD**: `docs/prd/005_adf_bootstrap_skill_system_2026-04-15.md`
- **Tech Spec**: `docs/tech/005_adf_bootstrap_skill_system_tech_2026-04-21.md`

### PRD #005 → QA Case 追溯矩阵

| PRD Section | 对应 TC | 覆盖状态 |
|-------------|---------|---------|
| 7.1 bootstrap-sync 机制文档 | TC-5-01, TC-5-02, TC-5-03, TC-5-04 | ✅ |
| 7.2 接入使用指南 | TC-5-05, TC-5-06 | ✅ |
| 7.3 Agent 角色能力边界文档 | TC-5-07, TC-5-08, TC-5-09 | ✅ |
| 7.4.1 CI 检查逻辑修复（P0） | TC-5-10, TC-5-11, TC-5-12, TC-5-13 | ✅ |
| 7.4.2 CI/CD 配置说明文档 | TC-5-14, TC-5-15 | ✅ |

### Tech Spec #005 → QA Case 追溯矩阵

| Tech Spec Section | 对应 TC | 覆盖状态 |
|-------------------|---------|---------|
| 交付分层 / 文档域拆分 | TC-5-01, TC-5-05, TC-5-07, TC-5-14 | ✅ |
| Gate 检查修复技术方案 | TC-5-10, TC-5-11, TC-5-12, TC-5-13 | ✅ |
| 文件级改动接口 | TC-5-03, TC-5-08, TC-5-10, TC-5-14 | ✅ |
| 可测试性 | TC-5-01 ~ TC-5-15 | ✅ |
| 风险与发布推进 | TC-5-04, TC-5-09, TC-5-15 | ✅ |

---

## TC-5-01：bootstrap-sync 映射表存在性验证

| 字段 | 内容 |
|------|------|
| 用例 ID | TC-5-01 |
| 标题 | bootstrap-sync 映射表存在性验证 |
| 追溯 | PRD 7.1 / 映射表；Tech Spec 文档域拆分 |
| 前置条件 | bootstrap-sync 机制文档已产出 |
| 测试步骤 | 1. 读取对应 guide 文档<br>2. 搜索源 skill → adf 产物映射表 |
| 预期结果 | 文档中存在完整映射表，覆盖被同步的 skill 源文件与 `.claude/skills/adf-*` 产物 |
| 验证方法 | 文档内容验证 |
| 优先级 | P1 |

## TC-5-02：安装前置与触发条件说明验证

| 字段 | 内容 |
|------|------|
| 用例 ID | TC-5-02 |
| 标题 | bootstrap-sync 安装前置与触发条件说明验证 |
| 追溯 | PRD 7.1 / 安装前置；Tech Spec 可测试性 |
| 前置条件 | bootstrap-sync 机制文档已产出 |
| 测试步骤 | 搜索 `Python 3.x`、`push to main`、依赖环境、触发条件等关键词 |
| 预期结果 | 文档明确说明 bootstrap-sync 依赖环境、触发条件与预期行为 |
| 验证方法 | 文档搜索 |
| 优先级 | P1 |

## TC-5-03：故障排查与验证方法说明验证

| 字段 | 内容 |
|------|------|
| 用例 ID | TC-5-03 |
| 标题 | bootstrap-sync 故障排查与验证方法说明验证 |
| 追溯 | PRD 7.1 / 故障排查、验证方法；Tech Spec 文件级改动接口 |
| 前置条件 | bootstrap-sync 机制文档已产出 |
| 测试步骤 | 1. 搜索至少 3 类失败模式<br>2. 搜索 hash / diff / 一致性验证说明 |
| 预期结果 | 文档覆盖至少 3 类已知失败模式，并说明如何通过 hash 或 diff 验证产物一致性 |
| 验证方法 | 文档内容验证 |
| 优先级 | P1 |

## TC-5-04：bootstrap 文档与仓库现状一致性验证

| 字段 | 内容 |
|------|------|
| 用例 ID | TC-5-04 |
| 标题 | bootstrap 文档与仓库现状一致性验证 |
| 追溯 | PRD 8 风险；Tech Spec 风险 |
| 前置条件 | bootstrap-sync 文档已产出 |
| 测试步骤 | 对照文档描述与当前仓库中的 `skills/`、`.claude/skills/`、workflow 路径 |
| 预期结果 | 文档描述不与当前仓库路径、命名空间、同步关系冲突 |
| 验证方法 | 文档交叉验证 |
| 优先级 | P1 |

## TC-5-05：新建项目 / 接入已有项目 / 启动团队三场景指南验证

| 字段 | 内容 |
|------|------|
| 用例 ID | TC-5-05 |
| 标题 | 三场景接入指南完整性验证 |
| 追溯 | PRD 7.2 / 三场景指南；Tech Spec 文档域拆分 |
| 前置条件 | 接入指南文档已产出 |
| 测试步骤 | 检查是否分别存在新建项目、接入已有项目、启动多 Agent 团队三个场景的说明 |
| 预期结果 | 三个场景均有清晰步骤说明，且内容与 PRD 范围一致 |
| 验证方法 | 文档内容验证 |
| 优先级 | P1 |

## TC-5-06：接入指南交叉引用链路验证

| 字段 | 内容 |
|------|------|
| 用例 ID | TC-5-06 |
| 标题 | 接入指南交叉引用链路验证 |
| 追溯 | PRD 7.2 / 交叉引用完整 |
| 前置条件 | 三场景指南已产出 |
| 测试步骤 | 检查新建项目、接入已有项目、启动多 Agent 团队三份指南之间的交叉引用 |
| 预期结果 | 三份指南形成完整链路，无孤立文档 |
| 验证方法 | 文档交叉验证 |
| 优先级 | P2 |

## TC-5-07：六角色能力映射文档化验证

| 字段 | 内容 |
|------|------|
| 用例 ID | TC-5-07 |
| 标题 | 六角色能力映射文档化验证 |
| 追溯 | PRD 7.3 / 六角色映射；Tech Spec 可测试性 |
| 前置条件 | 角色边界文档已补充 |
| 测试步骤 | 检查 PM、Architect、QA、Engineer、Team Lead、Platform-SRE 的 prompt 约束与 skill 能力映射说明 |
| 预期结果 | 六个角色均有明确映射关系说明 |
| 验证方法 | 文档内容验证 |
| 优先级 | P1 |

## TC-5-08：角色协作最小接口验证

| 字段 | 内容 |
|------|------|
| 用例 ID | TC-5-08 |
| 标题 | 角色协作最小接口验证 |
| 追溯 | PRD 7.3 / 最小接口；Tech Spec 文件级改动接口 |
| 前置条件 | 角色文档已补充 |
| 测试步骤 | 搜索 Issue 评论格式、Gate 留痕要求、文档追溯链等关键约束 |
| 预期结果 | 文档明确角色协作最小接口，不存在仅口头约定 |
| 验证方法 | 文档搜索 |
| 优先级 | P1 |

## TC-5-09：角色失败模式与纠正机制验证

| 字段 | 内容 |
|------|------|
| 用例 ID | TC-5-09 |
| 标题 | 角色失败模式与纠正机制验证 |
| 追溯 | PRD 7.3 / 失败模式；Tech Spec 风险 |
| 前置条件 | 角色边界文档已补充 |
| 测试步骤 | 检查是否列出不少于 3 个常见失败模式及对应纠正机制 |
| 预期结果 | 失败模式数量与纠正措施满足 PRD 要求 |
| 验证方法 | 文档内容验证 |
| 优先级 | P2 |

## TC-5-10：doc-pr-checks Gate 缺签字阻断验证

| 字段 | 内容 |
|------|------|
| 用例 ID | TC-5-10 |
| 标题 | doc-pr-checks Gate 缺签字阻断验证 |
| 追溯 | PRD 7.4.1 / P0-1；Tech Spec Gate 检查修复技术方案 |
| 前置条件 | `.github/workflows/doc-pr-checks.yml` 已修改 |
| 测试步骤 | 检查 workflow 中 Gate 检查步骤对缺签字场景是否返回非零退出码 |
| 预期结果 | 缺失必需签字时 workflow `exit 1`，不会仅输出 warning |
| 验证方法 | 配置阅读 + 执行路径验证 |
| 优先级 | P0 |

## TC-5-11：结构化正则检查验证

| 字段 | 内容 |
|------|------|
| 用例 ID | TC-5-11 |
| 标题 | Gate 结构化正则检查验证 |
| 追溯 | PRD 7.4.1 / P0-1；Tech Spec 技术方案 |
| 前置条件 | `.github/workflows/doc-pr-checks.yml` 已修改 |
| 测试步骤 | 检查 workflow 是否对 Review Record 表格行进行结构化模式匹配，而非简单关键词 grep |
| 预期结果 | 检查逻辑验证角色名、日期、结论字段同时存在 |
| 验证方法 | 配置阅读 |
| 优先级 | P0 |

## TC-5-12：Gate 1 角色名统一验证

| 字段 | 内容 |
|------|------|
| 用例 ID | TC-5-12 |
| 标题 | Gate 1 角色名统一验证 |
| 追溯 | PRD 7.4.1 / P0-2 |
| 前置条件 | `.github/workflows/doc-pr-checks.yml` 已修改 |
| 测试步骤 | 检查 Gate 1 检查逻辑是否使用“架构评审人”作为标准角色名 |
| 预期结果 | Gate 1 不再使用与 Gate 文档不一致的角色名口径 |
| 验证方法 | 配置阅读 |
| 优先级 | P0 |

## TC-5-13：QA Case Design 三方签字检查验证

| 字段 | 内容 |
|------|------|
| 用例 ID | TC-5-13 |
| 标题 | QA Case Design 三方签字检查验证 |
| 追溯 | PRD 7.4.1 / P0-2；Tech Spec 技术方案 |
| 前置条件 | `.github/workflows/doc-pr-checks.yml` 已修改 |
| 测试步骤 | 检查 QA Case Design 检查逻辑是否同时校验 PM + 架构评审人 + Engineer |
| 预期结果 | 缺失任一角色签字均判定为不通过 |
| 验证方法 | 配置阅读 |
| 优先级 | P0 |

## TC-5-14：CI 配置说明文档验证

| 字段 | 内容 |
|------|------|
| 用例 ID | TC-5-14 |
| 标题 | CI 配置说明文档验证 |
| 追溯 | PRD 7.4.2；Tech Spec 文档域拆分 |
| 前置条件 | CI 配置说明文档已产出 |
| 测试步骤 | 搜索 `doc-pr-checks.yml`、`issue-poll.yml`、`bootstrap-sync.yml` 的配置说明与行为描述 |
| 预期结果 | 文档覆盖三类 workflow 的配置说明、触发条件或行为说明 |
| 验证方法 | 文档搜索 |
| 优先级 | P1 |

## TC-5-15：CI 友好错误输出与等效部署说明验证

| 字段 | 内容 |
|------|------|
| 用例 ID | TC-5-15 |
| 标题 | CI 友好错误输出与等效部署说明验证 |
| 追溯 | PRD 7.4.2；Tech Spec 风险/发布推进 |
| 前置条件 | CI 配置说明文档与 workflow 修改已产出 |
| 测试步骤 | 1. 检查文档是否说明缺失签字时的错误输出口径<br>2. 检查是否存在可指导完成等效部署的说明 |
| 预期结果 | 文档说明缺失角色与修复方法，且部署说明足以支持使用者复现配置 |
| 验证方法 | 文档内容验证 |
| 优先级 | P1 |

---

## 当前评审状态

- **当前状态**：Draft
- **下一动作**：发起 QA Case Design 三方评审（PM + Architect + Engineer）
- **评审前提**：以本文件当前 Draft 为准，后续实现与文档修改不得绕过 QA Case 评审

## v1 Draft 变更说明（2026-04-21）

| 变更项 | 说明 |
|--------|------|
| 首次建立 QA Case | 基于 PRD #005 + Tech Spec #005 v1 建立当前有效 QA Case Draft |
| 覆盖范围建立 | 对 bootstrap 文档、接入指南、角色边界、CI Gate 修复建立追溯矩阵与测试用例 |
| 风险前置 | 将 Gate 正则误判、文档漂移、角色边界不一致纳入验证范围 |
