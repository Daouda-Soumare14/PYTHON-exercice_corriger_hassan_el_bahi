# ecrire un programme operations qui calcule la somme, le produit
# la difference la division  et le modulo de deux nombre reels

x = float(input('saisir la nombre 1 : '))
y = float(input('saisir la nombre 2 : '))

somme = x + y
dif = x - y
produit = x * y
div = x / y
mod = x % y

print('somme = {}'.format(somme))
print('dif = {}'.format(dif))
print('produit = {}'.format(produit))
print('div = {}'.format(div))
print('mod = {}'.format(mod))