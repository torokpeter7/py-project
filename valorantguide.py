from tkinter import *
from tkinter.ttk import *
ablak1 = Tk()

menubar = Menu(ablak1)

Kezdőoldalmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Kezdőooldal")

menubar.add_cascade(label="Akasztófa")

menubar.add_cascade(label="Valuta Váltó")

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

Sovakep=PhotoImage(file=r"H:/ikt/ikt py/py-project/kepek/sova.png")

Sova_gomb=Button(ablak1, image=Sovakep).pack

ablak1.mainloop()
