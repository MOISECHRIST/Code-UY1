from Tri import *
##########################################################
#1 Recherche Sequentielle
def seqSearch(tab,elt):
	trouve=False
	i=0
	while(tab[i]!=elt)and(i<len(tab)):
		i+=1
	if tab[i]==elt:
		trouve=True
	return trouve
##########################################################
#2 Recherche Dichotomique version iterative
def dichSearch(tab,elt):
	d=0
	f=len(tab)-1
	m=(d+f)//2
	trouve=False
	TriRapide(tab,0,len(tab)-1)
	while(d<f)and(trouve is False):
		if elt>tab[m]:
			d=m+1
			m=(d+f)//2
		elif elt<tab[m]:
			f=m-1
			m=(d+f)//2
		elif elt==tab[m]:
			trouve=True
	return trouve
##########################################################
#3 Recherche Dichotomique version recurcive
def RecdichSearch(tab,elt,d=0,f=None):
	if f==None:
		f=len(tab)-1
	m=(d+f)//2
	trouve=False
	if (d<f)and(trouve is False):
		if elt>tab[m]:
			RecdichSearch(tab,elt,m+1,f)
		elif elt<tab[m]:
			RecdichSearch(tab,elt,d,m-1)
		elif elt==tab[m]:
			trouve=True
	return trouve

