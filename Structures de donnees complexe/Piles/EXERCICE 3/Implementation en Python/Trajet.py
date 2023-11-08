from Manipulation.fonction import *
pile=Pile()
pile.read()
print("Longueur de la pile :",pile.nbelt())
pile.print_list()
d="Odza"
if pile.search_elt(d)==True:
	print("\n",d,"se trouve dans la pile")
else :
	print("\n",d,"ne se trouve pas dans la pile")
elt=pile.minimum()
print("\nLe trajet de prix minimum :\n{}\t{}\t{}\t{}".format(elt.depart,elt.arrivee,elt.prix,elt.duree))
pile=pile.sort_list()
print("\nLa liste trié est :")
pile.print_list()
print("\n(C) 2022 By MMCJ/INF-L1\n")
