from __future__ import unicode_literals
import yt_dlp as yt
import os
import time


def musicPlaylist(playlistURL):
    print(os.getcwd())
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio':True,
        'audioformat':'mp3',
        'ffmpeg_location': str(os.getcwd()),
        'outtmpl': u'%(title)s.%(ext)s',    # name the file the title of video
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt.YoutubeDL(ydl_opts) as ydl:
        ydl.download([str(playlistURL)])
        time.sleep(10)


def videoPlaylist(playlistURL):
        ydl_opts = {
            'ignoreerrors': True,
            'format': '(bestvideo[width>=1080][ext=mp4]/bestvideo)+bestaudio/best',
            'ffmpeg_location': str(os.getcwd()),
            'outtmpl': u'%(title)s.%(ext)s',  # name the file the title of video
            'writesubtitles': True,
            'subtitle': '--sub-lang en,es --write-sub',
            'fragment-retries': '--fragment-retries infinite'
        }

        with yt.YoutubeDL(ydl_opts) as ydl:
            ydl.download([str(playlistURL)])
            time.sleep(10)


def main():
    playlistURL = input('Please enter Youtube playlist URL: ')
    musicPlaylist(playlistURL)
    # videoPlaylist(playlistURL)


main()