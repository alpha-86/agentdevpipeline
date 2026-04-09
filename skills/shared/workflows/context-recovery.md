# 上下文恢复 Workflow

## 目标

在会话丢失、环境切换或角色交接后，恢复执行上下文，同时不降低评审严谨性。

## 触发条件

- 对话历史被清空
- agent 重启
- owner 交接
- 长时间暂停后的任务恢复

## 输入

- 关联 Issue ID
- 最新 Gate 状态
- 最新 memo 和 todo 链接
- 最新 change record 链接

## 推荐模板与输出目录

- 恢复摘要：`skills/shared/templates/context-recovery-template.md`
- 推荐输出目录：`docs/memo/` 或当前阶段工作目录

## 步骤

1. 读取 issue 状态和最近一次决策记录。
2. 读取当前阶段文档及其状态。
3. 读取未关闭 blocker、todo 和异常记录。
4. 产出恢复摘要。
5. 在执行前确认下一步动作仍然有效。

## 阶段最小产物集合

- 一份恢复摘要
- 当前 gate 结论
- 未关闭 blocker / todo 清单
- 下一步动作与 owner

## 恢复摘要字段

- 当前 issue
- 当前 gate
- 最近一次决策
- 未关闭 blocker
- 未关闭 todo
- 下一步动作
- 必需审批人或 owner

## 退出条件

- 已产出恢复摘要
- 当前执行阶段没有歧义
- 上游必需记录没有缺失
