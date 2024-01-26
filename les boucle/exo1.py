# ecrire un programme qui demande un nombre de depart, et qui ensuite
# affiche les dix nombres suivants en utilisant la boucle for
# par exemple, si l'utilisateur entre le nombre 44, le programme affichera 
# les nombres de 45 a 54

n = int(input('saisir le nombe n : '))
for i in range(n + 1, n + 11, 1):
    print(i, end=' ')