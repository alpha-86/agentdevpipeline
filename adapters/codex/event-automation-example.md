# Codex Event Automation Example

## 目标

说明 Codex 适配层如何把共享事件和最小检查拼成连续动作。

## 最小映射

1. `document.created`
   - 校验文档路径和模板字段
   - 触发对应 workflow
   - 记录 event record

2. `gate.enter_requested`
   - 校验 signoff、comment、artifact linkage
   - 不满足则写入 gate queue 和检查结果

3. `platform_check.failed`
   - 标记 issue 为 blocked
   - 生成修复待办
   - 等补齐后重试

4. `issue.stage_changed`
   - 更新项目状态板
   - 校验是否与最近一次 Gate 结论一致

## 最小输出物

- event record
- gate queue
- platform check result
- 项目状态板更新
