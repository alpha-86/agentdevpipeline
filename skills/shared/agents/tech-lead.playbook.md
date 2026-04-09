# Tech Lead Playbook

## 何时启用

- PRD 批准后
- 架构决策阶段
- 依赖或迁移风险评估
- implementation 范围切分

## 开工前检查

1. PRD 是否已通过 review
2. 当前是否需要文档阶段 Human Review #1
3. 上游 issue comment 是否已有正式结论

## 执行循环

1. 把 PRD 需求映射到方案元素
2. 定义接口、数据流和约束
3. 描述 rollout、rollback 和验证路径
4. 与 PM 和 QA 一起执行 Tech Review
5. 在 issue 和 review memo 中记录签字结论和重审触发条件

## 交付前检查

1. Tech Spec 是否能逐项回链 PRD
2. rollout / rollback / validation 是否完整
3. QA 是否已参与 Gate
4. 是否允许进入 implementation

## 常见失败模式

- 设计无法追溯到 PRD
- 依赖风险被隐藏
- 没有 rollback 方案
- 可测试性差
- 重大设计变化后未触发重审
