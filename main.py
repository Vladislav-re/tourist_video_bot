
from tourist_video_bot.video_fetcher import download_video
from tourist_video_bot.caption_generator import generate_caption
from tourist_video_bot.telegram_poster import send_video_to_telegram
import os

def main():
    video_path, location = download_video()
    caption = generate_caption(location)
    send_video_to_telegram(video_path, caption)
    os.remove(video_path)

if __name__ == "__main__":
    main()
