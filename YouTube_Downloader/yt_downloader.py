from tkinter import *
from PIL import ImageTk, Image
from urllib.request import urlopen
from pytube import *

list_of_streams = []

def click():
    audio_url = url.get()
    audio = YouTube(audio_url)

    for stream in audio.streams.filter(only_audio=True, file_extension='mp4'):
        list_of_streams.append(stream)
    
    highest = list_of_streams[0]
    for stream in list_of_streams:
        if stream.itag > highest.itag:
            highest = stream
    
    audio_title = IntVar(root, value=audio.title)
    title = Label(root, textvariable=audio_title, font=('Helvetica', 22, 'bold'), fg='#340D09', bg='#FE2712')
    title.grid(row=1, column=0, columnspan=5, pady=10)

    global thumbnail_url
    thumbnail_url = audio.thumbnail_url
    raw_url = urlopen(thumbnail_url)
    raw_url = raw_url.read()
    thumbnail_img = ImageTk.PhotoImage(data=raw_url)
    thumbnail = Label(root, image=thumbnail_img, bg='#FE2712')
    thumbnail.image = thumbnail_img
    thumbnail.grid(row=2, column=0, columnspan=5, padx=10)

    my_audio = audio.streams.get_by_itag(highest.itag)
    download = Button(root, text='Download', command=my_audio.download, width=10, fg='#340D09', bg='#66B032')
    download.grid(row=3, column=0, columnspan=5, pady=10)


def temp_text_hide(e):
    url.delete(0, "end")

root = Tk()
root.iconbitmap('python/youtube.ico')
root.title('YouTube Downloader')
root.resizable(0, 0)
root.configure(bg='#FE2712')

url = Entry(root, width=80, borderwidth=5)
url.insert(0, 'Enter link here...')
search = Button(root, text='Search', command=click,  width=10, fg='#340D09', bg='#66B032')

url.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
url.bind('<FocusIn>', temp_text_hide)
search.grid(row=0, column=4, padx=5)
root.mainloop()