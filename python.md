
# 📋 Memo Python

## 🔢 Variables

Une **variable** est un espace de mémoire qui contient une valeur. En Python, vous pouvez créer une variable en lui assignant une valeur avec le signe ``=`` :

```python
x = 10  # Variable de type entier
y = 5.5  # Variable de type flottant
nom = "Robot"  # Chaîne de caractères
```

## 💻 Affichage

Pour afficher une variable, vous pouvez utiliser la fonction ``print()`` :

```python
x = 10
print(x)
>> 10
```

On peut aussi ajouter du texte pour mieux comprendre l'affichage :

```python
x = 10
print("La valeur de x est", x)
>> La valeur de x est 10
```

## ➗ Operations mathématiques

Python permet de faire des opérations mathématiques de base :

- Addition : ``+``
- Soustraction : ``-``
- Multiplication : ``*``
- Division : ``/``
- Puissance : ``**``

```python
a = 5
b = 3
print(a + b)
>> 8

print(a - b)
>> 2

print(a * b)
>> 15

print(a / b)
>> 1.6666666666666667

print(a ** b)
>> 125
```

## #️⃣ Commentaires

Un commentaire est une ligne de texte qui n’est pas exécutée. Il sert à documenter le code.

Un commentaire s’écrit avec ``#`` au début de la ligne.

```python
# Ceci est un commentaire
print("Hello World") # Ceci est un autre commentaire
```

Le raccourci clavier pour commenter/décommenter une ligne de code est ``Ctrl + :`` sur Windows.

## 🔁 Conditions et boucles

### Conditions

Les conditions permettent de prendre des décisions dans un programme. En fonction de celles-ci, différentes parties du code peuvent être exécutées.

- ``if`` : vérifie une condition et exécute le bloc de code associé si elle est vraie.
- ``elif`` : vérifie une autre condition lorsque la première est fausse et exécute le bloc de code associé si cette nouvelle condition est vraie.
- ``else`` : exécute un bloc de code si toutes les conditions précédentes sont fausses

```python
if condition:
    # Bloc de code exécuté si la condition est vraie
elif autre_condition:
    # Bloc exécuté si la première condition est fausse et l’autre condition est vraie
else:
    # Bloc exécuté si toutes les conditions précédentes sont fausses
```

### Operateurs de comparaison

Les opérateurs de comparaison permettent de comparer deux valeurs. Ils sont utilisés dans les conditions pour vérifier si une condition est vraie ou fausse :

- ``==`` : égal à
- ``!=`` : différent de
- ``<`` : inférieur à
- ``>`` : supérieur à
- ``<=`` : inférieur ou égal à
- ``>=`` : supérieur ou égal à

```python
age = 18

if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")
>> Vous êtes majeur.
```

### Operateurs logiques

On peut combiner plusieurs conditions grâce aux opérateurs logiques :

- ``and`` :  toutes les conditions doivent être vraies.
- ``or`` : au moins une des conditions doit être vraie.
- ``not`` : inverse la condition.

```python
x = 12
y = 3

if x > 5 and y < 10:
    print("Les deux conditions sont vraies.")
>> Les deux conditions sont vraies.
```

### Boucles

Les boucles permettent de répéter un bloc de code plusieurs fois. Il existe deux types de boucles en Python : ``for`` et ``while``.

#### Boucle ``for``

La boucle ``for`` permet de répéter un bloc de code un nombre déterminé de fois. Elle est souvent utilisée pour parcourir des séquences (listes, chaînes de caractères, etc.)

```python
for variable in séquence:
    # Bloc de code exécuté pour chaque élément de la séquence
```

```python
for i in range(3):
    print(i)
>> 0
>> 1
>> 2
```

#### Boucle ``while``

La boucle ``while`` exécute un bloc de code tant qu’une condition est vraie.

```python
while condition:
    # Bloc de code exécuté tant que la condition est vraie
```

```python
compteur = 0
while compteur < 4:
    print(compteur)
    compteur = compteur + 1
>> 0
>> 1
>> 2
>> 3
```

#### Boucle infinie et sortie de boucle

Une boucle infinie se produit quand la condition de sortie n’est jamais atteinte. Cela peut bloquer l’exécution du programme. On peut interrompre une boucle avec l’instruction ``break``.

```python
compteur = 0
while True:
    print(compteur)
    compteur += 1
    if compteur == 4:
        break
>> 0
>> 1
>> 2
>> 3
```

## 📤 Fonctions

Une fonction est un bloc de code réutilisable qui permet d'effectuer une tâche spécifique. Elle prend en entrée des arguments et retourne un résultat. Les fonctions permettent de découper un programme en sous-programmes plus petits et plus faciles à gérer.

En Python, une fonction se définit avec le mot-clé ``def`` suivi du nom de la fonction, des parenthèses (qui peuvent contenir des paramètres), et d’un bloc de code indenté (l'indentation est l'espacement en début de ligne qui permet de structurer le code). Voici la syntaxe d'une fonction en Python :

```python
def nom_de_la_fonction(param1, param2):
    # Bloc de code qui s'exécute
    return résultat  # (optionnel)
```

Pour appeler une fonction (c'est à dire l'exécuter), on utilise son nom suivi de parenthèses contenant les arguments à passer à la fonction.

Exemple :

```python
def addition(a, b):
    c = a + b
    return c

print(addition(2, 3))
>> 5
```

Une fonction peut retourner une valeur avec l’instruction ``return``. Si aucune valeur n'est retournée, Python renvoie ``None`` par défaut. La valeur retournée peut être de n'importe quel type (entier, chaîne de caractères, liste, etc.). La valeur retournée est la valeur par laquelle est remplacée l'appel de la fonction.

Les variables définies à l’intérieur d’une fonction sont locales à cette fonction. Cela signifie qu'elles ne sont pas accessibles en dehors de la fonction (en dehors du bloc de code indenté).

```python	
def fonction_a():
    x = 10  # Variable locale
    return x

print(x) # La variable x n'est pas accessible en dehors de la fonction
>> NameError: name 'x' is not defined
```