
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from video_fetcher import download_video
from caption_generator import generate_caption
from telegram_poster import post_to_telegram

def main():
    video_path, location = download_video()
    caption = generate_caption(location)
    post_to_telegram(video_path, caption)
    os.remove(video_path)

if __name__ == "__main__":
    main()
