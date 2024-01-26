# ecrire un programme qui demande a l'utilisateur de taper 
# un entier n (rang) et qui calcule le terme Un de la suite
# defini par:
# Uo = 6
# Un+1 = 4Un + 10

n = int(input('saisir la valeur de n : '))

U = 6
for i in range(1, n+1):
    U = 4 * U + 10
print('U{} = {}'.format(n, U))