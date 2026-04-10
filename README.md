# AgentDevFlow

AgentDevFlow 是一套面向软件研发交付的多 Agent 流程资产包。它关注的不是“单个 Agent 会不会写代码”，而是在多 Agent 编排和多轮迭代推进下，如何把需求澄清、方案评审、实现、测试、发布、留痕、恢复和人机协同 Gate 串成一个可执行闭环。

## 它解决什么问题

很多团队已经在用 Claude、Codex 或其他 Agent 工具，但真正容易失控的往往不是编码本身，而是协作过程：

- 需求、方案、实现、测试各做各的，缺少统一主线
- Agent 能持续产出，但关键节点缺少人工确认与签核
- Issue、PR、评论、Todo、Memo 分散，责任人和证据对不上
- 多个问题并行推进时，状态、优先级和上下文恢复成本很高
- 不同平台各写一套规则，流程越做越碎，重复造轮子

AgentDevFlow 的目标，是把这些问题沉淀成一套可复用的共享角色、workflow、template 和平台入口约束，让多 Agent 协作具备清晰的流程治理，同时保留人类在关键 Gate 上的判断权。

## 它怎么工作

AgentDevFlow 的主线不是“让 Agent 自己跑完一切”，而是建立一条明确的人机协同研发链路：

- `Issue 全流程`：从主 Issue 启动，所有关键产物和结论持续回链，最终也在 Issue 上完成验收与关闭
- `问题先于方案`：先澄清目标、边界、约束，再写 PRD
- `双阶段 PR`：文档 PR 先确认设计，代码 PR 再确认实现
- `Human Review #1 / #2`：设计确认和实现确认都必须有人类显式签核
- `Issue Comment Gate`：关键结论必须真正回写到 Issue，而不是停留在聊天里
- `正式留痕`：PRD、Tech、QA、Memo、Todo、Release、Change Record 都有明确落点
- `Process Auditor`：把流程合规检查作为独立职责，而不是靠参与者自觉
- `优先复用现成能力`：Claude、Codex、Git、Issue、PR、CI 已有能力优先复用，本仓库只补流程约束和共享资产

完整原则见 [核心原则](./docs/governance/core-principles.md)。

## 完整流程

```text
需求 / 问题 / 异常
        │
        ▼
创建主 Issue
        │
        ▼
PM 澄清问题与边界
        │
        ▼
PRD
不写技术实现
        │
        ▼
架构评审 + QA Gate
        │
        ▼
QA Case Design
        │
        ▼
文档 PR
PRD + Tech + QA Case
        │
        ▼
Human Review #1
合并 = 设计确认
        │
        ▼
实现与验证
        │
        ▼
代码 PR
代码 + 测试证据
        │
        ▼
Human Review #2
合并 = 实现确认
        │
        ▼
Issue Comment Gate
        │
        ▼
Release / 验收 / Human 关闭
```

## 默认角色

默认团队：

- 团队负责人（Team Lead）
- 产品经理（Product Manager）
- 架构师（Architect）
- 工程师（Engineer）
- 测试工程师（QA Engineer）
- 平台 / SRE（Platform / SRE）
- 流程审计员（Process Auditor）

按需启用：

- 研究支持（Research Support）

## 如何安装

当前仓库提供安装脚本：

```bash
./scripts/install.sh --dry-run
./scripts/install.sh --channel dev --target ~/.claude
```

说明：

- `scripts/install.sh` 当前主要用于安装 Claude 本地技能包
- `--channel stable` 安装稳定版本
- `--channel dev` 安装当前仓库中的开发版本
- 默认目标目录是 `~/.claude`
- 如果要先预览改动，先执行 `--dry-run`

安装完成后，可继续阅读：

1. [Claude 接入](./docs/platforms/claude-code.md)
2. [插件入口](./plugins/agentdevflow/README.md)
3. [共享技能目录](./skills/shared/README.md)

如果你只想先理解这套机制，至少先读：

1. [核心原则](./docs/governance/core-principles.md)
2. [交付 Gate](./prompts/004_delivery_gates.md)
3. [Issue 与评审评论机制](./prompts/013_github_issue_and_review_comments.md)
4. [双阶段 PR 与三层保障](./prompts/019_dual_stage_pr_and_three_layer_safeguard.md)

## 依赖与复用边界

AgentDevFlow 不重复实现平台已经具备的能力。

优先复用：

- Claude 的 Agent Team 能力
- Codex 的多 agent 调度能力
- Git / Issue / PR / CI / `gh`
- 团队已有的 skills、plugin、agents 包

只有当现成能力不能承载主干机制时，才在本仓库补充自己的入口或约束。完整说明见 [依赖清单](./docs/reference/dependencies.md)。

## 人机沟通通道

AgentDevFlow 需要让人和 Agent Team 在不同场景下都能持续协作，因此 `Telegram`、`GitHub Issue`，以及未来的 `飞书 CLI`，都应被理解为沟通 channel，而不只是单点工具。

其中：

- `Telegram` 和未来的 `飞书 CLI` 更偏向异步或移动端的人机沟通入口，方便用户不在电脑旁时继续跟进
- `GitHub Issue` 不只是沟通 channel，还是正式流程主线的承载体，负责挂接过程产出物、状态、评论、Gate 结论以及最终验收关闭

当前仓库已经提供基于 Telegram 的通道能力，让用户即使只在手机上，也能接收状态、查看进展，并与 Agent Team 继续交互。

如果你要接入 Telegram，最小配置如下：

```bash
export TELEGRAM_BOT_TOKEN=<your-bot-token>
export TELEGRAM_CHAT_ID=<your-chat-id>
```

当前相关实现：

- `scripts/telegram_bot.service`
- `scripts/send_telegram.py`
- `channels/telegram/`
- `channels/core/telegram_monitor.py`

后续规划不只限于 Telegram，也会继续支持其他人机沟通通道，例如飞书 CLI，并继续强化 GitHub Issue 作为正式流程主线和产物挂载点的能力。

## 问题反馈

如果你发现问题或有改进建议，欢迎通过 GitHub Issue 反馈。
