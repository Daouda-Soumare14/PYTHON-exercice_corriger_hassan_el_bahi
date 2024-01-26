# ce jeu est tres simple. l'ordinateur tire un nombre au 
# hasard entre 1 et 30 et vous avez cinq essais pour le trouver
# Apres chaque tentative, l'ordinateur vous dira si le nombre
# que vous avez proposé est trop grand, trop petit, ou si vous
# trouvé le bon nombre

import random
n = random.randint(1, 30)
nombreTantatives = 5

print("deviné le nombre choisi par l'ordinateur (entre 1 et 30) ")
while nombreTantatives > 0:
    nombreTantatives -= 1
    var = int(input("Entrer un nombre : "))
    if var > n:
        print("C'est plus")
    elif var < n:
        print("C'est moins")
    elif var == n:
        break # si le nombre est trouvé on sort de la boucle
if nombreTantatives != 0:
    print('Bravo vous avez trouvé {} en {} essais'.format(var, 5 - nombreTantatives))
else:
    print('Oups!! vous avez depassé les 5 tentatives autorisées, le nombre etait {} :'.format(n))