from tkinter import *
import calendar
ablak1 = Tk()
ablak1.geometry("665x400")
ablak1.resizable(height=False, width=False)
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

    ablak1.config(background="white")

    ablak1.title("NAPTAR")

    ev = Label(ablak1, text="Adj meg 1 evszamot")

    ev_mezo=Entry(ablak1)

    szamitasgomb=Button(ablak1, text= "Mutasd a naptarat", command= showCal)
    ev.pack()
    ev_mezo.pack()
    szamitasgomb.pack()
    ablak1.config(menu=menubar)
    
    ablak1.mainloop()
