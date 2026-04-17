# GOV-010 Skill 结构冲突与不一致修复

## 基本信息

| 字段 | 内容 |
|------|------|
| PMO Issue | `docs/pmo/issues/010_2026-04-17_governance_skill_structure_consistency.md` |
| GitHub Issue | https://github.com/alpha-86/AgentDevFlow/issues/17 |
| 讨论日期 | 2026-04-17 |
| 验收日期 | 待填 |
| 状态 | ✅ 执行完成 |

---

## 一、P0 冲突修复

### P0-1: 产出者不评审自己的交付物

**决定**：在每个 SKILL 的"禁止行为"章节中显式声明"不得签署自己的交付物"。

**理由**：产出者不评审自己是三角制衡的核心原则，必须在每个角色的 SKILL 中显式声明，而非仅在 pipeline doc 中定义。

**执行动作**：
- 在 `skills/architect/SKILL.md` 禁止行为章节补充
- 在 `skills/qa-engineer/SKILL.md` 禁止行为章节补充
- 在 `skills/product-manager/SKILL.md` 禁止行为章节补充
- 在 `skills/engineer/SKILL.md` 禁止行为章节补充
- 在 `skills/team-lead/SKILL.md` 禁止行为章节补充
- 在 `skills/platform-sre/SKILL.md` 禁止行为章节补充

### P0-2: QA "三方签字"定义修正

**决定**：将 `skills/qa-engineer/SKILL.md` L23 中的"三方签字（PM + CTO + Engineer）"改为"三方签字（PM + Architect + Engineer）"。

**理由**："CTO"角色在 pipeline 中不存在，实际应为"Architect"。

---

## 二、P1 结构一致性修复

### P1-3: HR#1 命名统一

**决定**：统一为"Human Review #1"。

**理由**：消除命名歧义，与 `prompts/002_develop_pipeline.md` 保持一致。

**执行动作**：grep 全量替换所有 SKILL 文件中的"人工评审 #1"和"PR#1"为"Human Review #1"。

### P1-4: Architect 职责边界章节补全

**决定**：为 `skills/architect/SKILL.md` 补充完整的"职责边界"章节。

**理由**：Architect 是唯一缺少该章节的核心角色，导致与其他角色结构不一致。

**执行动作**：补充以下子章节：
- "完成"定义
- PR 合并权限
- 每个 Gate 的 Architect 职责与限制表

### P1-5: Platform/SRE 章节补全

**决定**：为 `skills/platform-sre/SKILL.md` 补充"职责边界"和"输出格式"章节。

**理由**：Platform/SRE 是唯一同时缺少这两个章节的角色。

---

## 三、P2 原则声明

### P2-6: "产出者不评审自己"原则显式声明

**决定**：在每个 SKILL 的"禁止行为"章节补充"不得签署自己的交付物"。

（已在 P0-1 中覆盖，统一执行）

### P2-7: PMO 章节顺序修正

**决定**：将 `skills/pmo/SKILL.md` 中的"何时启用"移至"必读文档"之前。

**理由**：与其他 SKILL 的章节顺序保持一致。

---

## 四、执行清单

| # | 待办 | 文件 | 状态 |
|---|------|------|------|
| 1 | P0-1: Architect 禁止行为补充 | `skills/architect/SKILL.md` | ✅ done |
| 2 | P0-1: 所有 SKILL 禁止行为补充 | `skills/*/SKILL.md` | ✅ done |
| 3 | P0-2: QA 三方签字修正 | `skills/qa-engineer/SKILL.md` | ✅ done |
| 4 | P1-3: HR#1 命名统一 | `skills/*/SKILL.md` | ✅ done |
| 5 | P1-4: Architect 职责边界补全 | `skills/architect/SKILL.md` | ✅ done |
| 6 | P1-5: Platform/SRE 章节补全 | `skills/platform-sre/SKILL.md` | ✅ done |
| 7 | P2-7: PMO 章节顺序修正 | `skills/pmo/SKILL.md` | ✅ done |
| 8 | GitHub Issue 创建 | — | ✅ done (#17) |
| 9 | QA Case L7 重复修正 | `skills/qa-engineer/SKILL.md` | ✅ done |
| 10 | Team Lead 产出者不评审自己补充 | `skills/team-lead/SKILL.md` | ✅ done |

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
