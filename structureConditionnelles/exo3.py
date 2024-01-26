# un magasin facture 150F les dix premier photocopie, 100F les vingt suivantes
# et 50F au dela. ecrire un programme qui demande a l'utilisateur le nombre de 
# photocopies effectuees et qui affiche la facture correcpondante

p = int(input('saisir le nombre de photocopie : '))
F1 = 150 * p
F2 = 100 * p
F3 = 50 * p

if p >= 1 and p <= 10:
    
    print('la facture = {}'.format(F1))
elif p >= 11 and p <= 20:
    print('la facture = {}'.format(F2))
else:
    print('la facture = {}'.format(F3))
    
    