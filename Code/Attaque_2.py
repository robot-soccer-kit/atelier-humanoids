import numpy as np
import math
import rsk
from rsk import constants

client = rsk.Client() #Crée un client Robot Soccer Kit, contenant nombre de variables utiles 

while(1):#Boucle infinie permettant d'actualiser l'ordre demandé    
    if client.ball[1] > constants.goal_width/2: # Si la balle est au dessus du but
        orientation = ...
        client.blue1.goto((client.ball[0]-constants.robot_radius*math.cos(orientation), client.ball[1]-constants.robot_radius*math.sin(orientation), math.radians(orientation)))#Déplace le robot derrière la balle, orienté à orientation°
    elif client.ball[1] < -constants.goal_width/2: # Si la balle est en dessous du but
        orientation = ...
        client.blue1.goto((client.ball[0]-constants.robot_radius*math.cos(orientation), client.ball[1]-constants.robot_radius*math.sin(orientation), math.radians(orientation)))#Déplace le robot derrière la balle, orienté à orientation°
    else:
        orientation = ...
        client.blue1.goto((client.ball[0]-constants.robot_radius*math.cos(orientation), client.ball[1]-constants.robot_radius*math.sin(orientation), math.radians(orientation)))#Déplace le robot derrière la balle, orienté à orientation°
    client.blue1.kick() #Tire