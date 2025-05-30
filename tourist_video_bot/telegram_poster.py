
import os
from telegram import Bot

def post_to_telegram(video_path, caption):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    channel_id = os.getenv("TELEGRAM_CHANNEL_ID")
    bot = Bot(token=token)

    with open(video_path, 'rb') as video:
        bot.send_video(chat_id=channel_id, video=video, caption=caption)

    os.remove(video_path)
