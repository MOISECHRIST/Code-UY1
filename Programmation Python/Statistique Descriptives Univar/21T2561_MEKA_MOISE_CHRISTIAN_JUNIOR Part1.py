from math import sqrt

#Fonction pour calculer le mode
def mode(M,n):
    mod=M[1][0]
    indMod=0
    i=1
    while i<n:
        if M[1][i]>mod:
            mod=M[1][i]
            indMod=i
        i+=1
    return M[0][indMod]

#Fonction pour calculer la moyenne
def moyenne(M,n):
    eff=0
    sum=0
    i=0
    while i<n:
        eff+=M[1][i]
        sum+=M[1][i]*M[0][i]
        i+=1
    return sum/eff

#Fonction pour calculer la variance
def variance(M,n):
    eff=0
    sum=0
    i=0
    moy=moyenne(M,n)
    while i<n:
        eff+=M[1][i]
        sum+=M[1][i]*((M[0][i]-moy)**2)
        i+=1
    return sum/eff

#Fonction pour calculer les quartiles
def quartile(M,T2,n,q=0.5):
    i=0
    while i<n and T2[i]<q:
        i+=1
    return M[0][i]

#Fonction pour calculer l'ecart type
def ecartype(M,n):
    return sqrt(variance(M,n))

#Fonction pour calculer EIQ
def eiq(M,T2,n):
    q3=quartile(M,T2,n,0.75)
    q1=quartile(M,T2,n,0.25)
    return q3-q1

#Fonction pour calcluer le coefficient de variation
def coeffvar(M,n):
    moy=moyenne(M,n)
    s=ecartype(M,n)
    return s/moy

#Fonction pour calcluer le minimum
def minimum(M,n):
    i=1
    m=M[0][0]
    while i<n:
        if m>M[0][i]:
            m=M[0][i]
        i+=1
    return m

#Fonction pour calcluer le maximum
def maximum(M,n):
    i=1
    m=M[0][0]
    while i<n:
        if m<M[0][i]:
            m=M[0][i]
        i+=1
    return m

#Fonction pour calcluer l'etendue
def etendu(M,n):
    maxi=maximum(M,n)
    mini=minimum(M,n)
    return maxi-mini

n=input("Entrer le nombre de valeurs distinctes de la serie : ")
try:
    n=int(n)
except ValueError:
    print("Erreur de saisir")
    n=input("Entrer le nombre de valeurs distinctes de la serie : ")
    n=int(n)

print("Entrer la serie :")
M=[]
l1=[]
l2=[]
i=0

while i<n:
    print("[{}]".format(i+1))
    x=int(input("Valeur : "))
    y=int(input("Effectif : "))
    l1+=[x]
    l2+=[y]
    i+=1

M+=[l1]
M+=[l2]

print("\nLa serie entree est :\n")
print("xi",end="\t")
for xi in M[0][:]:
    print(xi,end="\t")
print("\n")
print("ni",end="\t")
for ni in M[1][:]:
    print(ni,end="\t")
print("\n")

T1=[]
sum=0
for i in M[1][:]:
    sum+=i
    T1+=[sum]

f=[]
for i in M[1][:]:
    f+=[i/sum]
print("fi",end="\t")
for i in f:
    print(round(i,2),end="\t")
print("\n")
print("Ni",end="\t")
for i in T1:
    print(i,end="\t")
print("\n")

T2=[]
for i in T1:
    T2+=[i/sum]
print("Fi",end="\t")
for i in T2:
    print(round(i,2),end="\t")
print("\n")

print("I-Valeurs de tendance centrale : \n")
print("Mode = {}\nMoyenne = {}\nMédiane = {}\nQ1 = {}\nQ2 = {}\nQ3 = {}\n".format(mode(M,n),round(moyenne(M,n),2),quartile(M,T2,n,0.5),quartile(M,T2,n,0.25),quartile(M,T2,n,0.5),quartile(M,T2,n,0.75)))
print("II-Valeur de dispersion : \n")
print("Variance = {}\nEcart-type = {}\nEIQ = {}\nEtendu = {}\nCoefficient de variation = {}".format(round(variance(M,n),2),round(ecartype(M,n),2),eiq(M,T2,n),etendu(M,n),round(coeffvar(M,n),2)))
print("\n") 