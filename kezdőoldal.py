from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, askyesno
from tkinter import filedialog as fd
from PIL import Image, ImageTk
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

ablak = Tk()
ablak.geometry("665x400")
ablak.resizable(width=False, height=False)
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
elsomondat=Label(ablak, text="Üdvözlünk az alkalmazásunkban ami tele van minden-féle jósággal!", font=("Arial", 14,""))
masodikmondat=Label(ablak, text="Akasztófa, Valuta váltó, Valorant Line-up Guide, QR kód generátor,\n Jelszó generátor, Naptár és egy kis meglepetés", font=("Arial", 12,""))
harmadikmondat=Label(ablak, text="Válassz a menüpontok között és kezdd meg a világmegváltást még ma!", font=("Arial", 12,""))
elsomondat.pack()
masodikmondat.place(x=95, y=124)
harmadikmondat.place(x=80, y=214)
logo=Image.open("Névtelen.png")
test = ImageTk.PhotoImage(logo)
label1 = Label(image=test)
label1.place(x=262, y=250)
ablak.config(menu=menubar)
ablak.mainloop()