# 041 Phase 4.4 `skills/shared/` 正文中文化

## 目标

把 `skills/shared/` 中仍然面向用户可见的英文正文、英文标题、英文章节名、英文模板字段系统性改成中文。

## 本轮覆盖范围

### 1. 共享入口

- `skills/shared/README.md`
- `skills/shared/team-setup.md`
- `skills/shared/start-agent-team.md`
- `skills/shared/create-agent.md`
- `skills/shared/skill-protocol.md`
- `skills/shared/event-bus.md`

### 2. 角色与执行手册

- `skills/shared/agents/*.md`
- `skills/shared/agents/*.playbook.md`

### 3. 工作流

- `skills/shared/workflows/*.md`

### 4. 模板

- `skills/shared/templates/*.md`

## 本轮处理原则

1. 用户可见的标题、章节名、模板字段、说明性句子全部改成中文。
2. 不改动真实文件路径，不虚构中文文件名。
3. `Issue`、`ID`、事件名、文件路径、目录名等稳定标识暂不作为正文翻译对象。
4. 任何会导致路径失真的替换都必须回退到真实文件名。

## 本轮结果

- `skills/shared/` 的主标题、角色标题、执行手册标题已改成中文
- `Critical Rules`、`Success Metrics`、`Review Record`、`Step` 等章节名已改成中文
- 工作流标题、步骤说明、模板字段已大面积中文化
- 模板中的 `Priority`、`Due`、`State`、`From`、`To`、`Date` 等字段已改成中文
- 误伤到的路径引用已修回真实文件名

## 仍然保留的英文内容类型

- `Issue`
- `ID`
- 真实文件路径与文件名
- 事件名与检查名等稳定标识

这些内容将在后续 `Phase 4.7` 统一复核，不把它们和“英文正文”混为一谈。

## 下一步

1. 继续改写 `docs/` 下的英文示例正文
2. 清理“英文镜像 / 英文发布层 / localization policy”说明
3. 最后统一做中文单线复核
