from win10toast import ToastNotifier
from datetime import datetime
import DatabaseController_Calendar as Database


def notification(title, message, duration=5, icon_path="D:/Yumusak oyunlar/Grand Theft Auto San Andreas/Icon.ico"):
    toast = ToastNotifier()
    toast.show_toast(title, message, icon_path, duration, threaded=True)


while True:
    now = datetime.now()
    today = datetime.today()

    names, dates, not_types, event_amount = Database.data_retrieve()

