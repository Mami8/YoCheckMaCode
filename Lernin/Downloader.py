import tkinter as tk
import pytube as YouTube

font = ("Roboto", 20, "bold")
bg = "#212121"

root = tk.Tk()
canvas = tk.Canvas(width=400, height=400, background="#212121")
canvas.pack()

baslik = tk.Label(root, text=("YT Video İndirici"), font=("Roboto", 30, "bold"), bg="#212121",fg="white")
canvas.create_window(200, 50, window=baslik)

yazi1 = tk.Label(root, text="Adres giriniz", bg=bg, fg="white")
canvas.create_window(200, 100, window=yazi1)

girdi = tk.Entry(bg=bg, fg="white", font=font)
canvas.create_window(200, 200, window=girdi)

def DownloadVideo():
    url = girdi.get()
    try:
        video = YouTube.YouTube(url)
        video = video.streams.get_highest_resolution()

        video.download()
        basariyazi = tk.Label(root, text="    İndirme Başarılı!    ", bg=bg, fg="white", font=font)
        canvas.create_window(200, 350, window=basariyazi)

    except Exception as e:
        hatayazi = tk.Label(root, text="    İndirme Başarısız    ", font=font, bg=bg, fg="white")
        canvas.create_window(200, 350, window=hatayazi)

buton = tk.Button(root, command=DownloadVideo, text="İndir", font=font,bg=bg,fg="white")
canvas.create_window(200, 300, window=buton)

root.mainloop()