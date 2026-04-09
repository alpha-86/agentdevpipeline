# Gate Queue 示例

| Queue ID | Project ID | Issue ID | Gate | Current Status | Required Signoffs | Missing Items | Blocking Reason | Next Action | Owner |
|----------|------------|----------|------|----------------|-------------------|---------------|-----------------|-------------|-------|
| GQ-001 | `agentdevpipeline-core` | `#101` | `prd_review` | `in_progress` | `PM + Tech Lead` | `Tech Lead 评审结论` |  | `完成 PRD Gate 评论` | `product-manager` |
| GQ-002 | `agentdevpipeline-core` | `#102` | `tech_review` | `blocked` | `PM + Tech Lead + QA` | `Issue Comment` | `缺少正式 Gate 评论` | `补充结构化评论并重跑平台检查` | `tech-lead` |
| GQ-003 | `agentdevpipeline-core` | `#103` | `release_review` | `blocked` | `PM + Tech Lead + QA + Human Review #2` | `Human Review #2 结论` | `发布前人审未完成` | `发起 human_review.requested` | `team-lead` |
