#  ecrire un programme qui demande le nom et l'age d'un etudiant a 
# l'université et affiche "Bonjour" ...., tu as .... ans et bienvenue
# a l'université en remplacant les ... par, respectivement le nom et l'âge

nom = input('quel est votre nom : ')
age = int(input('quel est votre age : '))

print('bienvenue {} tu as {} ans'.format(nom, age))