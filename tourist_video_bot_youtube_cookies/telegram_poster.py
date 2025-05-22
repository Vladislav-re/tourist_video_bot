
import os
from telegram import Bot

def post_to_telegram(video_path, caption):
    bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    with open(video_path, "rb") as video:
        bot.send_video(chat_id=chat_id, video=video, caption=caption)
