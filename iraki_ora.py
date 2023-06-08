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
ablak.geometry("665x400")
ablak.title("Iraki óra")
menubar = Menu(ablak)
Kezdőoldalmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Kezdőoldal")
menubar.add_cascade(label="Akasztófa")
menubar.add_cascade(label="Valuta Váltó")
menubar.add_cascade(label="Valorant Line-up Guide")
menubar.add_cascade(label="QR kód generátor")
menubar.add_cascade(label="Jelszó generátor")
menubar.add_cascade(label="Naptár")
aksztofa=menubar.add_cascade(label="Iraki óra")
akszto=Menu(menubar, tearoff=0)
valuta=Menu(menubar, tearoff=0)
valolineup=Menu(menubar, tearoff=0)
qrkodgen=Menu(menubar, tearoff=0)
jelszogen=Menu(menubar, tearoff=0)
naptar=Menu(menubar, tearoff=0)
irakiora=Menu(menubar, tearoff=0)
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
óraEntry.place(x=260, y=100)
percEntry.place(x=310, y=100)
masodpercEntry.place(x=360, y=100)
gomb=Button(ablak, text="Bekapcsolás", bd="5",command=bekapcsolas)
gomb.place(x=293, y=150)
ablak.config(menu=menubar)
ablak.mainloop()