import sqlite3
import atexit

baglimi = False

def bagla():
    global con 
    con = sqlite3.connect("Lernin/database.db")
    global cursor 
    cursor = con.cursor()
    baglimi = True

bagla()
cursor.execute("SELECT * FROM paths")
yollar = cursor.fetchall()

cursor.execute("SELECT * FROM dersProgram")

def baglantıKopar(baglanti, commitMode):
    if commitMode:
        con.commit
    elif not commitMode:
        baglanti.rollback
    else:
        return 0
    baglanti.close
    baglimi = False

def yollarıAl():
    paths = []

    for i in yollar:
        paths.append(i[1])
    return paths

def degerEkle(trig, path, alt_trig):
    if baglimi:

        sql = "INSERT INTO paths(trigger,path,alt_trigger) "
        values = 'VALUES ("{0}", "{1}", "{2}")'.format(trig, path, alt_trig)

        cursor.execute(sql + values)

        print('Trigger is "{}", alternative trigger is "{}" and the path is\n{}\n'.format(trig, path, alt_trig))
        dogrumu = input("Is it ok? (Y/N)\n>> ").strip().lower()
        if dogrumu == "y":
            con.commit()
            print("Succesfully commited!!!")
        elif dogrumu == "n":
            con.rollback()
            print("Changes were reverted.")
        else:
            print("Enter a valid argument please.")
    else:
        bagla()
        degerEkle(trig, path, alt_trig)

def trigKontrol(istenenTrig):
    for i in yollar:
        if istenenTrig in i[0] or istenenTrig in i[2]:
            return i[1]
        else:
            return 0
