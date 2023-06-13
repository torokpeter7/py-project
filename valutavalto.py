from tkinter import *
import tkinter 
import random
import tkinter as tk
import subprocess

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

ablak = tkinter.Tk()
ablak.title("Valutaváltó")
ablak.geometry("665x400")

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
ablak.config(menu=menubar)

#combo = tk.Combobox()
#Lista
euro_huf = []
huf_euro = []

txt1 = Label(ablak, text="RŐL:")
txt2 = Label(ablak, text="RA:")
ertek = Label(ablak, text="Érték")
#combo = tk.Combobox(
    #state="readonly",
    #values=["Euro","HUF"])

input = Entry(ablak, )


ablak.mainloop()