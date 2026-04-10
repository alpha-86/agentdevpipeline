# 016 Phase 6.4 - 2026-04-10 evaluation checker 逐项复核

## 复核范围

- `prompts/015_review_evaluation_dimensions.md`
- `skills/shared/templates/review-comment-checklist-template.md`
- `skills/shared/templates/audit-report-template.md`
- `docs/migration/hedge-ai-plugin-migration-matrix.md`

## 本轮结论

此前这块的主要问题是：

- 只有“评审维度”说明
- 没有更像 `hedge-ai evaluation` 的检查器类型
- 模板字段也没把维度和失败结论压进去

## 本轮修正

### 1. 评审维度升级为检查器类型

在 `prompts/015_review_evaluation_dimensions.md` 中补充：

- 完整性检查器
- 一致性检查器
- 逻辑性检查器
- 证据充分性检查器

并明确：

- `Approved`
- `Conditional`
- `Rejected / fail`

的给出条件。

### 2. 模板层同步

- `review-comment-checklist-template.md`
  - 增加检查器类型
  - 增加四维检查
- `audit-report-template.md`
  - 增加检查器类型
  - 增加失败维度

### 3. 迁移矩阵同步

- 把 evaluation 的当前落点从“只有 `prompts/015`”更新为：
  - `prompts/015_review_evaluation_dimensions.md`
  - `review-comment-checklist-template.md`
  - `audit-report-template.md`

## 复核判断

`Phase 6.4` 可以落账，含义是：

- evaluation checker 已不再只是说明性文字
- 已经下沉为“检查器类型 + 模板字段”的组合能力

后续如果需要更进一步，可以再补单独的 checker 入口文件，但当前已经明显比之前更接近 hedge-ai 的执行形态。
