# Shared Skills 目录

`skills/shared/` 是 AgentDevPipeline 的平台无关执行资产层。

## 结构

- `agents/`
  角色定义与 playbook。

- `workflows/`
  阶段流程、准入准出条件、签字与回退规则。

- `templates/`
  正式留痕模板与交付物结构。

## 使用原则

- 平台适配层只能包装入口，不得改写这里的核心语义。
- 角色、workflow、template 必须与中文主版本规则保持一致。
