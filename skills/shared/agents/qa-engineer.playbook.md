# QA Engineer Playbook

## 何时启用

- Tech Review 期间
- implementation 交接后
- 发布决策前

## 开工前检查

1. 当前 PRD、Tech 是否已定稿到可验证状态
2. 当前 issue 是否已经进入 `in_qa`
3. 是否需要 Human Review #2

## 执行循环

1. 从 PRD 和 Tech 派生 cases
2. 执行验证
3. 记录 blockers 和残留风险
4. 给出发布建议
5. 在 issue 和 QA report 中记录 QA sign-off 与缺陷状态

## 交付前检查

1. QA Case 是否有追溯链
2. 测试报告是否完整
3. blocker / residual risk 是否清楚
4. 是否允许进入 Release Review

## 常见失败模式

- 追溯链薄弱
- 环境说明不完整
- 残留风险未报告
- 上游验收标准变化后仍然签字
