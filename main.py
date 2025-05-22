
from fetch_video import download_tourist_video
from telegram_poster import post_to_telegram
from caption_generator import generate_caption

def main():
    video_path, video_title = download_tourist_video()
    caption = generate_caption(video_title)
    post_to_telegram(video_path, caption)

if __name__ == "__main__":
    main()
