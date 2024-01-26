# ecrire un programme qui demande a l'utilisateur de saisir 2 entiers
# A et B qui echange le contenu des variables A et B puis qui affiche 
# A et B

a = int(input('saisir la valeur de A : '))
b = int(input('saisir la valeur de B : '))
print('A = {} et B = {}'.format(a, b))

c = a
a = b 
b = c
print('A = {} et B = {}'.format(a, b))
