# Human Review 与签字机制

## 目标

明确哪些交付物必须进入 Human Review，谁来 review，以什么形式 review，以及 review 结论如何影响后续流程。

## 核心原则

- Agent 可以起草、整理、预审，但关键交付物不能只在 Agent 内部自循环。
- Human Review 的对象、时机、形式、结论必须显式定义。
- 没有正式签字或确认记录，不视为已通过。

## 必须进入 Human Review 的对象

- 关键 PRD
- 关键 Tech Spec
- QA Case Design（高风险或复杂改动时）
- 代码 PR
- 发布放行
- Major / Breaking Change
- 例外审批

## 推荐 Review 形式

- 文档 Review
- Pull Request Review
- Issue Comment Confirm
- Release Approval

## 结论类型

- `Approved`
- `Conditional`
- `Rejected`

## 结论处理规则

### Approved

- 可以进入下游阶段
- 必须记录 reviewer、日期、证据链接

### Conditional

- 必须记录条件项、owner、due date
- 条件项关闭前不得进入下游

### Rejected

- 必须回到当前阶段修订
- 必须说明最关键失败原因

## 签字最小要求

- PRD：PM + Tech Lead
- Tech：Tech Lead + QA + PM 确认
- QA：QA + PM
- Release：PM + Tech Lead + Platform/SRE

## 禁止行为

- 口头说通过但不留正式记录
- 只让 Agent 自评就视为通过
- Conditional 未关闭就进入下游
- 用聊天摘要替代签字记录
