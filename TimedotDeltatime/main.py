import  DatabaseController_Calendar as Database
from win10toast import ToastNotifier


def notification(title, message, duration=5, icon_path="D:/Yumusak oyunlar/Grand Theft Auto San Andreas/Icon.ico"):
    toast = ToastNotifier()
    toast.show_toast(title, message, icon_path, duration, threaded=True)





while True:
    pass
