# les habitabts d'une ville paient l'impot selon les regles suivantes:
#     - les hommes de plus de 20 ans paient l'impot
#     - les femmes paient l'impot si elles ont entre 18 et 35
#     - les autres ne paient l'impot
# ecrire un programme qui demande l'age et le sexe d'un habitant 
# et affiche si celui ci est imposable

age = int(input("saisir l'age de l'habitant : "))
sexe = (input("saisir le sexe de l'habitant : "))
h = "homme"
f = "femme"

if age > 20 and sexe == h:
    print("vous etes un homme qui reuni les condition, l'impot obligatoire")
elif age >= 18 and age <= 35 and sexe == f:
    print("vous etes une femme qui reuni les condition, l'impot obligatoire")
else:
    print("vous etes imposable")
    