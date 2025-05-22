
from tourist_video_bot.video_fetcher import download_video
from tourist_video_bot.caption_generator import generate_caption
from tourist_video_bot.telegram_poster import post_to_telegram
import os

def main():
    video_path, location = download_video()
    caption = generate_caption(location)
    post_to_telegram(video_path, caption)
    if os.path.exists(video_path):
        os.remove(video_path)
    if os.path.exists("cookies.txt"):
        os.remove("cookies.txt")

if __name__ == "__main__":
    main()
