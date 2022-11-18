import sqlite3
import atexit


def bagla():
    global con 
    con = sqlite3.connect("D:/YoCheckMaCode/Python/TicTac.db")
    global cursor 
    cursor = con.cursor()
    global baglimi
    baglimi = True


bagla()
cursor.execute("SELECT * FROM paths")
trigYolAlt = cursor.fetchall()

cursor.execute("SELECT * FROM dersProgram")
ders_program = cursor.fetchall()

@atexit.register
def baglantıKopar(baglanti = con, commitmode = True):
    baglanti.close
    baglimi = False

def yollarıAl():
    paths = []

    for i in trigYolAlt:
        paths.append(i[1])
    return paths



def degerEkle(trig = "NULL", path = "NULL", alt_trig = "NULL"):
    if baglimi:
        cursor.execute('INSERT INTO paths (trigger, path, alt_trigger) VALUES ("{}", "{}", "{}")'.format(trig, path, alt_trig))
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
    else:
        a = input("Bağlantı yok. Tekrar bağla? (Y/N)").lower().strip()
        if a == "y":
            bagla()
            print("Bağlantı kuruldu.")

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