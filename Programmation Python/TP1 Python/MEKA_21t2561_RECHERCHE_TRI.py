#1 Fonction de recherche
def Search(tab,elt):
	trouve=-1
	i=0
	while(tab[i]!=elt)and(i<len(tab)):
		i+=1
	if tab[i]==elt:
		trouve=i
	return trouve

#2.1 Fonction tri insertion
def TriInsertion(tab):
	n=len(tab)
	for i in range(1,n):
		tmp=tab[i]
		k=i-1
		while k>=0 and tmp<tab[k]:
			tab[k+1]=tab[k]
			k-=1
		tab[k+1]=tmp

#2.2 Fonction tri bulle
def TriBulle(tab):
	echange=True
	while(echange):
		echange=False
		for i in range(len(tab)-1):
			if tab[i]>tab[i+1]:
				tab[i],tab[i+1]=tab[i+1],tab[i]
				echange=True

#2.3 Fonction tri fusion
def TriFusion(tab):
	if len(tab)>1:
		m=len(tab)//2
		gauche=tab[:m]
		droite=tab[m:]
		TriFusion(gauche)
		TriFusion(droite)
		i=j=k=0
		while(i<len(gauche))and(j<len(droite)):
			if gauche[i]<droite[j]:
				tab[k]=gauche[i]
				i+=1
			else:
				tab[k]=droite[j]
				j+=1
			k+=1
		while i<len(gauche):
			tab[k]=gauche[i]
			i+=1
			k+=1
		
		while j<len(droite):
			tab[k]=droite[j]
			j+=1
			k+=1
		
#2.4 Fonction tri bitonique
def fusion_bitonique(tab,start_tab,len_tab,direction):
	if len_tab>1:
		for i in range(len_tab):
			if direction:
				milieu=(len_tab-1)//2
				if tab[i]>tab[i+milieu]:
					tab[i],tab[i+milieu]=tab[i+milieu],tab[i]
			else :
				if tab[i]<tab[i+milieu]:
					tab[i],tab[i+milieu]=tab[i+milieu],tab[i]
		fusion_bitonique(tab,start_tab,milieu,direction)
		fusion_bitonique(tab,milieu+1,len_tab,direction)

def TriBitonique(tab,start_tab,len_tab,direction=True):
	if(len_tab>1):
		milieu=(start_tab+len_tab-1)//2
		TriBitonique(tab,start_tab,milieu,direction)
		TriBitonique(tab,milieu+1,len_tab,not direction)
		fusion_bitonique(tab,start_tab,len_tab,direction)

#3 Recherche Dichotomique
def dichSearch(tab,elt):
	d=0
	f=len(tab)-1
	m=(d+f)//2
	trouve=-1
	TriInsertion(tab)
	while(d<f)and(elt!=tab[m]):
		if elt>tab[m]:
			d=m+1
			m=(d+f)//2
		elif elt<tab[m]:
			f=m-1
			m=(d+f)//2
	if(elt==tab[m]):
		trouve=m
	return trouve


if __name__=="__main__":
	tab=[1,0,14,5,7,2,3]
	print("Tableau de depart :\n",tab)
	elt=5
	print("Recherche de {} donne : {} ".format(elt,Search(tab,elt)))
	TriInsertion(tab)
	print("Insertion :\n",tab)
	tab=[1,0,14,5,7,2,3]
	print("Tableau de depart :\n",tab)
	TriBulle(tab)
	print("Bulle :\n",tab)
	print("Recherche de {} donne : {} ".format(elt,dichSearch(tab,elt)))
	tab=[1,0,14,5,7,2,3]
	print("Tableau de depart :\n",tab)
	TriFusion(tab)
	print("Fusion :\n",tab)
	TriBitonique(tab,0,len(tab)-1)
	print("Bitonique :\n",tab)
