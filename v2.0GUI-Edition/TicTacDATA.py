import os
import sqlite3
import atexit


def bagla():
    """Aynı klasördeki Database'e bağlanır

    Returns:
        tuple: sqlite3 connection object ve sqlite3 cursor object dönderir
    """
    con = sqlite3.connect("D:/YoCheckMaCode/v2.0GUI-Edition/database.db")
    cursor = con.cursor()
    baglimi = True
    return con, cursor


con, cursor = bagla()

@atexit.register
def baglantikopar(baglanti=con, commitmode=True):
    """Bağlantıyı güvenli bir şekilde kapatır

    Args:
        baglanti (sqlite3 connection object, optional): Bağlantı nesnesi. Defaults to con.
        commitmode (bool, optional): Verilerin kaydedibip kaydedilmeyeceğini belirtir. Defaults to True.
    """    
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
    """Database'den verileri toplar.

    Args:
        curs (sqlite3 cursor object, optional): Eğer farklı bir cursor kullanılacaksa belirtilmeli. Defaults to cursor.

    Returns:
        tuple: isimleri, yolları, sözlüğü ve dersprogramı
    """ 
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
    """Açılacak programlara ekleme yapar

    Args:
        isim (str): Uygulamanın görünen ismi. Herhangi değer alabilir.
        path (str): Açılacak programın yolu.

    Returns:
        str: Uyarı metini. Sondaki ve baştaki boşluklar ayarlı.
    """    
    bagla()
    try:
        cursor.execute(
            'INSERT INTO paths (isim, path) VALUES ("{}", "{}")'.format(isim, path))
        return " Başarıyla eklendi  "
    except Exception as e:
        return " Ekleme Başarısız   "


def yolual(istek):
    """İstenilen programın yolunu döndürür

    Args:
        istek (str): istenilen programın ismi. Database'de bulunan isimle aynı olmalı

    Returns:
        str: İstenilen programın yolu
    """    
    for k in sozluk:
        if istek in k[0]:
            return k[1]
        else:
            continue
