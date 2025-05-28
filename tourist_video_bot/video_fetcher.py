
import yt_dlp

def download_video():
    search_query = "travel vlog"
    ydl_opts = {
        "format": "mp4",
        "outtmpl": "video.mp4",
        "noplaylist": True,
        "quiet": True,
        "cookies": "cookies.txt",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(f"ytsearch1:{search_query}", download=True)
        if 'entries' in result:
            video_info = result['entries'][0]
        else:
            video_info = result
        print(f"📍 Найдено видео: {video_info['title']}")
        return "video.mp4", video_info.get("title", "Unknown Location")
