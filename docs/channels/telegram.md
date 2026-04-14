# Telegram 通道接入

## 作用

Telegram 在 AgentDevFlow 中承担的是移动端实时沟通与状态跟进通道，不是正式交付主线。

正式流程主线仍然是：

- GitHub Issue
- 文档交付物
- PR / Human Review

Telegram 负责：
- 移动端实时通知
- 进展查看
- 人与 Agent 的即时沟通

## 配置方式

### 方式一：环境变量（推荐）

```bash
export TELEGRAM_BOT_TOKEN=<your-bot-token>
```

Bot Token 由 @BotFather 在 Telegram 中创建获取。

### 方式二：配置文件

创建 `/.claude/config/bot_config.json`：

```json
{
  "telegram": {
    "token": "<your-bot-token>",
    "chat_ids": [123456789]
  }
}
```

- `token`: Bot Token（与环境变量 TELEGRAM_BOT_TOKEN 等效）
- `chat_ids`: 授权用户 ID 列表（整数数组），用于白名单验证

### chat_ids 配置说明

- `chat_ids` 仅支持配置文件方式，不支持环境变量
- 格式为整数数组，如 `[123456789, 987654321]`
- 如果不配置 `chat_ids`，Bot 会自动授权所有发送过消息的用户
- 获取自己的 chat_id：发送 `/start` 给 Bot，然后查看 Bot 日志或使用 `scripts/send_telegram.py --setup`

## 最小运行步骤

1. **获取 Bot Token**
   - 在 Telegram 搜索 @BotFather
   - 发送 `/newbot` 创建机器人
   - 复制获得的 Token

2. **配置 Token**
   ```bash
   export TELEGRAM_BOT_TOKEN=<your-token>
   ```

3. **启动 Bot**
   ```bash
   # 直接运行
   python channels/telegram/bot_server.py

   # 或使用 systemd service
   sudo cp scripts/telegram_bot.service /etc/systemd/system/
   sudo systemctl enable telegram_bot
   sudo systemctl start telegram_bot
   ```

4. **获取 chat_id（可选，用于白名单）**
   ```bash
   # 先发送 /start 给 Bot
   python scripts/send_telegram.py --setup
   ```

5. **验证运行**
   ```bash
   # 查看日志
   tail -f logs/telegram_bot.log

   # 检查服务状态
   sudo systemctl status telegram_bot
   ```

## 组件说明

### bot_server.py

Telegram Bot 服务器核心组件，负责：

- 接收用户消息并写入 `.claude/task_queue/`
- 提供命令菜单（/start /help /status /health）
- 维护 session 映射（`.claude/telegram_sessions.json`）用于 Team Lead 回复闭环

### response_forwarder.py

Team Lead 回复转发器，持续监控 `.claude/telegram_response_queue/` 目录：

- 读取 Team Lead 写入的 `.response` 文件
- 根据 `issue_id` 查找对应 session 的 `chat_id`
- 将回复发送回 Telegram 用户
- 发送完成后删除 `.response` 文件

启动方式：
```bash
python channels/telegram/response_forwarder.py
```

### send_telegram.py

命令行消息发送工具：

```bash
# 设置 chat_id
python scripts/send_telegram.py --setup

# 发送自定义消息
python scripts/send_telegram.py --text "Hello from AgentDevFlow"
```

## 目录结构

```
.claude/
  config/
    bot_config.json      # Bot 配置（token, chat_ids）
  task_queue/            # 用户消息写入，触发 Team Lead 处理
  telegram_response_queue/  # Team Lead 回复，response_forwarder 消费
  telegram_sessions.json # session -> chat_id 映射
logs/
  telegram_bot.log      # Bot 运行日志
  response_forwarder.log # 转发器日志
```

## 使用边界

- Telegram 负责移动端实时通知、进展查看和人与 Agent 的即时沟通
- Telegram 不能替代 GitHub Issue、文档交付物和正式评审结论
- 关键结论仍必须回写到 GitHub Issue 和对应文件交付物

## 相关文件

- `channels/telegram/bot_server.py` - Bot 服务器
- `channels/telegram/response_forwarder.py` - 回复转发器
- `scripts/send_telegram.py` - CLI 发送工具
- `scripts/telegram_bot.service` - systemd service 模板
- `channels/core/telegram_monitor.py` - 消息监控与统计
