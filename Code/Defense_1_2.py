import numpy as np
import math
import rsk

client = rsk.Client() #Crée un client Robot Soccer Kit, contenant nombre de variables utiles 

while(1):#Boucle infinie permettant d'actualiser l'ordre demandé
    client.green1.goto((client.ball[0], 0.0, math.radians(-90)))#Déplace le robot Green1 à la position actuelle de la balle selon l'axe x, en restant sur la droite où y = 0, et oriente le robot vers le bas