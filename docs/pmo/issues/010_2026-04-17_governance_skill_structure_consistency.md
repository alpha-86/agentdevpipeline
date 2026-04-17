# GOV-010 Skill 结构冲突与不一致

## 基本信息

| 字段 | 内容 |
|------|------|
| 类别 | governance |
| 优先级 | P0 |
| 状态 | Closed |
| 发现日期 | 2026-04-17 |
| 发现者 | PMO |
| Resolution | `../resolutions/010_2026-04-17_governance_skill_structure_consistency_resolution.md` |
| GitHub Issue | https://github.com/alpha-86/AgentDevFlow/issues/17 |

## 问题描述

### P0-1: Architect 强制规则未声明"不签自己的交付物"

`prompts/002_product_engineering_roles.md` 明确"产出者不评审自己"原则，但 `skills/architect/SKILL.md` 强制规则中未显式声明。

### P0-2: QA "三方签字"定义错误

`skills/qa-engineer/SKILL.md` L23 写"三方签字（PM + CTO + Engineer）"，但"CTO"角色在 pipeline 中不存在，应为"Architect"。

### P1-3: HR#1 命名混乱

7 个 SKILL 中出现三种写法：人工评审 #1、Human Review #1、PR#1，应统一为"Human Review #1"。

### P1-4: Architect 缺少"职责边界"章节

PM、QA、Engineer、PMO、Team Lead 都有"职责边界"章节，Architect 是唯一缺失的核心角色。

### P1-5: Platform/SRE 缺少"职责边界"和"输出格式"章节

唯一同时缺少这两个章节的角色。

### P2-6: "产出者不评审自己"原则未在各 SKILL 中显式声明

`002_product_engineering_roles.md` 已明确，但各 SKILL 强制规则中无显式声明。

### P2-7: PMO 章节顺序异常

"何时启用"在"必读文档"之后，与其他 SKILL 顺序不一致。

## 讨论结论

详见 `../resolutions/010_2026-04-17_governance_skill_structure_consistency_resolution.md`

## 关联 Issue

- Refs #16（GitHub Issue 追踪）

## 里程碑

- [x] 创建 PMO Issue
- [x] 执行 P0-1/P0-2 修复
- [x] 执行 P1-3 HR#1 命名统一
- [x] 执行 P1-4 Architect 职责边界补全
- [x] 执行 P1-5 Platform/SRE 章节补全
- [x] 执行 P2-6 产出者不评审自己原则声明
- [x] 执行 P2-7 PMO 章节顺序修正
- [x] 创建 GitHub Issue
- [ ] 修复验收（待 Team Lead 确认）

---

*由 PMO (adf-pmo) 生成 | 2026-04-17*
