
from pytube import YouTube

VIDEO_URLS = [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://www.youtube.com/watch?v=aqz-KE-bpKQ",
    "https://www.youtube.com/watch?v=9No-FiEInLA"
]

def download_tourist_video():
    for url in VIDEO_URLS:
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(file_extension="mp4", progressive=True).order_by("resolution").desc().first()
            if stream:
                output_path = "video.mp4"
                stream.download(filename=output_path)
                print(f"Downloaded: {url}")
                return output_path, yt.title
        except Exception as e:
            print(f"Skipping unavailable video: {url}. Reason: {e}")
    
    raise Exception("No downloadable videos found.")
