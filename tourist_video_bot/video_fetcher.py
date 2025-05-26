
import yt_dlp
import random
import os
import sqlite3

DB_PATH = "history.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS videos (video_id TEXT PRIMARY KEY)")

def is_downloaded(video_id):
    with sqlite3.connect(DB_PATH) as conn:
        result = conn.execute("SELECT 1 FROM videos WHERE video_id = ?", (video_id,))
        return result.fetchone() is not None

def mark_downloaded(video_id):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("INSERT OR IGNORE INTO videos (video_id) VALUES (?)", (video_id,))

def download_video():
    init_db()
    locations = ["Rome", "Bangkok", "Tokyo", "Paris", "New York", "Barcelona"]
    location = random.choice(locations)
    search_query = f"{location} travel short"

    ydl_opts = {
        "format": "mp4",
        "outtmpl": "%(id)s.%(ext)s",
        "quiet": True,
        "noplaylist": True,
        "cookiefile": "cookies.txt",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch10:{search_query}", download=False)
        for entry in info.get("entries", []):
            if not is_downloaded(entry["id"]):
                print(f"[INFO] Downloading video: {entry['title']}")
                ydl.download([entry["webpage_url"]])
                filename = ydl.prepare_filename(entry)
                mark_downloaded(entry["id"])
                return filename, location

    raise Exception("No new videos found.")
