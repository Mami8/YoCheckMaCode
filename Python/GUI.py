import tkinter
import tictaclib

from tkinter.ttk import *

current_var = ""

window=tkinter.Tk()
window.geometry("300x200")

window.title = "Jarvis"
tkinter.Label(window, text="Choose an option: ", pady=10).grid(column=0, row=0)
combo = Combobox(window, textvariable=current_var)
combo["values"] = ("game","code","spotify","multi")
combo.grid(column=1,row=0)
combo.current(0)


mom = Label(text="oyun oynama").grid(column=1,row=1)

secim = combo.get()
if secim == "game":
    mom["text"] = "oynama"
else:
    mom["text"] = "gut"
# Button(window, text = "enter",command=tictaclib.Openapp(secim))

window.mainloop()