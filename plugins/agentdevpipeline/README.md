# AgentDevPipeline 插件

本插件的定位不是“另写一套流程”，而是承载从 `hedge-ai` 中拆出来的可迁移研发机制。

## 插件目标

- 把 hedge-ai 中可复用的研发角色、workflow、template、治理规则独立出来
- 去除量化交易业务语义
- 让这些机制能被不同 Agent 入口作为独立插件加载

## 插件资产来源

- `prompts/zh-cn/`
- `prompts/en/`
- `skills/shared/`
- `docs/zh-cn/`
- `docs/en/`

## 插件主入口

- 根仓库 `README.md`
- `docs/zh-cn/README.md`
- `docs/zh-cn/migration/hedge-ai-plugin-migration-matrix.md`
- `skills/shared/README.md`

## 规则

- 中文是内部主版本
- 英文是对外发布镜像
- 插件层不得改写 `skills/shared/` 的核心语义
- 插件层不得新增 hedge-ai 源文档中不存在的核心流程概念
