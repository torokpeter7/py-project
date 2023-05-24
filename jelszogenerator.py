from tkinter import *
import tkinter
import random
import tkinter as tk

ablak1 = tkinter.Tk()
ablak1.title("Jelszó generátor")
ablak1.geometry("680x400")

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
elsomondat=Label(ablak1, text="Üdvözlünk az alkalmazásunkban ami tele van minden-féle jósággal!")
masodikmondat=Label(ablak1, text="Akasztófa, Valuta váltó, Valorant Line-up Guide, QR kód generátor, Jelszó generátor, Naptár és egy kis meglepetés")
harmadikmondat=Label(ablak1, text="Válassz a menüpontok között és kezdd meg a világmegváltást még ma!")
ablak1.config(menu=menubar)

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
txt_1 = tkinter.Label(ablak1, textvariable=pswrd, font=("ComicSansMS", 14))

def display_password():
    global txt_1
    txt_1.pack_forget()
    pswrd.set(password())
    txt_1 = tkinter.Label(ablak1, textvariable=pswrd, font=("ComicSansMS", 14))
    txt_1.pack()

label_1 = tkinter.Label(ablak1, text="\nJelszó Generátor", font=("ComicSansMS", 20))
label_2 = tkinter.Label(ablak1, text = "Legalább két obciót válassz ki! \n", font=("ComicSansMS", 10))
label_1.pack()
label_2.pack()

chkbutton_1 = tkinter.Checkbutton(ablak1, text='Számok', variable=cond1, onvalue=1, offvalue=0)
chkbutton_2 = tkinter.Checkbutton(ablak1, text='Speciális karakterek', variable=cond2, onvalue=1, offvalue=0)
chkbutton_3 = tkinter.Checkbutton(ablak1, text='Kisbetűk', variable=cond3, onvalue=1, offvalue=0)
chkbutton_4 = tkinter.Checkbutton(ablak1, text='Nagybetűk', variable=cond4, onvalue=1, offvalue=0)
slider_1 = tkinter.Scale(ablak1, variable=length, orient=HORIZONTAL, label="Jelszó hossza", length=130,from_=8, to=30)
button_1 = tkinter.Button(ablak1, text="Jelszó generálása", command=display_password)

chkbutton_1.pack()
chkbutton_2.pack()
chkbutton_3.pack()
chkbutton_4.pack()
slider_1.pack()
button_1.pack()

ablak1.mainloop()