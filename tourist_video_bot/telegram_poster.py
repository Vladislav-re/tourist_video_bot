
import os
from telegram import Bot

def post_to_telegram(video_path, caption):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    channel_id = os.getenv("TELEGRAM_CHANNEL_ID")
    bot = Bot(token=bot_token)
    with open(video_path, "rb") as video_file:
        bot.send_video(chat_id=channel_id, video=video_file, caption=caption)
