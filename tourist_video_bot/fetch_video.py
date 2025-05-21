import os
from pytube import YouTube
import random

def download_tourist_video():
    sample_videos = [
        ("https://www.youtube.com/watch?v=oB69NIfZx8Y", "Бали"),
        ("https://www.youtube.com/watch?v=5oKJ0t8g-Og", "Париж"),
        ("https://www.youtube.com/watch?v=GZz0IhA6sWQ", "Тбилиси"),
    ]
    url, location = random.choice(sample_videos)
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension="mp4", progressive=True).order_by("resolution").desc().first()
    output_path = stream.download(filename="video.mp4")
    return output_path, location
