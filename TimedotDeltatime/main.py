import information_manager
import DatabaseController_Calendar as Database

import atexit
import datetime


def notification(message=""):
    pass

Database.date_complexer()

# Main loop
while True:
    now_hour = int(datetime.datetime.now().strftime("%H"))
    now_date = datetime.datetime.now().strftime("%d;%m;%Y")

    names, dates, not_types, event_amount = Database.data_retrieve()

    i = 0
    while i <  event_amount:
        pass












