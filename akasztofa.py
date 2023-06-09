from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random


window = Tk()
menubar = Menu(window)
window.geometry("600x270")
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
window.title('Akasztófa')
word_list= ['MUMBAI','DELHI','BANGLORE','HYDRABAD','AHMEDABAD','CHENNAI','KOLKATA','SURAT','PUNE','JAIPUR','AMRITSAR','ALLAHABAD','RANCHI',
            'LUCKNOW','KANPUR','NAGPUR','INDORE','THANE','BHOPAL','PATNA','GHAZIABAD','AGRA','FARIDABAD','MEERUT','RAJKOT','VARANASI','SRINAGAR',
            'RAIPUR','KOTA','JHANSI']
            
photos = [PhotoImage(file="kepek\hang1.png"), PhotoImage(file="kepek\hang2.png"), PhotoImage(file="kepek\hang3.png"),
PhotoImage(file="kepek\hang4.png"), PhotoImage(file="kepek\hang5.png"), PhotoImage(file="kepek\hang6.png"),
PhotoImage(file="kepek\hang7.png"), PhotoImage(file="kepek\hang8.png"), PhotoImage(file="kepek\hang9.png"),
PhotoImage(file="kepek\hang10.png"), PhotoImage(file="kepek\hang11.png")]






def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses =0
    
    the_word=random.choice(word_list)
    the_word_withSpaces = " ".join(the_word)
    lblWord.set(' '.join("_"*len(the_word)))

def guess(letter):
	global numberOfGuesses
	if numberOfGuesses<11:	
		txt = list(the_word_withSpaces)
		guessed = list(lblWord.get())
		if the_word_withSpaces.count(letter)>0:
			for c in range(len(txt)):
				if txt[c]==letter:
					guessed[c]=letter
				lblWord.set("".join(guessed))
				if lblWord.get()==the_word_withSpaces:
					messagebox.showinfo("Eredmény","Kitaláltad a szót!")
		else:
			numberOfGuesses += 1
			imgLabel.config(image=photos[numberOfGuesses])
			if numberOfGuesses==10:
					messagebox.showwarning("Eredmény","Játék Vége")


imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)


  
lblWord = StringVar()
Label(window, textvariable  =lblWord,font=('consolas 24 bold')).grid(row=0, column=3 ,columnspan=6,padx=10)

n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=('Helvetica 18'), width=4).grid(row=1+n//9,column=n%9)
    n+=1

Button(window, text="New\nGame", command=lambda:newGame(), font=("Helvetica 10 bold")).grid(row=3, column=8)

newGame()
window.config(menu=menubar)
window.mainloop()