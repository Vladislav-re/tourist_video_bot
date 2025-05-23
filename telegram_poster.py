
import os
from telegram import Bot

def post_to_telegram(video_path, caption):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHANNEL_ID")
    bot = Bot(token=token)
    with open(video_path, "rb") as video:
        bot.send_video(chat_id=chat_id, video=video, caption=caption)
