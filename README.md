# AgentDevFlow

AgentDevFlow 是一套面向软件研发交付的多 Agent 流程资产包。它关注的不是“单个 Agent 会不会写代码”，而是如何用 GitHub Issue 主线、双阶段 PR、多 Agent 协作和关键节点上的人类判断，把需求到发布串成一个可执行闭环。

## 它解决什么问题

很多团队已经在用 Claude、Codex 或其他 Agent 工具，但真正容易失控的往往不是编码本身，而是协作过程：

- 需求、方案、实现、测试各做各的，缺少统一主线
- Agent 能持续产出，但关键节点缺少人工确认与签核
- Issue、PR、评论、Todo、Memo 分散，责任人和证据对不上
- 多个问题并行推进时，状态、优先级和上下文恢复成本很高
- 人与 Agent Team 的直接沟通入口往往只有 CLI，一旦离开电脑，跟进、确认、恢复和通知就容易断掉
- 不同平台各写一套规则，流程越做越碎，重复造轮子

AgentDevFlow 的目标，是把这些问题沉淀成一套可复用的 agent、workflow、template 和平台入口约束，让多 Agent 协作具备清晰的流程治理，同时保留人类在关键节点上的判断权。

## 它怎么工作

AgentDevFlow 的主线不是“让 Agent 自己跑完一切”，而是建立一条以 CLI 为启动入口、以 GitHub Issue 为正式主线、由多 Agent 推进并在关键节点保留人类判断的研发链路：

- `GitHub Issue 全流程`：从主 Issue 启动，所有关键产物和结论持续回链，最终也在 Issue 上完成验收与关闭
- `问题先于方案`：先澄清目标、边界、约束，再写 PRD
- `双阶段 PR + Human Review`：通过文档 PR 和代码 PR 两个阶段引入人类评审；文档 PR 合并代表设计确认，代码 PR 合并代表实现确认
- `Issue Comment Gate`：关键结论必须真正回写到 Issue，而不是停留在聊天里
- `正式留痕`：PRD、Tech、QA、Memo、Todo、Release、Change Record 都有明确落点
- `Process Auditor`：把流程合规检查作为独立职责，而不是靠参与者自觉
- `多通道协作`：CLI 负责同步编排，GitHub Issue 承担正式流程主线，Telegram 与未来的飞书 CLI 用来补足异步、移动端和离开电脑后的协作
- `优先复用现成能力`：Claude、Codex、Git、Issue、PR、CI 已有能力优先复用，本仓库只补流程约束和共享资产

完整原则见 [核心原则](./docs/governance/core-principles.md)。

## 完整流程

```text
需求 / 问题 / 异常
        │
        ▼
创建主 GitHub Issue
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
Human Review #1
合并 = 设计确认
        │
        ▼
实现与验证
        │
        ▼
代码 PR
代码 + 测试证据
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

| 启用方式 | 角色 | 一句话职责 | 定义文档 |
| --- | --- | --- | --- |
| 默认 | 团队负责人（Team Lead） | 负责团队节奏、流程完整性、跨角色协同和升级协调。 | [team-lead.md](./skills/shared/agents/team-lead.md) |
| 默认 | 产品经理（Product Manager） | 负责把用户问题、业务目标和范围边界转成可评审、可实现、可验收的正式交付物。 | [product-manager.md](./skills/shared/agents/product-manager.md) |
| 默认 | 架构师（Architect） | 负责技术可行性判断、架构与接口收敛、Tech Spec 产出以及技术 Gate 守门。 | [architect.md](./skills/shared/agents/architect.md) |
| 默认 | 工程师（Engineer） | 负责把已确认的设计转成代码、测试和实现证据。 | [engineer.md](./skills/shared/agents/engineer.md) |
| 默认 | 质量工程师（QA Engineer） | 负责测试设计、验证执行、测试报告和质量 Gate。 | [qa-engineer.md](./skills/shared/agents/qa-engineer.md) |
| 默认 | 平台与发布负责人（Platform / SRE） | 负责环境稳定性、CI 与自动化检查、部署准备、回滚能力和发布风险控制。 | [platform-sre.md](./skills/shared/agents/platform-sre.md) |
| 默认 | 流程审计员（Process Auditor） | 负责流程合规审计、状态一致性检查和例外审批检查。 | [process-auditor.md](./skills/shared/agents/process-auditor.md) |
| 按需 | 研究支持（Research Support） | 负责在正式立项或方案收敛前降低认知不确定性，为 PRD、Tech 或流程设计提供证据、选项和建议。 | [researcher.md](./skills/shared/agents/researcher.md) |

## 人与 Agent 的沟通通道

当前很多宿主里，人与 Agent Team 的直接交互入口主要还是 CLI。这样做适合同步编排，但也意味着用户一旦离开电脑，很多跟进、确认、恢复和通知动作都会变得不连续。

因此，AgentDevFlow 把 `CLI`、`GitHub Issue`、`Telegram`，以及未来的 `飞书 CLI` 统一看作协作通道，而不是孤立工具。

其中：

- `CLI` 负责主会话编排、角色启动和同步推进
- `GitHub Issue` 不只是沟通通道，还是 GitHub Issue 全流程的正式主线，负责挂接过程产出物、状态、评论、Gate 结论以及最终验收关闭
- `Telegram` 和未来的 `飞书 CLI` 更偏向异步或移动端的人与 Agent 协作入口，方便用户不在电脑旁时继续跟进

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

后续规划不只限于 Telegram，也会继续支持其他协作通道，例如飞书 CLI，并继续强化 GitHub Issue 作为正式流程主线和产物挂载点的能力。

## 依赖与复用边界

AgentDevFlow 不重复实现平台已经具备的能力。

优先复用：

- Claude 的 Agent Team 能力
- Codex 的多 agent 调度能力
- Git / Issue / PR / CI / `gh`
- 团队已有的 skills、plugin、agents 包

只有当现成能力不能承载主干机制时，才在本仓库补充自己的入口或约束。完整说明见 [依赖清单](./docs/reference/dependencies.md)。

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

## 继续阅读

如果你要接入平台入口，可继续阅读：

1. [Claude 接入](./docs/platforms/claude-code.md)
2. [插件入口](./plugins/agentdevflow/README.md)
3. [共享技能目录](./skills/shared/README.md)

如果你想先理解这套机制，至少先读：

1. [核心原则](./docs/governance/core-principles.md)
2. [交付 Gate](./prompts/004_delivery_gates.md)
3. [Issue 与评审评论机制](./prompts/013_github_issue_and_review_comments.md)
4. [双阶段 PR 与三层保障](./prompts/019_dual_stage_pr_and_three_layer_safeguard.md)

## 问题反馈

如果你发现问题或有改进建议，欢迎通过 GitHub Issue 反馈。
