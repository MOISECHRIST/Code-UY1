from Manipulation.manipliste import *
from random import randrange
ListeAge=Listechainee()
print(type(ListeAge))
print(ListeAge.Sivide())
n=10
for i in range(n):
	age=randrange(16,30)
	ListeAge.ajoutdebut(age)
print("Total element :",ListeAge.nbelt())
ListeAge.affiche()
ListeAge=ListeAge.InversList()
print("Liste inversee est :")
print("Total element :",ListeAge.nbelt())
ListeAge.affiche()
age=randrange(26,30)
i=0
while ListeAge.recherche(age)==True:
	i+=1
	ListeAge.suppelt(age)
if i>0:
	print(age,"se trouve dans la liste",i,"fois")
	print("Total element :",ListeAge.nbelt())
	print("La nouvelle liste est :")
	ListeAge.affiche()
	print("Total element :",ListeAge.nbelt())
else:
	print(age,"ne se trouve pas dans la liste")
print("Liste triee ordre croissant est :")
ListeAge=ListeAge.TriCrois()
print("Total element :",ListeAge.nbelt())
ListeAge.affiche()
print("Liste triee ordre decroissant est :")
ListeAge=ListeAge.TriDecrois()
print("Total element :",ListeAge.nbelt())
ListeAge.affiche()
