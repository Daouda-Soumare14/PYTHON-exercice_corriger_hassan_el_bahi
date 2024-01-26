# ecrire un programme qui demande a l'utilisateur de saisir un 
# entier n puis qui calcule la somme des carrées des n premiers 
# entier impairs
# par exemple, si n = 5 le resultat est 1^2 + 3^2 + 5^2 + 7^2 + 9^2

n = int(input('saisir la valeur de n : '))
s = 0
j = 1
for i in range(n):
    s = s + (j ** 2)
    j = j + 2
print(s)