import tkinter as tk
import DownloadLIB

# sürekli kullanacağın için bunları önden tanımladın
font = ("Roboto", 20, "bold")
bg = "#212121"

# TikTak'a implemente edersin die bak sana ne yaptim, iyisin yine
def calis():
    # Ana pencere ve pencere içindeki çerçevenin tanımlanması
    root = tk.Tk()
    canvas = tk.Canvas(width=400, height=400, background="#212121")
    canvas.pack()

    baslik = tk.Label(root, text="YT Video İndirici", font=("Roboto", 30, "bold"), bg="#212121", fg="white")
    input_yazi = tk.Label(root, text="Adres giriniz", bg=bg, fg="white")
    sonuc_yazi = tk.Label(root, text="Sonuç", bg=bg, fg="white", font=font)

    # Butona basılınca çalışması için fonksiyon olarak tanımlanan indirme kodu. Sonucu kendisi ekrana yazar 
    # biraz aşağıda var tanımlanıyor. mp3 modu kendisi
    
    def indir():
        url = girdi.get()
        print(f"var'ın aldığı değer: |{var.get()}|")
        if var.get() == 0:
            
            sonuc = DownloadLIB.DownloadVideo(url)
            sonuc_yazi.config(text=sonuc)
        else:
            sonuc = DownloadLIB.DownloadAudio(url)
            sonuc_yazi.config(text=sonuc)


    girdi = tk.Entry(bg=bg, fg="white", font=font)
    buton = tk.Button(root, command=indir, text="İndir", font=font, bg=bg, fg="white")

    # var, bizim mp3 modunu takip eder. True yani seçili 1, False yani seçili değil 0 olur.
    var = tk.IntVar()
    var.trace = ('w')
    
    # Tanımlanan ögelerin çerçeveye eklenmesi
    sesayar = tk.Checkbutton(root, text=".mp3 Modu", variable=var, bg=bg, fg="white", selectcolor=bg)
    canvas.create_window(200, 50, window=baslik)
    canvas.create_window(200, 350, window=sonuc_yazi)
    canvas.create_window(200, 100, window=input_yazi)
    canvas.create_window(200, 200, window=girdi)
    canvas.create_window(200, 300, window=buton)
    canvas.create_window(300, 150, window=sesayar)

    # Pencere döngüsünün başlaması
    root.mainloop()


calis()
