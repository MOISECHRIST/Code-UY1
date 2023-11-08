#Methode de tri des tableaux

############################################################
#1 Tri Selection
#Fonction tri selection
def TriSelection(tab):
	for i in range(len(tab)-1):
		mini=i
		for j in range(i+1,len(tab)):
			if tab[j]<tab[mini]:
				mini=j
		tab[i],tab[mini]=tab[mini],tab[i]

############################################################
#2 Tri Rapide
#Fonction partition
def partition(tab,d,f):
	pivot=tab[f]
	ind=d
	for i in range(d,f):
		if tab[i]<pivot:
			tab[i],tab[ind]=tab[ind],tab[i]
			ind+=1
	tab[f],tab[ind]=tab[ind],tab[f]
	return ind
#Fonction de trie
def TriRapide(tab,d,f):
	if d<f:
		m=partition(tab,d,f)
		TriRapide(tab,d,m-1)
		TriRapide(tab,m+1,f)

#############################################################
#3 Tri Insertion
#Fonction tri insertion
def TriInsertion(tab):
	for i in range(1,len(tab)):
		tmp=tab[i]
		k=i-1
		while k>=0 and tmp<tab[k]:
			tab[k+1]=tab[k]
			k-=1
		tab[k+1]=tmp

###########################################################
#4 Trie Bulle
#Fonction tri bulle
def TriBulle(tab):
	echange=True
	while(echange):
		echange=False
		for i in range(len(tab)-1):
			if tab[i]>tab[i+1]:
				tab[i],tab[i+1]=tab[i+1],tab[i]
				echange=True
