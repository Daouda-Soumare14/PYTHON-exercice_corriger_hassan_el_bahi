# ecrire un programme qui demande a l'utilisateur de taper
# la largeur et la longueur d'un rectangle et qui affiche le
# perimetre et la surface

largeur = float(input('saisir la largeur du rectangle : '))
longueur = float(input('saisir la longueur du rectangle : '))

perimetre = (longueur + largeur) * 2
surface = longueur * largeur

print('le perimetre du rectangle = {}'.format(perimetre))
print('la surface du rectangle = {}'.format(surface))
