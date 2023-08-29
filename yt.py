import subprocess
import os

from yt_dlp import YoutubeDL



def down(url):
    cmd = "yt-dlp" + " " + str(url) + ' --format mp4 filename -P  /Users/jonas/IdeaProjects/api2/video/ filenames video.mp4'

    subprocess.run(cmd, shell=True)


