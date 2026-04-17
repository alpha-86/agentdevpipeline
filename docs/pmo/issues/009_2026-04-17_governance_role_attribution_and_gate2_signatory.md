# GOV-009 职责归属矩阵缺失 + Gate 2 签字规范问题

## 基本信息

| 字段 | 内容 |
|------|------|
| 类别 | governance |
| 优先级 | P1 |
| 状态 | Open |
| 发现日期 | 2026-04-17 |
| 发现者 | PMO |
| Resolution | `../resolutions/009_2026-04-17_governance_role_attribution_and_gate2_signatory_resolution.md` |

## 问题描述

### 问题 1: Gate 2 — Architect self-review

`prompts/002_develop_pipeline.md` Gate 2 规定"Architect（必签）"，但 Architect 也是 Tech Spec 的产出者，造成 self-review。

**影响**：Tech Spec 评审缺乏真正的独立制衡。

### 问题 2: 职责归属矩阵缺失

PRD / Tech Spec / QA Case 设计文档 / 代码 / 测试报告 各交付物的产出角色、评审角色、评审立场未明确。

### 问题 3: Gate 定义不一致

`prompts/004_delivery_gates.md`（V2.3）和 `prompts/002_develop_pipeline.md`（Gate 0~5）存在重复定义。

## 讨论结论

详见 `../resolutions/009_2026-04-17_governance_role_attribution_and_gate2_signatory_resolution.md`

**已达成的宏观结论**：
1. Gate 2：Engineer + QA 签字，Architect 主持不签自己的
2. 产出者不评审自己，三角制衡
3. 统一 Gate 定义到 `002_develop_pipeline.md`
4. 下一轮逐个细化 5 个产出物的评审逻辑

## 关联 Issue

- Refs #3（Tech Spec self-review 发生在此 Issue 的 Gate 2）
- Refs #16（GitHub Issue 追踪）

## 里程碑

- [ ] 讨论 PRD 评审逻辑
- [ ] 讨论 Tech Spec 评审逻辑
- [ ] 讨论 QA Case 设计文档评审逻辑
- [ ] 讨论代码评审逻辑
- [ ] 讨论测试报告评审逻辑
- [ ] 统一 Gate 定义文档
- [ ] GitHub Issue 关闭

---

*由 PMO (adf-pmo) 生成 | 2026-04-17*
