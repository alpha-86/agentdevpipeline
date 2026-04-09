# 双阶段 PR 与三层保障体系

## 目标

把“设计确认”和“实现确认”拆成两个明确的人机协同节点，并建立避免流程被绕过的三层保障体系。

## 为什么需要双阶段

如果文档设计和代码交付混在同一个模糊流程里，会出现三类问题：

- 设计是否被确认不清楚
- Human Review 到底 review 了什么不清楚
- QA 介入时机和验收边界不清楚

## 双阶段定义

### 阶段 1：文档阶段

- 产物：PRD、Tech、必要时的 QA Case Design
- 目标：锁定需求、方案、测试思路
- Human Review：确认设计可以进入实现
- 结果：通过后，Implementation 才能正式开始

### 阶段 2：实现阶段

- 产物：代码、测试、测试报告、发布准备
- 目标：确认实现与设计一致且可交付
- Human Review：确认代码/交付物可以进入发布或验收完成
- 结果：通过后，Issue 才能进入关闭或发布完成状态

## Human Review 最小要求

- reviewer 身份明确
- 评审对象明确
- 结论明确（Approved / Conditional / Rejected）
- 证据链接明确
- 是否允许进入下游阶段明确

## 三层保障体系

### 第一层：流程规则

- Prompt / Workflow / Template 明确阶段、签字、退回条件
- Team Lead / PM / Tech Lead / QA 持有强规则
- 没有当前阶段通过结论，不得推进下游

### 第二层：执行留痕

- Issue Comment
- Memo
- Review Record
- Change Record
- Todo Registry

要求：

- 所有关键结论都必须进入正式留痕对象
- 口头确认不具备流程效力

### 第三层：平台与自动化检查

- PR / Issue / CI 规则
- 文档存在性检查
- 状态一致性检查
- Comment / artifact linkage 检查

说明：

- AgentDevPipeline 不绑定某个特定平台实现
- 但任何平台适配都应该提供等价的自动化保障

## 强制规则

- 文档阶段未确认，不得正式进入实现阶段
- 实现阶段未确认，不得正式关闭 Issue 或发布
- QA 测试报告不得缺席实现阶段确认
- Major / Breaking 变更必须判断是否回退到文档阶段重新确认

## 失败信号

- 文档和代码混在一个无法区分的确认节点里
- Human Review 没有明确对象
- 设计未确认就开始实现
- 实现已变更但文档阶段结论未更新
