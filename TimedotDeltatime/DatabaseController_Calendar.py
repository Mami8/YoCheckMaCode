import sqlite3 as sqlite


def connect():
    con = sqlite.connect("")
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
    con, cursor = connect()
    db = cursor.execute("SELECT * FROM events").fetchall()
    con.close()

    names = []
    dates = []
    not_types = []

    for i in db:
        names.append(i[1])
        dates.append(i[2])
        not_types.append(i[3])

    return names, dates, not_types


def data_append(event_name, date, not_type):
    con, cursor = connect()
    cursor.execute('''INSERT INTO events (event_name, date, notification_type) 
    VALUES ("{}", "{}", "{}")'''.format(event_name, date, not_type))
    close_connection(con, True)


def date_simplifier(day, month, year):
    day.strip()
    month.strip()
    year.strip()

    return day + ";" + month + ";" + year
