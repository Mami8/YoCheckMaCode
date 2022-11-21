import sqlite3
import atexit

con = sqlite3.connect("D:/YoCheckMaCode/Python/TicTac.db")
cursor = con.cursor()
baglimi = True


def bagla():
    con = sqlite3.connect("D:/YoCheckMaCode/Python/TicTac.db")
    cursor = con.cursor()
    baglimi = True


bagla()
cursor.execute("SELECT * FROM paths")
trigYolAlt = cursor.fetchall()

cursor.execute("SELECT * FROM dersProgram")
ders_program = cursor.fetchall()


@atexit.register
def baglantikopar(baglanti=con, commitmode=True):
    if commitmode:
        baglanti.close()
    else:
        baglanti.rollback()
    baglimi = False


def yollarial():
    paths = []

    for i in trigYolAlt:
        paths.append(i[1])
    return paths


def degerekle(trig="NULL", path="NULL", alt_trig="NULL"):
    bagla()

    cursor.execute(
        'INSERT INTO paths (trigger, path, alt_trigger) VALUES ("{}", "{}", "{}")'.format(trig, path, alt_trig))
    print("Tetikleyici: {}\nYol: {}\nAltrnatif tetikleyici: {}".format(trig, path, alt_trig))
    dogrumu = input("Bilgiler doğru mu? (Y/N)\n>> ").strip()
    if dogrumu.lower() == "y":
        print("Bilgiler eklendi.")
        con.commit()
    elif dogrumu.lower() == "n":
        print("İşlem iptal edili")
        con.rollback()
    else:
        print("Geçerli değer giriniz !!!")


def trigKontrol(istenenTrig):
    bulundu = False
    bulunan = ""

    for i in trigYolAlt:
        if istenenTrig in i[0] or istenenTrig in i[2]:
            bulundu = True
            bulunan = i[1]
            break
        else:
            bulundu = False

    if bulundu:
        return bulunan
    else:
        return 0
