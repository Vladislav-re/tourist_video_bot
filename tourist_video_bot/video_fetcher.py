
import yt_dlp
import os
import uuid

def download_video():
    search_query = "funny tourist travel moments"
    output_path = f"{uuid.uuid4()}.mp4"

    ydl_opts = {
        'format': 'mp4',
        'noplaylist': True,
        'quiet': True,
        'outtmpl': output_path,
        'default_search': 'ytsearch5',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search_query, download=True)
        if 'entries' in info:
            for entry in info['entries']:
                if entry and entry.get('title'):
                    return output_path, entry.get('title')

    raise Exception("No downloadable videos found.")
