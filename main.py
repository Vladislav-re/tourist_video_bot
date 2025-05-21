from tourist_video_bot.fetch_video import download_tourist_video
from tourist_video_bot.caption_generator import generate_caption
from tourist_video_bot.telegram_poster import post_to_telegram
import os

def main():
    video_path, location = download_tourist_video()
    if video_path:
        caption = generate_caption(location)
        post_to_telegram(video_path, caption)
        os.remove(video_path)

if __name__ == "__main__":
    main()
