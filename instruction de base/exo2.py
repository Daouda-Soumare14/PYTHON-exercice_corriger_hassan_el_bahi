# ecrire un programme qui demande l'année de naissance d'une personne
# puis calcule et affiche l'age de la personne

anneeActuelle = 2024
anneeNaissace = int(input('quel est votre annee de naissance : '))
calculAge = anneeActuelle - anneeNaissace

print('vous avez {} ans'.format(calculAge))