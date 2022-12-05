import os
import atexit
import datetime
import time
import webbrowser
import locale

import TicTacDATA
import DownloaderGUI
import weather


# Program kapatılmadan önce çalışacak metod
@atexit.register
def ExitHandler():
    TicTacDATA.baglantikopar(TicTacDATA.con, True)

def indextogun(index):
    """Verilen index değerinin güne dönüşümü

    Args:
        index (int): PazartesiPazartesi 1 pazar 7 ve tüm günler 8 olacak şekilde gün 

    Returns:
        str: Günün tam ismi
    """
    match index:
        case "1":
            return "Pazartesi"
        case "2":
            return "Salı"
        case "3":
            return "Çarşamba"
        case "4":
            return "Perşembe"
        case "5":
            return "Cuma"
        case "6":
            return "Cumartesi"
        case "7":
            return "Pazar"
        case "8":
            return "Tüm günler"


secenekler = []
yol = "D:/YoCheckMaCode/Shortcuts/"

def dersprogramal(gunsayi):
    """Ders programını istenen güne göre döndürür

    Args:
        gunsayi (int): pazartesi 1 pazar 7 ve tüm günler 8 olacak şekilde gün 

    Returns:
        str: Ders programı
    """
    for i in TicTacDATA.ders_program:
        if gunsayi == str(i[0]):
            return indextogun(gunsayi) + ":\n " + i[1]

lat, lon = weather.get_geocode("Afşin", "TR")
locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254")
tarih = datetime.datetime.now()

program = []

print("Günaydın Lordum. Bugün günlerden {3}, {1}'ın {0}'i, {2}.".format(tarih.day, tarih.strftime("%B"), tarih.year,
                                                                        tarih.strftime("%A")))
time.sleep(1)




# Döngü
while True:
    print("")
    secim = input("Ne yapmamı istersiniz? (Yeni eylem eklemek için ğ, çıkış için Ğ giriniz)\n>> ").strip()

    # Seçenek değerlendirmesi
    if secim == "ğ":
        # Yeni kısayol eklenmesi
        trig = input("Tetikleyici giriniz.\n>> ")
        path = input("Shortcuts klasörü içindeki dosyayı uzantsı ile beraber giriniz.\n>> ").strip()
        alt_trig = input("Alternatif olarak kullanabileceğiniz bir tetikleyici giriniz.\n>> ")

        path_ = yol + path

        TicTacDATA.degerekle(trig, path_, alt_trig)

    elif secim == "Ğ":
        # Çıkış
        exit()

    elif secim.lower() == "dersprog":
        # Ders Programı
        istekgun = input("Pazartesi 1, tüm günler 8 olacak şekilde programını istediğiniz günün sayısını giriniz.\n>> ")

        print(dersprogramal(istekgun))


    elif secim == "browse":
        webbrowser.open("https://www.w3schools.com/python/default.asp")
        exit()

    elif secim in "yutupindir":
        DownloaderGUI.calis()
        
    elif secim == "hava":
        desc, temp = weather.get_weather(lat, lon)
        print ("\nHava şu an", desc, "ve", temp, "derece selsiyus")
        time.sleep(1)

    # Yol açılımı
    else:
        # Kısayol açımı ve kapanış

        secimList = []
        coklumod = False
        bulundu = False
        secim = secim.lower().strip()

        if ";" in secim:
            for i in secim.split(";"):
                secimList.append(i.strip())
            coklumod = True

        if coklumod:
            for i in secimList:
                if TicTacDATA.trigKontrol(i) != 0:
                    bulundu = True
                else:
                    bulundu = False
                    break
        else:
            if TicTacDATA.trigKontrol(secim) != 0:
                bulundu = True

        if bulundu:
            if not coklumod:
                os.startfile(TicTacDATA.trigKontrol(secim.lower()))
            else:
                for i in secimList:
                    os.startfile(TicTacDATA.trigKontrol(i))
            exit()
        else:
            print("İstenen eylem kayıtlı değil.")
            time.sleep(1)
            continue
