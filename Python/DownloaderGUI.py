import tkinter as tk
import DownloadLIB


font = ("Roboto", 20, "bold")
bg = "#212121"


def Calis():
    root = tk.Tk()
    canvas = tk.Canvas(width=400, height=400, background="#212121")
    canvas.pack()

    baslik = tk.Label(root, text=("YT Video İndirici"), font=("Roboto", 30, "bold"), bg="#212121", fg="white")
    yazi1 = tk.Label(root, text="Adres giriniz", bg=bg, fg="white")

    def İndir():
        url = girdi.get()

        if var == 0:
            sonuc = DownloadLIB.DownloadVideo(url)
            yazi = tk.Label(root, text=sonuc, bg=bg, fg="white", font=font)

        else:
            sonuc = DownloadLIB.DownloadAudio(url)
            yazi = tk.Label(root, text=sonuc, bg=bg, fg="white", font=font)

        canvas.create_window(200, 350, window=yazi)

    girdi = tk.Entry(bg=bg, fg="white", font=font)
    buton = tk.Button(root, command=İndir, text="İndir", font=font,bg=bg,fg="white")

    var = tk.IntVar()
    sesayar = tk.Checkbutton(root, text = ".mp3 Modu", variable=var,bg=bg, fg="white", selectcolor=bg)
    canvas.create_window(200, 50, window=baslik)
    canvas.create_window(200, 100, window=yazi1)
    canvas.create_window(200, 200, window=girdi)
    canvas.create_window(200, 300, window=buton)
    canvas.create_window(300, 150, window=sesayar)

    root.mainloop()
