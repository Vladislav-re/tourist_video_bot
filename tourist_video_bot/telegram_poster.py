
import os
from telegram import Bot

def send_video_to_telegram(video_path, caption):
    bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
    channel_id = os.getenv("TELEGRAM_CHANNEL_ID")
    with open(video_path, 'rb') as video_file:
        bot.send_video(chat_id=channel_id, video=video_file, caption=caption)
