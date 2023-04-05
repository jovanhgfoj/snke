# -*- coding: utf-8 -*-
"""
Programme Snake 

"""
from tkinter import * # Importation de la bibliothèque  Tkinter 
from tkinter import font as tkfont
from random import randint

from PIL import Image, ImageTk 
# On crée un environnement Tkinter
tk = Tk()
im_teteN = Image.open("tete-N.png") 
teteN = ImageTk.PhotoImage(im_teteN) 
im_teteS = Image.open("tete-S.png") 
teteS = ImageTk.PhotoImage(im_teteS) 
im_teteE = Image.open("tete-E.png") 
teteE = ImageTk.PhotoImage(im_teteE) 
im_teteW = Image.open("tete-W.png") 
teteW = ImageTk.PhotoImage(im_teteW) 
im_noeud1 = Image.open("noeud3.png") 
noeud1 = ImageTk.PhotoImage(im_noeud1) 
im_noeud2 = Image.open("noeud4.png") 
noeud2 = ImageTk.PhotoImage(im_noeud2)
pomme = Image.open("pomme.png") 
pomme = ImageTk.PhotoImage(pomme)
poison = Image.open("pomme_poison.jpg")
poison = ImageTk.PhotoImage(poison)
piege = Image.open("pomme_piege.png")
piege = ImageTk.PhotoImage(piege)
#mise a 0 de la variable score 
score=0
def right(event):
    # Modification de la variable globale direction
    global direction
    direction = 'right'
    
def left(event):
    # Modification de la variable globale direction
    global direction
    direction = 'left'
    
def down(event):
    # Modification de la variable globale direction
    global direction
    direction = 'down'
    
def up(event):
    # Modification de la variable globale direction
    global direction
    direction = 'up'

# Calcule la nouvelle frame de jeu
def computeNextFrame(numFrame,coordonnee, objet, objet_2,objet_3):
    global direction
    global score
    global vitesse
    #création de la mort pour pomme 3
    mort = False
    # Affiche le numérod de la frame
    #print(numFrame)
    numFrame = numFrame + 1
    # Effacer le canevas
    can.delete('all')
    # Propagation du déplacement des noeuds
    for n in range (len(coordonnee)-1,0,-1):
        coordonnee[n][0] = coordonnee[n-1][0]
        coordonnee[n][1] = coordonnee[n-1][1]
        
    # Mise à jour des coordonnées
    if direction == 'right':
        coordonnee[0][0] += 20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteE)
        if coordonnee[0][0] > 480:
            coordonnee[0][0] = 0
    elif direction == 'left':
        coordonnee[0][0] += -20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteW)
        if coordonnee[0][0] < 0:
            coordonnee[0][0] = 480
    elif direction == 'up':
        coordonnee[0][1] += -20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteN)
        if coordonnee[0][1] < 0:
            coordonnee[0][1] = 480
    elif direction == 'down':
        coordonnee[0][1] += 20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteS)
        if coordonnee[0][1] > 480:
            coordonnee[0][1] = 0

    
    for n in range(1,len(coordonnee)):
        if n%2 == 0: 
            can.create_image(coordonnee[n][0], coordonnee[n][1], anchor = NW, image = noeud1)
        else:
            can.create_image(coordonnee[n][0], coordonnee[n][1], anchor = NW, image = noeud2)
        
    # Dessine les objets
    for p in range(len(objet)):
        can.create_image(objet[0][0], objet[0][1], anchor = NW, image = pomme)   
    
    for p in range(len(objet_2)):
        can.create_image(objet_2[0][0], objet_2[0][1], anchor = NW, image = poison)   
    
    for p in range(len(objet_3)):
        can.create_image(objet_3[0][0], objet_3[0][1], anchor = NW, image = piege) 
    
    for p in range(len(objet)):
        if coordonnee[0][0] == objet [0][0] and coordonnee[p][1] == objet [p][1]:
            # Déplacement de la pomme
            objet[0][0] = randint(1,24)* 20
            objet[0][1] = randint(1,24)* 20
            # Ajout d'un noeud au serpent (à la même place que le dernier noeud) et modification score
            coordonnee.append([-20, -20]) # Caché pour l'instant
            score=score+1
      
    for p in range(len(objet_2)):
        if coordonnee[0][0] == objet_2 [0][0] and coordonnee[p][1] == objet_2 [p][1]:
            mort = True
    for p in range(len(objet_3)):
        if coordonnee[0][0] == objet_3 [0][0] and coordonnee[p][1] == objet_3 [p][1]:
            objet_3[0][0] = randint(1,24)* 20
            objet_3[0][1] = randint(1,24)* 20
            # Ajout d'un noeud au serpent (à la même place que le dernier noeud) et modification score
            coordonnee.append([-20, -20]) # Caché pour l'instant
            score=score-5
    game_over = False     
    # On test la position de la tête par rapport aux noeuds du serpent
    for n in range(1,len(coordonnee)): # L'indice 0 est exclu, c'est la tête
        if coordonnee[0][0] == coordonnee [n][0] and coordonnee[p][1] == coordonnee [n][1]:
            game_over = True # La partie est finie        
        if mort == True:
            game_over = True
    
    if game_over : 
        # Fin de partie
        TEXTE = "GAME OVER"
        score=str(score)
        normal_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
        can.create_text(100,200,text = TEXTE, fill='red',  font=normal_font)
        normal_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
        can.create_text(100,300,text = "score = "+score, fill='red',  font=normal_font)
    
    else:
        # La partie n'est pas finie
        tk.after(50, lambda:computeNextFrame(numFrame,coordonnee, objet , objet_2,objet_3))
    
    

if __name__ == "__main__":
    # On crée un canevas dans l'environnement Tkinter d'une taille de 500x500
    # Ce constructeur prend comme premier paramètre l'objet dans lequel il sera
    # intégré (ici l'environnement Tkinter)
    # Les trois autres paramètres permettent de spécifier la taille et la couleur
    # de fond du canevas
    can = Canvas(tk, width=500, height=500, bg='black')
    
    # On affiche le canevas
    can.pack()
    
    # Direction par défaut
    direction = 'up' 
    
    coordonnee = [ [200, 200], [200, 220], [200, 240], [220, 240] ]
    objet = []
    
    # Premier objet (la pomme)
    x = randint(1,24)
    y = randint(1,24)
    objet.append([x*20, y*20, 0])
    
    # Second objet (le poison)
    objet_2=[]
    a = randint(5,24)
    b = randint(5,24)
    objet_2.append([a*20, b*20, 0])

    # Troisieme objet (pomme pige qui fait perdre en score)
    objet_3=[]
    c = randint(1,24)
    d = randint(1,24)
    objet_3.append([a*20, b*20, 0])
    
    # Construction de la première étape de simulation
    computeNextFrame(0,coordonnee, objet, objet_2, objet_3)
    
    # Appuyer sur la touche 'd' appellera la fonction right()
    tk.bind('<d>', right) 
    tk.bind('<q>', left) 
    tk.bind('<s>', down) 
    tk.bind('<z>', up) 
    
    # lancement de la boucle principale qui écoute les évènements (claviers...)
    tk.mainloop() # Cet appel doit être la derniere instruction du programme