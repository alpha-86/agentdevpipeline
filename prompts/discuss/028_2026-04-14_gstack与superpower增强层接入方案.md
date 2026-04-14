# 028：gstack 与 superpower 增强层接入方案

**编号**: 028
**日期**: 2026-04-14
**类型**: proposal
**关联背景**:
- `027_2026-04-14_Claude自举目标复核_review.md`
- `README.md` 中新增的 FAQ：AgentDevFlow 与 gstack / superpower 的区别

---

## 一、背景

随着 `README.md` 中对 `AgentDevFlow`、`gstack`、`superpower` 差异的说明明确下来，一个自然的问题是：

**是否可以利用 `gstack / superpower` 来增强 AgentDevFlow 中各角色 Agent 的能力？**

从当前项目定位看，答案是：

**可以，而且值得做；但必须按“能力增强层”方式接入，不能替代 AgentDevFlow 本身的流程约束层。**

---

## 二、统一定位

三者解决的层级不同：

- `gstack`：偏工具与任务工作流，增强单个 Agent 的执行能力
- `superpower`：偏通用方法论与执行模式，增强单个 Agent 的规划、拆解和协作能力
- `AgentDevFlow`：偏多 Agent 的交付流程层，定义 `Issue / PRD / Tech / QA / Gate / Human Review / Release` 的正式协作机制

因此，统一定位应为：

**`gstack / superpower` 作为 AgentDevFlow 的“能力插件层”，按角色和阶段增强 Agent 的分析、评审、执行与验证能力。**

---

## 三、接入原则

### 原则 1：增强角色，不替代角色

`gstack / superpower` 只能增强：

- PM
- Architect
- QA
- Engineer
- PMO
- Team Lead

这些角色的工作质量与方法，不替代这些角色在 AgentDevFlow 流程中的正式职责。

例如：

- `plan-ceo-review` 可以增强 PM 的需求审视能力
- `plan-eng-review` 可以增强 Architect 的技术评审能力
- `review` 可以增强 Engineer 的代码审查能力

但这些 skill **不能替代**：

- PRD Gate 门控
- Tech Gate 门控
- QA Gate 门控
- Human Review
- Issue Comment Gate

### 原则 2：增强输出不能替代正式交付物

skill 生成的内容只能作为：

- 分析过程
- 补充视角
- 评审建议
- 质量增强输入

不能直接替代以下正式交付物：

- PRD
- Tech Spec
- QA Case Design
- QA Report
- Issue Comment
- 正式评审结论

也就是说：

**skill 负责“增强思考和执行质量”，正式文件负责“形成流程留痕与交付依据”。**

### 原则 3：默认不强依赖

AgentDevFlow 本体仍应保持可独立运行。

因此：

- 不安装 `gstack / superpower` 时，AgentDevFlow 仍应能完整运行
- 安装并启用后，只是在部分角色和阶段上获得更强能力

这决定了增强能力必须设计成一个 **可开关的增强层**，而不是强耦合主路径。

---

## 四、开关设计

### 目标

必须增加一个明确的能力增强开关，用于控制：

**当前项目是否启用 `gstack / superpower` 增强层。**

### 建议口径

建议采用统一术语：

- `增强层关闭`：仅使用 AgentDevFlow 原生机制
- `增强层开启`：允许角色在指定阶段调用 `gstack / superpower` 相关 skill

### 约束要求

如果增强层开启，则必须满足前置条件：

1. 已安装 `gstack` skill 包
2. 已安装 `superpower` skill 包
3. 对应运行环境能够正确发现并调用这些 skill

如果未满足安装前置条件，则：

- 不得在正式流程中默认依赖这些 skill
- 应回退到 AgentDevFlow 原生机制

### 建议默认值

建议默认值为：

**关闭**

原因：

- 保持 AgentDevFlow 本体自包含
- 避免把外部能力包变成 1.0 的强依赖
- 降低首次接入复杂度

---

## 五、建议的增强映射

### 1. Product Manager

可选增强：

- `brainstorming`
- `plan-ceo-review`

适用阶段：

- 需求澄清
- PRD 起草前
- PRD 文档评审前

价值：

- 提高需求边界澄清质量
- 提高范围判断与价值判断质量
- 提高方案发散和收敛质量

### 2. Architect

可选增强：

- `plan-eng-review`
- `brainstorming`

适用阶段：

- Tech Spec 起草前
- 技术方案评审前

价值：

- 提高架构边界收敛能力
- 提高风险识别和技术方案评审质量

### 3. QA Engineer

可选增强：

- `qa-only`
- `qa`

适用阶段：

- QA Case Design 后
- QA 验证阶段

价值：

- 提高验证覆盖率
- 提高测试证据质量
- 提高缺陷暴露率

### 4. Engineer

可选增强：

- `review`
- `investigate`

适用阶段：

- 开发前
- 修 Bug 时
- 代码 PR 前

价值：

- 提高结构化审查质量
- 提高定位根因和修复质量

### 5. Team Lead / PMO

可选增强：

- `brainstorming`
- `plan-devex-review`
- `document-release`

适用阶段：

- 流程改进
- 接入文档优化
- 发布后文档同步

价值：

- 提高机制设计质量
- 提高接入文档和发布文档一致性

---

## 六、接入边界

以下边界必须写清楚：

### 可以做的

- 在角色文档中说明“如增强层开启，可调用哪些 skill”
- 在平台文档中说明“启用增强层需要哪些安装前置”
- 在流程文档中说明“哪些阶段适合启用能力增强”

### 不能做的

- 不能让 AgentDevFlow 强依赖 `gstack / superpower`
- 不能把 skill 输出当作正式 Gate 结论
- 不能让 skill 替代正式角色职责
- 不能为了接 skill 而改造出 hedge-ai 之外的新流程能力边界

---

## 七、落地建议

建议按两步走：

### 第一步：先完成文档和口径收口

需要补充的内容包括：

- 在 `README.md` 或平台接入文档中说明增强层定位
- 在 Claude / Codex 平台文档中补充“增强层开关”说明
- 在相关角色文档中增加“可选增强 skill”说明

这一阶段先完成：

- 定位
- 边界
- 开关语义
- 安装前置

### 第二步：再决定是否做配置化接入

如果后续确认需要真正可执行的增强层开关，再进入实现阶段，例如：

- 配置文件开关
- 环境变量开关
- 平台适配器侧的条件启用逻辑

当前阶段不建议直接跳到实现，而应先把规则层和接入层文档沉淀完整。

---

## 八、统一结论

本次讨论的统一结论是：

1. `gstack / superpower` 适合作为 AgentDevFlow 的能力增强层接入
2. 它们增强的是角色能力，不替代流程约束
3. 它们的输出不能替代正式交付物和 Gate 结论
4. 增强层必须设计成一个显式开关
5. 若开启增强层，则必须先安装 `gstack` 与 `superpower` skill 包
6. AgentDevFlow 本体仍应保持在未开启增强层时可独立运行

---

## 九、建议后续动作

建议基于本方案创建一个 GitHub Issue，推进以下事项：

1. 明确增强层开关的文档口径
2. 决定增强层是否只做文档声明，还是继续进入实现
3. 梳理各角色对应可选增强 skill 清单
4. 补充平台接入文档中的安装前置说明

---

*方案完成 | 2026-04-14*
