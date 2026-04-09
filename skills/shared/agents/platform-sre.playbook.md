# Platform/SRE Playbook

## 何时启用

- 部署规划
- 发布准备
- 回滚规划
- CI 或运行稳定性工作

## 执行循环

1. 校验部署前提条件
2. 确认可观测性和 rollback 路径
3. 支持发布执行
4. 记录发布结果

## 常见失败模式

- 发布执行没有 rollback 证据链接
- 运行风险被接受但没有显式签字
- release record 和 issue 状态不同步
