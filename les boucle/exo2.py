# ecrire un programme qui demande un nombre de depart, et qui ensuite
# affiche les dix nombres suivants en utilisant la boucle while
# par exemple, si l'utilisateur entre le nombre 44, le programme affichera 
# les nombres de 45 a 54

n = int(input('saisir la valeur de n : '))
i = n + 1
while i <= n + 10:
    print(i, end=' ')
    i += 1