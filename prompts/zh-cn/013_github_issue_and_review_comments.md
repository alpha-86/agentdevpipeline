# GitHub Issue 与评审评论机制

## 目标

把 GitHub Issue、评审评论和文档 Gate 绑定起来，确保线上协作轨迹可追溯、可审计。

## 主规则

- 一个正式交付流程必须有主 Issue。
- PRD / Tech / QA / Release 的结论必须能在 Issue 中找到。
- 评审评论不是聊天记录替代品，而是 Gate 留痕的一部分。

## Issue 最小结构

- 背景
- 目标
- 当前阶段
- 当前 owner
- 关联文档链接
- 最新 Gate 结论
- 打开的 Todo / blocker

## 评论写入时机

- PRD Review 结束
- Tech Review 结束
- QA 结论输出
- Release 决策输出
- Major / Breaking 变更发生
- 异常升级或恢复完成

## Gate 评论最小字段

- Gate 名称
- 决策人
- 结论
- 证据链接
- 待办与 owner
- 是否允许进入下游阶段

## 评论约束

- 禁止只写“LGTM”“通过”“看过了”之类无结构结论
- 禁止评论结论与正式文档状态不一致
- 条件通过必须写清条件和复核人
- 评论中只放结构化结论与链接摘要，不粘贴长篇设计正文
- Agent 默认不自行关闭主 Issue，除非项目策略显式允许

## 失败处理

- 若当前阶段缺少必需 comment，则该阶段不能视为完成
- 若 comment 字段不完整，则必须补齐后重试
- 若 comment 与 issue / 文档状态不一致，则以更严格状态为准并触发纠正
- 必须指定修复 owner 和重试条件

## PR / Issue 关系

- PR 必须回链主 Issue
- 合并前必须确认主 Issue 的阶段状态与 PR 实际内容一致
- 若 PR 引入 Major / Breaking 变更，Issue 必须先完成重审记录
