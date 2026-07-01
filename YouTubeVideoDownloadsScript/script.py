"""
YouTube Video Downloader using yt-dlp

Installation:
    pip install yt-dlp

(Optional)
Install FFmpeg for best quality:
https://ffmpeg.org/download.html
"""

import os
import yt_dlp


def download_video():
    print("=" * 50)
    print("      YouTube Video Downloader")
    print("=" * 50)

    url = input("Enter YouTube Video URL: ").strip()

    if not url:
        print("Error: URL cannot be empty!")
        return

    download_folder = "Downloads"
    os.makedirs(download_folder, exist_ok=True)

    options = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": os.path.join(download_folder, "%(title)s.%(ext)s"),
        "noplaylist": True,
        "quiet": False,
        "progress_hooks": [],
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            print("\nDownloading...\n")
            ydl.download([url])

        print("\nDownload Completed Successfully!")
        print(f"Saved in: {os.path.abspath(download_folder)}")

    except Exception as e:
        print("\nDownload Failed!")
        print("Error:", e)


if __name__ == "__main__":
    download_video()