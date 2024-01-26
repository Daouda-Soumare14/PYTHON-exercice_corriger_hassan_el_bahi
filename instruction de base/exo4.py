# ecrire un programme qui demande a l'utilisateur de saisir
# deux reels X et Y, et qui affiche la puissance X en Y

x = float(input('saisir la valeur de x : '))
y = float(input('saisir la valeur de y : '))

p = x ** y

print('{} a la puissance {} = {}'.format(x, y, p))