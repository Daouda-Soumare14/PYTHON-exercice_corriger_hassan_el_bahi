# ecrire un programme qui demande a l'utilisateur de saisir 
# le nombre d'equipes participant a un championnat, puis le 
# programme affiche la liste des matchs a domicile et a 
# l'exeterieur pour ce championnat

n = int(input('saisir la valeur de n : '))

for i in range(1, n+1):
    for j in range(1, n+1):
        if i != j:
            print('Equipe{} VS Equipe{}'.format(i, j))