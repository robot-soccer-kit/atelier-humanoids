import numpy as np
import math
import rsk
from rsk import constants

client = rsk.Client() #Crée un client Robot Soccer Kit, contenant nombre de variables utiles 

while(1):#Boucle infinie permettant d'actualiser l'ordre demandé    
    #Position du milieu des buts [constants.field_length/2 ; 0.0]
    #La fonction arctan est disponible dans la bibliothèque math, en utilisant la fonction math.atan()

    orientation = math.atan(...)
    client.blue1.goto((client.ball[0]-constants.robot_radius*math.cos(orientation), client.ball[1]-constants.robot_radius*math.sin(orientation), orientation))#Déplace le robot derrière la balle, orienté à orientation°
    client.blue1.kick() #Tire