
import os
from tourist_video_bot.video_fetcher import download_video
from tourist_video_bot.caption_generator import generate_caption
from tourist_video_bot.telegram_poster import post_to_telegram

def main():
    print("🔁 Запуск бота...")
    try:
        video_path, location = download_video()
        if not os.path.exists(video_path):
            print(f"❌ Видео не найдено по пути: {video_path}")
            return
        print(f"✅ Видео скачано: {video_path}")
        caption = generate_caption(location)
        print(f"📝 Сгенерировано описание: {caption}")
        post_to_telegram(video_path, caption)
        print(f"📤 Видео отправлено в Telegram: {video_path}")
        os.remove(video_path)
        print(f"🗑️ Видео удалено: {video_path}")
    except Exception as e:
        print(f"🚨 Ошибка при выполнении: {e}")

if __name__ == "__main__":
    main()
