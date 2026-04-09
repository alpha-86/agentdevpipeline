# Claude Adapter

这个适配层负责把 AgentDevPipeline 包装成 Claude 可使用的本地 skill pack。

## 最小要求

- 不改写 `skills/shared/` 的核心语义
- 支持读取中文主版本规则
- 至少具备 issue / gate / artifact linkage 的最小检查能力

参考：

- `docs/zh-cn/governance/platform-minimum-checks.md`
