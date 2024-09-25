import yt_dlp
import time
import random


def download_youtube_video(url: str, output_dir: str = './youtube-videos'):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("Download completed successfully!")
            time.sleep(random.uniform(1, 5))  # Random sleep between 1-5 seconds
    except Exception as e:
        print(f"Error downloading video: {e}")


url = [
    "https://www.youtube.com/watch?v=M0lUdywLMQs",
]
for _ in url:
    download_youtube_video(_)
