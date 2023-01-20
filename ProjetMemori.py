import pygame
import sys
import fonctions

#Taille fenetre
LARGEUR_FENETRE = 600*1
HAUTEUR_FENETRE = 600*1

#taille CASE
LARGEUR_CASE = 300
HAUTEUR_CASE = 300

#Taille Bouton MENU
LARGEUR_FIG = 350
HAUTEUR_FIG = 100

COULEUR_FOND = (114, 213, 201) #couleur du fond d'écran
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRIS = (128, 128, 128)


pygame.init()


fenetre = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
pygame.display.set_caption("FISH MEMORY")

# Préparation de la Police utilisée pour l'affichage des textes
fonte = pygame.font.Font("PlayfairDisplay-Regular.ttf", 40)
fonte1 = pygame.font.Font("PlayfairDisplay-Regular.ttf",45)
fonte2 = pygame.font.Font("PlayfairDisplay-Regular.ttf",30)
fonte3 = pygame.font.Font("PlayfairDisplay-Regular.ttf",20)

# Préparation du rendu du texte
txt_1 = fonte.render("1", True, COULEUR_FOND)
txt_2 = fonte.render("2", True, COULEUR_FOND)
txt_3 = fonte.render("3", True, COULEUR_FOND)
txt_4 = fonte.render("4", True, COULEUR_FOND)
titre = fonte1.render("Fish Memory", True , WHITE)
commencer = fonte1.render("Commencer", True ,GRIS )
regles = fonte2.render("Regles du jeu:", True , GRIS)
ligne1 = fonte3.render("- Pour remporter le jeu il faut trouver toutes les paires:", True , (0,0,0))
ligne2 = fonte3.render("- Retourne les cartes une à une ", True , (0,0,0))
ligne3 = fonte3.render("- Si t'en trouves deux identiques à la suite", True , (0,0,0))
ligne4 = fonte3.render("tu as réussi!!", True , (0,0,0))
lignefin =fonte3.render("Bravo t'as réussi!", True ,(0,0,0))
retour = fonte1.render("Retour Menu", True ,GRIS )




img_1 = pygame.image.load("memori_1.jpg").convert()
img_2 = pygame.image.load("memori_2.jpg").convert()

jeu = 0  #trigger pour affichage menu/jeu/fin   0=menu  1=jeu  2=fin
couleur_cercle = 0 #trigger pour mettre en surbrillance les cercles
cpt_carte_retournee = 0 #compteur pour savoir le nb de carte qui sont retournées
cpt_paire_trouvee = 0 #compteur pour les paires trouvées

tab_carte = [[1, False, False],  #tableau représentant les cartes,  indice 0 : un identifiant
             [2, False, False],  #									indice 1 : le trigger carte retournée
             [2, False, False],  #									indice 2 : le trigger qui laisse la carte retournée quand une paire est trouvée
             [1, False, False]]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        ## L'utilisateur a-t-il enfoncé un bouton de souris dans la case numero x
        #Lorsque l'on clique dans la case, la carte se retourne si il n'y a pas déjà deux cartes de retourné.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] > 125 and event.pos[0]<475 and event.pos[1]>350 and event.pos[1] < 450 and jeu == 0:
                jeu = 1
            elif event.pos[0] > 125 and event.pos[0]<475 and event.pos[1]>200 and event.pos[1] < 300 and jeu == 2:
                jeu = 0
            elif 2 < event.pos[0] < 298 and 2 <event.pos[1] < 298 and jeu == 1: #CASE 1
                if cpt_carte_retournee <= 2 and not tab_carte[0][1]:
                    cpt_carte_retournee = fonctions.plus1(cpt_carte_retournee)
                    tab_carte[0][1] = True
            elif 302 < event.pos[0] < 598 and 2 <event.pos[1] < 298 and jeu == 1: #CASE 2
                if cpt_carte_retournee <= 2 and not tab_carte[1][1]:
                    cpt_carte_retournee = fonctions.plus1(cpt_carte_retournee)
                    tab_carte[1][1] = True
            elif 2 < event.pos[0] < 298 and 302 <event.pos[1] < 598 and jeu == 1: #CASE 3
                if cpt_carte_retournee <= 2 and not tab_carte[2][1]:
                    cpt_carte_retournee = fonctions.plus1(cpt_carte_retournee)
                    tab_carte[2][1] = True
            elif 302 < event.pos[0] < 598 and 302 <event.pos[1] < 598 and jeu == 1: #CASE 4
                if cpt_carte_retournee <= 2 and not tab_carte[3][1]:
                    cpt_carte_retournee = fonctions.plus1(cpt_carte_retournee)
                    tab_carte[3][1] = True
        
        # L'utilisateur a-t-il déplacé sa souris dans la case numero x
        elif event.type == pygame.MOUSEMOTION:
            if 2 < event.pos[0] < 298 and 2 <event.pos[1] < 298 and jeu == 1:
                couleur_cercle = 1
            elif 302 < event.pos[0] < 598 and 2 <event.pos[1] < 298 and jeu == 1:
                couleur_cercle = 2
            elif 2 < event.pos[0] < 298 and 302 <event.pos[1] < 598 and jeu == 1:
                couleur_cercle = 3
            elif 302 < event.pos[0] < 598 and 302 <event.pos[1] < 598 and jeu == 1:
                couleur_cercle = 4
     
    
    
    if cpt_carte_retournee > 2:
        cpt_carte_retournee = 0
        for i in range(len(tab_carte)):
            tab_carte[i][1] = False
        
       
    ## AFFICHAGE ##
    
    if jeu == 0: #MENU
        fenetre.fill(COULEUR_FOND)
        fenetre.blit(titre,(180,20))
        fenetre.blit(regles,(20,80))
        fenetre.blit(ligne1,(25,130))
        fenetre.blit(ligne2,(25,170))
        fenetre.blit(ligne3,(25,210))
        fenetre.blit(ligne4,(25,250))
        pygame.draw.rect(fenetre,WHITE,(125,350, LARGEUR_FIG,HAUTEUR_FIG))
        fenetre.blit(commencer,(175,365))
    elif jeu == 1: #JEU     
        fenetre.fill(COULEUR_FOND)
        
        if couleur_cercle == 0:        
            pygame.draw.rect(fenetre, WHITE, (0, 0, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, WHITE, (150,150), 50)
            fenetre.blit(txt_1, (142, 115))
                
            pygame.draw.rect(fenetre, WHITE, (300, 0, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, WHITE, (450,150), 50)
            fenetre.blit(txt_2, (442, 115))
            
            pygame.draw.rect(fenetre, WHITE, (0, 300, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, WHITE, (150,450), 50)
            fenetre.blit(txt_3, (142, 415)) 
            
            pygame.draw.rect(fenetre, WHITE, (300, 300, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, WHITE, (450,450), 50)
            fenetre.blit(txt_4, (442, 415))
        elif couleur_cercle == 1:
            pygame.draw.rect(fenetre, WHITE, (0, 0, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, RED, (150,150), 50)
            fenetre.blit(txt_1, (142, 115))
            if tab_carte[0][1] == True or tab_carte[0][2] == True:
                fenetre.blit(img_1, (2, 2))
                  
            pygame.draw.rect(fenetre, WHITE, (300, 0, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, WHITE, (450,150), 50)
            fenetre.blit(txt_2, (442, 115))
            if tab_carte[1][1] == True or tab_carte[1][2] == True:
                fenetre.blit(img_2,(302, 2))
            
            pygame.draw.rect(fenetre, WHITE, (0, 300, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, WHITE, (150,450), 50)
            fenetre.blit(txt_3, (142, 415))
            if tab_carte[2][1] == True or tab_carte[2][2]:
                fenetre.blit(img_2,(2,302))
            
            pygame.draw.rect(fenetre, WHITE, (300, 300, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, WHITE, (450,450), 50)
            fenetre.blit(txt_4, (442, 415))
            if tab_carte[3][1] == True or tab_carte[3][2]:
                fenetre.blit(img_1,(302,302))
                
        elif couleur_cercle == 2:
            pygame.draw.rect(fenetre, WHITE, (0, 0, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, WHITE, (150,150), 50)
            fenetre.blit(txt_1, (142, 115))
            if tab_carte[0][1] == True or tab_carte[0][2] == True:
                fenetre.blit(img_1,(2, 2))
                
            pygame.draw.rect(fenetre, WHITE, (300, 0, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, RED, (450,150), 50)
            fenetre.blit(txt_2, (442, 115))
            if tab_carte[1][1] == True or tab_carte[1][2] == True:
                fenetre.blit(img_2, (302, 2))  
            
            pygame.draw.rect(fenetre, WHITE, (0, 300, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, WHITE, (150,450), 50)
            fenetre.blit(txt_3, (142, 415))
            if tab_carte[2][1] == True or tab_carte[2][2]:
                fenetre.blit(img_2, (2, 302))
            
            pygame.draw.rect(fenetre, WHITE, (300, 300, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, WHITE, (450,450), 50)
            fenetre.blit(txt_4, (442, 415))
            if tab_carte[3][1] == True or tab_carte[3][2]:
                fenetre.blit(img_1, (302, 302))
                
        elif couleur_cercle == 3:
            pygame.draw.rect(fenetre, WHITE, (0, 0, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, WHITE, (150,150), 50)
            fenetre.blit(txt_1, (142, 115))
            if tab_carte[0][1] == True or tab_carte[0][2] == True:
                fenetre.blit(img_1,(2, 2))
                
            pygame.draw.rect(fenetre, WHITE, (300, 0, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, WHITE, (450,150), 50)
            fenetre.blit(txt_2, (442, 115))
            if tab_carte[1][1] == True or tab_carte[1][2] == True:
                fenetre.blit(img_2, (302, 2))
            
            pygame.draw.rect(fenetre, WHITE, (0, 300, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, RED, (150,450), 50)
            fenetre.blit(txt_3, (142, 415)) 
            if tab_carte[2][1] == True or tab_carte[2][2]:
                fenetre.blit(img_2, (2, 302))
                
            pygame.draw.rect(fenetre, WHITE, (300, 300, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, WHITE, (450,450), 50)
            fenetre.blit(txt_4, (442, 415))
            if tab_carte[3][1] == True or tab_carte[3][2]:
                fenetre.blit(img_1, (302, 302))
                
        elif couleur_cercle == 4:
            pygame.draw.rect(fenetre, WHITE, (0, 0, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, WHITE, (150,150), 50)
            fenetre.blit(txt_1, (142, 115))
            if tab_carte[0][1] == True or tab_carte[0][2] == True:
                fenetre.blit(img_1,(2, 2))
                
            pygame.draw.rect(fenetre, WHITE, (300, 0, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, WHITE, (450,150), 50)
            fenetre.blit(txt_2, (442, 115))
            if tab_carte[1][1] == True or tab_carte[1][2] == True:
                fenetre.blit(img_2, (302, 2))
            
            pygame.draw.rect(fenetre, WHITE, (0, 300, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, WHITE, (150,450), 50)
            fenetre.blit(txt_3, (142, 415))
            if tab_carte[2][1] == True or tab_carte[2][2]:
                fenetre.blit(img_2, (2, 302))
            
            pygame.draw.rect(fenetre, WHITE, (300, 300, LARGEUR_CASE, HAUTEUR_CASE), 2)
            pygame.draw.circle(fenetre, RED, (450,450), 50)
            fenetre.blit(txt_4, (442, 415))
            if tab_carte[3][1] == True or tab_carte[3][2]:
                fenetre.blit(img_1, (302, 302))
        
        if cpt_carte_retournee == 2:
            t = []
            for i in range(len(tab_carte)):
                if tab_carte[i][1] == True:
                    t.append(i)
            if tab_carte[t[0]][0] == tab_carte[t[1]][0]:
                tab_carte[t[0]][2]= True
                tab_carte[t[1]][2] = True
                cpt_carte_retournee = fonctions.plus1(cpt_carte_retournee)
                cpt_paire_trouvee = fonctions.plus1(cpt_paire_trouvee)
            del t
        if cpt_paire_trouvee == 2:
            jeu = 2
    elif jeu == 2:
        cpt_paire_trouvee = 0
        for i in range(len(tab_carte)):
            tab_carte[i][1] = False
            tab_carte[i][2] = False
        cpt_carte_retournee = 0
        fenetre.fill(COULEUR_FOND)
        fenetre.blit(titre,(150,25))
        fenetre.blit(lignefin,(222,400))
        pygame.draw.rect(fenetre,WHITE,(125,200, LARGEUR_FIG,HAUTEUR_FIG))
        fenetre.blit(retour,(185,215))
  
        

    pygame.display.update()
    