# GOV-009 职责归属矩阵 + Gate 2 签字规范

## 基本信息

| 字段 | 内容 |
|------|------|
| PMO Issue | `docs/pmo/issues/009_2026-04-17_governance_role_attribution_and_gate2_signatory.md` |
| GitHub Issue | https://github.com/alpha-86/AgentDevFlow/issues/16 |
| 讨论日期 | 2026-04-17 |
| 验收日期 | 2026-04-17 |
| 状态 | ✅ 执行完成，待验收 |

---

## 一、问题回顾

### Issue 1: Gate 2 签字 — Architect self-review

**问题描述**：`prompts/002_develop_pipeline.md` Gate 2 章节规定"Architect（必签）"，但 Architect 也是 Tech Spec 的产出者，造成 self-review 违规。

**影响**：Tech Spec 的评审缺乏真正的独立制衡，降低了技术方案评审的质量保障。

### Issue 2: 职责归属矩阵缺失

**问题描述**：PRD / Tech Spec / QA Case 设计文档 / 代码 / 测试报告各交付物的产出角色和评审角色未明确，尤其是每个评审角色的**立场**未定义。

**影响**：Agent 在执行评审时缺乏明确立场，可能导致评审流于形式。

### Issue 3: Gate 定义不一致

**问题描述**：`prompts/004_delivery_gates.md`（Gate 编号 V2.3）和 `prompts/002_develop_pipeline.md`（Gate 0~5）各有一套 Gate 定义，存在不一致。

**影响**：Agent 和 Human 引用不同版本，导致流程执行歧义。

---

## 二、讨论对齐结论

### 结论 1: Gate 2 签字规范

**决定**：Architect 主持 Tech Spec 评审，**Engineer + QA 签字**。Architect 作为评审人参与，不签自己的 Tech Spec。

**理由**：产出者不评审自己的交付物，是评审的基本原则。Engineer 作为实现者，最有立场评估 Tech Spec 的可实现性；QA 作为测试路径设计者，评估 Tech Spec 的可测试性。

**执行动作**：更新 `prompts/002_develop_pipeline.md` Gate 2 签字要求，将 "Architect（必签）" 改为 "Engineer（必签）" + "QA（必签）"。

---

### 结论 2: 职责归属原则

**核心原则**：产出者不评审自己交付物，通过三角制衡确保评审质量。

**完整产出物清单**（含评审立场定义，已通过 `/plan-ceo-review` 讨论细化）：

| # | 产出物 | 产出角色 | 评审角色 | 评审立场 | 状态 |
|---|--------|---------|---------|---------|------|
| 1 | PRD | PM | Architect（必签）、PM（自审） | Architect：技术可行性 + 需求合理性；PM：需求完整性 + 范围控制 | ✅ 已讨论 |
| 2 | Tech Spec | Architect | Engineer（必签）、QA（必签） | Engineer：可实现性；QA：可测试性；PRD 不含技术实现，Tech Spec 不含代码 | ✅ 已讨论 |
| 3 | QA Case 设计文档 | QA | Architect（Architecture 维度）、QA（Test 维度，自审）、Engineer（可实现性维度）、QA+Engineer（Data 维度，联合） | Architecture：技术可测性；Test：测试覆盖完整性；可实现性：测试步骤是否可达；Data：测试数据设计合理性 | ✅ 已讨论 |
| 4 | 代码 | Engineer | Architect（必签）、QA（必签） | Architect：架构一致性（是否符合 Tech Spec 设计）；QA：功能覆盖率（是否覆盖 QA Case 所有用例） | ✅ 已讨论 |
| 5 | 测试报告 | QA | PM（必签）、Engineer（必签） | PM：验收口径（是否满足 PRD 验收标准，残留风险是否可接受）；Engineer：缺陷处理（所有缺陷是否已修复，修复方案是否合理） | ✅ 已讨论 |

**核心原则**：
- 产出者不评审自己（三角制衡）
- PRD 不含技术实现内容
- Tech Spec 不含代码内容
- QA Case 设计文档 ≠ case 实现代码
- 测试报告 = 跑完所有 case + 驱动 Engineer 修复 bug 后的过程记录文档
- 引入 gstack 多维度评审模式：评审分多个独立维度，每个维度有明确立场

**执行动作**：下一步将完整结论写入 `prompts/002_product_engineering_roles.md` 和 `prompts/002_develop_pipeline.md`。

---

### 结论 3: Gate 定义统一

**决定**：以 `prompts/002_develop_pipeline.md` 为唯一 Gate 定义源，`prompts/004_delivery_gates.md` 中的 Gate 编号定义（V2.3）删除或降级为 CI 检查逻辑参考附录。

**理由**：两份文档存在本质重复，以更完整的 pipeline doc 为准，消除二义性。

**执行动作**：
1. 将 `004_delivery_gates.md` 中 CI 检查逻辑部分迁移到独立文件 `ci-gate-checks.md`
2. 删除 `004_delivery_gates.md` 中的 Gate 定义章节
3. 或直接删除 `004_delivery_gates.md`，将 CI 检查逻辑集成到 `021_platform_checks_and_gate_automation.md`

---

## 三、GitHub Issue 追踪

| 字段 | 内容 |
|------|------|
| GitHub Issue URL | 待创建 |
| 责任人 | PMO |
| 关联 PMO Issue | `../issues/009_2026-04-17_governance_role_attribution_and_gate2_signatory.md` |

---

## 四、待办清单

| # | 待办 | 负责人 | 状态 |
|---|------|--------|------|
| 1 | 更新 Gate 2 签字规范：Engineer + QA 必签，Architect 主持 | PMO | ✅ done |
| 2 | 将 5 个产出物的评审角色+立场写入 `prompts/002_product_engineering_roles.md` | PMO | ✅ done |
| 3 | 更新 `prompts/002_develop_pipeline.md` Gate 2 签字矩阵 | PMO | ✅ done |
| 4 | 统一 Gate 定义：删除 `004_delivery_gates.md` 重复内容 | PMO | ✅ done |
| 5 | GitHub Issue #16 关联 Issue #3（Gate 2 合规偏离） | PMO | pending |

---

## 五、验收结论

| 字段 | 内容 |
|------|------|
| 最终验收人 | Team Lead |
| 验收日期 | 待填 |
| GitHub Issue 状态 | 待创建 |
| PMO Issue 状态 | Open |

---

*由 PMO (adf-pmo) 基于 `/plan-ceo-review` 讨论生成 | 2026-04-17*
