# ecrire un programme qui affiche la ou les solutions d'une equation du 
# second degré de la forma 
# ax carrée + bx + c

# nb : utiliser la fonction sqrt() de la bibliotheque math pour calculer la 
# racine carrée

import math
a = int(input('saisir la valeur de a non nulle : '))
while a == 0:
    a = int(input('saisir la valeur de a non nulle : '))
b = int(input('saisir la valeur de b : '))
c = int(input('saisir la valeur de c : '))

delta = b**2 -(4 * a * c)

if delta == 0:
    print('on a une solution double X0')
    X0 = (-b) / (2 * a)
    print('X0 = {}'.format(X0))
elif delta > 0:
    print('on a une double solution X1, X2')  
    X1 = (-b - (math.sqrt(delta))) / (2 * a)
    X2 = (-b + (math.sqrt(delta))) / (2 * a)
    print('X1 = {} et X2 = {}'.format(X1, X2))
else:
    print('impossible')
      