
import yt_dlp
import random
import os

def download_video():
    with open("cookies.txt", "r") as f:
        cookies = f.read()

    tourist_keywords = ["travel tips", "funny travel", "travel fails", "tourist advice"]
    keyword = random.choice(tourist_keywords)

    ydl_opts = {
        "format": "mp4",
        "outtmpl": "video.%(ext)s",
        "cookiefile": "cookies.txt",
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch5:{keyword}", download=True)["entries"][0]
        return ydl.prepare_filename(info), info.get("title", "Travel moment")
