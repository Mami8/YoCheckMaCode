import datetime
import json
import os
import time


# Program kapatılmadan önce çalışacak metod
def ExitHandler(yollar):
    with open("D:\YoCheckMaCode\Python\paths.txt") as file:
        file.write(json.dumps(yollar))

# Girilen index değerinin cümle olarak düzenlenmesi
def İndextoGün(index):
    match index:
        case "0":
            return "Monday"
        case "1":
            return "Tuesday"
        case "2":
            return "Wednesday"
        case "3":
            return "Thursday"
        case "4":
            return "Friday"
        case "5":
            return "Saturday"
        case "6":
            return "Sunday"
        case "7":
            return "All days"

gün = datetime.datetime.now
yol = "D:\YoCheckMaCode\Shortcuts"
tarih = datetime.datetime.now()


# Yolların ataması
yolDosya = open("D:\YoCheckMaCode\Python\paths.txt")
secenekler = json.loads(yolDosya.read())

# Ders programının listeye aktarımı
programDosya = open("D:\YoCheckMaCode\Python\dersProg.txt")
program = programDosya.read().split(";")
progSTR = ""
for i in program:
    progSTR = progSTR + i + " ||| "
program.append(progSTR)


def Openapp(secim):
    if secim == "ğ":
        # Yeni kısayol eklenmesi
        trigger = input("Please, add a trigger to launch the application.\n>> ")
        yol_ = input("Enter path of the shortcut that will get executed.\n>> ")
        secenekler[trigger] = yol_
        print("Function succesfully added!\n")
    elif secim == "Ğ":
        # Çıkış
        ExitHandler(secenekler)
        exit()

    elif secim.lower() == "dersprog":
        # Ders Programı
        günSec = int(input("\nPlease, enter the index of the day you want. For all days, enter 7.\n>> ").strip())
        print("The program of the {0} is:\n".format(İndextoGün(günSec)) + program[günSec])

    else:
        # Kısayol açımı ve kapanış
        # Çoklu uygulama açımına olanak sağlarken kullanıcı ögelerin arasına ; koyar
        # Daha sonra script bu ögeleri ; kısmından ayırır, temizler ve her biri için işlem yaparız
        if secim.find(";"):
            for i in secim.strip().split(";"):
                os.startfile(secenekler[i.strip().lower()])
        else:
            os.startfile(secenekler[secim.lower()])
        ExitHandler(secenekler)
        exit()

