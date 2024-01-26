# ecrire un programme qui affiche les deviseurs d'un entier
# positif n non nul

n = int(input('saisir la valeur de n : '))
while n <= 0:
    n = int(input('saisir la valeur de n : '))

print('les diviseur de {} :'.format(n))
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=' ')