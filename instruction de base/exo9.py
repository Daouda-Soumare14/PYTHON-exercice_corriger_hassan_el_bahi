# ecrire un programme qui demande un temps T (entier) exprimer
# en seconde, et qui le convertis en heures, minutes, seconde

t = int(input('saisir le temps en seconde : '))

h = t // 3600
r = t % 3600
m = r // 60
s = r // 60



print('{} h {} m {} s'.format(h, m, s))