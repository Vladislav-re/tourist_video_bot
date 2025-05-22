
import os
import uuid
import yt_dlp

def download_video():
    cookies_txt = os.getenv("YOUTUBE_COOKIES")
    with open("cookies.txt", "w", encoding="utf-8") as f:
        f.write(cookies_txt)

    output_path = f"{uuid.uuid4()}.mp4"
    ydl_opts = {
        "format": "mp4",
        "outtmpl": output_path,
        "quiet": True,
        "noplaylist": True,
        "cookiefile": "cookies.txt",
        "default_search": "ytsearch5",
    }

    query = "funny tourist travel moments"
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(query, download=True)
        if "entries" in result:
            first = result["entries"][0]
            return output_path, first.get("title", "Unknown location")
        else:
            return output_path, result.get("title", "Unknown location")
