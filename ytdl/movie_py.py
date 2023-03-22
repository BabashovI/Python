# Import the necessary modules
import youtube_dl
import os

# Set the URL of the video to be downloaded
url = "https://www.youtube.com/watch?v=bFAVGed6sO0"

# Set the download directory
download_dir = "/tmp"

# Create the download directory if it does not exist
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Set the options for the download
ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192"
    }],
    "outtmpl": os.path.join(download_dir, "%(title)s.%(ext)s"),
    "quiet": False
}

# Download the video
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
