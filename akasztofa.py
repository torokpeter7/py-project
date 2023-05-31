from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random


ablak = Tk()
ablak.title('Akasztófa')
word_list= ["cutting","sale","eject","at","invisible","finger","embark","misery","tooth","printer","conceive","vegetable","marriage","size","progressive","road","smoke","secretion","stamp","transfer","introduce","reasonable","invite","capital","package","ancestor","fever","produce","poetry","revolution","spirit","steak","field","whip","due","section","majority","archive","insight","vacuum","relaxation","partner","wash","qualification","pride","activity","trouser","healthy","painter", "discriminate"]
            
photos = [PhotoImage(file="kepek/hang1.png"), PhotoImage(file="kepek/hang2.png"), PhotoImage(file="kepek/hang3.png"),
PhotoImage(file="kepek/hang4.png"), PhotoImage(file="kepek/hang5.png"), PhotoImage(file="kepek/hang6.png"),
PhotoImage(file="kepek/hang7.png"), PhotoImage(file="kepek/hang8.png"), PhotoImage(file="kepek/hang9.png"),
PhotoImage(file="kepek/hang10.png"), PhotoImage(file="kepek/hang11.png")]






def ujjatek():
    global the_word_withSpaces
    global talalatokszama
    talalatokszama =0
    
    a_szo=random.choice(word_list)
    the_word_withSpaces = " ".join(a_szo)
    lblWord.set(' '.join("_"*len(a_szo)))

def talalat(betu):
	global talalatokszama
	if talalatokszama<11:	
		txt = list(the_word_withSpaces)
		guessed = list(lblWord.get())
		if the_word_withSpaces.count(betu)>0:
			for c in range(len(txt)):
				if txt[c]==betu:
					guessed[c]=betu
				lblWord.set("".join(guessed))
				if lblWord.get()==the_word_withSpaces:
					messagebox.showinfo("Hangman","You guessed it!")
		else:
			talalatokszama += 1
			imgLabel.config(image=photos[talalatokszama])
			if talalatokszama==11:
					messagebox.showwarning("Hangman","Game Over")


imgLabel=Label(ablak)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)


  
lblWord = StringVar()
Label(ablak, textvariable  =lblWord,font=('consolas 24 bold')).grid(row=0, column=3 ,columnspan=6,padx=10)

n=0
for c in ascii_uppercase:
    Button(ablak, text=c, command=lambda c=c: talalat(c), font=('Helvetica 18'), width=4).grid(row=1+n//9,column=n%9)
    n+=1

Button(ablak, text="New\nGame", command=lambda:ujjatek(), font=("Helvetica 10 bold")).grid(row=3, column=8)

ujjatek()
ablak.mainloop()