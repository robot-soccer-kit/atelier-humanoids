# *Atelier Robot Soccer Kit - Programme ton robot footballeur*

## Introduction

Dans cet atelier, vous allez apprendre à programmer des robots omnidirectionnels (qui peuvent se déplacer dans toutes les directions) afin qu'ils jouent au football.

## Prise en main de l'environnement de programmation

### 🚀 Lancement du simulateur

Pour lancer le simulateur, cliquez sur l'icône <img src="./img/RSK_simu.ico" width="30">  sur le Bureau.


Cela ouvrira une fenêtre de simulation dans un navigateur avec un terrain de football, quatre robots, une balle ainsi que l'interface d'arbitrage telle que présentée ci-dessous:


<img src="./img/referee.png" style="max-width: 80%; align-items: center">

<br>
<blockquote style="border-left: 5px solid yellow; padding-bottom:1px"><span style='font-size:20px;'>❕ </span>
<span style="font-weight: bold; color:yellow;">
Astuce
</span>

Si vous fermez le navigateur par inadvertance, l'interface reste accessible en réouvrant le navigateur et en allant à l'adresse [`http://127.0.0.1:7070`](http://127.0.0.1:7070).

</blockquote>

### Interface de programmation

Vous vous trouvez actuellement dans **Visual Studio Code**, un éditeur de texte que nous allons utiliser pour programmer en **Python**.

### ➕ Création d'un nouveau fichier

Pour créer un nouveau fichier, il suffit de faire un clic droit dans la zone à gauche, sur le dossier Code, et de cliquer sur `New File...`, puis d'entrer le nom du fichier, avec l'extension `.py`, car nous programmons ici en Python.


<video src="./video/creation_fichier.mp4" style="max-width: 50%; align-items: center" autoplay muted loop></video>


Si la zone n'apparait pas, cliquer sur l'icone : <img src="./img/explorer.png" width="35">

### ▶️ Lancement d'un programme

Pour lancer un programme, cliquer sur le bouton suivant:

![Play](./img/play.png)



Une fenêtre de terminal apparaît alors en bas de l'écran.


<img src="./img/ecran.png" style="max-width: 100%; align-items: center">


### ⏹️ Arrêter un programme

Enfin pour couper un programme, cliquer sur la petite poubelle (entourée en rouge ci-dessous) dans la partie terminal


<img src="./img/poubelle.png" style="max-width: 100%; align-items: center">

## Système de coordonnées

Par la suite, nous utiliserons le système de coordonnées suivant:



<img src="./img/field-frame.svg" style="max-width: 100%; align-items: center">



<blockquote style="border-left: 5px solid lightblue; color:lightblue; padding-bottom:1px"><span style='font-size:20px;'>&#x24D8; </span><span style="font-weight: bold">Info</span>

* $x$ et $y$ sont la position (exprimées en mètres)
* $\alpha$ est une orientation (exprimée en radians)
* l'origine du repère (le zéro) est au centre du terrain, comme indiqué sur la figure
</blockquote>

## Programmation des robots

## 1. Première défis: un robot défenseur

<blockquote style="border-left: 5px solid green; padding-bottom:1px">
<span style='font-size:20px'>📝 </span>
<span style="font-weight: bold; color:lightgreen">
Objectif
</span> <p>
Le but de cette première partie est de programmer un robot défenseur qui doit empêcher l'équipe adverse de marquer un but.
</blockquote>


### 1.1 Aligner le robot avec la balle

Ouvrez le fichier `defenseur.py`, et exécutez le. Observez le comportement du robot vert #1 lorsque vous déplacez la balle sur le terrain.

<blockquote style="border-left: 5px solid lightblue; color:lightblue; padding-bottom:1px"><span style='font-size:20px'>&#x24D8; </span><span style="font-weight: bold">Info</span>

- `balle_x` et `balle_y` sont les coordonnées de la balle dans le terrain, récupérées par le client
- `x`, `y` et `orientation` sont les coordonnées cible (à atteindre) pour notre robot
- `constants.field_width` est une constante définie dans la bibliothèque RSK, qui correspond à la largeur du terrain
- `math.radians(-90)` est une fonction de la bibliothèque math qui convertit un angle en degrés en radians
- la fonction `goto()` permet de déplacer le robot à la position cible, et l'orienter dans la direction souhaitée
</blockquote>
<br>

Comme vous pouvez le voir, ce n’est pas un très bon défenseur.

<blockquote style="border-left: 5px solid red; padding-bottom:1px">
<span style='font-size:20px;'>🎮 </span>
<span style="font-weight: bold; color:red;">
À vous de jouer !
</span>
<p style="font-style: italic; color:white;">
Changez le code de manière à ce que le robot se place dans ses cages, tout en restant en face de la balle.
</blockquote>
<br>

<blockquote style="border-left: 5px solid yellow; padding-bottom:1px"><span style='font-size:20px;'>❕ </span>
<span style="font-weight: bold; color:yellow;">
Astuce
</span>

Vous pourrez utiliser les constantes `constants.field_length` qui correspond à la longueur du terrain.

*On peut remarquer une latence entre le moment où la balle bouge et le moment où le robot bouge. Pour éviter cette latence, vous pouvez faire le changement suivant:*

```python
# Remplacez cette ligne:
client.green1.goto((x, y, orientation))

# Par celle-ci:
client.green1.goto((x, y, orientation), wait=False)
```

</blockquote>

---

### 1.2 Rester dans les cages

On aimerait désormais que le robot défenseur ne quitte pas la zone du gardien et reste entre ses poteaux.

Pour cela, nous allons utiliser des *conditions*. Ouvrez le fichier `defenseur_condition.py`. Ce dernier est similaire au code précédent, sauf que le robot ne se déplace pas vers la balle lorsque sa coordonnée $x$ est négative.

Cela est réalisé à l'aide de la condition `if balle_x > 0`.

<blockquote style="border-left: 5px solid red; padding-bottom:1px">
<span style='font-size:20px;'>🎮 </span>
<span style="font-weight: bold; color:red;">
À vous de jouer !
</span>
<p style="font-style: italic; color:white;">
En vous inspirant de ce code, modifiez le code précédent pour que le robot ne quitte pas la zone du gardien.
</blockquote>
<br>

<blockquote style="border-left: 5px solid yellow; padding-bottom:1px"><span style='font-size:20px;'>❕ </span>
<span style="font-weight: bold; color:yellow;">
Astuce
</span>

Vous pourrez utiliser les constantes `constants.goal_width` qui correspond à la largeur des cages.
</blockquote>

---

### 1.3 🌟 BONUS: Intersection de la trajectoire de l'attaquant

Nous avons désormais un gardien  qui reste dans ses cages, capable d'arrêter les tirs horizontaux.
Cependant, il est possible que l'attaquant fasse des tirs diagonaux, qui seront difficilement arrêtés par notre gardien actuel.

Pour cela, nous pouvons calculer un point d'intersection entre le segment attaquant-balle et la ligne de but, et déplacer notre gardien à ce point.

Nous pourrons utiliser la formule suivante:

$
y_{defenseur} = 
\frac{y_{balle} - y_{attaquant}}{x_{balle} - x_{attaquant}} \times (x_{cages} - x_{balle}) + y_{balle}
$

<blockquote style="border-left: 5px solid red; padding-bottom:1px">
<span style='font-size:20px;'>🎮 </span>
<span style="font-weight: bold; color:red;">
À vous de jouer !
</span>
<p style="font-style: italic; color:white;">
Modifiez le code précédent de façon à prendre en compte la position de l'attaquant
</blockquote>
<br>

<blockquote style="border-left: 5px solid yellow; padding-bottom:1px"><span style='font-size:20px;'>❕ </span>
<span style="font-weight: bold; color:yellow;">
Astuce
</span>

Vous pourrez récupérer la position de l'attaquant ( par exemple blue#1 ) avec les variables suivantes:

```python
# Position de l'attaquant (bleu 1)
attaquant_x = client.blue1.position[0]
attaquant_y = client.blue1.position[1]
```

</blockquote>

## 2. Deuxième défis: un robot attaquant

<blockquote style="border-left: 5px solid green; padding-bottom:1px">
<span style='font-size:20px'>📝 </span>
<span style="font-weight: bold; color:lightgreen">
Objectif
</span> <p>
Dans cette seconde partie, nous allons programmer un robot attaquant qui doit tenter de marquer des buts.
Afin de pouvoir jouer contre notre robot défenseur, nous allons maintenant nous placer du coté bleu.
</blockquote>

### 2.1 Attaque face aux cages

Pour commencer, nous allons réaliser un tir perpendiculaire aux cages.

Ouvrez le fichier `attaquant.py` et exécutez-le. Observez ce que fait le robot bleu #1 lorsque vous déplacez la balle sur le terrain.



<blockquote style="border-left: 5px solid red; padding-bottom:1px">
<span style='font-size:20px;'>🎮 </span>
<span style="font-weight: bold; color:red;">
À vous de jouer !
</span>
<p style="font-style: italic; color:white;">
Modifiez le code de l'attaquant de manière à ce que le robot tire vers les cages
</blockquote>
<br>

<blockquote style="border-left: 5px solid yellow; padding-bottom:1px"><span style='font-size:20px;'>❕ </span>
<span style="font-weight: bold; color:yellow;">
Astuce
</span>

*De nouveau, une latence est présente entre le mouvement de la balle et le mouvement du robot. Pour l'éviter, vous pouvez ajouter l'argument `wait=False` à la fonction `goto()`. En revanche, il faudra alors vérifier que le robot a fini son
déplacement avant de tirer:*

```python
# Placement du robot, test si le robot a fini son déplacement
if client.blue1.goto((x, y, orientation), wait=False):
    # Déclenchement du tir
    client.blue1.kick()
```

</blockquote>

---

### 2.2 Tir vers les buts selon 3 couloirs

Nous avons maintenant un robot attaquant capable de tirer de manière perpendiculaire aux cages.
Cependant, si le robot n'est pas aligné avec les cages, le tir ne sera pas cadré.

Une première approche pour résoudre ce problème serait de découper le terrains en 3 zones:

 <img src="./img/zones.png" style="max-width: 480px;" alt="45">


- dans la zone rouge, le tir sera effectué à -45°
- dans la zone jaune, le tir sera effectué à 0°
- dans la zone bleue, le tir sera effectué à 45°

<blockquote style="border-left: 5px solid red; padding-bottom:1px">
<span style='font-size:20px;'>🎮 </span>
<span style="font-weight: bold; color:red;">
À vous de jouer !
</span>
<p style="font-style: italic; color:white;">
Modifiez le code de l'attaquant de manière à ce que le robot tire vers les cages selon 3 couloirs
</blockquote>
<br>

<blockquote style="border-left: 5px solid yellow; padding-bottom:1px"><span style='font-size:20px;'>❕ </span>
<span style="font-weight: bold; color:yellow;">
Astuce
</span>

Remarque: pour placer un robot à une distance $d$ d'une balle, avec une orientation de -45°, vous pourrez utiliser un dégagement de $\frac{d}{\sqrt{2}}$ en $x$ et en $y$, comme indiqué sur la figure suivante:

<span style="background-color: green; margin: 4px; display: inline-block; z-index: -1">
    <img src="./img/45.svg" style="max-width: 60%; z-index: 10000" alt="45">
</span>

Pour orientation de 45°, le signe du dégagement en $y$ est inversé.
</blockquote>

### 2.3 🌟 BONUS : Tir vers les but selon n'importe quelle orientation

Au lieu de se limiter à 3 couloirs, on souhaiterait que le robot tire vers les cages, peu importe son orientation.

Pour cela, nous allons calculer l'orientation du robot par rapport à la position de la balle et des cages.

<blockquote style="border-left: 5px solid red; padding-bottom:1px">
<span style='font-size:20px;'>🎮 </span>
<span style="font-weight: bold; color:red;">
À vous de jouer !
</span>
<p style="font-style: italic; color:white;">
Modifiez le code de l'attaquant de manière à ce que le robot tire vers les cages, peu importe son orientation
</blockquote>
<br>

<blockquote style="border-left: 5px solid yellow; padding-bottom:1px"><span style='font-size:20px;'>❕ </span>
<span style="font-weight: bold; color:yellow;">
Astuce
</span>

Les fonctions trigonométriques `math.cos`, `math.sin`, `math.acos`, `math.asin` et `math.atan` sont disponibles dans la bibliothèque `math`.
</blockquote>

### 2.4 🌟 BONUS : Éviter les collisions avec la balle

Dans le cas où la balle se trouve sur la trajectoire du robot, il risque de la percuter et de la déplacer en essayant de se placer pour tirer.

<blockquote style="border-left: 5px solid red; padding-bottom:1px">
<span style='font-size:20px;'>🎮 </span>
<span style="font-weight: bold; color:red;">
À vous de jouer !
</span>
<p style="font-style: italic; color:white;">
Modifiez le code de l'attaquant de manière à ce qu'il évite les collisions avec la balle
</blockquote>


## 3. C'est l’heure du match !

<blockquote style="border-left: 5px solid red; padding-bottom:1px">
<span style='font-size:20px;'>🎮 </span>
<span style="font-weight: bold; color:red;">
À vous de jouer dans la cours des grand 🩻 !
</span>
<p style="font-style: italic; color:white;">
Il est temps de rassembler tout ce que vous avez appris pour faire un programme prêt à affronter un adversaire. Les terrains n’attendent que vous !
</blockquote>
