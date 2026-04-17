# TODO Registry

## 项目信息
- `project_id`: alpha-86/AgentDevFlow
- 主 issue: #1
- 当前阶段: Gate 2 Tech Review (Issue #3 v3, 2026-04-17)
- 启动方式: 补充创建 Engineer、Platform/SRE、PMO Agent 实例

## 角色分配

| 角色 | 状态 | Agent ID | tmux  panes |
|------|------|----------|-------------|
| Team Lead | ✅ | - | - |
| Product Manager | ✅ | product-manager@agentdevflow | %54 |
| 架构师 | ✅ | architect@agentdevflow | %55 |
| QA Engineer | ✅ | qa-engineer@agentdevflow | %56 |
| Engineer | ✅ | engineer@agentdevflow | %57 |
| Platform/SRE | ✅ | platform-sre@agentdevflow | %58 |
| PMO | ✅ | pmo@agentdevflow | %59 |

## 当前 Gate

- Gate 0: Team Startup ✅ 已完成 (2026-04-16 全员角色补充完成，tmux 模式)
- Gate 1: PRD Review ✅ Issue #3 v3 三方签字完成 (2026-04-17)
- Gate 2: Tech Review 🔄 Tech Spec v3 已提交，评审进行中
- Gate 3-5: 待 HR#1 完成后继续

## 待处理 Issue

| Issue | 标题 | 路由 | 状态 | 备注 |
|-------|------|------|------|------|
| #8 | GOV-004 HR#1 被跳过 | PMO | pending | 机制改进执行中 |
| #5 | ADF 技能系统完善 | Engineer | pending | — |
| #3 | gstack/superpower 增强层接入 | PM | pending | Gate 1 ✅, Gate 2 🔄 |

## 已知问题

- Platform/SRE 报告 4 个 skill 文件缺失：release-review.md, anomaly-response.md, release-record-template.md, platform-check-result-template.md
- PM 合规审计（2026-04-17）：见下方审计记录，5 项违规已记录

## 启动会

- 时间: 2026-04-16
- 负责人: Team Lead
- 结论: 全员角色补充完成，3个 open issues 已路由至 Engineer，等待 Human Review #1

## PM 合规审计记录（2026-04-17）

**触发原因**：Human 对 PM 工作严重不满，Team Lead 要求 PMO 紧急介入

| # | 违规项 | 违规归属 | 当前状态 |
|---|--------|---------|---------|
| 1 | PRD 命名不符合标准（`PRD-3_v3.md`） | PM（初次）→ Human（rename 已纠正） | ✅ 已纠正 |
| 2 | 直接 push 到 main 而非通过 PR | Human 操作，PMO 审计范围外 | ⚠️ 待规范 |
| 3 | 在 Human 确认前发起 Gate 1 评审（声称 v3 "Human 确认" 但缺乏独立证据） | PM | ⚠️ 待 PM 区分"Human 反馈"与"Human 确认" |
| 4 | PR #1 不存在（历史示例文件误解） | PM 误解 | ✅ 已澄清 |
| 5 | PM 发布 Issue 关闭评论（Issue 关闭是 Human 专属） | PM Agent（历史） | ✅ Human 已重新打开纠正 |

**纠正动作**：
- P0：PM 重新阅读 SKILL.md，明确 Issue 关闭 Human 专属边界（负责人：PM）
- P1：在 `003_document_contracts.md` 补充 PRD 命名反面示例（负责人：PMO）
- P1：在 `skills/workflows/prd-review.md` 明确"Human 确认"需独立 Issue 评论证据（负责人：PMO）
- P2：明确 Human 直接 push 与 PR 提交的边界（负责人：PMO/Team Lead）
