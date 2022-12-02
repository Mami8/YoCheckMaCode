import atexit

import DatabaseManager_Calendar as Database

from win10toast import ToastNotifier
from datetime import datetime


def notification(title: str, message: str, duration=int):
    toast = ToastNotifier()
    toast.show_toast(title=title, msg=message, duration=duration, threaded=True)

@atexit.register
def ExitManager():
    notification("From mamığ, to mamığ", "Date Manager is down. ReOpen to gain functionality again.")


notification("hello", "how are you", duration=5)


while True:
    nowHour = datetime.now().hour
    today = datetime.today()
    dict_name_day = {}
    dates_ = []
    times_ = []

    names, dates, not_types, event_amount = Database.data_retrieve()
    for i in dates:
        dates_.append(i.split("|")[0])
        times_.append(i.split("|")[1])

    for i in range(event_amount):
        print(names[i])
        day, month, year = dates_[i].split(";")
        rem_day = Database.date_difference_finder(year, month, day)

        if not_types[i] == "day_before":

            if rem_day <= 1:
                notification("Tomorrow", names[i])
                exit()

        elif not_types[i] == "hour_before":
            if rem_day == 0:
                if nowHour + 1 >= times_[i]:
                    notification("In 1 hour", names[i])
