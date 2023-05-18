from tkinter import *
import calendar

def showCal():
    uj_ablak=Tk()
    uj_ablak.config (background="white")
    uj_ablak.title("NAPTAR")
    uj_ablak.geometry("550x600")
    visszaadhato_ev = int(ev_mezo.get())
    naptar_content=calendar.calendar(visszaadhato_ev)
    naptari_ev=Label(uj_ablak, text=naptar_content)
    naptari_ev.grid(row=5, column=1, padx=20)
    uj_ablak.mainloop()

    

if __name__ == "__main__" :
    ablak1 = Tk()

    ablak1.config(background="white")

    ablak1.title("NAPTAR")

    ablak1.geometry("250x150")

    napt = Label(ablak1, text="NAPTAR", bg= "dark gray", font= ("times", 28, "bold"))

    ev = Label(ablak1, text="adj meg 1 evszamot")

    ev_mezo=Entry(ablak1)

    szamitasgomb=Button(ablak1, text= "Mutasd a naptarat", command= showCal)
    napt.grid(row=1, column=1)
    ev.grid(row=2, column=1)
    ev_mezo.grid(row=3, column=1)
    szamitasgomb.grid(row=4, column=1)
    ablak1.mainloop()
