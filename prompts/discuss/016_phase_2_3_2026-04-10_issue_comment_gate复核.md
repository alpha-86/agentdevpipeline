# 027 - 2026-04-10 Phase 2.3 Issue Comment Gate 复核

## 对照源文件

- `hedge-ai/prompts/V3.0/change_record/V2.2.5_Issue_Comment机制修复与强制Gate建立.md`

## 本次只复核什么

本次只复核这三件事：

1. Issue Comment 必须成为正式 Gate
2. Comment 必须真实写到目标 Issue
3. Comment 缺失或投递失败时，必须阻断下游动作

## 当前项目原有问题

当前仓库已经强调了：

- Comment 必须结构化
- 没有 Comment 的阶段视为未完成
- Comment 与产物要能回链

但还缺源文档里最关键的一层“执行真实性”约束：

- 不是生成了本地 pending comment 就算完成
- 自动投递失败时不能继续报 success
- 缺 Comment 应该直接阻断 PR / Gate，而不是只写成建议

## 本次落地调整

### 1. 补齐 Comment 成功的判定

现在已经明确：

- Comment 只有真正写入目标 Issue 后才算完成
- 本地草稿、pending 文件、聊天摘要都不算正式完成

### 2. 补齐失败处理约束

现在已经明确：

- 自动投递失败时，当前动作必须返回失败状态
- 不能把“评论没发出去”的情况伪装成成功
- 缺失 Comment 时必须阻断下游动作

### 3. 把阻断条件落到检查模板

`review-comment-checklist-template.md` 已补充：

- comment 已真实写入目标 issue
- 代码 PR 前置检查时，上游必需 comment 已存在
- 自动投递失败时返回非成功状态

## 结论

`Issue Comment Gate` 这条线，现在比之前更接近 `hedge-ai V2.2.5` 的原始要求了，特别是：

- 从“结构化评论”收紧到“真实落地评论”
- 从“建议检查”收紧到“缺失就阻断”
- 从“留痕原则”收紧到“失败必须显式失败”

后续仍需继续推进的部分：

- 插件入口层如何承载 comment 检查
- README 流程图如何简洁体现 comment gate
- 与 PMO 主动合规检查的联动
