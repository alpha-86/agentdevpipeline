# 030 start-agent-team 能力对比与缺失分析

**日期**: 2026-04-14
**分析来源**: `prompts/by-me/005_V5_start-agent-team能力分析.md`
**对比基准**: hedge-ai `.claude/skills/start-agent-team/SKILL.md`
**重要说明**: 本文档所有根因主体均为 `skills/shared/start-agent-team.md`，`.claude/skills/adf-start-agent-team/SKILL.md` 是 bootstrap-sync 生成的重命名产物，不是根因主体。

---

## 一、需求回顾

1. 安排创建 agent team，让每个 agent 按照规定的方式去创建
2. 检查所有任务清单包括 GitHub Issue、`.claude/task_queue/`、todo 等
3. 基于第 2 项内容，召集团队开日同步会

---

## 二、hedge-ai 能力清单

> **注**：以下对比项中，带 ~~删除线~~ 的为 hedge-ai 特定业务运营机制，不属于通用研发流程，不应作为 AgentDevFlow 的缺失项。

### 2.1 Agent 创建机制

| 能力项 | hedge-ai 现状 |
|--------|---------------|
| Team 创建检查 | ✅ 有 Step 1.5，强制检查 Team 是否存在，不存在则创建 |
| Agent 创建命令 | ✅ 明确使用 TeamCreate tooling，按顺序创建 |
| Agent 必读文档分配 | ✅ 每个 Agent 有明确的必读文档速查表 |
| Agent 创建日志 | ✅ 记录到 `.claude/agent-creation-log.md` |
| 创建后立即初始化 | ✅ 创建完下一个 Agent 后直接继续，无确认环节 |

### 2.2 任务发现机制

| 能力项 | hedge-ai 现状 |
|--------|---------------|
| GitHub Issue 列表 | ✅ Agent 有触发条件关联 GitHub Issue |
| Todo 管理 | ✅ `WORKFLOWS/todo-management.md` |
| ~~每日四次 DBR~~ | ~~08:00, 12:00, 16:00, 20:00~~（业务运营节奏） |
| 日会内容覆盖 | ✅ 进展 + 阻塞 + 优先级 + 决策 + Todo |
| ~~会议记录三合一~~ | ~~save + git push + Telegram 摘要~~（业务运营机制） |

### 2.3 Agent 触发机制

| Agent | 触发条件 | 关联文档 |
|-------|---------|---------|
| Team Lead | 每日08:00 | daily-standup.md |
| CSO | 每周一11:00 | strategy-review.md（业务） |
| CRO | 每日16:00 | risk-report.md（业务） |
| PM Agent | 辩论触发条件满足 | strategy-debate.md（业务） |
| Backtest Agent | 策略回测完成时 | backtest-review.md（业务） |
| SRE | 每日08:00/16:00 | daily-standup.md |

---

## 三、`skills/shared/start-agent-team.md` 能力现状分析

> **注**：根因主体为 `skills/shared/start-agent-team.md`。`.claude/skills/adf-start-agent-team/SKILL.md` 只是 bootstrap-sync 的重命名产物。

### 3.1 Agent 创建机制

| 能力项 | `skills/shared/start-agent-team.md` 现状 | 判断 |
|--------|----------------------------------------|------|
| Team 创建检查 | ⚠️ `skills/shared/create-agent.md` 已定义 Team Lead 角色和创建规则，但 `start-agent-team` 未编排为自动执行流程 | 规则存在，**缺少自动编排** |
| Agent 创建命令 | ⚠️ `skills/shared/create-agent.md` 已定义 `create-agent` skill，但 `start-agent-team` 只描述"加载团队角色"，未给出执行步骤 | 规则存在，**缺少自动编排** |
| Agent 必读文档分配 | ✅ `skills/shared/create-agent.md` 中每个角色有明确的必读文档要求 | 已完整 |
| Agent 创建日志 | ✅ `skills/shared/create-agent.md` 要求记录创建日志 | 已完整 |
| 创建后立即初始化 | ✅ `skills/shared/create-agent.md` 定义了激活后立即检查 | 已完整 |

### 3.2 任务发现机制

| 能力项 | `skills/shared/start-agent-team.md` 现状 | 判断 |
|--------|----------------------------------------|------|
| GitHub Issue 发现 | ⚠️ `scripts/github_issue_sync.py` 存在，但 `start-agent-team` 未集成调用 | **缺少工具集成** |
| `.claude/task_queue/` 读取 | ⚠️ 目录存在，但 `start-agent-team` 未编排读取步骤 | **缺少流程编排** |
| Todo 管理 | ✅ `skills/shared/workflows/todo-review.md` 已定义，但无定时触发 | 规则存在，缺少触发 |
| 日同步会 | ✅ `skills/shared/workflows/daily-sync.md` 已定义，但 `start-agent-team` 未编排为启动步骤 | **缺少流程编排** |
| 会议记录 | ✅ `skills/shared/templates/memo-template.md` 等已定义，但三合一机制为业务运营语义 | 不适用于通用研发 |

### 3.3 Agent 触发机制

| 能力项 | `skills/shared/start-agent-team.md` 现状 | 判断 |
|--------|----------------------------------------|------|
| Issue 触发 Workflow | ✅ `skills/shared/workflows/issue-lifecycle.md` 已定义，但无触发集成 | 规则存在，**缺少触发编排** |
| 统一触发/编排闭环 | ⚠️ `scripts/task_router.py` 存在，但 `start-agent-team` 未编排路由步骤 | 工具存在，**缺少流程编排** |

---

## 四、核心差距总结

### 4.1 问题根因

**根因主体**：`skills/shared/start-agent-team.md`

```
问题：`skills/shared/start-agent-team.md` 需要"先检查 open issues"，
但源文件里没有任何 tooling 调用指令，只是告诉人类"去检查"。

bootstrap-sync 只做路径替换和 SKILL.md 生成，不会补全 tooling 调用。
```

### 4.2 tooling 能力现状

| tooling | 用途 | 现状 |
|---------|------|------|
| `scripts/github_issue_sync.py` | 发现/同步 GitHub Issues | ✅ 工具存在，`start-agent-team` 未集成 |
| `.claude/task_queue/` | 读取待处理任务 | ✅ 目录存在，未编排读取步骤 |
| `docs/todo/TODO_REGISTRY.md` | 读取 todo | ✅ 文档存在，未编排读取步骤 |
| `scripts/task_router.py` | 任务路由 | ✅ 工具存在，未编排触发 |
| `skills/shared/create-agent.md` | Agent 创建规则 | ✅ 规则存在，启动流程未编排 |

### 4.3 编排缺失的 workflow 能力

| workflow | 现状 |
|-----------|------|
| GitHub Issue 发现 -> 启动流程 | ❌ `start-agent-team` 未编排 github_issue_sync.py 调用 |
| task_queue 读取 -> 启动流程 | ❌ `start-agent-team` 未编排 task_queue 读取步骤 |
| todo 读取 -> 启动流程 | ❌ `start-agent-team` 未编排 todo 读取步骤 |
| issue -> Agent 路由闭环 | ⚠️ 已有 issue-routing.md 和 task_router.py，但缺少统一触发/编排闭环 |

---

## 五、GitHub Issue 能力迁移完整性检查

### 5.1 已迁移

| 文件 | 状态 |
|------|------|
| `skills/shared/workflows/issue-lifecycle.md` | ✅ 已迁移，有状态机设计 |
| `skills/shared/workflows/issue-routing.md` | ✅ 已迁移，有角色路由规则 |
| `scripts/task_router.py` | ✅ 已迁移，有路由脚本 |
| `.github/workflows/issue-status-sync.yml` | ✅ 已迁移 |
| `scripts/post_comments.py` | ✅ 已迁移 |

### 5.2 需补充编排

| 能力 | 现状 | 修复方向 |
|------|------|---------|
| Issue 发现 -> 启动流程 | ⚠️ github_issue_sync.py 存在，但 start-agent-team 未集成 | 在 `start-agent-team.md` 中编排调用 |
| 统一触发/编排闭环 | ⚠️ 已有路由规则和 task_router.py，但缺少触发层 | 设计触发机制 |

---

## 六、建议修复方向

### P0（立即修复）

1. **修改 `skills/shared/start-agent-team.md`，编排 GitHub Issue 发现步骤**
   - 调用 `scripts/github_issue_sync.py --sync-issues` 发现 open issues
   - 编排读取 `.claude/task_queue/` 目录
   - 编排读取 `docs/todo/TODO_REGISTRY.md`

2. **修改 `skills/shared/start-agent-team.md`，编排任务发现步骤**
   - 将 todo review 作为启动会前检查项

### P1（短期修复）

3. **补充 issue -> Agent 触发编排**
   - 在 `start-agent-team.md` 或独立 workflow 中定义触发机制
   - 与 `task_router.py` 集成

### P2（中期修复）

4. **补充 Team 创建检查步骤**
   - 在 `start-agent-team.md` 中编排 Team 状态检查
   - 参照 hedge-ai Step 1.5

---

## 七、结论

**根因主体**：`skills/shared/start-agent-team.md`

| 维度 | 判断 |
|------|------|
| **规则层面** | `create-agent.md`、`issue-lifecycle.md`、`issue-routing.md` 等已定义完整规则 |
| **工具层面** | `github_issue_sync.py`、`task_router.py` 等工具已存在 |
| **编排层面** | `start-agent-team.md` 未将规则和工具编排成可执行的启动流程 |
| **触发层面** | 缺少统一触发/唤醒/编排闭环 |

**缺失性质分类**：
- 规则缺失：❌ 无（规则已存在）
- tooling 缺失：❌ 无（工具已存在）
- **编排/触发缺失**：✅ 是（未编排进 start-agent-team 流程）

**不属于通用研发缺失项**（业务运营语义）：
- 每日四次 DBR（hedge-ai 特定业务节奏）
- DBR #1/#2/#3 差异化（A股市场特定）
- save + git push + Telegram 摘要三合一（Telegram 业务通知）

---

## 八、Codex Review 补充审计（2026-04-15）

### 8.1 本轮确认已修正的问题

1. **GitHub Issue 检查入口口径已修正**
   - 不应直接写成调用 `gh issue list`。
   - 本项目已经有统一脚本 `scripts/github_issue_sync.py`，`start-agent-team` 若要补齐 issue 检查能力，应优先通过该脚本发现 / 同步 open issues。

2. **真正应修改的对象是共享源 skill，不是别名产物**
   - `/adf-start-agent-team` 只是 `/start-agent-team` 在本项目 `.claude/skills/` 下的重命名产物。
   - 真正的源定义位于 `skills/shared/start-agent-team.md`。
   - 能力缺口、修复点、设计责任都应首先落在 `skills/shared/start-agent-team.md`。

3. **问题主体已统一为 `skills/shared/start-agent-team.md`**
   - 前文 4.1"自举悖论"和第七部分结论的主语已统一修正。

4. **缺失判断已区分三类**
   - 规则缺失
   - tooling 缺失
   - 编排 / 自动触发缺失

5. **hedge-ai 业务语境项已排除**
   - 每日四次 DBR、DBR #1/#2/#3 差异化、save+git push+Telegram 摘要已标注为业务运营语义，不列为通用研发缺失。

### 8.2 保留的争议点

无。

### 8.3 最终判断

文档前七节与第八节 Codex Review 补充审计已对齐：
- 根因主体：`skills/shared/start-agent-team.md`
- GitHub Issue 入口：`scripts/github_issue_sync.py`
- 缺失定性：编排/触发缺失，非规则或 tooling 缺失
- 业务运营语义项已排除
