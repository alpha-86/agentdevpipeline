# OpenCode Event Automation Example

## 目标

说明 OpenCode 适配层如何围绕共享事件模型做最小自动化接入。

## 最小映射

1. `issue.created` / `issue.routed`
   - 写入项目状态板
   - 创建或确认 artifact linkage 主记录

2. `review.approved` / `review.rejected`
   - 更新 gate queue
   - 更新 issue 当前阶段
   - 触发下一步 workflow 或回退动作

3. `platform_check.started` / `platform_check.failed`
   - 写入检查结果
   - 补充 memo 或 issue comment
   - 阻断 release / implementation

4. `human_review.timeout`
   - 升级到 Team Lead
   - 生成 overdue review 待办

## 最小输出物

- event record
- gate queue
- issue comment
- overdue review todo
