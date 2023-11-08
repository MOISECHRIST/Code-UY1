from Manipulation.fonction import *
pile=Pile()
pile.read()
print("Longueur de la pile :",pile.nbelt())
pile.print_list()
r="Okok"
print("Le resultat de la recherche de",r,"est :",pile.search_elt(r))
print("\nLa liste trie est :")
print("Longueur de la pile :",pile.nbelt())
pile=pile.sort_list()
pile.print_list()
