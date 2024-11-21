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

    if balle_x > 0:
        # Si la balle est à une position x positive,
        # on se place à la même position x que la balle
        x = balle_x
    else:
        # Sinon, on se place à la position x = 0
        x = 0.0
    y = constants.field_width / 2.0
    orientation = math.radians(-90)

    # La fonction goto permet de déplacer le robot vers des
    # coordonnées (x, y, orientation)
    client.green1.goto((x, y, orientation))
