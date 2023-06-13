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
ablak.title("Jelszó generátor")
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



cond1 = IntVar()
cond2 = IntVar()
cond3 = IntVar()
cond4 = IntVar()
length = IntVar()

#Listák
list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list_2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_3 = ['!', '@', '#', '$', '%', '^', "&", "*"]
list_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#Jelszó legenerálása
def password():
    final_list = []
    ln = length.get()
    if (cond3.get()):
        final_list.append(list_1)
    if (cond4.get()):
        final_list.append(list_2)
    if (cond2.get()):
        final_list.append(list_3)
    if (cond1.get()):
        final_list.append(list_4)
    bound = cond1.get() + cond2.get() + cond3.get() + cond4.get()
    if not (bound):
        return("Nem vállasztottál ki semmit a lehetőségek közül.")
    password=[]
    for i in range(ln):
        if (i == 0):
            a = 1
        else:
            a = random.randint(1,bound)
        k = final_list[a - 1]
        b = random.randint(0, len(k) - 1)
        password.append(str(k[b]))
    return (''.join(password))

pswrd = StringVar()
pswrd.set(password())
txt_1 = tkinter.Entry(ablak, textvariable=pswrd, font=("ComicSansMS", 14))

def display_password():
    global txt_1
    txt_1.pack_forget()
    pswrd.set(password())
    txt_1 = tkinter.Entry(ablak, textvariable=pswrd, font=("ComicSansMS", 14), width=37, justify=CENTER)
    txt_1.pack()


label_1 = tkinter.Label(ablak, text="\nJelszó Generátor", font=("ComicSansMS", 20))
label_2 = tkinter.Label(ablak, text = "Legalább két obciót válassz ki! \n", font=("ComicSansMS", 10))
label_1.pack()
label_2.pack()

chkbutton_1 = tkinter.Checkbutton(ablak, text='Számok', variable=cond1, onvalue=1, offvalue=0)
chkbutton_2 = tkinter.Checkbutton(ablak, text='Speciális karakterek', variable=cond2, onvalue=1, offvalue=0)
chkbutton_3 = tkinter.Checkbutton(ablak, text='Kisbetűk', variable=cond3, onvalue=1, offvalue=0)
chkbutton_4 = tkinter.Checkbutton(ablak, text='Nagybetűk', variable=cond4, onvalue=1, offvalue=0)
slider_1 = tkinter.Scale(ablak, variable=length, orient=HORIZONTAL, label="Jelszó hossza", length=130,from_=8, to=30)
button_1 = tkinter.Button(ablak, text="Jelszó generálása", command=display_password)
button_2 = tkinter.Button(ablak, text="Jelszó másolás [Még nem működik]")

chkbutton_1.pack()
chkbutton_2.pack()
chkbutton_3.pack()
chkbutton_4.pack()
slider_1.pack()
button_1.pack()

ablak.mainloop()