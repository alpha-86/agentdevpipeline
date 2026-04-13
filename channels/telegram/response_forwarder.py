#!/usr/bin/env python3
"""
Telegram 响应转发器

持续监控 .claude/telegram_response_queue/ 目录，
将 Team Lead 的回复发送回对应用户。

Team Lead 回复格式 (.response 文件):
{
    "issue_id": "telegram_abc12345",  # 用于查找 chat_id
    "chat_id": 123456789,            # 可选，直接指定 chat_id
    "text": "这是 Team Lead 的回复"
}

循环完成后删除 .response 文件。
"""

import os
import sys
import json
import time
import logging
from pathlib import Path
from typing import Dict, Optional

# 添加项目路径
AGENTDEVFLOW_ROOT = Path(__file__).parent.parent.parent.resolve()
sys.path.insert(0, str(AGENTDEVFLOW_ROOT))

from channels.telegram.bot_server import get_bot_server, TelegramBotServer

# 配置
RESPONSE_QUEUE_DIR = AGENTDEVFLOW_ROOT / ".claude" / "telegram_response_queue"
SESSION_FILE = AGENTDEVFLOW_ROOT / ".claude" / "telegram_sessions.json"
LOG_FILE = AGENTDEVFLOW_ROOT / "logs" / "response_forwarder.log"

# 日志配置
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
handler = logging.FileHandler(LOG_FILE)
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger = logging.getLogger("response_forwarder")
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def load_sessions() -> Dict[str, int]:
    """加载 session -> chat_id 映射"""
    try:
        if SESSION_FILE.exists():
            with open(SESSION_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        logger.warning(f"加载 sessions 失败: {e}")
    return {}


def get_chat_id_for_response(issue_id: str, direct_chat_id: Optional[int] = None) -> Optional[int]:
    """获取响应目标 chat_id

    优先级:
    1. 直接指定的 chat_id
    2. 通过 issue_id 查找 session 映射
    """
    if direct_chat_id:
        return direct_chat_id

    sessions = load_sessions()
    chat_id = sessions.get(issue_id)
    if chat_id:
        logger.info(f"通过 session 找到 chat_id: {issue_id} -> {chat_id}")
    return chat_id


def process_response_file(resp_file: Path, bot: TelegramBotServer) -> bool:
    """处理单个 response 文件"""
    try:
        content = resp_file.read_text(encoding="utf-8")
        resp_data = json.loads(content)

        issue_id = resp_data.get("issue_id", "")
        direct_chat_id = resp_data.get("chat_id")
        text = resp_data.get("text", "")

        if not text:
            logger.warning(f"响应文件 {resp_file.name} 无 text 字段")
            return False

        # 获取目标 chat_id
        chat_id = get_chat_id_for_response(issue_id, direct_chat_id)
        if not chat_id:
            logger.error(f"无法确定 chat_id: issue_id={issue_id}, direct_chat_id={direct_chat_id}")
            return False

        # 发送消息
        result = bot.send_message(chat_id, text)
        if result:
            logger.info(f"响应已转发到 chat_id={chat_id}, issue_id={issue_id}")
            resp_file.unlink()  # 删除已处理的响应文件
            return True
        else:
            logger.error(f"发送消息失败: chat_id={chat_id}")
            return False

    except json.JSONDecodeError as e:
        logger.error(f"JSON 解析失败 {resp_file.name}: {e}")
        resp_file.unlink()  # 删除无效文件
        return False
    except Exception as e:
        logger.error(f"处理响应文件 {resp_file.name} 失败: {e}")
        return False


def run_forwarder(poll_interval: int = 2):
    """运行响应转发器主循环"""
    logger.info("=" * 50)
    logger.info("Telegram Response Forwarder 启动")
    logger.info(f"监控目录: {RESPONSE_QUEUE_DIR}")
    logger.info(f"轮询间隔: {poll_interval}s")
    logger.info("=" * 50)

    RESPONSE_QUEUE_DIR.mkdir(parents=True, exist_ok=True)

    # 获取 bot 实例
    try:
        bot = get_bot_server()
        logger.info("Bot 服务器连接成功")
    except Exception as e:
        logger.error(f"无法连接 Bot 服务器: {e}")
        sys.exit(1)

    processed_count = 0
    error_count = 0

    while True:
        try:
            response_files = sorted(RESPONSE_QUEUE_DIR.glob("*.response"))
            if not response_files:
                time.sleep(poll_interval)
                continue

            for resp_file in response_files:
                success = process_response_file(resp_file, bot)
                if success:
                    processed_count += 1
                else:
                    error_count += 1

            time.sleep(poll_interval)

        except KeyboardInterrupt:
            logger.info("收到中断信号，停止 Response Forwarder")
            break
        except Exception as e:
            logger.error(f"主循环异常: {e}")
            error_count += 1
            time.sleep(poll_interval)

    logger.info(f"Response Forwarder 已停止 (processed={processed_count}, errors={error_count})")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Telegram Response Forwarder")
    parser.add_argument("--interval", "-i", type=int, default=2, help="轮询间隔 (秒)")
    args = parser.parse_args()

    run_forwarder(poll_interval=args.interval)
