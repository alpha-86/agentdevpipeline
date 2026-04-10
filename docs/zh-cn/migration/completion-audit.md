# hedge-ai 可迁移机制中文落地完成度审计

## 结论

截至当前版本，hedge-ai 中大量“可迁移”和“部分迁移”的通用产研机制已经在 `agentdevpipeline` 中文主版本中形成主干，但不能再表述为“已基本完成拆解”。更准确的状态是：

- 主干机制已经初步迁移
- 边界已经明确
- 逐文档到插件落点的覆盖检查还没有彻底完成
- 插件入口表达仍然弱于目标要求

## 已落地的主干机制

### 组织与角色

- 团队拓扑与角色边界：`prompts/zh-cn/001_*`、`002_*`
- Team Lead 边界与角色强规则：`skills/shared/agents/*`
- 团队启动机制：`prompts/zh-cn/010_team_setup_and_bootstrap.md`

### 流程与 Gate

- 文档契约：`prompts/zh-cn/003_document_contracts.md`
- Gate 机制：`prompts/zh-cn/004_delivery_gates.md`
- 双轨交付：`prompts/zh-cn/016_dual_track_delivery_mechanism.md`

### Issue / 评论 / 变更

- Issue 驱动：`prompts/zh-cn/007_issue_driven_orchestration.md`
- GitHub Issue 评论门禁：`prompts/zh-cn/013_github_issue_and_review_comments.md`
- 变更记录与重审：`prompts/zh-cn/008_change_record_and_revalidation.md`
- Issue 生命周期 workflow：`skills/shared/workflows/issue-lifecycle.md`

### 会议 / Todo / 异常 / 恢复

- 日会与 Todo：`prompts/zh-cn/005_meeting_and_todo.md`
- 异常升级闭环：`prompts/zh-cn/012_anomaly_and_escalation_loop.md`
- 上下文恢复：`prompts/zh-cn/009_review_rigor_and_context_recovery.md`
- 对应 workflows：`daily-sync.md`、`todo-review.md`、`anomaly-response.md`、`context-recovery.md`

### 合规与审计

- 流程合规：`prompts/zh-cn/014_process_compliance_and_audit.md`
- 周/月复盘：`skills/shared/workflows/weekly-review.md`、`monthly-review.md`
- Skill 协议：`docs/zh-cn/governance/skill-protocol.md`

### 评审评估

- 评审维度：`prompts/zh-cn/015_review_evaluation_dimensions.md`
- Review Comment / Change Record / Handoff / Recovery / Anomaly 模板：`skills/shared/templates/*`

## 明确排除

以下内容仍然保持禁止迁移状态：

- 基金经理、交易员、CRO/CSO（量化语境）
- 盘前、盘后、DBR、异常日报（交易运营语境）
- 因子研究、回测评审、策略辩论、持仓与回撤指标

详见：

- [迁移边界（强约束）](/home/work/code/agentdevpipeline/docs/zh-cn/governance/migration-boundary-from-hedge-ai.md)
- [源文档清单与迁移判定](/home/work/code/agentdevpipeline/docs/zh-cn/migration/hedge-ai-source-inventory.md)

## 审计口径

本审计目前只表示“已有初步落点”，不表示“独立插件目标已经完成”。更严格的检查请以：

- [hedge-ai 研发机制拆解到独立插件的迁移矩阵](/home/work/code/agentdevpipeline/docs/zh-cn/migration/hedge-ai-plugin-migration-matrix.md)
- [围绕独立插件目标的总复核与纠偏](/home/work/code/agentdevpipeline/prompts/discuss/015_2026-04-10_围绕独立插件目标的总复核与纠偏.md)

为准。

英文镜像尚未开始，本审计不覆盖英文版。
