
import yt_dlp
import random
import os

def download_video():
    search_terms = ["travel vlog", "туризм", "приключения", "поездка"]
    query = random.choice(search_terms)
    output_path = "video.mp4"

    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': output_path,
        'noplaylist': True,
        'quiet': True,
        'cookiefile': 'cookies.txt'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_query = f"ytsearch1:{query}"
        info = ydl.extract_info(search_query, download=True)
        video_title = info['entries'][0]['title']

    return output_path, video_title
