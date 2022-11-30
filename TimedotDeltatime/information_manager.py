import atexit
import locale
from datetime import datetime

import DatabaseController_Calendar as Database

locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254")
today = datetime.now()

# [0] is numeric day, [1] is numeric month, [2] is two digit year and [3] is hour in 24-hour format
current_date = today.strftime("%d;%m;%y;%H").split(";")

events, raw_dates, raw_not_types, event_amount = Database.data_retrieve()
dates = []
times = []

for i in raw_dates:
    x, y = i.split("|")
    dates.append(x)
    times.append(y)


@atexit.register
def exit_handler():
    pass


def process():
    print("\nFor the list of events, type events\n"
          "To add event, type addevent\n")
    secim = input(">> ").strip().lower()

    match secim:
        case "Ğ":
            exit()
        case "events":
            i = 0
            while i < event_amount:
                print("-----------------------------------")
                print("name = " + events[i], "\nDate = " + dates[i], "\nTime = " + times[i],
                      "\nnot_type = " + raw_not_types[i])
                i += 1
        case "addevent":
            name = input("Please enter the name of the event\n>> ").strip()
            date = input("Please enter the date of the event in the form of dd/mm/yy\n>> ").strip().split("/")
            time = input("Please enter the time of your event in 24-hour format hh\n>> ").strip()
            not_type = input("Please enter the not_type of the event.( day_before or hour_before)").strip().lower()

            if not_type != "day_before" and not_type != "hour_before":
                print("Invlid not_type")
            else:
                simp_time = Database.date_merger(date[0], date[1], date[2], time)

                correct = input(name, not_type, date, time, "\nIs the information correct?( Y/N )").lower()
                if correct != "y" and correct != "n":
                    return 1

                elif correct == "y":
                    Database.data_append(name, simp_time, not_type)

                else:
                    return 0
