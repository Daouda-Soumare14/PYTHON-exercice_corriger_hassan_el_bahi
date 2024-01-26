# ecrire un programme qui calcule et affiche la distance entre deux points
# A et B du plan dont les coordonnees (Xa, Ya) et (Xb, Yb) sont entrees au clavier 
# comme entiers

# NB : utileser la fonction math.sqrt() pour calculer la racine carree

import math
Xa = float(input('saisir la coordonnee X de A'))
Xb = float(input('saisir la coordonnee X de B'))
Ya = float(input('saisir la coordonnee Y de A'))
Yb = float(input('saisir la coordonnee Y de B'))

AB = (Xa - Xb)**2 + (Ya - Yb)**2
AB = math.sqrt(AB)

print('la distance entre les deux points A et B = {}'.format(AB))