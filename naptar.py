from tkinter import *
import calendar
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
ablak.resizable(height=False, width=False)
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

def showCal():
    uj_ablak=Tk()
    uj_ablak.config (background="white")
    uj_ablak.title("NAPTAR")
    uj_ablak.geometry("1000x1000")
    visszaadhato_ev = int(ev_mezo.get())
    naptar_content=calendar.calendar(visszaadhato_ev)
    naptari_ev=Label(uj_ablak, text=naptar_content, font="Consolas 10 bold")
    naptari_ev.grid(row=5, column=1, padx=20)
    uj_ablak.mainloop()

    

if __name__ == "__main__" :

    ablak.config(background="white")

    ablak.title("NAPTAR")

    ev = Label(ablak, text="Adj meg 1 evszamot")

    ev_mezo=Entry(ablak)

    szamitasgomb=Button(ablak, text= "Mutasd a naptarat", command= showCal)
    ev.pack()
    ev_mezo.pack()
    szamitasgomb.pack()
    ablak.config(menu=menubar)
    
    ablak.mainloop()
