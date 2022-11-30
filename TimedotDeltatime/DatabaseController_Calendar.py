import datetime
import sqlite3 as sqlite


def connect():
    con = sqlite.connect("D:/YoCheckMaCode/TimedotDeltatime/Calendar.db")
    cursor = con.cursor()

    return con, cursor


def close_connection(connection, commit_mode=True):
    try:
        if commit_mode:
            connection.commit()
            connection.close()
        else:
            connection.rollback()
            connection.close()
    except Exception as e:
        print("Cannot close connection. Reason: ", e.args)


def data_retrieve():
    """
    Returns names of events, dates of events and notification types of events with same order.
    """
    # Connecting, getting needed data and closing the connection
    con, cursor = connect()
    db = cursor.execute("SELECT * FROM events").fetchall()
    con.close()

    event_amount = 0
    names = []
    dates = []
    not_types = []

    # Spliting data retrieved and returning in an order
    for i in db:
        event_amount += 1
        names.append(i[1])
        dates.append(i[2])
        not_types.append(i[3])

    return names, dates, not_types, event_amount


def data_append(event_name, date, not_type):
    """
    Connection and getting data appended. This function needs four variables
    The first one can be anything
    Second one should come from function date_simplifier

    The last one can currently get 2 values even tough It's a string. These are
    (day_before, hour_before)
    Meanings are the same with names. Values are set, day_before means one day before at 18:00
    and hour_before means 2 hours before
    """
    con, cursor = connect()
    cursor.execute('''INSERT INTO events (event_name, date, notification_type) 
    VALUES ("{}", "{}", "{}")'''.format(event_name, date, not_type))

    close_connection(con, True)


def date_merger(day, month, year, hour):
    """
    Inputs should be like (dd, mm, yy, hh) and not like (dd, Month, yyyy, hh:mm:ss).
    Hour should be in 24-hour format. Example: 07, 15, 21, 00
    Return value can be used in data_append.
    Make sure to put in numeric date. If It's already in dd;mm;yy form, don't use this function and feed
    it directly to data_append. Program uses dd;mm;yy|hh format everywhere.
    """
    day = day.strip()
    month = month.strip()
    year = year.strip()
    hour = hour.strip()

    return day + ";" + month + ";" + year + "|" + hour


def date_difference_finder(year, month, day):
    """
    Finds the difference between now and given date.
    All parameters must be filled
    Returns the days between. No hours included
    """
    now = datetime.datetime.today()
    target_date = datetime.datetime(year, month, day)
    result = target_date - now

    return result

