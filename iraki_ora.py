from tkinter import *
import time
from tkinter import messagebox
import os
import subprocess
import pygame

def kezdooldal_menu_button_press():
    subprocess.Popen(args=['python', r'kezdőoldal.py'])
    ablak.destroy()
def akasztofa_menu_button_press():
    subprocess.Popen(args=['python', r'akasztofa.py'])
    ablak.destroy()
def valuta_menu_button_press():
    subprocess.Popen(args=['python', r'valutavalto.py'])
    ablak.destroy()
def valorant_menu_button_press():
    subprocess.Popen(args=['python', r'valorantguide.py'])
    ablak.destroy()
def qrcode_menu_button_press():
    subprocess.Popen(args=['python', r'qrcodegen.py'])
    ablak.destroy()
def jelszo_menu_button_press():
    subprocess.Popen(args=['python', r'jelszogenerator.py'])
    ablak.destroy()
def naptar_menu_button_press():
      subprocess.Popen(args=['python', r'naptar.py'])
      ablak.destroy()
def iraki_menu_button_press():
    subprocess.Popen(args=['python', r'iraki_ora.py'])
    ablak.destroy()


pygame.mixer.init()

def bekapcsolas():
    try:
        temp =int(masodperc.get())
    except:
        hiba.set("Számot írj be kérlek!")
    pygame.mixer.music.load("20 Second Timer Bomb Countdown With Sound.mp3")
    pygame.mixer.music.play(loops=0)
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
            #os.system("shutdown /s /t 1")
        temp -= 1


ablak=Tk()
ablak.geometry("665x400")
ablak.title("Iraki óra")
menubar = Menu(ablak)
Kezdőoldalmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Kezdőoldal", command=kezdooldal_menu_button_press)
menubar.add_cascade(label="Akasztófa", command=akasztofa_menu_button_press)
menubar.add_cascade(label="Valuta Váltó", command=valuta_menu_button_press)
menubar.add_cascade(label="Valorant Line-up Guide", command=valorant_menu_button_press)
menubar.add_cascade(label="QR kód generátor", command=qrcode_menu_button_press)
menubar.add_cascade(label="Jelszó generátor", command=jelszo_menu_button_press)
menubar.add_cascade(label="Naptár", command=naptar_menu_button_press)
menubar.add_cascade(label="Iraki óra", command=iraki_menu_button_press)
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
masodperc.set("15")
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