import numpy as np
import math
import rsk
from rsk import constants

# Créé un client Robot Soccer Kit, qui permettra
# de communiquer avec le simulateur de soccer
client = rsk.Client()

# Boucle infinie
while True:
    # Récupération de la position de la balle
    balle_x = client.ball[0]
    balle_y = client.ball[1]

    # Définition de la position cible du robot
    x = balle_x
    y = balle_y + constants.robot_radius
    orientation = math.radians(-90)

    # Placement du robot
    client.blue1.goto((x, y, orientation), wait=False)

    # Déclenchement du tir
    client.blue1.kick()
