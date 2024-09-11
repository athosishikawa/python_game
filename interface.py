import tkinter
import WConio2 as WConio2
import cursor
import os
import pickle

cursor.hide()

def abrirFile():
  cont = 0
  os.system('cls')
  highscore = open('highscore.bin', 'rb')
  print('-- H I G H S C O R E S --')
  scores = pickle.load(highscore)
  
  for jogador, score in scores:
    cont += 1
    print(str(cont) + "º -", jogador + ":", score)
  highscore.close()


def sair():
  exit()
  
def highscore():
  pass


def menu():
  window = tkinter.Tk()
  window.title("Car Racing Game")
  window.geometry("800x400")
  window.configure(background="black")

  window.line = tkinter.Label(window, text="CAR RACING\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n───────────────────────", fg="yellow", bg="black", font="Times 20 bold ", height=4)

  window.newGame = tkinter.Button(window, 
    text="New Game",  fg="yellow", bg="black", font="Times 20 bold italic",
    width=20,
    height=0,
    command=window.destroy
  )
  window.highscore = tkinter.Button(window, 
    text="High Scores",  fg="yellow", bg="black", font="Times 20 bold italic",
    width=20,
    height=0,
    command = abrirFile
  )
  window.exit = tkinter.Button(window, 
    text="Exit",  fg="yellow", bg="black", font="Times 20 bold italic",
    width=20,
    height=0,
    command = sair
  )

  window.line2 = tkinter.Label(window, text="_______________________________\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄", fg="yellow", bg="black", font="Times 20 bold italic", height=2)

 
  window.line.pack(side="top")
  window.newGame.pack()
  window.highscore.pack()
  window.exit.pack()
  window.line2.pack(side="top")
  

  # window.bind("<Return>", lambda event: window.destroy())

  window.mainloop()

