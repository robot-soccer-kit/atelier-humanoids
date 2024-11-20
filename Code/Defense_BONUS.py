import numpy as np
import math
import rsk

from rsk import constants

client = rsk.Client() #Crée un client Robot Soccer Kit, contenant nombre de variables utiles 

while(1):#Boucle infinie permettant d'actualiser l'ordre demandé
    xb1 = client.blue1.position[0]
    yb1 = client.blue1.position[1]

    xballe = client.ball[0]
    yballe = client.ball[1]
    if xballe > xb1: #Si l'attaquant est plus avancé que la balle, il ne peut pas tirer, donc pas besoin de se déplacer
        pente = (yb1-yballe)/(xb1-xballe)

        xg1 = constants.field_length/2
        yg1 = ...
        
        if yg1 > ... :
            client.green1.goto((xg1, constants.goal_width/2, math.radians(180)))#Déplace le robot Green1 à son poteaux haut, et oriente le robot vers la gauche
        elif yg1 < -... :
            client.green1.goto((xg1, -constants.goal_width/2, math.radians(180)))#Déplace le robot Green1 à son poteaux bas, et oriente le robot vers la gauche
        else:
            client.green1.goto((xg1, yg1, math.radians(180)))#Déplace le robot Green1 à la position actuelle de la balle selon l'axe y, et oriente le robot vers la gauche