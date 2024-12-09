# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 18:16:57 2024

@author: mar et manj 
"""
import curses
stdscr = curses.initscr()
curses.noecho()
import random
import numpy 
import time   #gestion du temps d'affichage du message d'erreur 

#1.1 Création de la matrice du labyrinthe

def create_maze(size):
    Maze=[]
    for i in range(size):
       maze=[]
       for j in range(size):
           res = numpy.random.binomial(1,0.2,size) #création d'un liste de size éléments avec une proba de 0.3 d'apparition de 1 ou 0 not sure 
           res=list(res)
           maze=res
       Maze.append(maze)
    Maze[0][0]=0
    Maze[size-1][size-2] =0
    Maze[size-2][size-1]=0
    Maze[size-1][size-1]=2
    return Maze 

#TEST TEST TEST         
inter= create_maze(10)  #création des maze pour chaque niveau 
inter2=create_maze(25)
inter3=create_maze(15)
inter4=create_maze(12)


#1.2 Affichage 

def draw_maze(maze,dico):
   m=len(maze)
   for i in range(m):
       for j in range(m):
          print(dico[maze[i][j]],end="")
       print()


    
           
dico={0:"_",1:"X",2:"🏲"}     #dictionnaire des carcatère pour l'affichage 

#TEST TEST TEST 




#2.1 Initialisation du joueur

def create_perso(start):
    joueuse={"char":"⛹","x":start[0],"y":start[1]}
    return joueuse

#TEST TEST TEST 

joueuse= create_perso((0,0))  #création de notre joueur



def draw_maze_with_char(maze,dico,perso):
    n= len(maze)
    for i in range(n):
        for j in range(n):
            if i== perso["x"] and j==perso["y"]:
                print("⛹",end="")
            else : 
                print(dico[maze[i][j]],end="")
        print()


#TEST TEST TEST


def update_p1(letter,p):  #c'est la version mise à jour qui est utilisée 
    if letter =="z":
        p["x"]-=1
    if letter =="g":
        p["y"]-=1
    if letter =="s":
        p["x"]+=1
    if letter =="d":
        p["y"]+=1
    else:
        print("Donner une lettre valide")
        
        
        
#TEST TEST TEST 










    


#Déplacement en respectant le labyrinthe

def update_p(maze,letter,p):
    n=len(maze)-1
    message = "" #gestion du cas ou la position donnée n'est pas bonne 
    if letter =="z" and p["x"]-1>=0 and maze[p["x"]-1][p["y"]]!=1:
        p["x"]-=1
    if letter =="g"and p["y"]-1>=0 and maze[p["x"]][p["y"]-1]!=1:
        p["y"]-=1
    if letter =="s"  and p["x"]+1<=n and maze[p["x"]+1][p["y"]]!=1:
        p["x"]+=1
    if letter =="d" and p["y"]+1<=n and maze[p["x"]][p["y"]+1]!=1:
        p["y"]+=1
    if letter !="s" and letter !="z" and letter!="d" and letter!="g":
        message="Donner une lettre valide"
    
    if message: #Affichage du message 
        
        stdscr.addstr(len(maze)+4, 0, message)  # Afficher le message
        stdscr.refresh()
        time.sleep(1.5)  # Maintenir le message pendant 4 secondes / pas de mouvement possible pdt ce temps 
        # Effacer la ligne du message
        stdscr.move(len(maze)+4, 0) #bouger le curseur  pour le mettre à la ligne du message à supprimer 
        stdscr.clrtoeol()   #suppresion 
        stdscr.refresh()

   
        




# 5.1 Création des objets à récolter 

#pour les fonctions create items il ya possibilité de les transformer en une seule fonction en rajoutant le paramètre de l ataille de map si on a le temps on implémentera 


def create_items(maze,num_items):  #fonction pour le niveau 1
    res=[]
    n=0
    while n!= num_items: 
        x,y=random.randint(0,9),random.randint(0,9)
        if maze[x][y]!=2 and (x!=0 and y!=0) and maze[x][y]!=1:
            res.append((x,y))
            n+=1
    return res 



def create_itemsmap2(maze,num_items):  #fonction pour le niveau 2
    res=[]
    n=0
    while n!= num_items: 
        x,y=random.randint(0,24),random.randint(0,24)
        if maze[x][y]!=2 and (x!=0 and y!=0) and maze[x][y]!=1:
            res.append((x,y))
            n+=1
    return res 

def create_itemsmap3(maze,num_items): #fonction pour le niveau 3
    res=[]
    n=0
    while n!= num_items: 
        x,y=random.randint(0,14),random.randint(0,14)
        if maze[x][y]!=2 and (x!=0 and y!=0) and maze[x][y]!=1:
            res.append((x,y))
            n+=1
    return res 

def create_itemsmap4(maze,num_items): #fonction des objets bonus  pour le niveau 4
    res=[]
    n=0
    while n!= num_items: 
        x,y=random.randint(0,11),random.randint(0,11)
        if maze[x][y]!=2 and (x!=0 and y!=0) and maze[x][y]!=1:
            res.append((x,y))
            n+=1
    return res 

def create_items_mal(maze,num_items,liste_bon_obj):   #fonction des  objets malus pour le niveau 4
    mal=[]
    n=0
    while n!= num_items: 
        x,y=random.randint(0,9),random.randint(0,9)   #on les place sur une aire plus petite
        if maze[x][y]!=2 and (x!=0 and y!=0) and maze[x][y]!=1 and (x,y) not in liste_bon_obj:
            mal.append((x,y))
            n+=1
    return mal


#TEST TEST TEST 

objets =create_items(inter, 9)
objetsniv2=create_itemsmap2(inter2, 50)
objetsniv3=create_itemsmap3(inter3, 40)
objetsniv4=create_itemsmap4(inter4, 15)
objetsmauvais=create_items_mal(inter4, 8, objetsniv4)


#5.2 Affichage du labyrinthe avec les objets 

def draw_maze_with_char_and_items( maze, dico, items, perso):
    n = len(maze)
    for i in range(n):
        for j in range(n):
            char = dico[maze[i][j]]  # Caractère par défaut de la case
            if (i, j) in items:  # Si un objet est présent
                char = "*"
            if i == perso["x"] and j == perso["y"]:  # Si c'est la position du joueur
                char = "⛹"
            stdscr.addstr(i, j , char)  # Afficher le caractère
    stdscr.refresh()


def draw_maze_with_char_and_itemsniv4( maze, dico, items,items_mal, perso):  #affichage de la maze avec 
    n = len(maze)
    for i in range(n):
        for j in range(n):
            char = dico[maze[i][j]]  # Caractère par défaut de la case
            if( (i, j) in items) or ((i,j) in items_mal) :  # Si un objet est présent
                char = "*"
            if i == perso["x"] and j == perso["y"]:  # Si c'est la position du joueur
                char = "⛹"
            stdscr.addstr(i, j , char)  # Afficher le caractère
    stdscr.refresh()
    


      
#TEST TEST TEST 




#5.2 Ramassage des objets 

def collect_items(perso,items):
    for obj in items: 
        if perso["x"]==obj[0] and perso["y"]==obj[1]:
            items.remove(obj)


def collect_itemsniv4(perso, items, items_mal):
    for obj in items[:]:  # Vérifie les bons objets /sur un copie sinon pb avec le remove
        if perso["x"] == obj[0] and perso["y"] == obj[1]:
            items.remove(obj)  # Supprime le bon objet collecté
            return "+"

    for obj in items_mal[:]:  # Vérifie les mauvais objets
        if perso["x"] == obj[0] and perso["y"] == obj[1]:
            items_mal.remove(obj)  # Supprime le mauvais objet collecté
            return "-"

    return None  # Aucun objet collecté
            
    
#TEST TEST TEST 

#collect_items(perso, items) pas encore testé on tertera plus tard 





def Niv1(inter, dico, objets, joueuse):
    #flag1,flag2=True,True
    objets_collected = 0  # Réinitialiser le compteur d'objets

    # Affichage des instructions
    stdscr.addstr(0, 0, "Bienvenue dans Mar&Manj! Pour ce niveau 1 il te suffira d'atteindre la sortie marquée par un drapeau.")
    stdscr.addstr(1, 0, "Pour les déplacemnts du joueur, utilise'z' pour le haut, 's' pour le bas, 'd' pour la droite et 'g' pour la gauche!")
    stdscr.addstr(2, 0, "Sur ton chemin tu pourra collecter les pièces marquées par '*'.")
    stdscr.addstr(4, 0, "Appuyez sur une touche pour commencer.")
    
    stdscr.getkey()
    stdscr.erase()
    
   
    # Boucle principale du niveau 1
    while True:
        draw_maze_with_char_and_items(inter, dico, objets, joueuse)  # Affichage du labyrinthe
        
        entrer = stdscr.getkey() #on récupère le déplacement du joueur 
        update_p(inter, entrer, joueuse)  # Mise à jour de la position du joueur

        # Gestion des objets collectés
        les_objets = len(objets)
        collect_items(joueuse, objets)
        if len(objets) < les_objets:
            objets_collected += 1
            stdscr.addstr(len(inter) + 2, 0, "Pièces collectées : " + str(objets_collected))

        stdscr.refresh()
        
        draw_maze_with_char_and_items(inter, dico, objets, joueuse)
        # Vérification si le joueur a atteint la sortie
        if inter[joueuse["x"]][joueuse["y"]] == 2:
            stdscr.addstr(len(inter) + 3, 0, "C'est gagné ! Appuyez sur une touche pour passer au niveau 2.")
            stdscr.refresh()
            stdscr.getkey()
            stdscr.erase()
            return
            
    
            
def Niv2( inter2, dico, objetsniv2, joueuse):
    objets_collected = 0  # Réinitialiser le compteur d'objets
    joueuse["x"], joueuse["y"] = 0, 0  # Réinitialiser la position du joueur

    # Affichage des instructions
    stdscr.addstr(0, 0, "Bienvenue dans Mar&Manj! Pour ce niveau 2, atteignez la sortie marquée par un drapeau.")
    stdscr.addstr(1, 0, "Tu utilisera toujours les même flèches pour te déplacer!")
    stdscr.addstr(2, 0, "Collectez les pièces marquées par '*'.")
    stdscr.addstr(4, 0, "Appuyez sur une touche pour commencer.")
   
    stdscr.getkey()
    stdscr.erase()

    # Boucle principale du niveau 2
    while True:
        draw_maze_with_char_and_items(inter2, dico, objetsniv2, joueuse)  # Affichage du labyrinthe
        
        entrer = stdscr.getkey()
        update_p(inter2, entrer, joueuse)  # Mise à jour de la position du joueur

        # Gestion des objets collectés
        les_objets = len(objetsniv2)
        collect_items(joueuse, objetsniv2)
        if len(objetsniv2) < les_objets:
            objets_collected += 1
            stdscr.addstr(len(inter2) + 2, 0, "Pièces collectées : " + str(objets_collected))

        stdscr.refresh() #on applique les changements effectué par la collecte d'objets 
        draw_maze_with_char_and_items(inter2, dico, objetsniv2, joueuse)
        # Vérification si le joueur a atteint la sortie
        if inter2[joueuse["x"]][joueuse["y"]] == 2:
            stdscr.addstr(len(inter2) + 3, 0, "C'est gagné ! Appuyez sur une touche pour quitter.")
            stdscr.refresh()
            stdscr.getkey()
            stdscr.erase()
            return #pour arreter la fonction 
             
def Niv3(inter3, dico, objetsniv3, joueuse, mouv):
    while True:  # Boucle pour permettre de recommencer le niveau en cas d'échec
        objets_collected = 0  # Réinitialiser le compteur d'objets (vider de ceux du niveau présédants)
        joueuse["x"], joueuse["y"] = 0, 0  # Réinitialiser la position du joueur
        mouvements_restants = mouv  # Réinitialiser les mouvements disponibles/évite d'utiliser la variable passées en paramètre même

        # Affichage des instructions
        stdscr.addstr(0, 0, "Bienvenue dans Mar&Manj! Niveau 3 - Atteignez la sortie avec un nombre limité de mouvements.")
        stdscr.addstr(1, 0, "Vous disposez de  " + str(mouvements_restants)+ "mouvements")
        stdscr.addstr(4, 0, "Appuyez sur une touche pour commencer.")
        
        stdscr.getkey()
        stdscr.erase()

        # Boucle principale du niveau 3
        while True:
            # Affichage du labyrinthe et des statistiques
            draw_maze_with_char_and_items(inter3, dico, objetsniv3, joueuse)
            stdscr.addstr(len(inter3) + 1, 0, "Nombre de déplacement restants: " + str(mouvements_restants))
            stdscr.addstr(len(inter3) + 2, 0,"Pièces collectées : " + str(objets_collected) )
            
            stdscr.refresh()

            # Lire l'entrée utilisateur
            entrer = stdscr.getkey()
            update_p(inter3, entrer, joueuse)  # Mettre à jour la position du joueur
            mouvements_restants -= 1  # Décrémenter les mouvements restants

            # Gestion des objets collectés
            les_objets = len(objetsniv3)
            collect_items(joueuse, objetsniv3)
            if len(objetsniv3) < les_objets:  # Un objet a été collecté
                objets_collected += 1
            draw_maze_with_char_and_items(inter3, dico, objetsniv3, joueuse) 
            # Vérification des conditions de victoire ou d'échec
            if inter3[joueuse["x"]][joueuse["y"]] == 2:  # Si le joueur atteint la sortie
                stdscr.addstr(len(inter3) + 4, 0, "C'est gagné ! Appuyez sur une touche pour continuer.")
                stdscr.refresh()
                stdscr.getkey()
                stdscr.erase()
                return  # Terminer le niveau/sortie totale du jeu 

            if mouvements_restants <= 0:  # Si plus de mouvements disponibles
                stdscr.addstr(len(inter3) + 4, 0, "Perdu ! Vous avez épuisé vos déplacements.")
                stdscr.addstr(len(inter3) + 5, 0, "Appuyez sur une touche pour recommencer.")
                stdscr.refresh()
                stdscr.getkey()
                stdscr.erase()
                break  # Redémarrer le niveau / sortie de la boucle interne



def Niv4(inter4, dico, objetsniv4,objetsmauvais, joueuse, mouv):
    while True:  # Boucle pour recommencer en cas d'échec
        objets_collected = 0
        joueuse["x"], joueuse["y"] = 0, 0  # Position initiale
        mouvements_restants = mouv

        # Instructions du niveau
        stdscr.addstr(0, 0, "Bienvenue au niveau 4 ! Attention aux objets '*', certains vous rapporteront des déplacements, d'autres vous enlèveront!")
        stdscr.addstr(1, 0, f"Vous disposez de {mouvements_restants} mouvements.")
        stdscr.addstr(4, 0, "Appuyez sur une touche pour commencer.")
        
        stdscr.getkey()
        stdscr.erase()

        # Boucle principale
        while True:
            draw_maze_with_char_and_itemsniv4(inter4, dico, objetsniv4, objetsmauvais, joueuse)
            stdscr.addstr(len(inter4) + 1, 0, f"Mouvements restants : {mouvements_restants}")
            stdscr.addstr(len(inter4) + 2, 0, f"Pièces collectées : {objets_collected}")
            stdscr.refresh()

            entrer = stdscr.getkey()  # Entrée utilisateur
            update_p(inter4, entrer, joueuse)  # Mise à jour de la position
            mouvements_restants -= 1  # Réduction des mouvements

            # Gestion des objets collectés
            res = collect_itemsniv4(joueuse, objetsniv4, objetsmauvais)
            if res == "+":
                mouvements_restants += 3
                objets_collected += 1
                stdscr.addstr(len(inter4) + 3, 0, "Vous avez collecté un bon objet ! (+3 mouvements)")
                stdscr.refresh()
                time.sleep(1)  # Maintenir le message pendant 4 secondes / pas de mouvement possible pdt ce temps 
                # Effacer la ligne du message
                stdscr.move(len(inter4)+3, 0) #bouger le curseur  pour le mettre à la ligne du message à supprimer 
                stdscr.clrtoeol()   #suppresion 
                stdscr.refresh()
            elif res == "-":
                mouvements_restants -= 3
                stdscr.addstr(len(inter4) + 4, 0, "Vous avez collecté un mauvais objet ! (-3 mouvements)")
                stdscr.refresh()
                time.sleep(1)  # Maintenir le message pendant 4 secondes / pas de mouvement possible pdt ce temps 
                # Effacer la ligne du message
                stdscr.move(len(inter4)+4, 0) #bouger le curseur  pour le mettre à la ligne du message à supprimer 
                stdscr.clrtoeol()   #suppresion 
                stdscr.refresh()

            # Vérifications de fin de partie
            if inter4[joueuse["x"]][joueuse["y"]] == 2:  # Sortie atteinte
                stdscr.addstr(len(inter4) + 5, 0, "Bravo, vous avez gagné le niveau 4 !")
                stdscr.refresh()
                stdscr.getkey()
                stdscr.erase()
                return  # Fin du niveau

            if mouvements_restants <= 0:  # Plus de mouvements
                stdscr.addstr(len(inter4) + 5, 0, "Perdu ! Vous n'avez plus de mouvements.")
                stdscr.addstr(len(inter4) + 6, 0, "Appuyez sur une touche pour recommencer.")
                stdscr.refresh()
                stdscr.getkey()
                break  # Recommencer le niveau
   








#5.4 Modification de la boucle de jeux 

#on modifie la boucle de jeux 
        
#LE JEU 

def jeu():
    flag1, flag2,flag3,flag4 = True, True , True ,True # Indicateurs de niveaux actifs

    while flag1 or flag2 or flag3 or flag4:
        if flag1:
            Niv1( inter, dico, objets, joueuse)
            flag1 = False  # Niveau 1 terminé
        if flag2:
            Niv2( inter2, dico, objetsniv2, joueuse)
            flag2 = False  # Niveau 2 terminé
        if flag3 : 
            Niv3(inter3,dico,objetsniv3,joueuse,50)
            flag3=False   #Niveau 3 terminé 
        if flag4: 
            Niv4(inter4,dico,objetsniv4,objetsniv3,joueuse,mouv=45)
            flag4=False #Niveau 4 terminé 
        

    # Fin du jeu
    stdscr.erase()  # Effacer l'écran avant d'afficher le message de félicitations
    stdscr.addstr(0, 0, "Félicitations ! Vous avez terminé le jeu.")
    stdscr.addstr(1, 0, "Appuyez sur une touche pour quitter.")
    stdscr.refresh()  # Actualiser l'affichage
    stdscr.getkey()  # Attendre une entrée utilisateur avant de quitter


jeu()  #appel de la fonction pour lancer le jeu 


         

#TEST TEST TEST TEST 

    
    
        

