# Team Lead Playbook

## 何时启用

- 项目 kickoff
- 日常协调
- 跨角色冲突
- 超期 review 升级

## 开工前检查

1. 检查活跃 issue、当前 gate 和 blocked 项。
2. 检查 todo registry 中的逾期项和缺 owner 项。
3. 确认今天要主持的会议，并先读对应 workflow。

## 执行循环

1. 识别当前交付阶段
2. 校验每个活跃项都有 linked issue 和 gate
3. 确认 owners、blockers 和 due dates
4. 在执行前读取当前会议或 review 对应的 workflow
5. 执行必需 review gates
6. 写 memo 并更新 todo registry

## 交付前检查

1. 会议纪要是否已落地
2. todo 是否都具备 owner / due / evidence
3. issue 状态是否与实际阶段一致
4. 是否存在未升级的超时 review

## 升级触发器

- review 超过约定 SLA，若未定义则默认 24h
- gate 被跳过或被绕过
- 范围或 owner 冲突
- blocked todo 没有 owner
- issue 状态与实际 gate 阶段不一致
