# Process Auditor Playbook

## 何时启用

- 日常流程巡检
- PR / Gate 合规检查
- 周复盘 / 月复盘
- 例外审批检查

## 开工前检查

1. 明确审计范围：单 issue、单项目还是项目组合。
2. 读取最近一次审计记录和当前 warning / fail 项。
3. 检查是否存在有效例外审批。

## 执行循环

1. 检查 issue 与实际 gate 是否一致。
2. 检查 PRD / Tech / QA / Release / Human Review 证据是否齐全。
3. 检查 todo 是否具备 owner / due / evidence。
4. 检查 comment、artifact linkage 和 release record 是否完整。
5. 输出 `pass / warning / fail` 结论与纠正动作。

## 交付前检查

1. fail 项是否都已形成纠正动作
2. owner 和 due 是否明确
3. warning 项是否已写明影响范围
4. 审计结论是否已回链主 issue 或项目视图
