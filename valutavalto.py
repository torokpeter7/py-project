from tkinter import *
import tkinter
import random
import tkinter as tk

ablak1 = tkinter.Tk()
ablak1.title("Valutaváltó")
ablak1.geometry("665x400")

menubar = Menu(ablak1)
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
ablak1.config(menu=menubar)

combo = tk.Combobox()
#Lista
euro_huf = []
huf_euro = []

txt1 = Label(ablak1, text="RŐL:")
txt2 = Label(ablak1, text="RA:")
ertek = Label(ablak1, text="Érték")
combo = tk.Combobox(
    state="readonly",
    values=["Euro","HUF"]
)
input = Entry(ablak1, )


ablak1.mainloop()