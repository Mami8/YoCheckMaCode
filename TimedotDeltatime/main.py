import atexit

import OLD_Info_centre as Database

from win10toast import ToastNotifier
from datetime import datetime


def notification(title, message, duration=5, icon_path="D:/Yumusak oyunlar/Grand Theft Auto San Andreas/Icon.ico"):
    toast = ToastNotifier()
    toast.show_toast(title, message, icon_path, duration, threaded=True)

@atexit.register
def ExitManager():
    notification("From mamığ, to mamığ", "Date Manager is down. ReOpen to gain functionality again.")


while True:
    nowHour = datetime.now().hour()
    today = datetime.today()
    dict_name_day = {}
    dates_ = []
    times_ = []

    names, dates, not_types, event_amount = Database.data_retrieve()
    for i in dates:
        dates_.append(i.split("|")[0])
        times_.append(i.split("|")[1])

    for i in range(event_amount):
        year, month, day = dates_[i].split(";")
        rem_day = Database.date_difference_finder(year, month, day)

        if not_types[i] == "day before":

            if rem_day == 1:
                notification("Tomorrow", names[i])
                exit()

        elif not_types[i] == "hour_before":
            if rem_day == 0:
                if nowHour + 1 == times_[i]:
                    notification("In 1 hour", names[i])

