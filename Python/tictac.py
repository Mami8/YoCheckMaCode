import os
import atexit
import datetime
import time
import webbrowser
import TicTacDATA
import locale
import DownloaderGUI

# Program kapatılmadan önce çalışacak metod
@atexit.register
def ExitHandler():
    TicTacDATA.baglantıKopar(TicTacDATA.con, True)

# Girilen index değerinin cümle olarak düzenlenmesi
def İndextoGün(index):
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

locale.setlocale(locale.LC_ALL , "Turkish_Turkey.1254")
tarih = datetime.datetime.now()


program = []


print("Günaydın Lordum. Bugün günlerden {3}, {1}'ın {0}'i, {2}.".format(tarih.day, tarih.strftime("%B"), tarih.year, tarih.strftime("%A")))
time.sleep(1)


# Ders programının listeye aktarımı
def DersProgramAl(günSayı):
    for i in TicTacDATA.ders_program:
        if günSayı == str(i[0]):
            return İndextoGün(günSayı)+ ":\n " + i[1]

# # Döngü
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

        TicTacDATA.degerEkle(trig, path_, alt_trig)

    elif secim == "Ğ":
        # Çıkış
        exit()

    elif secim.lower() == "dersprog":
        # Ders Programı
        istekgün = input("Pazartesi 1, tüm günler 8 olacak şekilde programını istediğiniz günün sayısını giriniz.\n>> ")

        print(DersProgramAl(istekgün))


    elif secim == "browse":
        webbrowser.open("https://www.w3schools.com/python/default.asp")
        exit()

    elif secim in "yutupindir":
        DownloaderGUI.Calis()

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
