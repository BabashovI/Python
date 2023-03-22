from __future__ import unicode_literals
import youtube_dl
from pytube import Playlist
import re


DOWNLOAD_DIR = '/Users/ibabashov/Desktop/mp3'

playlist = Playlist(
    'https://www.youtube.com/playlist?list=PLBIdr70JMtcIdGPIbydWfJbxBwDuKswrl')
# playlist = Playlist('https://www.youtube.com/playlist?list=PLLGmt3bXA_93pvHgKm7dbEvW410pDFKKl')

playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
# print(list(playlist.video_urls))


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '/Users/qwe/Desktop/mp3/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '64',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
print("test")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    print("test with")
    ydl.download(list(playlist.video_urls))
