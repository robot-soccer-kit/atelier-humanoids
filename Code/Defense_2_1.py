import rsk
import math

client = rsk.Client() #Crée un client Robot Soccer Kit, contenant nombre de variables utiles 

while(1): #Boucle infinie permettant d'actualiser l'ordre demandé
    if client.ball[0] > 0.0: #Si la balle est dans la zone de l'équipe verte
        client.green1.goto((client.ball[0], 0.0, math.radians(-90)), wait=False) #Déplace le robot Green1 à la position actuelle de la balle selon l'axe x, et oriente le robot vers le bas
    else: #Sinon
        client.green1.goto((0.5, 0.0, math.radians(-90)), wait=False)#Déplace le robot Green1 à la position [0.5,0.0], et oriente le robot vers le bas