# ecrire un programme qui verifie si un nombre ou pair ou impair

n = int(input('saisir le nombre n : '))

if n % 2 == 0:
    print('{} est pair'.format(n)) 
else:
    print('{} est impair'.format(n)) 