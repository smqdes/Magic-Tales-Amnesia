

#on importe les bibliothèques nécessaires
import pygame
from pygame.locals import *
import time
import teleportation
import os
from random import *

pv_perso=3 #on définit les points de vie de base du perso
orientation_perso=0 #on définit une variable orientation qui servira plus tard : 0 pour gauche, 1pour droite






#on initialise la bibliothèque pygame
pygame.init()
os.environ["SDL_VIDEO_WINDOW_POS"]="%d,%d" % (10,30)



#on crée et on dimensionne la fenêtre
fenetre = pygame.display.set_mode((1420,724))

pygame.key.set_repeat(200,5) # cette ligne gère la réactivité du clavier, 400 ms pour le premier enfoncement de la touche, puis 30 ms si touche maintenue enfoncée

fond1 = pygame.image.load("LVL1.png").convert() #on charge les trois fonds des trois niveaux

fond2 = pygame.image.load("LVL2.png").convert()

fond3 = pygame.image.load("LVL3.png").convert()

perso=pygame.image.load("sorcier 3 RD2 gauche calque.png").convert_alpha() #on charge le perso

idole=pygame.image.load("idole_maudite.png").convert_alpha() #on charge l'idole

tpdroite=pygame.image.load("teleporteur_droite.png").convert_alpha() #on charge la statue, qui fait office de téléporteur

tpgauche=pygame.image.load("teleporteur_gauche.png").convert_alpha()

sqel1=pygame.image.load("sqel1_gauche.png").convert_alpha() #on charge les deux squelettes qui sont les ennemis du jeu
sqel2=pygame.image.load("sqel1_droite.png").convert_alpha() #l'un est tourné vers la gauche, l'autre vers la droite

flamme=pygame.image.load("flamme.png").convert_alpha() #on charge la flamme, ainsi que les sons associée et le hadoken pour notre easter-egg (voir le dossier projet)
tir_flamme=pygame.mixer.Sound("Boule_de_feu_1.wav")
hit_flamme=pygame.mixer.Sound("Boule_de_feu_2.wav")
hadoken=pygame.mixer.Sound("hadoken_son.wav")

hit=pygame.mixer.Sound("degats.wav") #on charge le son qui sera joué quand le personnage prendra des dégâts

vie1=pygame.image.load("coeur.png").convert_alpha() #on charge les 3 coeurs qui symbolistent les PV du perso ainsi que le sont qui sera joué qund ces derniers tomberont à 0
vie2=pygame.image.load("coeur.png").convert_alpha()
vie3=pygame.image.load("coeur.png").convert_alpha()
game_over=pygame.mixer.Sound("Game_over.wav")

musique_in_game=pygame.mixer.music.load("In_game.wav") #enfin on charge la musique du jeu

position_perso_x=1358 #on place le perso pour le premier niveau. Il pourra ensuite se déplacer comme bon lui semble
position_perso_y=332



pos_idole_x=9999 #on place l'idole hors de l'écran car elle n'apparaît pas avant le niveau 3. On réutilise souvent cette méthode dans le programme
pos_idole_y=9999


vie_sqel1=1 #on définit les points de vie des squelettes. Ici ils mourront en 1 coup, mais on pourrait changer cela simplement en modifiant la variable
vie_sqel2=1

continuer = True #on définit la variable continuer sur "True" ce qui permet de rentrer dans la première grande boucle
#ce principe sera réutilisé afin de sortir de cette boucle pour rentrer dans les autres grandes boucles


pygame.mixer.music.play(loops=10) #on lance la musique avant les boucles pour qu'elle soit jouéée quelle que soit la boucle en cours. "loop" permet de rejouer la musique quand elle arrive à la fin
#1ère grande boucle
#les trois boucles sont quasi-identiques, celle ci sera donc la plus commentée. Seuls les points qui diffèrent dans les autres le seront
while continuer==True:


    position_flamme_x=2000 #on place la flamme hors de l'écran à chaque boucle, car elle n'apparaît que lorsqu'une boule de feu est tirée
    position_flamme_y=0

    if vie_sqel1==1 : #on place les ennemis en fonction de leurs PV. S'il n'en on plus, on les fait sortir de l'écran
        position_sqel1_x=700
        position_sqel1_y=320
    elif vie_sqel1==0:
        position_sqel1_x=2001

    if vie_sqel2==1 :
        position_sqel2_x=100
        position_sqel2_y=320
    elif vie_sqel2==0:
        position_sqel2_x=2001

    if pv_perso==3: #même principe que pour les squellettes, le nombre de coeurs affichés depend directement des PV du perso. A chaque fois que le perso perd un PV, un coeur disparaît
        position_vie1_x=0
        position_vie1_y=0
        position_vie2_x=35
        position_vie2_y=0
        position_vie3_x=70
        position_vie3_y=0
    elif pv_perso==2:
        position_vie1_x=0
        position_vie1_y=0
        position_vie2_x=35
        position_vie2_y=0
        position_vie3_x=2000
        position_vie3_y=0
    elif pv_perso==1:
        position_vie1_x=0
        position_vie1_y=0
        position_vie2_x=2000
        position_vie2_y=0
        position_vie3_x=2000
        position_vie3_y=0
    elif pv_perso==0: #si les PV du perso tombent à 0, on le fait sortir de l'écran et on définit continuer sur "False", ce qui fait sortir de la boucle
        position_vie1_x=2000
        position_vie1_y=0
        position_vie2_x=2000
        position_vie2_y=0
        position_vie3_x=2000
        position_vie3_y=0
        position_perso_x=2000
        continuer=False

    for event in pygame.event.get():  #cette ligne gère les évènements reçus
        if event.type == QUIT: #si on clique sur la croix en haut à droite, on sort de la boucle et on passe au niveau suivant.
            continuer = False # cela nous a permit de coder plus facilement



        if event.type == KEYDOWN: # si on enfonce une touche de clavier


            if event.key == K_LEFT and orientation_perso==1  : #si cette touche est la flèche de gauche et que le perso est orienté vers la droite, il se retourne et vas vers la gauche
                perso=pygame.image.load("sorcier 3 RD2 gauche calque.png").convert_alpha()
                orientation_perso=0
                position_perso_x-=2
                if position_perso_x==position_sqel1_x and position_perso_y==position_sqel1_y+12: #si le perso rencontre un squellette, il recule et prend des dégâts
                    position_perso_x+=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()
                elif position_perso_x==position_sqel2_x and position_perso_y==position_sqel2_y+12:
                    position_perso_x+=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()
            elif event.key == K_LEFT and orientation_perso==0 : #sinon il va tout simplement vers la gauche
                position_perso_x-=2
                if position_perso_x==position_sqel1_x and position_perso_y==position_sqel1_y+12:
                    position_perso_x+=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()
                elif position_perso_x==position_sqel2_x and position_perso_y==position_sqel2_y+12:
                    position_perso_x+=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()


            if event.key == K_RIGHT and orientation_perso==0: #même principe mais vers la droite cette fois
                perso=pygame.image.load("sorcier 3 RD2 droite calque.png").convert_alpha()
                orientation_perso=1
                position_perso_x+=2
                if position_perso_x==position_sqel1_x and position_perso_y==position_sqel1_y+12:
                    position_perso_x-=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()
                elif position_perso_x==position_sqel2_x and position_perso_y==position_sqel2_y+12:
                    position_perso_x-=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()
            elif event.key == K_RIGHT and orientation_perso==1 :
                position_perso_x+=2
                if position_perso_x==position_sqel1_x and position_perso_y==position_sqel1_y+12:
                    position_perso_x-=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()
                elif position_perso_x==position_sqel2_x and position_perso_y==position_sqel2_y+12:
                    position_perso_x-=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()

            if event.key == K_UP and orientation_perso==1 : #si la touche est la flèche du haut et que le perso est tourné vers la droite
                    i=randint(0,11)# on lance une variable aléatoire entre 0 et 10


                    position_flamme_x=position_perso_x
                    position_flamme_y=position_perso_y
                    if i==10 : #si i=10, la boule de feu sera remplacée par le célèbre hadoken de la série Street Fighter, il y a donc une chance sur dix
                        flamme=pygame.image.load("hadoken.png").convert_alpha() #c'est un "easter-egg", un clin d'oeil à un jeu dans un autre jeu
                        hadoken.play()
                        tir_flamme.play()
                    else: #sinon le perso tirera une boule de feu basique
                        tir_flamme.play()
                        flamme=pygame.image.load("flamme.png").convert_alpha()
                    while 0<=position_flamme_x<=1420 : #tant que la flamme n'est pas aux limites de l'écran, elle avance
                        time.sleep(0.0001) #on "stoppe le temps" la boule de feu avance de deux pixels et ainsi de suite jusqu'à ce qu'elle rencontre un ennemi ou le bord de l'écran

                        position_flamme_x+=2
                        fenetre.blit(fond1, (0,0))
                        fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                        fenetre.blit(perso, (position_perso_x, position_perso_y))
                        fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                        fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                        fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                        fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                        fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                        pygame.display.flip()
                        if position_flamme_x==1420 : #si la boule de feu arrive au bord de l'écran, elle en sort, ce qui arrête la boucle
                            position_flamme_x=2000
                        elif position_flamme_x==0:
                            position_flamme_x=2000
                        elif position_flamme_x== position_sqel1_x and position_flamme_y==position_sqel1_y+12 : #si la flamme rencontre un squelette, le squelette meurt et la flamme sort de l'écran, ce qui arrête la boucle
                            vie_sqel1=0
                            hit_flamme.play()
                            time.sleep( 0.01 )
                            position_flamme_x=2000
                            fenetre.blit(fond1, (0,0))
                            fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                            fenetre.blit(perso, (position_perso_x, position_perso_y))
                            fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                            fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                            fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                            fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                            fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                            pygame.display.flip()

                        elif position_flamme_x== position_sqel2_x and position_flamme_y==position_sqel2_y+12 :
                            vie_sqel2=0
                            hit_flamme.play()
                            time.sleep( 0.01 )
                            position_flamme_x=2000
                            fenetre.blit(fond1, (0,0))
                            fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                            fenetre.blit(perso, (position_perso_x, position_perso_y))
                            fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                            fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                            fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                            fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                            fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                            pygame.display.flip()


            elif event.key == K_UP and orientation_perso==0 : #exactement le même principe, mais vers la gauche cette fois
                i=randint(0,11)


                position_flamme_x=position_perso_x
                position_flamme_y=position_perso_y
                if i==10 :
                   flamme=pygame.image.load("hadoken2.png").convert_alpha()
                   hadoken.play()
                   tir_flamme.play()
                else:
                   tir_flamme.play()
                   flamme=pygame.image.load("flamme2.png").convert_alpha()
                while 0<=position_flamme_x<=1420 :
                        time.sleep(0.0001)

                        position_flamme_x-=2
                        fenetre.blit(fond1, (0,0))
                        fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                        fenetre.blit(perso, (position_perso_x, position_perso_y))
                        fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                        fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                        fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                        fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                        fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                        pygame.display.flip()
                        if position_flamme_x==1420 :
                            position_flamme_x=2000
                        elif position_flamme_x==0:
                            position_flamme_x=2000
                        elif position_flamme_x== position_sqel1_x and position_flamme_y==position_sqel1_y+12 :
                            vie_sqel1=0
                            hit_flamme.play()
                            time.sleep( 0.01 )
                            position_flamme_x=2000
                            fenetre.blit(fond1, (0,0))
                            fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                            fenetre.blit(perso, (position_perso_x, position_perso_y))
                            fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                            fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                            fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                            fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                            fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                            pygame.display.flip()
                        elif position_flamme_x== position_sqel2_x and position_flamme_y==position_sqel2_y+12 :
                            vie_sqel2=0
                            hit_flamme.play()
                            time.sleep( 0.01 )
                            position_flamme_x=2000
                            fenetre.blit(fond1, (0,0))
                            fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                            fenetre.blit(perso, (position_perso_x, position_perso_y))
                            fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                            fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                            fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                            fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                            fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                            pygame.display.flip()

    if position_perso_x<4: #si le perso sort de l'écran par la gauche on sort de la boucle et on passe à la suivante, donc au niveau suivant
        continuer=False



    fenetre.blit(fond1, (0,0))
    fenetre.blit(perso, (position_perso_x, position_perso_y))
    fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
    fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
    fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
    fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
    fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
    fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
    pygame.display.flip()

position_perso_x=1356 # une fois sorti de la boucle, on place les différents éléments pour le niveau suivant
position_perso_y=634 #

tpdroite_x=520
tpdroite_y=613

tpgauche_x=467
tpgauche_y=546

fond=fond2
vie_sqel1=1 #on régénere les squelettes pour le prochain niveau
vie_sqel2=1

if pv_perso>0: #si il reste des PV au perso, on redéfinit continuer sur True ce qui permet de rentrer dans la boucle suivante. Sinon on passe la boucle suivante
    continuer = True

#2ème grande boucle
while continuer==True:
    position_flamme_x=2000
    position_flamme_y=0
    if vie_sqel1==1 :
        position_sqel1_x=100
        position_sqel1_y=550
    elif vie_sqel1==0:
        position_sqel1_x=2001

    if vie_sqel2==1 :
        position_sqel2_x=700
        position_sqel2_y=617
    elif vie_sqel2==0:
        position_sqel2_x=2001

    if pv_perso==3:
        position_vie1_x=0
        position_vie1_y=0
        position_vie2_x=35
        position_vie2_y=0
        position_vie3_x=70
        position_vie3_y=0
    elif pv_perso==2:
        position_vie1_x=0
        position_vie1_y=0
        position_vie2_x=35
        position_vie2_y=0
        position_vie3_x=2000
        position_vie3_y=0
    elif pv_perso==1:
        position_vie1_x=0
        position_vie1_y=0
        position_vie2_x=2000
        position_vie2_y=0
        position_vie3_x=2000
        position_vie3_y=0
    elif pv_perso==0:
        position_vie1_x=2000
        position_vie1_y=0
        position_vie2_x=2000
        position_vie2_y=0
        position_vie3_x=2000
        position_vie3_y=0
        position_perso_x=2000
        continuer=False #fond 2




    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False

        if event.type == KEYDOWN:

            if event.key == K_LEFT and orientation_perso==1 and position_perso_x!=572 :
                perso=pygame.image.load("sorcier 3 RD2 gauche calque.png").convert_alpha()
                orientation_perso=0
                position_perso_x-=2
                if position_perso_x==position_sqel1_x and position_perso_y==position_sqel1_y+17:
                    position_perso_+=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()
                elif position_perso_x==position_sqel2_x and position_perso_y==position_sqel2_y+17 :
                    position_perso_x+=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play
            elif event.key == K_LEFT and orientation_perso==0 and position_perso_x!=572:
                position_perso_x-=2
                if position_perso_x==position_sqel1_x and position_perso_y==position_sqel1_y+17:
                    position_perso_x+=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()
                elif position_perso_x==position_sqel2_x and position_perso_y==position_sqel2_y+17:
                    position_perso_x+=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()


            if event.key == K_RIGHT and orientation_perso==0 and position_perso_x!=1356 and position_perso_x!=424 :
                perso=pygame.image.load("sorcier 3 RD2 droite calque.png").convert_alpha()
                orientation_perso=1
                position_perso_x+=2
                if position_perso_x==position_sqel1_x and position_perso_y==position_sqel1_y+17:
                    position_perso_x-=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()
                elif position_perso_x==position_sqel2_x and position_perso_y==position_sqel2_y+17:
                    position_perso_x-=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()
            elif event.key == K_RIGHT and orientation_perso==1 and position_perso_x!=1356 and position_perso_x!=424:
                position_perso_x+=2
                if position_perso_x==position_sqel1_x and position_perso_y==position_sqel1_y+17:
                    position_perso_x-=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()
                elif position_perso_x==position_sqel2_x and position_perso_y==position_sqel2_y+17:
                    position_perso_x-=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()

            if event.key == K_UP and orientation_perso==1 :
                    i=randint(0,11)


                    position_flamme_x=position_perso_x
                    position_flamme_y=position_perso_y
                    if i==10 :
                        flamme=pygame.image.load("hadoken.png").convert_alpha()
                        hadoken.play()
                        tir_flamme.play()
                    else:
                        tir_flamme.play()
                        flamme=pygame.image.load("flamme.png").convert_alpha()
                    while 0<=position_flamme_x<=1420 :
                        time.sleep(0.0001)

                        position_flamme_x+=2
                        fenetre.blit(fond2, (0,0))
                        fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                        fenetre.blit(perso, (position_perso_x, position_perso_y))
                        fenetre.blit(tpdroite, (tpdroite_x,tpdroite_y))
                        fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                        fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                        fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                        fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                        fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                        pygame.display.flip()
                        if position_flamme_x==1420 :
                            position_flamme_x=2000
                        elif position_flamme_x==0:
                            position_flamme_x=2000
                        elif position_flamme_x== position_sqel1_x and position_flamme_y==position_sqel1_y+17 :
                            vie_sqel1=0
                            hit_flamme.play()
                            time.sleep( 0.01 )
                            position_flamme_x=2000
                            fenetre.blit(fond, (0,0))
                            fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                            fenetre.blit(perso, (position_perso_x, position_perso_y))
                            fenetre.blit(tpdroite, (tpdroite_x,tpdroite_y))
                            fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                            fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                            fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                            fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                            fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                            pygame.display.flip()

                        elif position_flamme_x== position_sqel2_x and position_flamme_y==position_sqel2_y+17 :
                            vie_sqel2=0
                            hit_flamme.play()
                            time.sleep( 0.01 )
                            position_flamme_x=2000
                            fenetre.blit(fond2, (0,0))
                            fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                            fenetre.blit(perso, (position_perso_x, position_perso_y))
                            fenetre.blit(tpdroite, (tpdroite_x,tpdroite_y))
                            fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                            fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                            fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                            fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                            fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                            pygame.display.flip()


            elif event.key == K_UP and orientation_perso==0 :
                i=randint(0,11)


                position_flamme_x=position_perso_x
                position_flamme_y=position_perso_y
                if i==10 :
                   flamme=pygame.image.load("hadoken2.png").convert_alpha()
                   hadoken.play()
                   tir_flamme.play()
                else:
                   tir_flamme.play()
                   flamme=pygame.image.load("flamme2.png").convert_alpha()
                while 0<=position_flamme_x<=1420 :
                        time.sleep(0.0001)

                        position_flamme_x-=2
                        fenetre.blit(fond2, (0,0))
                        fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                        fenetre.blit(perso, (position_perso_x, position_perso_y))
                        fenetre.blit(tpdroite, (tpdroite_x,tpdroite_y))
                        fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                        fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                        fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                        fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                        fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                        pygame.display.flip()
                        if position_flamme_x==1420 :
                            position_flamme_x=2000
                        elif position_flamme_x==0:
                            position_flamme_x=2000
                        elif position_flamme_x== position_sqel1_x and position_flamme_y==position_sqel1_y+17 :
                            vie_sqel1=0
                            hit_flamme.play()
                            time.sleep( 0.01 )
                            position_flamme_x=2000
                            fenetre.blit(fond2, (0,0))
                            fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                            fenetre.blit(perso, (position_perso_x, position_perso_y))
                            fenetre.blit(tpdroite, (tpdroite_x,tpdroite_y))
                            fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                            fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                            fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                            fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                            fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                            pygame.display.flip()
                        elif position_flamme_x== position_sqel2_x and position_flamme_y==position_sqel2_y+17 :
                            vie_sqel2=0
                            hit_flamme.play()
                            time.sleep( 0.01 )
                            position_flamme_x=2000
                            fenetre.blit(fond2, (0,0))
                            fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                            fenetre.blit(perso, (position_perso_x, position_perso_y))
                            fenetre.blit(tpdroite, (tpdroite_x,tpdroite_y))
                            fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                            fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                            fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                            fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                            fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                            pygame.display.flip()

            if event.key == K_SPACE: #si la touche pressée est la barre d'espace et que le perso est à proximité d'une statue, on utilise la fonction téléportation
                if position_perso_x<687:
                    teleportation.fumeedispa(perso,position_perso_x,position_perso_y,fenetre,fond,fond3,fond1,fond2,idole,pos_idole_x,pos_idole_y, sqel1, position_sqel1_x, position_sqel1_y, sqel2, position_sqel2_x, position_sqel2_y)
                    if fond==fond2:
                        position_perso_x=422 #on fait réaparaître le personnage ailleurs
                        position_perso_y=567
                        teleportation.fumeeappa(perso,position_perso_x,position_perso_y,fenetre,fond,fond3,fond1,fond2,idole,pos_idole_x,pos_idole_y, sqel1, position_sqel1_x, position_sqel1_y, sqel2, position_sqel2_x, position_sqel2_y)
                        tpdroite_x=tpgauche_x
                        tpdroite_y=tpgauche_y
                        tpdroite=tpgauche
                        fenetre.blit(tpgauche,(tpgauche_x,tpgauche_y))

    if position_perso_x<4:
        continuer=False



    fenetre.blit(fond2, (0,0))
    fenetre.blit(perso, (position_perso_x, position_perso_y))
    fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
    fenetre.blit(tpdroite, (tpdroite_x,tpdroite_y))
    fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
    fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
    fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
    fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
    fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
    pygame.display.flip()

position_perso_x=1356
position_perso_y=328
tpdroite_x=0
tpdroite_y=307

tpgauche_x=1356
tpgauche_y=613

vie_idole=5

fond=fond3
vie_sqel1=1
vie_sqel2=1

if pv_perso>0:
    continuer = True

#3ème grande boucle
while continuer==True:

    position_flamme_x=2000
    position_flamme_y=0
    if vie_sqel1==1 :
        position_sqel1_x=100
        position_sqel1_y=615
    elif vie_sqel1==0:
        position_sqel1_x=2001

    if vie_sqel2==1 :
        position_sqel2_x=500
        position_sqel2_y=315
    elif vie_sqel2==0:
        position_sqel2_x=2000

    if vie_idole>0: #le but est de détruire l'idole maudite, qui possède 5 PV
        pos_idole_x=0
        pos_idole_y=615
    elif vie_idole==0:
        pos_idole_x=2000
        time.sleep(0.5)
        continuer=False

    if pv_perso==3:
        position_vie1_x=0
        position_vie1_y=0
        position_vie2_x=35
        position_vie2_y=0
        position_vie3_x=70
        position_vie3_y=0
    elif pv_perso==2:
        position_vie1_x=0
        position_vie1_y=0
        position_vie2_x=35
        position_vie2_y=0
        position_vie3_x=2000
        position_vie3_y=0
    elif pv_perso==1:
        position_vie1_x=0
        position_vie1_y=0
        position_vie2_x=2000
        position_vie2_y=0
        position_vie3_x=2000
        position_vie3_y=0
    elif pv_perso==0:
        position_vie1_x=2000
        position_vie1_y=0
        position_vie2_x=2000
        position_vie2_y=0
        position_vie3_x=2000
        position_vie3_y=0
        position_perso_x=2000
        continuer=False

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False


        if event.type == KEYDOWN:


            if event.key == K_LEFT and orientation_perso==1 and position_perso_x!=52  :
                perso=pygame.image.load("sorcier 3 RD2 gauche calque.png").convert_alpha()
                orientation_perso=0
                position_perso_x-=2
                if position_perso_x==position_sqel1_x and position_perso_y==position_sqel1_y:
                    print(position_sqel1_y)
                    position_perso_x+=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()
                elif position_perso_x==position_sqel2_x and position_perso_y==position_sqel2_y+13:
                    position_perso_x+=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()
            elif event.key == K_LEFT and orientation_perso==0 and position_perso_x!=52 :
                position_perso_x-=2
                if position_perso_x==position_sqel1_x and position_perso_y==position_sqel1_y:
                    position_perso_x+=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()
                elif position_perso_x==position_sqel2_x and position_perso_y==position_sqel2_y+13:
                    position_perso_x+=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()


            if event.key == K_RIGHT and orientation_perso==0 and position_perso_x!=1356:
                perso=pygame.image.load("sorcier 3 RD2 droite calque.png").convert_alpha()
                orientation_perso=1
                position_perso_x+=2
                if position_perso_x==position_sqel1_x and position_perso_y==position_sqel1_y+20:
                    position_perso_x-=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()
                elif position_perso_x==position_sqel2_x and position_perso_y==position_sqel2_y+13:
                    position_perso_x-=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()
            elif event.key == K_RIGHT and orientation_perso==1 and position_perso_x!=1356 :
                position_perso_x+=2
                if position_perso_x==position_sqel1_x and position_perso_y==position_sqel1_y+20:
                    position_perso_x-=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()
                elif position_perso_x==position_sqel2_x and position_perso_y==position_sqel2_y+13:
                    position_perso_x-=100
                    time.sleep(0.5)
                    pv_perso-=1
                    hit.play()

            if event.key == K_UP and orientation_perso==1 :
                    i=randint(0,11)


                    position_flamme_x=position_perso_x
                    position_flamme_y=position_perso_y
                    if i==10 :
                        flamme=pygame.image.load("hadoken.png").convert_alpha()
                        hadoken.play()
                        tir_flamme.play()
                    else:
                        tir_flamme.play()
                        flamme=pygame.image.load("flamme.png").convert_alpha()
                    while 0<=position_flamme_x<=1420 :
                        time.sleep(0.0001)

                        position_flamme_x+=2
                        fenetre.blit(fond3, (0,0))
                        fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                        fenetre.blit(perso, (position_perso_x, position_perso_y))
                        fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                        fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                        fenetre.blit(tpdroite, (tpdroite_x,tpdroite_y))
                        fenetre.blit(tpgauche,(tpgauche_x,tpgauche_y))
                        fenetre.blit(idole, (pos_idole_x, pos_idole_y))
                        fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                        fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                        fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                        pygame.display.flip()
                        if position_flamme_x==1420 :
                            position_flamme_x=2000
                        elif position_flamme_x==0:
                            position_flamme_x=2000
                        elif position_flamme_x== position_sqel1_x and position_flamme_y==position_sqel1_y+20 :
                            vie_sqel1=0
                            hit_flamme.play()
                            time.sleep( 0.01 )
                            position_flamme_x=2000
                            fenetre.blit(fond3, (0,0))
                            fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                            fenetre.blit(perso, (position_perso_x, position_perso_y))
                            fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                            fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                            fenetre.blit(tpdroite, (tpdroite_x,tpdroite_y))
                            fenetre.blit(idole, (pos_idole_x, pos_idole_y))
                            fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                            fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                            fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                            pygame.display.flip()

                        elif position_flamme_x== position_sqel2_x and position_flamme_y==position_sqel2_y+13 :
                            vie_sqel2=0
                            hit_flamme.play()
                            time.sleep( 0.01 )
                            position_flamme_x=2000
                            fenetre.blit(fond3, (0,0))
                            fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                            fenetre.blit(perso, (position_perso_x, position_perso_y))
                            fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                            fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                            fenetre.blit(tpdroite, (tpdroite_x,tpdroite_y))
                            fenetre.blit(idole, (pos_idole_x, pos_idole_y))
                            fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                            fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                            fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                            pygame.display.flip()
                        elif position_flamme_x== pos_idole_x and position_flamme_y==pos_idole_y+20 :
                            vie_idole-=1
                            hit_flamme.play()
                            time.sleep( 0.01 )
                            position_flamme_x=2000
                            fenetre.blit(fond3, (0,0))
                            fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                            fenetre.blit(perso, (position_perso_x, position_perso_y))
                            fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                            fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                            fenetre.blit(tpdroite, (tpdroite_x,tpdroite_y))
                            fenetre.blit(idole, (pos_idole_x, pos_idole_y))
                            fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                            fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                            fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                            pygame.display.flip()


            elif event.key == K_UP and orientation_perso==0 :
                i=randint(0,11)


                position_flamme_x=position_perso_x
                position_flamme_y=position_perso_y
                if i==10 :
                   flamme=pygame.image.load("hadoken2.png").convert_alpha()
                   hadoken.play()
                   tir_flamme.play()
                else:
                   tir_flamme.play()
                   flamme=pygame.image.load("flamme2.png").convert_alpha()
                while 0<=position_flamme_x<=1420 :
                        time.sleep(0.0001)

                        position_flamme_x-=2
                        fenetre.blit(fond3, (0,0))
                        fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                        fenetre.blit(perso, (position_perso_x, position_perso_y))
                        fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                        fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                        fenetre.blit(tpdroite, (tpdroite_x,tpdroite_y))
                        fenetre.blit(idole, (pos_idole_x, pos_idole_y))
                        fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                        fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                        fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                        pygame.display.flip()
                        if position_flamme_x== position_sqel1_x and position_flamme_y==position_sqel1_y+20:
                            vie_sqel1=0
                            hit_flamme.play()
                            time.sleep( 0.01 )
                            position_flamme_x=2000
                            fenetre.blit(fond3, (0,0))
                            fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                            fenetre.blit(perso, (position_perso_x, position_perso_y))
                            fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                            fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                            fenetre.blit(tpdroite, (tpdroite_x,tpdroite_y))
                            fenetre.blit(idole, (pos_idole_x, pos_idole_y))
                            fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                            fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                            fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                            pygame.display.flip()
                        elif position_flamme_x== position_sqel2_x and position_flamme_y==position_sqel2_y+13:
                            vie_sqel2=0
                            hit_flamme.play()
                            time.sleep( 0.01 )
                            position_flamme_x=2000
                            fenetre.blit(fond3, (0,0))
                            fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                            fenetre.blit(perso, (position_perso_x, position_perso_y))
                            fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                            fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                            fenetre.blit(tpdroite, (tpdroite_x,tpdroite_y))
                            fenetre.blit(idole, (pos_idole_x, pos_idole_y))
                            fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                            fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                            fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                            pygame.display.flip()
                        elif position_flamme_x== pos_idole_x and position_flamme_y==pos_idole_y+20 :
                            vie_idole-=1
                            hit_flamme.play()
                            time.sleep( 0.01 )
                            position_flamme_x=2000
                            fenetre.blit(fond3, (0,0))
                            fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
                            fenetre.blit(perso, (position_perso_x, position_perso_y))
                            fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
                            fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
                            fenetre.blit(tpdroite, (tpdroite_x,tpdroite_y))
                            fenetre.blit(idole, (pos_idole_x, pos_idole_y))
                            fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
                            fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
                            fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
                            pygame.display.flip()

            if event.key == K_SPACE:
                if position_perso_x<=53:
                    teleportation.fumeedispa(perso,position_perso_x,position_perso_y,fenetre,fond,fond3,fond1,fond2,idole,pos_idole_x,pos_idole_y, sqel1, position_sqel1_x, position_sqel1_y, sqel2, position_sqel2_x, position_sqel2_y)
                    if fond==fond3:
                        position_perso_x=1308
                        position_perso_y=635
                        teleportation.fumeeappa(perso,position_perso_x,position_perso_y,fenetre,fond,fond3,fond1,fond2,idole,pos_idole_x,pos_idole_y, sqel1, position_sqel1_x, position_sqel1_y, sqel2, position_sqel2_x, position_sqel2_y)
                        tpdroite_x=tpgauche_x
                        tpdroite_y=tpgauche_y
                        tpdroite=tpgauche
                        fenetre.blit(tpgauche,(tpgauche_x,tpgauche_y))


    if position_perso_x<4 :
        continuer=False

    elif position_perso_x<56 and position_perso_y>350:
        continuer=False
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False




    fenetre.blit(fond3, (0,0))
    fenetre.blit(idole, (pos_idole_x, pos_idole_y))
    fenetre.blit(perso, (position_perso_x, position_perso_y))
    fenetre.blit(flamme, (position_flamme_x, position_flamme_y))
    fenetre.blit(tpdroite, (tpdroite_x,tpdroite_y))
    fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
    fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
    fenetre.blit(vie1,(position_vie1_x, position_vie1_y))
    fenetre.blit(vie2,(position_vie2_x, position_vie2_y))
    fenetre.blit(vie3,(position_vie3_x, position_vie3_y))
    pygame.display.flip()



if pv_perso==0:#si on est sortit des boucles car le perso n'a plus de PV, on "gèle" l'écran le temps que la musique de Game Over se joue, puis le jeu se ferme
    game_over.play()
    time.sleep(2)
    pygame.quit()

else : #sinon le jeu se ferme tout simplement
    pygame.quit()
