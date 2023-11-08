from Manipulation.fonction import *
liste=File()
liste.read()
print("Longueur de la pile :",liste.nbelt())
liste.print_list()
d="Odza"
if liste.search_elt(d)==True:
	print(d,"se trouve dans la file")
else :
	print(d,"se trouve dans la file")
elt=liste.minimum()
print("Minimum : {}\t{}".format(elt.depart,elt.prix))
liste=liste.sort_list()
liste.print_list()
