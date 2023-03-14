import youtube_dl
import secrets
from os import rename, path

basedir = path.abspath(path.dirname(__file__))
target = path.join(basedir, 'storage/')

class YTubeVideoConverter:

    def __init__(self, video_url):
        self.video_url = video_url
        self.video_info = youtube_dl.YoutubeDL().extract_info(url = self.video_url, download=False)

    def menu(self):
        while True:
            print('Enter 1 to download as mp3: ')
            print('Enter 2 to download as mp4: ')
            print('Enter 3 to quit: ')
            print('='*25)

            selected_opt = input('Choose an option: ')

            # Validate input
            opts = ('1','2','3')
            while True:
                if selected_opt in opts:
                    break
                else:
                    print('Invalid option, please try again!')
                    selected_opt = input('Choose an option: ')

            if selected_opt == '1':
                self.to_mp3()

            if selected_opt == '2':
                self.to_mp4()

            if selected_opt == '3':
                break


    def to_mp3(self):
        filename = f"{secrets.token_hex(16)}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
        }
        self.download(filename, options)

    def to_mp4(self):
        filename = f"{secrets.token_hex(16)}.mp4"
        options = {
            'format':'136',
            'keepvideo': False,
            'noplaylist' : True,
            'merge_output_format': 'mp4',
            'outtmpl':filename,
        }
        self.download(filename, options)

    def download(self, filename, options):
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([self.video_info['webpage_url']])

        rename(filename, target+filename)        
        print("Download complete... {}".format(filename))
        print('='*25)

# https://youtu.be/kV_jtZGVkn4
video_url = input("Enter url of youtube video:")

user_input = YTubeVideoConverter(video_url)
user_input.menu()