# ecrire un programme qui determine si un nombre est premier 
# ou non (rappel: un nombre premier n'est divisible que par 1 et lui meme)

n = int(input('saisir la valeur de n : '))

estPremier = 1
for i in range(2, int(n/2)):
    if n % i == 0:
        estPremier = 0
        print('le nombre {} n est pas premier'.format(n))
        break
if estPremier == 1:
    print('le nombre {} est premier'.format(n))