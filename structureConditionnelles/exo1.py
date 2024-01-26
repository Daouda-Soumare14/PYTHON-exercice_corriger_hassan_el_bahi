# ecrire un programme qui retourne si deux nombres entiers 
# donnes sont de meme signe ou non

a = int(input('saise la valeur de a : '))
b = int(input('saise la valeur de b : '))

if a * b > 0:
    print('les deux valeurs sont de meme signe')
else:
    print('ils ne sont de signe differente')