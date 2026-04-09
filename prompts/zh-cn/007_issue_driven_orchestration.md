# Issue 驱动编排机制

## 目标

把交付流程统一收敛到 Issue 主线，确保每个 Gate 的输入、输出、结论、行动项都可追溯。

## 核心原则

- 无 Issue 不进入正式交付流程。
- Issue 是唯一流程主索引，PRD/Tech/QA/Release 都必须回链到该 Issue。
- Gate 结论必须写入 Issue 评论或关联记录，不允许口头通过。

## Issue 状态机（最小）

- `open`：已创建，待需求澄清
- `in_prd`：PRD 编写/评审中
- `in_tech`：Tech 方案编写/评审中
- `in_impl`：开发实现中
- `in_qa`：验证中
- `in_release`：发布评审中
- `done`：完成
- `blocked`：阻塞
- `canceled`：取消

## Gate 与 Issue 的绑定规则

### Gate 1 PRD Review

- 入场条件：Issue 有明确背景、目标、范围。
- 出场条件：PRD 状态 `Approved`，Issue 留下评审结论与 action items。

### Gate 2 Tech Review

- 入场条件：PRD `Approved`。
- 出场条件：Tech Spec `Approved`，Issue 留下风险、依赖、重审条件。

### Gate 3 Implementation

- 入场条件：Tech Spec `Approved`。
- 出场条件：实现证据（代码、测试、说明）回链 Issue。

### Gate 4 QA Validation

- 入场条件：实现证据完整。
- 出场条件：测试报告与缺陷结论回链 Issue，给出放行或阻断意见。

### Gate 5 Release Review

- 入场条件：QA 无阻塞缺陷或风险已明确接受。
- 出场条件：发布结论、回滚方案、值守安排回链 Issue。

## 强制评论模板（Issue 内）

每次 Gate 完成后必须包含：

- Gate 名称与日期
- 结论（Approved / Conditional / Rejected）
- 关键证据链接
- 待办清单（负责人 + 截止时间）
- 下一 Gate 的入场条件

## 禁止行为

- 跳过 Issue 直接开工
- Gate 结论不留痕
- 用聊天记录替代正式评审结论
- 状态与实际阶段不一致且不修正
