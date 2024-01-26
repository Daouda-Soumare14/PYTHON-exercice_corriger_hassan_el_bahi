# ecrire un programme qui calcule et affiche la somme
# s = 1/1 + 1/2 + ..... + 1/

n = int(input('saisir la valeur de n : '))
s = 0

for i in range(1, n + 1):
    s = s + 1 / i
print('la somme = {}'.format(s))



