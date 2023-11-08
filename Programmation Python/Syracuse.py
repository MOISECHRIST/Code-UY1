def Syracuse(n):
	if n==0:
		return 10;
	if (n%2==0):
		return (Syracuse(n-1)/2)
	else:
		return (3*Syracuse(n-1)+1)

n=input("Entrer un entier : ")
try :
	n=int(n)
except :
	print("Erreur de saisie")
	n=input("Entrer un entier : ")
	n=int(n)
print("Syracuse({})={}".format(n,Syracuse(n)))
		
