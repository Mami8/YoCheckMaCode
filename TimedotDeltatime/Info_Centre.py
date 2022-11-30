import datetime

import OLD_Info_centre as Database

print("\n\n¯\\_(ツ)_/¯ The Date Manager from mamığ, to mamığ ¯\\_(ツ)_/¯\n\n")

# Main loop
while True:
    now_hour = int(datetime.datetime.now().strftime("%H"))
    now_date = datetime.datetime.now().strftime("%d;%m;%Y")

    names, dates, not_types, event_amount = Database.data_retrieve()

    secim = input("To see all events, type 1. This will also give you the numbers of events.\nTo find out how much "
                  "time left to an event, type ğ;(event name)\n"
                  "To exit type Ğ\n>> ").strip()

    i = 0
    if secim == "Ğ":
        exit()

    elif secim == "1":
        while i < event_amount:
            print(i+1, "  Name: ", names[i], "  Date: ", dates[i], "  NOT_TYPE: ", not_types[i])
            i += 1

    elif secim.split(";")[0] == "ğ":
        req = secim.split(";")[1]
        for j in range(event_amount):
            if req in names[j]:
                date = dates[j].split("|")[0]
                day, month, year = date.split(";")

                diff = Database.date_difference_finder(year, month, day)
                print(diff)
                continue
