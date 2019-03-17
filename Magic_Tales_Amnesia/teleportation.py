# Crée par dornier, le 06/04/2017 en Python 3.2
import pygame
from pygame.locals import *
import time
#les définitions et les partis de ces définitions sont quasi-identiques, le début sera donc le plus commentée. Seuls les points qui diffèrent dans les autres le seront
#il y à deux définitions: une pour faire disparaîtrent le personnage et la statue, l'autre pour les faire réapparaîtrent
#on définit les variables de la définition
def fumeedispa(perso,position_perso_x,position_perso_y,fenetre,fond,fond3,fond1,fond2,idole,pos_idole_x,pos_idole_y, sqel1, position_sqel1_x, position_sqel1_y, sqel2, position_sqel2_x, position_sqel2_y):

    position_perso_x-=30
    position_perso_y-=40

    time.sleep( 0.3) #on "gèle" le jeu le temps d'afficher une image de fumée représentant la téléportation
    perso=pygame.image.load("fume 1_4.png").convert_alpha()
    if fond==fond1:
        fenetre.blit(fond1, (0,0)) #en fonction du niveau on affiche un fond différent
    elif fond==fond2:
        fenetre.blit(fond2, (0,0))
    elif fond==fond3:
        fenetre.blit(fond3, (0,0))
    fenetre.blit(idole, (pos_idole_x, pos_idole_y)) #puis on affiche tous les autres images
    fenetre.blit(perso, (position_perso_x, position_perso_y))
    fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
    fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
    pygame.display.flip()
    time.sleep( 0.3 ) #on répète ce "gèle" pour chaque image
    perso=pygame.image.load("fume 2_4.png").convert_alpha()
    if fond==fond1:
        fenetre.blit(fond1, (0,0))
    elif fond==fond2:
        fenetre.blit(fond2, (0,0))
    elif fond==fond3:
        fenetre.blit(fond3, (0,0))
    fenetre.blit(idole, (pos_idole_x, pos_idole_y))
    fenetre.blit(perso, (position_perso_x, position_perso_y))
    fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
    fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
    pygame.display.flip()
    time.sleep( 0.3 )
    perso=pygame.image.load("fume 3_4.png").convert_alpha()
    if fond==fond1:
        fenetre.blit(fond1, (0,0))
    elif fond==fond2:
        fenetre.blit(fond2, (0,0))
    elif fond==fond3:
        fenetre.blit(fond3, (0,0))
    fenetre.blit(idole, (pos_idole_x, pos_idole_y))
    fenetre.blit(perso, (position_perso_x, position_perso_y))
    fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
    fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
    pygame.display.flip()
    time.sleep( 0.3 )
    perso=pygame.image.load("fume 4_4.png").convert_alpha()
    if fond==fond1:
        fenetre.blit(fond1, (0,0))
    elif fond==fond2:
        fenetre.blit(fond2, (0,0))
    elif fond==fond3:
        fenetre.blit(fond3, (0,0))
    fenetre.blit(idole, (pos_idole_x, pos_idole_y))
    fenetre.blit(perso, (position_perso_x, position_perso_y))
    fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
    fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
    pygame.display.flip()
    time.sleep( 0.3 )
    perso=pygame.image.load("fume 5_4.png").convert_alpha()
    if fond==fond1:
        fenetre.blit(fond1, (0,0))
    elif fond==fond2:
        fenetre.blit(fond2, (0,0))
    elif fond==fond3:
        fenetre.blit(fond3, (0,0))
    fenetre.blit(idole, (pos_idole_x, pos_idole_y))
    fenetre.blit(perso, (position_perso_x, position_perso_y))
    fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
    fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
    pygame.display.flip()





def fumeeappa(perso,position_perso_x,position_perso_y,fenetre,fond,fond3,fond1,fond2,idole,pos_idole_x,pos_idole_y, sqel1, position_sqel1_x, position_sqel1_y, sqel2, position_sqel2_x, position_sqel2_y):
    position_perso_x+=15
    position_perso_y-=40
    time.sleep( 0.3)
    perso=pygame.image.load("fume 5_4.png").convert_alpha() #on affiche les images de fumée dans l'autre sens pour représenter une réapparittion
    if fond==fond1:
        fenetre.blit(fond1, (0,0))
    elif fond==fond2:
        fenetre.blit(fond2, (0,0))
    elif fond==fond3:
        fenetre.blit(fond3, (0,0))
    fenetre.blit(idole, (pos_idole_x, pos_idole_y))
    fenetre.blit(perso, (position_perso_x, position_perso_y))
    fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
    fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
    pygame.display.flip()
    time.sleep( 0.3 )
    perso=pygame.image.load("fume 4_4.png").convert_alpha()
    if fond==fond1:
        fenetre.blit(fond1, (0,0))
    elif fond==fond2:
        fenetre.blit(fond2, (0,0))
    elif fond==fond3:
        fenetre.blit(fond3, (0,0))
    fenetre.blit(idole, (pos_idole_x, pos_idole_y))
    fenetre.blit(perso, (position_perso_x, position_perso_y))
    fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
    fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
    pygame.display.flip()
    time.sleep( 0.3 )
    perso=pygame.image.load("fume 3_4.png").convert_alpha()
    if fond==fond1:
        fenetre.blit(fond1, (0,0))
    elif fond==fond2:
        fenetre.blit(fond2, (0,0))
    elif fond==fond3:
        fenetre.blit(fond3, (0,0))
    fenetre.blit(idole, (pos_idole_x, pos_idole_y))
    fenetre.blit(perso, (position_perso_x, position_perso_y))
    fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
    fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
    pygame.display.flip()
    time.sleep( 0.3 )
    perso=pygame.image.load("fume 2_4.png").convert_alpha()
    if fond==fond1:
        fenetre.blit(fond1, (0,0))
    elif fond==fond2:
        fenetre.blit(fond2, (0,0))
    elif fond==fond3:
        fenetre.blit(fond3, (0,0))
    fenetre.blit(idole, (pos_idole_x, pos_idole_y))
    fenetre.blit(perso, (position_perso_x, position_perso_y))
    fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
    fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
    pygame.display.flip()
    time.sleep( 0.3 )
    perso=pygame.image.load("fume 1_4.png").convert_alpha()
    if fond==fond1:
        fenetre.blit(fond1, (0,0))
    elif fond==fond2:
        fenetre.blit(fond2, (0,0))
    elif fond==fond3:
        fenetre.blit(fond3, (0,0))
    fenetre.blit(idole, (pos_idole_x, pos_idole_y))
    fenetre.blit(perso, (position_perso_x, position_perso_y))
    fenetre.blit(sqel1,(position_sqel1_x, position_sqel1_y))
    fenetre.blit(sqel2,(position_sqel2_x, position_sqel2_y))
    pygame.display.flip()