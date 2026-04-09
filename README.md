# AgentDevPipeline

[详细中文说明](./README_CN.md)

AgentDevPipeline 是一个独立的研发全流程编排项目，用来把需求、设计、实现、测试、发布和复盘串成可追溯、可审计、可人机协同的多 agent 交付系统。

## 这个项目解决什么问题

很多团队已经能让 Agent 写代码、做研究、出文档，但交付仍然容易失控：

- 需求、方案、代码、测试之间断链
- 评审靠聊天推进，没有正式 Gate
- Issue、Todo、PR、文档状态经常漂移
- 会话一断、角色一换，上下文就丢
- 不同平台各写一套流程，无法复用

AgentDevPipeline 解决的是这些“跨角色、跨阶段、跨平台”的流程问题，而不是只提供一个单点 prompt。

## 它如何运作

- 用 `Issue` 作为主线，把 PRD、Tech、QA、Release、Todo、Memo、Comment 全部串起来
- 用 `Gate` 控制阶段切换，禁止跳过评审直接推进
- 用 `Human Review` 明确设计确认和实现确认两个关键协同节点
- 用 `agents / workflows / templates` 把角色、流程和留痕结构固化下来
- 用 `Platform Checks` 和 `Process Auditor` 把流程从“文档规则”推进到“可审计约束”

## 完整流程图

```text
需求 / 问题 / 异常
        │
        ▼
   创建主 Issue
        │
        ▼
Research / PRD
        │
        ▼
Tech Spec + 必要时 QA Case Design
        │
        ▼
Human Review #1
设计确认 / 退回重审
        │
        ▼
Implementation
        │
        ▼
QA Validation + 测试报告
        │
        ▼
Human Review #2
代码/交付确认
        │
        ▼
Release Decision
        │
        ▼
Todo Closure / Weekly Review / Monthly Review
```

## 核心原则

- `Issue First`
- `Human In The Loop`
- `Gate 不可绕过`
- `正式留痕优先于聊天推进`
- `双阶段交付`
- `平台适配不能改写核心语义`
- `只保留通用研发语义，不引入 hedge-ai 的量化交易业务内容`

完整定义见 [核心原则](./docs/zh-cn/governance/core-principles.md)。

## 角色与结构

项目当前沉淀的共享角色包括：

- Team Lead
- Product Manager
- Tech Lead
- Engineer
- QA Engineer
- Researcher
- Platform/SRE
- Process Auditor

其中每个角色都应至少包含：

- 角色主规范
- playbook 执行手册
- 必读文档
- 初始化动作
- 上下文恢复
- Issue / Gate / Human Review 责任
- 禁止行为
- 输出格式

## 目录结构

```text
AgentDevPipeline/
├── adapters/           # 平台适配入口
├── docs/               # 中文治理、发布文档、交付目录
├── plugins/            # 插件与包装
├── prompts/            # 流程规则、讨论审计、发布镜像
├── registry/           # 依赖元数据
└── skills/shared/      # 角色、workflow、template、playbook
```

## 从哪里开始读

1. [README_CN.md](./README_CN.md)
2. [docs/zh-cn/README.md](./docs/zh-cn/README.md)
3. [docs/zh-cn/architecture/repository-map.md](./docs/zh-cn/architecture/repository-map.md)
4. [prompts/zh-cn/README.md](./prompts/zh-cn/README.md)
5. `skills/shared/`

## 当前版本

- Internal source version: `0.3.0`
- Public release version: `0.3.0`
