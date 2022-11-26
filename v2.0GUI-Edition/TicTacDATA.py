import os
import sqlite3
import atexit


def bagla():
    con = sqlite3.connect("D:/YoCheckMaCode/v2.0GUI-Edition/database.db")
    cursor = con.cursor()
    baglimi = True
    return con, cursor


con, cursor = bagla()

@atexit.register
def baglantikopar(baglanti=con, commitmode=True):
    try:
        if commitmode:
            baglanti.commit()
        else:
            baglanti.rollback()
    except Exception as e:
        pass
    baglanti.close()
    baglimi = False


def verial(curs=cursor):
    db = cursor.execute("SELECT * FROM paths").fetchall()
    sozluk = {}
    isimler = []
    paths = []
    program = cursor.execute("SELECT * FROM dersprogram")


    for i in db:
        isimler.append(i[0])
        paths.append(i[1])
        sozluk[i[0]] = i[1]

    return isimler, paths, sozluk, program


isimler, paths, sozluk, program = verial(cursor)


def degerekle(isim, path):
    bagla()
    try:
        cursor.execute(
            'INSERT INTO paths (isim, path) VALUES ("{}", "{}")'.format(isim, path))
        return " Başarıyla eklendi  "
    except Exception as e:
        return " Ekleme Başarısız   "


def yolual(istek):
    for k in sozluk:
        if istek in k[0]:
            return k[1]
        else:
            continue
