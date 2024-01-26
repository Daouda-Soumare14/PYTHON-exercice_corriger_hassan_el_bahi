# a la naissance de Amal, son grand pere Ali, lui ouvre 
# un compte bancaire. ensuite , a chaque anniversaire, 
# le grand perede Amal verse sur compte 500F, auquels il ajoute le 
# triple de l'age de Amal. par exemple, lorsqu'elle a quatre ans, il lui 
# verse 512F. ecrire un programme qui permette de determiner quelle 
# somme aura Amal lors de son nième anniversaire 

age = int(input("saisir l'age de Amal : "))
s = 0

for i in range(1, age+1):
    s = s + (500 + (i * 3))
print('le compte de Amal au {} ième anniversaire = {} F'.format(age, s))