# Claude Event Automation Example

## 目标

说明 Claude 适配层如何把共享事件模型映射成最小可执行动作。

## 最小映射

1. 监听 `document.created`
   - 解析 `project_id`、`issue_id`、`document_type`
   - 根据文档类型选择 `prd-review` 或 `tech-review`
   - 生成一条 event record

2. 监听 `review.requested`
   - 生成待办
   - 更新项目状态板
   - 提醒对应角色发起正式评审

3. 监听 `issue.comment_missing`
   - 运行平台检查
   - 写入 platform check result
   - 阻断下游 Gate

4. 监听 `human_review.completed`
   - 更新 artifact linkage
   - 从 Gate Queue 中移除或更新对应项目

## 最小输出物

- event record
- gate queue 更新
- platform check result
- issue comment 或 memo 链接
