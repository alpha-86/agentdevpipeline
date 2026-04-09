# Issue Comment 缺失阻断示例

**平台**: Claude
**日期**: 2026-04-09
**Issue**: #0
**当前 Gate**: QA
**结论**: fail
**执行人**: Process Auditor

## 失败原因

- QA 测试报告已存在，但主 Issue 下缺少 QA 结论 comment
- 当前 issue 状态已尝试进入 `in_release`，与缺失的 QA comment 不一致

## 阻断范围

- 当前阶段不得进入 Release Review
- issue 状态不得继续推进到 `in_release`

## 修复 Owner

- QA Engineer：补 QA 结论 comment
- Team Lead：纠正 issue 状态并重新检查阶段一致性

## 重试条件

- QA comment 已写入主 Issue
- comment 字段齐全且与测试报告状态一致
- issue 状态回到与 QA 阶段一致的值

## 相关链接

- `docs/qa/000_user_notification_center_qa_2026-04-09.md`
- `skills/shared/templates/review-comment-template.md`
