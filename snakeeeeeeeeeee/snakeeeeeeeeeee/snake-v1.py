# -*- coding: utf-8 -*-
"""
Programme Snake

"""

from tkinter import * # Importation de la bibliothèque  Tkinter 

def right(event):
    global direction
    direction = 'right'
    
def left(event):
    global direction
    direction = 'left'

def up(event):
    global direction
    direction = 'up'
    
def down(event):
    global direction
    direction = 'down'

def computeNextFrame(numFrame,coordonnee):
    global direction
    print(numFrame)
    numFrame = numFrame + 1
    can.delete('all')
    for n in range (len(coordonnee)-1,0,-1):
        coordonnee[n][0] = coordonnee[n-1][0]
        coordonnee[n][1] = coordonnee[n-1][1]
    if direction == 'right':
        coordonnee[0][0] += 1
    if direction == 'left':
        coordonnee[0][0] += -1
    if direction == 'up':
        coordonnee[0][1] += -1
    if direction == 'down':
        coordonnee[0][1] += 1
    
    can.create_rectangle(coordonnee[0][0], coordonnee[0][1], coordonnee[0][0] + 20, coordonnee[0][1] + 20, outline='yellow', fill='red')
    
    for n in range(1, len(coordonnee)):
        can.create_rectangle(coordonnee[n][0], coordonnee[n][1], coordonnee[n][0] + 20, coordonnee[n][1] + 20, outline='blue', fill='green') 
    
    tk.after(4, lambda:computeNextFrame(numFrame,coordonnee))
if __name__ == "__main__":
    tk = Tk()
    direction = 'up' 
    # On crée un canevas dans l'environnement Tkinter d'une taille de 500x500
    # Ce constructeur prend comme premier paramètre l'objet dans lequel il sera
    # intégré (ici l'environnement Tkinter)
    # Les trois autres paramètres permettent de spécifier la taille et la couleur
    # de fond du canevas
    can = Canvas(tk, width=500, height=500, bg='black')
    # On affiche le canevas
    can.pack()
    can.create_rectangle(500, 0, 480, 20, outline='yellow', fill='green')
    can.create_oval(100, 200, 120, 120, outline='red', fill='blue')
    computeNextFrame(0,[[ 200,200], [200,220], [200,240], [220,240]])
    tk.bind('<d>', right)
    tk.bind('<q>', left)
    tk.bind('<z>', up)
    tk.bind('<s>', down)

    
    tk.mainloop() # Cet appel doit être la derniere instruction du programme




