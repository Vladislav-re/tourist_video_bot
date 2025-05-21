import os
import asyncio
import random
import yt_dlp
import requests
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

VIDEOS = [
    {
        "url": "https://www.youtube.com/shorts/Xu2id_7I7_k",
        "location": "Пикос-де-Европа, Испания 🇪🇸"
    },
    {
        "url": "https://www.youtube.com/shorts/B4UgaFJDdOY",
        "location": "Бангкок, Таиланд 🇹🇭"
    }
]

def download_video(url, filename="video.mp4"):
    ydl_opts = {
        'outtmpl': filename,
        'format': 'mp4',
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def generate_caption(location):
    prompt = (
        f"Сделай короткое описание (до 50 слов) туристического видео. Локация: {location}. "
        "Событие — турист попадает в неловкую или необычную ситуацию. "
        "Напиши с иронией, но не слишком грубо, добавь эмодзи, не упоминай название видео."
    )

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://t.me/a_kak_zarabotat",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Ты автор тревел-канала с ироничным стилем."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    if "choices" in response.json():
        return f"📍 {location}

{response.json()['choices'][0]['message']['content'].strip()}"
    else:
        return f"📍 {location}

(Описание не сгенерировано)"

async def send_video(file_path, caption):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    with open(file_path, "rb") as video:
        await bot.send_video(chat_id=CHANNEL_ID, video=video, caption=caption, parse_mode="HTML")

def cleanup(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

if __name__ == "__main__":
    selected = random.choice(VIDEOS)
    try:
        download_video(selected["url"])
        caption = generate_caption(selected["location"])
        asyncio.run(send_video("video.mp4", caption))
        print("✅ Видео отправлено")
    except Exception as e:
        print("❌ Ошибка:", e)
    finally:
        cleanup("video.mp4")
