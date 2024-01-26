# ecrire un programme qui echange les contenus de deux donnees 
# numerique si elles sont de meme signe, sinon il met la somme des 
# deux dans la premiere donnee et leur produit dans la seconde

a = int(input('la valeur de a : '))
b = int(input('la valeur de b : '))
print('la valeur de a = {} et la valeur de b = {}'.format(a, b))

if a * b > 0:
    c = a 
    a = b
    b = c
    print('la valeur de a = {} et la valeur de b = {}'.format(a, b))
else:
    E = a + b
    F = a * b
    A = E
    B = F
    print('la somme = {}'.format(A))
    print('la produit = {}'.format(B))