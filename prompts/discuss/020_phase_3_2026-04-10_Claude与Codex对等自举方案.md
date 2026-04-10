# 020 Phase 3 - Claude 与 Codex 对等自举方案

## 目的

本文件用于执行 [020_2026-04-10_AgentDevFlow_1.0_自举里程碑执行计划](/home/work/code/AgentDevFlow/prompts/discuss/020_2026-04-10_AgentDevFlow_1.0_自举里程碑执行计划.md) 的 `Phase 3`，在 `Phase 2` 边界已锁定的前提下，明确：

1. `Claude Code` 如何复用现有 Agent Team 能力完成 AgentDevFlow 自举
2. `Codex` 如何复用现有多 agent 能力实现对等编排
3. 两个平台的共同主干是什么，差异点是什么
4. 后续平台入口文档和演练方案应如何落地

## 结论摘要

`Phase 3` 锁定以下平台对等方案：

1. **共同主干不变**
   - `Issue -> PRD -> Tech -> QA -> 文档确认 -> 实现 -> QA 验证 -> 代码确认 -> Release`
   - 双阶段 PR、Human Review、Issue Comment Gate、Todo、Memo、恢复机制保持一致
2. **Claude 侧复用 Agent Team**
   - 不重新发明 Team 机制
   - 由 Team Lead 按 AgentDevFlow 共享规则组织团队
3. **Codex 侧复用多 agent 调度**
   - 不模拟 Claude 的 Team 产品形态
   - 由主编排会话承担 `Team Lead 等效编排者`
   - 通过 `spawn_agent / send_input / wait_agent / close_agent` 承载多角色协作
4. **默认团队不强制包含研究支持**
   - `研究支持` 只在需要调研时启用
5. **正式角色口径使用 `架构师`**
   - 后续平台文档和共享角色入口都按这个名称收口

## 一、双平台共同主干

无论是 Claude 还是 Codex，1.0 自举都必须复用同一套共享资产和同一条阶段主线。

### 共同必读入口

1. 根 `README.md`
2. `docs/README.md`
3. `docs/governance/core-principles.md`
4. `docs/reference/dependencies.md`
5. `skills/shared/README.md`
6. `skills/shared/team-setup.md`
7. `skills/shared/start-agent-team.md`
8. `skills/shared/create-agent.md`
9. 当前阶段相关 `prompts/` 与 `workflows/`

### 共同默认角色

默认启用：

1. Team Lead
2. Product Manager
3. 架构师
4. QA Engineer
5. Engineer
6. Platform/SRE
7. Process Auditor

按需启用：

1. 研究支持

### 共同启动前置条件

在任何平台中，正式并发前必须先完成：

1. 确认 `project_id`
2. 确认主 issue 或本轮主工作索引
3. 建立：
   - `docs/prd/`
   - `docs/tech/`
   - `docs/qa/`
   - `docs/release/`
   - `docs/memo/`
   - `docs/todo/`
4. 建立或确认：
   - 启动会纪要
   - `TODO_REGISTRY`
   - 项目状态板
   - 产物关联主记录
5. 明确当前 Gate 和本轮人审节点

### 共同执行纪律

1. 角色未读完必读文档，不得开始正式判断
2. Team Lead 只协调，不越权签字
3. 关键 Gate 结论必须回到 Issue / PR / 正式文档
4. 文档阶段和代码阶段必须拆开
5. Comment 未真实落地，不得继续推进

## 二、Claude Code 方案

## 定位

Claude 已有 Agent Team 能力，因此 AgentDevFlow 在 Claude 侧的目标不是“再搭一套 Team 产品”，而是：

- 约束现有 Team Lead
- 约束角色装载顺序
- 绑定共享规则与工作流
- 保证团队按 AgentDevFlow 运转

## Claude 侧宿主复用

直接复用：

1. Claude Agent Team 能力
2. Claude 本地 skill 入口
3. Claude 已支持的多 agent 上下文切换和团队协作能力
4. Claude 可安装或已有的官方 / 社区技能

AgentDevFlow 自己补：

1. 启动入口顺序
2. Team Lead 必读链路
3. 角色创建约束
4. 共享 workflow / template 绑定
5. 平台最小检查与失败阻断规则

## Claude 侧 Team Lead 约束

Claude 中的 Team Lead 必须先完成以下动作，再允许创建其他角色：

1. 读取 `skills/shared/start-agent-team.md`
2. 读取 `skills/shared/team-setup.md`
3. 读取 `skills/shared/create-agent.md`
4. 读取：
   - `prompts/001_team_topology.md`
   - `prompts/002_product_engineering_roles.md`
   - `prompts/004_delivery_gates.md`
   - `prompts/013_github_issue_and_review_comments.md`
   - `prompts/019_dual_stage_pr_and_three_layer_safeguard.md`
5. 输出初始化确认：
   - 本轮 project_id
   - 主 issue
   - 当前 Gate
   - 已启用角色
   - 未启用但需兜底的职责

## Claude 侧角色装载顺序

推荐顺序：

1. Team Lead
2. Product Manager
3. 架构师
4. QA Engineer
5. Engineer
6. Platform/SRE
7. Process Auditor
8. 研究支持（按需）

## Claude 侧运行模型

1. Team Lead 负责启动团队
2. 各角色按 `create-agent` 统一入口加载
3. 每个角色先读自身主规范和 playbook
4. 在文档阶段：
   - PM 产出 PRD
   - 架构师产出 Tech Spec
   - QA 产出 QA Case
   - Human Review #1 确认文档 PR
5. 在实现阶段：
   - Engineer 实现
   - QA 验证
   - Human Review #2 确认代码 PR

## Claude 侧关键风险

1. 若 Team Lead 不先读共享入口，就会退化成平台默认 Team，而不是 AgentDevFlow Team
2. 若角色初始化不输出确认结果，后续很难验证是否真正按规则装载
3. 若 Comment / Gate 仍停留在聊天层，就无法证明真实自举

## 三、Codex 方案

## 定位

Codex 没有现成的 “Agent Team 产品壳”，但已有多 agent 编排能力。

因此 Codex 侧不追求“界面形态一致”，而追求“机制对等”：

- 共享规则一致
- 角色职责一致
- Gate 和人审一致
- 留痕和恢复一致

## Codex 侧宿主复用

直接复用：

1. `spawn_agent`
2. `send_input`
3. `wait_agent`
4. `close_agent`
5. 本地插件能力与工作区共享上下文

AgentDevFlow 自己补：

1. Team Lead 等效编排者定义
2. subagent 创建与回收规则
3. 角色提示装配规则
4. 文档 / Gate / Comment / 人审执行顺序

## Codex 侧 Team Lead 等效机制

Codex 中的主会话承担 `Team Lead 等效编排者`，职责包括：

1. 启动前读取所有共享入口
2. 建立主 issue / Gate / Todo / 状态板
3. 决定是否需要创建对应角色 subagent
4. 给每个 subagent 分配清晰职责和写入范围
5. 在关键 Gate 后回收、重派发或升级
6. 控制人审节点和最终收口

注意：

- 这里的“主会话编排者”是平台承载差异，不是 AgentDevFlow 在创造新角色
- 其语义上等价于 Team Lead 的组织职责，而不是额外新增角色

## Codex 侧角色装载方式

每个 subagent 在创建时都必须带上：

1. 角色定义
2. Critical Rules
3. 必读文档
4. 当前 Gate
5. 当前 issue / project_id
6. 允许写入的文件范围
7. 初始化后必须输出的确认格式

## Codex 侧推荐角色拆分

最小推荐并发：

1. Product Manager
2. 架构师
3. QA Engineer
4. Engineer
5. Process Auditor

按需补充：

1. Platform/SRE
2. 研究支持

## Codex 侧运行模型

1. 主会话先按 Team Lead 等效职责完成启动
2. 文档阶段按需并发：
   - PM
   - 架构师
   - QA
3. 文档确认后再派发 Engineer
4. 关键 Gate 由主会话统一判断是否允许进入下游
5. Process Auditor 可在关键 PR / Gate 节点并发检查
6. 所有子角色执行完毕后，主会话负责整合、验证、人审和关闭

## Codex 侧关键风险

1. 如果把所有工作都堆在主会话里，就失去多 agent 的对等价值
2. 如果 subagent 没有明确读物和写入范围，会退化成普通并行写手
3. 如果主会话不承担 Gate 管理，会出现角色各做各的、没有阶段边界

## 四、双平台差异清单

### 共同点

1. 同一套共享规则
2. 同一套角色职责
3. 同一套文档和交付物
4. 同一条 Gate 主线
5. 同一套人审与 Comment 约束

### 差异点

| 维度 | Claude | Codex |
|------|--------|-------|
| 多 agent 载体 | 现有 Agent Team | 主会话 + `spawn_agent` |
| Team Lead 载体 | 平台中的 Team Lead 角色 | 主会话承担 Team Lead 等效编排 |
| 角色初始化 | 通过 Team / skill 入口装载 | 通过创建 subagent 时注入上下文 |
| 团队生命周期 | 平台团队工作流 | 会话级编排与回收 |
| 入口文件诉求 | 强化 `.claude/skills` 入口 | 强化插件入口与编排说明 |

## 五、后续文档和实现要求

### 对平台入口文档的要求

后续平台文档必须从“最小安装说明”升级为“可执行入口”，至少包含：

1. 启动前必读
2. 默认角色顺序
3. 可选角色启用条件
4. Team Lead / Team Lead 等效编排者职责
5. 文档阶段与代码阶段的执行顺序
6. 最小检查与失败阻断规则

### 对适配层文件的要求

Claude 侧：

- `adapters/claude/.claude/skills/TEAM_SETUP.md` 必须改成真实入口
- 不再引用失效的 `prompts/zh-cn/`

Codex 侧：

- `plugins/agentdevflow/` 需要明确多 agent 编排入口
- 不再停留在只有 `plugin.json` 元数据

## 六、Phase 4 的输入要求

`Phase 4` 需要在本方案基础上继续细化：

1. 选取一个真实的 AgentDevFlow 改动主题，作为自举演练任务
2. 为 Claude 编写可执行演练脚本
3. 为 Codex 编写可执行演练脚本
4. 定义通过 / 失败标准
5. 明确证据收集要求

## 七、Phase 3 最终判断

到本阶段为止，Claude / Codex 的对等方案已经足够明确：

- Claude 复用 Agent Team
- Codex 复用多 agent 编排
- 共享规则、角色职责、Gate 主线和留痕要求保持一致

因此，下一步不再讨论“大方向是否成立”，而是直接进入 `Phase 4`，把演练和验收方案写成可执行脚本。
