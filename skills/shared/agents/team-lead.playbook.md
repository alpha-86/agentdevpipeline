# Team Lead Playbook

## 何时启用

- 项目 kickoff
- 日常协调
- 跨角色冲突
- 超期 review 升级

## 执行循环

1. 识别当前交付阶段
2. 校验每个活跃项都有 linked issue 和 gate
3. 确认 owners、blockers 和 due dates
4. 在执行前读取当前会议或 review 对应的 workflow
5. 执行必需 review gates
6. 写 memo 并更新 todo registry

## 升级触发器

- review 超过约定 SLA，若未定义则默认 24h
- gate 被跳过或被绕过
- 范围或 owner 冲突
- blocked todo 没有 owner
- issue 状态与实际 gate 阶段不一致
