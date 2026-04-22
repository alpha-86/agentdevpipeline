---
name: ADF Bootstrap Skill System Enhancement — Tech Spec v1
description: 基于 PRD #005 的当前有效 Tech Spec，定义 bootstrap 文档补齐、角色能力边界文档化与 doc-pr-checks.yml Gate 检查修复方案
status: Draft
owner: Architect
date: 2026-04-21
update_date: 2026-04-21
issue: "#5"
prd: docs/prd/005_adf_bootstrap_skill_system_2026-04-15.md
---

# Tech Spec #005 — AgentDevFlow Bootstrap: 技能系统、文档与自动化流程（v1）

---

**ID**: Tech-5_v1
**状态**: Draft
**负责人**: Architect
**日期**: 2026-04-21
**更新日期**: 2026-04-21
**基于**: PRD #005（Approved, 2026-04-15）
**当前评审状态**: 待进入 Gate 2 Tech Review（PM + QA + Engineer）

---

## 上下文

PRD #005 已批准，目标是在 AgentDevFlow 仓库自身补齐三类能力：

1. ADF bootstrap-sync 机制文档化
2. AgentDevFlow 接入与角色协作文档化
3. `doc-pr-checks.yml` Gate 检查逻辑修复与 CI 配置说明

本 Tech Spec 将产品层需求落到当前仓库可执行的技术交付面，作为 #5 当前有效 Tech Review 输入。

## 架构

### 1. 交付分层

Issue #5 的技术交付分为两层：

- **文档层**：在 `docs/`、`README.md`、`skills/*/SKILL.md` 中补齐用户接入、角色能力边界、bootstrap-sync 说明与 CI 配置说明
- **自动化层**：在 `.github/workflows/doc-pr-checks.yml` 中修复 Gate 签字检查逻辑

### 2. 文档域拆分

| 交付域 | 目标 | 主要位置 |
|---|---|---|
| bootstrap-sync 机制文档 | 解释源文件→产物映射、触发条件、故障排查、验证方法 | `docs/guides/`、`README.md` |
| 接入指南 | 覆盖新建项目 / 接入已有项目 / 启动多 Agent 团队 | `docs/guides/` |
| 角色能力边界文档 | 明确 prompt 约束、skill 能力、角色最小接口、失败模式 | `skills/*/SKILL.md`、补充说明文档 |
| CI 配置说明 | 解释 Gate 检查与 workflow 行为 | `docs/guides/` |

### 3. Gate 检查修复技术方案

针对 PRD 4.4.1 的 P0 要求，`doc-pr-checks.yml` 的 Gate 检查采用以下原则：

- 从 markdown Review Record 表格行中做**结构化匹配**，而不是仅做关键词 grep
- Gate 缺少必需签字时必须 `exit 1`
- Gate 1 角色名统一为 **架构评审人**
- QA Case Design 检查三方签字：**PM + 架构评审人 + Engineer**

推荐实现方式：

- 在 workflow bash 步骤内使用明确正则校验 Review Record 表格行
- 对每个 Gate 输出缺失角色的明确错误信息
- 保持修复范围只在 `doc-pr-checks.yml`，不改 `bootstrap-sync.yml` 与 `bootstrap-sync.py`

## 接口

### 1. 文档接口

| 输入 | 输出 |
|---|---|
| PRD #005 | Tech Spec #005 |
| Tech Spec #005 | QA Case Design #005 |
| bootstrap-sync 现状 | 映射表 / 安装前置 / 故障排查 / 验证说明 |
| 角色现状文档 | 角色能力边界说明 |
| CI workflow 现状 | Gate 检查修复 + 配置说明 |

### 2. 文件级改动接口

| 类型 | 路径 | 动作 |
|---|---|---|
| 代码 | `.github/workflows/doc-pr-checks.yml` | 修改 |
| 文档 | `docs/guides/*` | 新建/补充 |
| 文档 | `README.md` | 补充入口与交叉引用 |
| 角色文档 | `skills/*/SKILL.md` | 补充能力边界与协作接口 |

## 数据流

```text
PRD #005 Approved
    ↓
Tech Spec #005 Draft / Review
    ↓
QA Case Design #005
    ↓
文档与 workflow 修改
    ↓
文档 PR / Human Review #1
```

### 执行流

```text
1. 先补齐 Tech Spec 与 QA Case
2. 再进入文档/CI 改动实施
3. `doc-pr-checks.yml` 修复后用于后续 doc PR Gate 阻断
4. 文档 PR 合并后才允许进入下游实现/收口动作
```

## 可测试性

### QA 可直接据此起草 Case 的验证面

1. **bootstrap-sync 文档完整性**
   - 是否存在映射表
   - 是否说明触发条件、安装前置、故障排查、验证方法

2. **接入指南完整性**
   - 是否覆盖新建项目、接入已有项目、启动多 Agent 团队三场景
   - 是否存在交叉引用链路

3. **角色能力边界完整性**
   - 6 个角色是否有 prompt 约束与 skill 能力映射说明
   - 是否定义 Issue 评论格式、Gate 留痕、文档追溯链
   - 是否记录常见失败模式与纠正机制

4. **CI Gate 修复正确性**
   - 缺签字时 workflow 必须失败
   - Gate 1 使用“架构评审人”
   - QA Case Design 三方签字检查正确
   - 错误输出可指出缺失角色与修复方法

## 风险

| 风险 | 级别 | 缓解 |
|---|---|---|
| 文档说明与实际 bootstrap-sync 行为漂移 | 高 | 文档直接引用仓库现状并在同 PR 中交付 |
| Gate 检查正则过严或过松 | 高 | QA Case 中覆盖正例/反例；以结构化表格行为基准 |
| 修复范围扩散到 bootstrap-sync 脚本本体 | 中 | 明确仅修改 `doc-pr-checks.yml` |
| 角色边界文档补充后与 SKILL 实际内容不一致 | 中 | 逐角色核对后修改，不引入抽象性新规则 |

## 发布推进

1. Gate 2 通过后，QA 起草 #5 QA Case Design
2. QA Case 通过后，进入文档与 workflow 修改
3. 形成文档 PR，等待 Human Review #1
4. HR#1 通过并合并后，再进入后续实现/收口

## 回滚

- 若 `doc-pr-checks.yml` 修复导致误判，可回滚 workflow 变更但保留文档补充
- 若文档结构不合理，可在文档 PR 阶段重审，不影响主流程定义
- 若角色边界说明与现行规则冲突，以 PRD / prompts 主规则为准并触发文档修订

## 评审记录

| 日期 | 评审人 | 备注 | 决策 |
|---|---|---|---|
| 2026-04-21 | Architect | 补齐当前有效 Tech Spec，解除 #5 无 Tech 文档 blocker | Draft |

## 版本历史

| 版本 | 日期 | 变更说明 | 变更人 |
|------|------|---------|-------|
| v1 | 2026-04-21 | 首次补齐 #5 当前有效 Tech Spec Draft | Architect |

## 前序文档追溯链

基于：`docs/prd/005_adf_bootstrap_skill_system_2026-04-15.md`
Tech Spec 依赖：PRD #005 Approved

## 评审记录表

| 评审日期 | 评审节点 | 评审结果 | 评审人 | 意见/打回原因 | 修改后版本 |
|----------|---------|---------|-------|-------------|-----------|
| 2026-04-21 | Gate 2 | 待评审 | PM + QA + Engineer | — | v1 |
