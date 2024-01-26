# ecrire un programme qui demande un nombre positif non nul
# de depart et qui calcule sa factorielle.
# par exemple, la factorielle de 6, notée 6! vaut 
# 1 * 2 * 3 * 4 * 5 * 6

n = int(input('saisir la valeur de n : '))
f = 1

for i in range(1, n+1):
    f = f * i
print(f) 