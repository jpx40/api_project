import subprocess
import os

from yt_dlp import YoutubeDL



def down(url):
    cmd = "yt-dlp" + " " + str(url) + ' --format mp4  -P  /Users/jonas/IdeaProjects/api_dashboard/video/'

    subprocess.run(cmd, shell=True)


