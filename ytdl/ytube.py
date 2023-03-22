import re
from pytube import Playlist, YouTube
import timeit
from pydub import AudioSegment
import os
from concurrent.futures import ThreadPoolExecutor
import datetime
import contextlib
import time


YOUTUBE_STREAM_AUDIO = '140' #'251' # modify the value to download a different stream
TMP_DIR = '/tmp/temp_mp3/'
MP3_DIR = '/Users/ibabashov/Desktop/mp3/'

playlist = Playlist('https://www.youtube.com/playlist?list=PLBIdr70JMtcIdGPIbydWfJbxBwDuKswrl')
#playlist = Playlist('https://www.youtube.com/playlist?list=PLLGmt3bXA_93pvHgKm7dbEvW410pDFKKl')

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(playlist.length)
# physically downloading the audio track
def create_tmp_dir():

    os.makedirs(TMP_DIR)

def ytube_download(playlist, TMP_DIR):
    os.chdir(TMP_DIR)
    for video in playlist.videos:
        if "Not Available" not in video.title:
            print(f"Downloading:  {video.title}")
            with contextlib.suppress(KeyError):
                audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
                audioStream.download()
            time.sleep(1)
#ytube_download(playlist, TMP_DIR)

def convert_webm():
    os.chdir(TMP_DIR)
    filenames = next(os.walk('.'), (None, None, []))[2]  # [] if no file
    #print(filenames)
    for file in filenames:
        name = file.split('.')
        # if name[-1] == "webm":
        given_audio = AudioSegment.from_file(f"{TMP_DIR}{file}", format="mp4")
        given_audio.export(f"{MP3_DIR}czech/{name[0]}.mp3", format="mp3", bitrate="128k")
        os.remove(file)
    #os.rmdir(TMP_DIR)

if __name__ == '__main__':

    start_time=datetime.datetime.now()
    #create_tmp_dir()
    ytube_download(playlist, TMP_DIR)
    convert_webm()
    end_time=datetime.datetime.now()
    exec_time= end_time-start_time
    print(f"Total execution time for the function {exec_time}")

    #tic=timeit.default_timer()
    #create_tmp_dir()
    # ytube_download(playlist, TMP_DIR)
    # convert_webm()
    #toc=timeit.default_timer()
    #print(f"Overall time spent: {int((toc - tic))}")
