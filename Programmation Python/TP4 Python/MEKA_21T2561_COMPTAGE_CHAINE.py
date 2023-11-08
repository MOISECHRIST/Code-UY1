def Search(tab,elt):
	trouve=-1
	i=0
	while(i<len(tab)):
		if tab[i]==elt:
			trouve=i
			break
		i+=1
	return trouve

def compare(v,w):
	sum=0
	for i in range(len(v)):
		if w[i]==v[i]:
			sum+=1
		else:
			break
	return sum==len(v)

def Search_first(tab,elt):
	trouve=[]
	i=0
	while(i<len(tab)):
		if(tab[i]==elt):
			trouve+=[i]
		i+=1
	return trouve

def Occurence(M,T):
	first=Search_first(T,M[0])
	occ=0
	n=len(M)
	if len(first)>=1:
		for i in first:
			texte=[]
			if i+n<len(T):
				for j in range(n):
					texte+=T[i+j]
				occ+=compare(M,texte)
	return occ


TEXTE="MAMAN VA AU MARCHE; OUI AU MARCHE"
nom="MARCHE"
T = list(TEXTE)
N=list(nom)

occ = Occurence(N,T)
print(occ)