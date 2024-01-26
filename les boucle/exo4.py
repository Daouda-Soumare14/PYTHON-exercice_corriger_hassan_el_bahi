# ecrire un programmequi calcule et affiche la somme 
# s = 10^0 + 10^1 + 10^2 + ..... + 10^n

n = int(input('saisir la valeur de n : '))
s = 0
for i in range(0, n+1):
    s = s + (10 ** i)
print(s)