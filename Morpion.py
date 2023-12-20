#Programme du Morpion
#Bibliothèques
from tkinter import *

def clic(event):
    """Fonction qui prend en compte où l'utilisateur clic pour savoir où placer son pion"""
    #Position du pointeur de la souris
    X=event.x
    Y=event.y
    #Variable
    global sym, liste, compteur
    a=0
    #Program
    if X>0 and X<100 and Y>100 and Y<200 and liste[0]==0:
        liste[0]+=sym
        a=1
        if sym%2==0:
            can.create_line(25,125,75,175)
            can.create_line(75,125,25,175)
        else:
            ellipse=can.create_oval(25,125,75,175,fill='white',outline='black')
    elif X>0 and X<100 and Y>200 and Y<300 and liste[1]==0:
        liste[1]+=sym
        a=1
        if sym%2==0:
            can.create_line(25,225,75,275)
            can.create_line(75,225,25,275)
        else:
            ellipse=can.create_oval(25,225,75,275,fill='white',outline='black')
    elif X>0 and X<100 and Y>300 and Y<400 and liste[2]==0:
        liste[2]+=sym
        a=1
        if sym%2==0:
            can.create_line(25,325,75,375)
            can.create_line(75,325,25,375)
        else:
            ellipse=can.create_oval(25,325,75,375,fill='white',outline='black')
    elif X>100 and X<200 and Y>100 and Y<200 and liste[3]==0:
        liste[3]+=sym
        a=1
        if sym%2==0:
            can.create_line(125,125,175,175)
            can.create_line(175,125,125,175)
        else:
            ellipse=can.create_oval(125,125,175,175,fill='white',outline='black')
    elif X>100 and X<200 and Y>200 and Y<300 and liste[4]==0:
        liste[4]+=sym
        a=1
        if sym%2==0:
            can.create_line(125,225,175,275)
            can.create_line(175,225,125,275)
        else:
            ellipse=can.create_oval(125,225,175,275,fill='white',outline='black')
    elif X>100 and X<200 and Y>300 and Y<400 and liste[5]==0:
        liste[5]+=sym
        a=1
        if sym%2==0:
            can.create_line(125,325,175,375)
            can.create_line(175,325,125,375)
        else:
            ellipse=can.create_oval(125,325,175,375,fill='white',outline='black')
    elif X>200 and X<300 and Y>100 and Y<200 and liste[6]==0:
        liste[6]+=sym
        a=1
        if sym%2==0:
            can.create_line(225,125,275,175)
            can.create_line(275,125,225,175)
        else:
            ellipse=can.create_oval(225,125,275,175,fill='white',outline='black')
    elif X>200 and X<300 and Y>200 and Y<300 and liste[7]==0:
        liste[7]+=sym
        a=1
        if sym%2==0:
            can.create_line(225,225,275,275)
            can.create_line(275,225,225,275)
        else:
            ellipse=can.create_oval(225,225,275,275,fill='white',outline='black')
    elif X>200 and X<300 and Y>300 and Y<400 and liste[8]==0:
        liste[8]+=sym
        a=1
        if sym%2==0:
            can.create_line(225,325,275,375)
            can.create_line(275,325,225,375)
        else:
            ellipse=can.create_oval(225,325,275,375,fill='white',outline='black')
    if liste[0]==liste[1]==liste[2]!=0 or liste[3]==liste[4]==liste[5]!=0 or liste[6]==liste[7]==liste[8]!=0 or liste[0]==liste[3]==liste[6]!=0 or liste[1]==liste[4]==liste[7]!=0 or liste[2]==liste[5]==liste[8]!=0 or liste[0]==liste[4]==liste[8]!=0 or liste[6]==liste[4]==liste[2]!=0:
        gagnant(sym)
    elif a==1:
        sym-=1
        compteur+=1
        if sym<1:
            sym=2
    elif compteur==9:
        perdant()
def gagnant(a):
    """Fonction qui affiche le gagnant et arrête le programme"""
    if a==2:
        can.create_rectangle(25,125,275,375,fill='white',outline='black')
        txt=can.create_text(150,150,text='Gagné !',fill="black",font=("Arial",30))
        txt=can.create_text(150,200,text='gagnant:',fill="black",font=("Arial",20))
        can.create_line(125,225,175,275)
        can.create_line(175,225,125,275)
    else:
        can.create_rectangle(25,125,275,375,fill='white',outline='black')
        txt=can.create_text(150,150,text='Gagné !',fill="black",font=("Arial",30))
        txt=can.create_text(150,200,text='gagnant:',fill="black",font=("Arial",20))
        ellipse=can.create_oval(125,225,175,275,fill='white',outline='black')

def perdant():
    """Fonction qui affiche les perdants et arrête le programme"""
    can.create_rectangle(25,125,275,375,fill='white',outline='black')
    txt=can.create_text(150,150,text='Perdu !',fill="black",font=("Arial",30))
    txt=can.create_text(150,250,text="T'es nul",fill="black",font=("Arial",20))


#Programme Principal
# Création de la fenêtre principale
fen=Tk()
fen.geometry("300x400")
fen.title("Morpion")
can=Canvas(fen,bg="white",width=300,height=400)
can.place(x=0,y=0)

#Title
txt=can.create_text(150,50,text='Morpion',fill="black",font=("Arial",30))

#Plateau
can.create_line(0,100,300,100)  #Title line
can.create_line(0,200,300,200)  #Hozintal lines
can.create_line(0,300,300,300)
can.create_line(0,400,300,400)
can.create_line(1,100,1,400)    #Vertical lines
can.create_line(100,100,100,400)
can.create_line(200,100,200,400)
can.create_line(300,100,300,400)

#Variables
sym=2
liste=[0,0,0,0,0,0,0,0,0]
l=[0,0,0,0,0,0,0,0,0]
compteur=0
#Détection des clics
can.bind("<Button-1>",clic)

#Mainloop
fen.mainloop()