# ecrire un programme qui demande a l'utilisateur de saise le rayon
# d'uns sphère quis calcule et affiche son volume 
# formule volume d'une sphère = 4*PI*r**3 / 3
import math
r = float(input('saisir le rayon du sphere : '))

volumeSphere = (4*math.pi*(r**3)) / 3

print('le volume du sphere = {}'.format(volumeSphere))             