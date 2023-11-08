from Manipulation.fonction import *
pile=Pile()
pile.read_file()
print("Longueur de la pile :",pile.nbelt())
pile.print_list()
r="Okok"
print("\nLe resultat de la recherche de",r,"est :",pile.search_elt(r))
print("\nLa liste trie est :")
print("Longueur de la pile :",pile.nbelt())
pile=pile.sort_list()
pile.print_list()
print("\n(C) 2022 By MMCJ/INF-L1")
