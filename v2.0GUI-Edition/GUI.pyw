import DownloadLIB as downloader
import DownloaderGUI as downGUI
import TicTacDATA as database

import  os
import tkinter as tk
from  tkinter.ttk import *
import atexit

@atexit.register
def exithandler():
    database.baglantikopar(commitmode = True)


font = ("Roboto", 18, "bold")
bg = "#212121"
fg = "white"
sozluk = database.sozluk

root = tk.Tk()
root.title("Hel")
canvas_secim = tk.Canvas(root, width=400, height=400, bg=bg)
canvas_secim.pack()


def yol_ekle_GUI(yol = "D:/YoCheckMaCode/Shortcuts/"):  
    """Girilen yolu seçeneklere eklemek için panel açar

    Args:
        yol (str, optional): açılacak uygulamanın bulunduğu konum. Standart haldeki gibi sonuna / eklenmeli. Defaults to "D:/YoCheckMaCode/Shortcuts/".
    """      

    def A():
        database.degerekle(entry_isim.get(), yol + entry_path.get())

    canvas_yeniyol = tk.Canvas(root, width=400, height=400, bg=bg)
    canvas_yeniyol.pack(side="right")

    entry_isim = tk.Entry(root, bg=bg, fg=fg, font=("Roboto", 15, "bold"))
    entry_path = tk.Entry(root, bg=bg, fg=fg, font=("Roboto", 15, "bold"))

    label_isim = tk.Label(root, text="İsim :", bg=bg, fg=fg, font=("Roboto", 12, "bold"))
    label_yol = tk.Label(root, text="Path  :", bg=bg, fg=fg, font=("Roboto", 12, "bold"))

    button = tk.Button(root, text="Ekle", command=A, bg=bg, fg=fg, font=font)

    canvas_yeniyol.create_window(75, 35, window=label_isim)
    canvas_yeniyol.create_window(125, 75, window=entry_isim)
    canvas_yeniyol.create_window(75, 110, window=label_yol)
    canvas_yeniyol.create_window(125, 150, window=entry_path)
    canvas_yeniyol.create_window(200, 200, window=button)


def yol_ac():
    """semimbox.get() kullanılarak seçilen öge alınır. Database'den gelen sözluk ile bu seçime ait yol alınır ve açılır
    """
    secim = secimbox.get()
    yol = sozluk[secim]
    os.startfile(yol)


def video_indir_GUI():
    """downGUI.calis fonksiyonu çağrılır. Bir UI aracılığıyla YouTube'dan video indirm işlemi gerçekleşir
    """
    downGUI.calis(root)


secimbox = Combobox(root, font=font, values=database.isimler, background=bg, foreground=fg)
label_comb = tk.Label(root, text="Uygulama seçiniz: ", bg=bg, fg=fg, font=font)

buton_path = tk.Button(root, text="Program Aç", command=yol_ac, bg=bg, fg=fg, font=font)
buton_yol_ekle = tk.Button(root, text="Program Ekle", command=yol_ekle_GUI, bg=bg, fg=fg, font=font)
buton_indir = tk.Button(root, text="YouTube İndir", command=video_indir_GUI, bg=bg, fg=fg, font=font)


canvas_secim.create_window(125, 50, window=label_comb)
canvas_secim.create_window(150, 100, window=secimbox)

canvas_secim.create_window(100, 150, window=buton_path)
canvas_secim.create_window(200, 225, window=buton_indir)
canvas_secim.create_window(200, 300, window=buton_yol_ekle)

root.mainloop()