# 补齐 release install bootstrap 端到端演练证据计划

**编号**: 026  
**阶段**: `P2-1`  
**日期**: 2026-04-14  
**来源文档**:
- `026_2026-04-14_迁移进展审计报告_review.md`
- `026_PLAN_2026-04-14_迁移进展审计_待修复清单.md`

**目标**: 为 `install / bootstrap / release` 三条关键路径补齐端到端演练证据，证明脚本和文档不只是“存在”，而是“经过验证”。

---

## 一、问题定义

当前仓库已经有：

- `scripts/install.sh`
- `scripts/release.sh`
- `.github/workflows/bootstrap-sync.py`
- `.github/workflows/bootstrap-sync.yml`

但仍缺少一份清晰的、可回溯的端到端演练证据，来回答：

- 安装是否真实可跑
- 自举同步是否真实可用
- 发布流程是否真实可执行

---

## 二、演练范围

### 1. install 路径

目标：

- 验证 `scripts/install.sh --dry-run`
- 验证 `scripts/install.sh --channel dev --target <dir>`
- 确认生成结果与文档一致

### 2. bootstrap 路径

目标：

- 验证 `skills/shared/` 变更后能否正确生成 `.claude/skills/adf-*`
- 验证关键入口产物是否正确

### 3. release 路径

目标：

- 验证 `scripts/release.sh` 的前置检查、版本处理、tag 创建逻辑
- 至少形成 dry-run 或受控演练证据

---

## 三、涉及文件

- `scripts/install.sh`
- `scripts/release.sh`
- `.github/workflows/bootstrap-sync.py`
- `.github/workflows/bootstrap-sync.yml`
- `docs/platforms/claude-code.md`
- `docs/platforms/codex.md`
- 后续新增的演练记录文档

---

## 四、交付物建议

本阶段建议补齐以下交付物：

1. `install` 演练记录
2. `bootstrap` 演练记录
3. `release` 演练记录
4. 如有问题，附修复记录或阻断说明

---

## 五、完成标准

`P2-1` 完成时，必须同时满足：

1. 三条关键路径至少各有一份演练证据
2. 关键命令、预期结果、实际结果被记录
3. 若某条路径未通过，阻断点被明确记录

---

## 六、交付结论

本阶段完成后的目标结论应是：

**install / bootstrap / release 三条关键路径已有可追溯演练证据。**
