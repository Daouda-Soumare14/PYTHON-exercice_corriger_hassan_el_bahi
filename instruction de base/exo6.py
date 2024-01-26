# ecrire un programme qui demande a l'utilisateur de taper 5 notes 
# et qui affiche leur somme et leur moyenne

note1 = float(input('saisir note 1 : '))
note2 = float(input('saisir note 2 : '))
note3 = float(input('saisir note 3 : '))
note4 = float(input('saisir note 4 : '))
note5 = float(input('saisir note 5 : '))

somme = note1 + note2 + note3 + note4 + note5
moyenne = somme / 5

print('la somme = {}'.format(somme))
print('la moyenne = {}'.format(moyenne))