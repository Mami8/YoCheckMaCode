import os
import json
import atexit
import datetime
import time
import webbrowser

# Program kapatılmadan önce çalışacak metod
def ExitHandler(yollar):
    with open("D:\YoCheckMaCode\Python\paths.txt","w") as file:
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

secenekler = []
gün = datetime.datetime.now
yol = "D:\YoCheckMaCode\Shortcuts"

program = []

tarih = datetime.datetime.now()
print("Hello my Lord. Today's {0}th of {1}, {2}. Which corresponds to {3}".format(tarih.day, tarih.month, tarih.year, tarih.strftime("%A")))
time.sleep(2)

# Yolların ataması

saves = open("D:/YoCheckMaCode/Python/paths.txt")
secenekler = json.loads(saves.read())
progSTR = ""

# Ders programının listeye aktarımı
with open("D:/YoCheckMaCode/Python/dersProg.txt") as dersprog:
    program = dersprog.read().split(";")
    for i in program:
        progSTR = progSTR + "|||< " + i + " >|||\n"
    program.append(progSTR)


# Döngü
while True:
    print("")
    secim = input("What do you want me to do? (To add an path, type ğ, to exit type Ğ)\n>> ").strip()

    # Seçenek değerlendirmesi
    if secim == "ğ":
        # Yeni kısayol eklenmesi
        trigger = input("Please, add a trigger to launch the application.\n>> ")
        yol_ = input("Enter the name of the shortcut file. Make sure to enter it's type (.exe .lnk etc).\n>> ")
        _yol = yol + "\\" + yol_
        print(_yol)

        dogrumu = input("Is the path correct?(Y/N)\n>> ").lower().strip()
        if dogrumu == "y":
            secenekler[trigger] = _yol
            print("Function succesfully added!\n")
            continue

        elif dogrumu == "n":
            continue


    elif secim == "Ğ":
        # Çıkış
        ExitHandler(secenekler)
        exit()

    elif secim.lower() == "dersprog":
        # Ders Programı
        günSec = input("\nPlease, enter the index of the day you want. For all days, enter 7.\n>> ").strip()
        print("The program of the {0} is:\n".format(İndextoGün(günSec)) + program[int(günSec)])
        continue


    elif secim == "browse":
        webbrowser.open("https://www.w3schools.com/python/default.asp")
        ExitHandler(secenekler)
        exit()

    else:
        # Kısayol açımı ve kapanış
        if secim.find(";"):
            for i in secim.strip().split(";"):
                os.startfile(secenekler[i.strip().lower()])
        else:
            os.startfile(secenekler[secim.lower()])
        ExitHandler(secenekler)
        exit()

