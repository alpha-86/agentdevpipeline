---
name: AgentDevFlow gstack/superpower 增强层接入 — Tech Spec
description: 定义增强层接入的文档交付架构、角色映射、可测试性、风险与研发计划
status: In Review
owner: Architect
date: 2026-04-15
update_date: 2026-04-17
issue: "#3"
prd: docs/prd/003_adf_enhancement_layer_2026-04-17.md
---

# Tech Spec #003 — AgentDevFlow gstack/superpower 增强层接入

---

## 上下文

本 Tech Spec 对应 Issue #3 PRD #003 v3（2026-04-17）。

**PRD v3 关键变更**（基于 Human Comment #4259950108）：

1. **检测时机**：`start-agent-team` 启动时**统一检测一次**，结果在各 Agent 间共享，不再逐个 agent 重复检测
2. **角色映射**：5 角色 → **6 角色**（新增 PMO）
3. 增强层输出不能替代正式交付物和 Gate 结论
4. AgentDevFlow 本体在无增强层时仍可独立完整运行
5. skill 名称精确性属于**外部依赖**，由 Engineer 在实现阶段确认，Tech Spec 仅记录映射关系

**本 Tech Spec 范围**：纯文档交付，无代码实现。

---

## 架构

### 交付域分析

基于 PRD #003 v3，Issue #3 的交付内容分为 5 个文档域：

| # | 交付域 | 文档位置 | 操作 |
|---|--------|---------|------|
| 1 | 增强层定位总述 + 统一检测机制 | `docs/platforms/enhancement-layer.md` | 新建 |
| 2 | 增强层回落机制说明 | `docs/platforms/enhancement-layer.md` | 合并入域1 |
| 3 | 角色增强映射（6 角色）| 对应角色文档 | 修改 |
| 4 | 增强层安装与使用指南 | `docs/guides/enhancement-guide.md` | 新建 |
| 5 | 增强层边界说明（可做/不可做）| `docs/platforms/enhancement-layer.md` | 合并入域1 |

### 文档结构

```
docs/
├── platforms/
│   └── enhancement-layer.md    # 新建：增强层定位 + 统一检测机制 + 回落语义 + 边界说明
└── guides/
    └── enhancement-guide.md     # 新建：增强层安装与使用指南
README.md                       # 修改：补充增强层链接
skills/*/SKILL.md              # 修改：各角色文档补充可选增强 skill（6 角色）
```

### 增强层统一检测机制

**语义**：
- **统一检测**：`start-agent-team` 入口统一检测 gstack / superpower 是否已安装（只检测一次）
- **结果共享**：检测结果在各 Agent 间共享，无需重复检测
- **回落保障**：均未安装时自动回落 AgentDevFlow 原生机制 + 提示建议安装
- **零配置**：用户无需手动开启或关闭增强层

**用户视角**：
> "安装 gstack/superpower → 启动 start-agent-team → 自动检测一次 → 各 Agent 自动获得增强 → 卸载 → 自动回落原生机制"

---

## 接口

### 角色增强映射表

| 角色 | 可选增强 skill | 适用阶段 | 增强价值 | 验证状态 |
|------|--------------|---------|---------|----------|
| Product Manager | `brainstorming`, `plan-ceo-review` | 需求澄清、PRD 起草前 | 需求边界澄清、方案收敛 | ✅ |
| Architect | `plan-eng-review`, `brainstorming` | Tech Spec 起草前、技术评审前 | 架构边界收敛、风险识别 | ✅ |
| QA Engineer | `qa-only`, `qa` | QA Case Design 后、验证阶段 | 验证覆盖率、缺陷暴露率 | ✅ |
| Engineer | `review`, `investigate` | 开发前、代码 PR 前、修 Bug 时 | 结构化审查、根因定位 | ✅ |
| Team Lead | `brainstorming`, `plan-design-review`, `document-release` | 流程改进、发布后文档同步 | 机制设计质量 | ✅ |
| PMO | `brainstorming`, `plan-design-review`, `document-release` | 流程改进、接入文档优化、发布后文档同步 | 机制设计质量 | ✅ |

> **验证状态**：经 Engineer 验证，`plan-devex-review` → `plan-design-review`（gstack 中存在）。其余 skill 均已确认。

### 外部依赖验证项

| 依赖项 | 状态 | 说明 |
|--------|------|------|
| skill 名称与 gstack/superpower 包实际命名一致 | ✅ 已验证 | Engineer 确认：plan-devex-review → plan-design-review；其余 skill 均已确认 |
| gstack/superpower 包可用性 | 待实施 | 安装前置条件，文档说明安装来源 |

---

## 数据流

### 文档交付流程

```text
1. Engineer 确认 skill 名称（外部依赖验证）
        ↓
2. 创建 docs/platforms/enhancement-layer.md（增强层定位 + 统一检测 + 回落 + 边界）
        ↓
3. 创建 docs/guides/enhancement-guide.md（安装与使用指南）
        ↓
4. 修改各角色文档（6 个角色补充可选增强 skill）
        ↓
5. 修改 README.md（补充增强层链接）
        ↓
6. Human Review #1（文档 PR）
```

---

## 可测试性

### 文档验收测试

| # | 验证项 | 验证方法 | 预期结果 |
|---|--------|---------|---------|
| TC-1 | 增强层定位说明 | 文档搜索"能力插件层"或"增强层" | 文档可找到定位说明 |
| TC-2 | 统一检测机制说明 | 搜索"统一检测"关键词 | 文档明确说明 start-agent-team 入口统一检测一次 |
| TC-3 | 结果共享说明 | 搜索"共享"关键词 | 文档明确说明检测结果在各 Agent 间共享 |
| TC-4 | 回落机制说明 | 搜索"回落"关键词 | 文档明确说明未安装时的回落行为 |
| TC-5 | skill 名称与外部包一致 | Engineer 提供 skill 名称对照确认单 | 文档引用的 skill 名称与 Engineer 确认单匹配 |
| TC-6 | 6 角色文档包含增强 skill 引用 | 检查 6 个角色文档 | 每个角色文档至少有一条增强 skill 引用 |
| TC-7 | 增强层边界清晰 | 搜索"不能替代"或"边界" | 文档明确说明 skill 输出不能替代 Gate 结论 |
| TC-8 | 零配置语义 | 搜索"零配置"或"无需配置" | 文档明确说明用户无需手动配置 |
| TC-9 | 安装前置条件 | 检查 enhancement-guide.md | 文档包含 gstack + superpower 安装前置说明 |

---

## 风险

| 风险 | 级别 | 缓解 |
|------|------|------|
| skill 名称与 gstack/superpower 实际命名不一致 | **高** | Engineer 已验证；TC-5 记录验证方法 |
| 文档与 PRD v3 统一检测机制描述漂移 | 中 | Tech Spec 直接引用 PRD #003 v3 结论作为基准 |
| 统一检测时机与某些动态安装场景冲突 | 低 | 文档说明以 start-agent-team 启动时的检测结果为准；TC-3 覆盖结果共享验证 |

---

## 发布推进

### 阶段 1：文档创建与修改

- `docs/platforms/enhancement-layer.md`：增强层定位 + 统一检测 + 回落语义 + 边界说明
- `docs/guides/enhancement-guide.md`：增强层安装与使用指南
- 各角色文档：补充可选增强 skill 列表（6 个角色）
- `README.md`：补充增强层链接

### 阶段 2：文档 PR

- 分支：`doc-3-enhancement-layer`
- 包含：所有增强层相关文档修改

### 阶段 3：Human Review #1

- 评审人：PM + QA + Architect
- 重点：统一检测机制描述准确性、6 角色映射完整性

---

## 回滚

### 回滚方案

文档 PR 回滚：删除或 close `doc-3-enhancement-layer` PR。

### 回滚条件

- skill 名称与实际包命名不一致且无法在当前 PR 中修正
- 文档与 PRD v3 统一检测机制描述存在冲突

---

## 评审记录

| 日期 | 评审人 | 备注 | 决策 |
|---|---|---|---|
| 2026-04-15 | 架构师 | 初始起草（v1，基于手动开关方案） | Draft |
| 2026-04-15 | 架构师 | 更新至 v2：增强层改为自动检测+回落机制 | Draft |
| 2026-04-15 | QA Engineer | v1 Conditional 项已解决；TC-1~TC-8 覆盖完整 | Approved |
| 2026-04-15 | PM | PM 评审 v2 — 范围与 PRD v2 一致 | Approved |
| 2026-04-15 | 架构师 | Gate 2 Tech Review — 技术可行性确认 | Approved |
| 2026-04-15 | PM | Skill 名称验证更新 | v2.1 |
| 2026-04-15 | Team Lead | Gate 2 补签 | Approved |
| 2026-04-17 | 架构师 | 更新至 v3：PRD v3 迭代 — 统一检测（start-agent-team一次）+ 6角色映射 | Draft |
| 2026-04-17 | PM | Gate 2 发起评审 — Tech Spec + QA Case 均已起草 | In Review |
