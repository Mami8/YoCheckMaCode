import datetime

import DatabaseManager_Calendar as Database

print("\n\n¯\\_(ツ)_/¯ The Date Manager from mamığ, to mamığ ¯\\_(ツ)_/¯\n\n")

# Main loop
while True:
    now_hour = int(datetime.datetime.now().strftime("%H"))
    now_date = datetime.datetime.now().strftime("%d;%m;%Y")

    names, dates, not_types, event_amount = Database.data_retrieve()

    secim = input("To see all events, type 1. This will also give you the numbers of events.\nTo add event, type addevent.\nTo find out how much "
                  "time left to an event, type ğ;(event name)\n"
                  "To exit type Ğ\n>> ").strip()

    i = 0
    if secim == "Ğ":
        exit()

    elif secim == "1":
        while i < event_amount:
            print(i+1, "  Name: ", names[i], "  Date: ", dates[i], "  NOT_TYPE: ", not_types[i])
            i += 1
        print("\n\n")

    elif secim == "addevent":
        newName = input("\nEnter the name for the event\n>> ")
        newYear = input("Enter the year of the event in yyyy format\n>> ")
        newMonth = input("Ente the month of the year in mm numerical format\n>> ")
        newDay = input("Enter the day of the month in dd format\n>> ")
        newTime = input("Enter the time of the event in hh format\n>> ")
        newNotType = input("Enter the NOT_TYPE. ( day_before || hour_before)\n>> ")

        newDate = Database.date_merger(newDay, newMonth, newYear, newTime)
        Database.data_append(newName, newDate, newNotType)

        print("\nOperation was succesfull!\n")
        continue

    elif secim.split(";")[0] == "ğ":
        req = secim.split(";")[1]
        for j in range(event_amount):
            if req in names[j]:
                date = dates[j].split("|")[0]
                day, month, year = date.split(";")

                diff = Database.date_difference_finder(year, month, day)
                print(diff)
                continue
