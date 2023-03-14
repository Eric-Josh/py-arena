from pytube import YouTube
import secrets
from os import rename, path
from time import strftime
from time import gmtime

basedir = path.abspath(path.dirname(__file__))
target = path.join(basedir, 'storage/')

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

def Download_2(link):
    youtubeObject = YouTube(link)
    videoLength = youtubeObject.length

    if videoLength >= 3600:
        actualTime = strftime("%H:%M:%S", gmtime(youtubeObject.length))
    else:
        actualTime = strftime("%M:%S", gmtime(youtubeObject.length))

    # youtubeObject = youtubeObject.streams.get_by_itag(22)
    

    try:
        filename = f"{secrets.token_hex(16)}.mp4"
        # youtubeObject.download(output_path=target, filename=filename)
        # actualTime = strftime("%H:%M:%S", gmtime(videoLength))
        
    except:
        print("An error has occurred")
    print("Download is completed successfully")
    print('Video length: '+ actualTime)

link = input("Enter the YouTube video URL: ")
Download_2(link)