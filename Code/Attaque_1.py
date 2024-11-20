import numpy as np
import math
import rsk
from rsk import constants

client = rsk.Client() #Crée un client Robot Soccer Kit, contenant nombre de variables utiles 

while(1):#Boucle infinie permettant d'actualiser l'ordre demandé    
    client.blue1.goto((client.ball[0], client.ball[1]+constants.robot_radius, math.radians(-90)))#Déplace le robot derrière la balle, orienté vers le bas
    client.blue1.kick() #Tire