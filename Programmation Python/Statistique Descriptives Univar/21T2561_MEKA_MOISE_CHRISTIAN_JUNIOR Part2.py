from math import sqrt

#Fonction pour calculer le Mode
def classe_modale(T3,n):
    mod=T3[0]
    ind=0
    i=0
    while i<n:
        if T3[i]>mod:
            ind=i
            mod=T3[i]
        i+=1
    return ind
def mode2(M1,T3,n):
    ind=classe_modale(T3,n)
    return M1[0][ind]+(M1[1][ind]-M1[0][ind])*(T3[ind]-T3[ind-1])/((T3[ind]-T3[ind-1])+(T3[ind]-T3[ind+1]))


#Fonction pour calculer la Moyenne
def moyenne2(M1,n):
    sum=0
    eff=0
    i=0
    while i<n:
        sum+=((M1[0][i]+M1[1][i])/2)*M1[2][i]
        eff+=M1[2][i]
        i+=1
    return sum/eff

#Fonction pour calculer le quartile
def quartile2(M1,T5,n,q=0.5):
    i=0
    while(i<n and T5[i]<q):
        i+=1
    if i>0:
        return M1[0][i]+(M1[1][i]-M1[0][i])*(q-T5[i-1])/(T5[i]-T5[i-1])
    else :
        return M1[0][i]

#Fonction pour calculer la variance 
def variance2(M1,n):
    sum=0
    eff=0
    i=0
    while i<n:
        sum+=(((M1[0][i]+M1[1][i])/2)*((M1[0][i]+M1[1][i])/2))*M1[2][i]
        eff+=M1[2][i]
        i+=1
    return (sum/eff)-moyenne2(M1,n)**2

#Fonction pour calculer l'ecart type
def ecartype2(M,n):
    return sqrt(variance2(M,n))

#Fonction pour calculer EIQ
def eiq2(M1,T5,n):
    q3=quartile2(M1,T5,n,0.75)
    q1=quartile2(M1,T5,n,0.25)
    return q3-q1

#Fonction pour calcluer le coefficient de variation
def coeffvar2(M1,n):
    moy=moyenne2(M1,n)
    s=ecartype2(M1,n)
    return s/moy

#Fonction pour calcluer le minimum
def minimum2(M1,n):
    i=1
    m=M1[0][0]
    while i<n:
        if m>M1[0][i]:
            m=M1[0][i]
        i+=1
    return m

#Fonction pour calcluer le maximum
def maximum2(M1,n):
    i=1
    m=M1[0][0]
    while i<n:
        if m<M1[2][i]:
            m=M1[2][i]
        i+=1
    return m

#Fonction pour calcluer l'etendue
def etendu2(M1,n):
    maxi=maximum2(M1,n)
    mini=minimum2(M1,n)
    return maxi-mini

n=input("Entrer le nombre de classes de la serie : ")
try:
    n=int(n)
except ValueError:
    print("Erreur de saisir")
    n=input("Entrer le nombre de valeurs distinctes de la serie : ")
    n=int(n)

print("Entrer la serie :")
M1=[]
l1=[]
l2=[]
l3=[]
i=0

while i<n:
    print("[{}]".format(i+1))
    x1=int(input("Valeur Minimum : "))
    x2=int(input("Valeur Maximum : "))
    y=int(input("Effectif : "))
    l1+=[x1]
    l2+=[x2]
    l3+=[y]
    i+=1

M1+=[l1]
M1+=[l2]
M1+=[l3]
c=[]
for i in range(n):
    c+=[(M1[1][i]+M1[0][i])/2]
print("\nLa serie entree est :\n")
print("xi",end="\t")
for i in M1[0][:]:
    print(i,end="\t")
print("\n")
print("xi+1",end="\t")
for i in M1[1][:]:
    print(i,end="\t")
print("\n")
print("ci",end="\t")
for i in c:
    print(i,end="\t")
print("\n")
print("ni",end="\t")
for i in M1[2][:]:
    print(i,end="\t")
print("\n")

T3=[]
i=0
while i<n:
    T3+=[M1[2][i]/(M1[1][i]-M1[0][i])]
    i+=1
T4=[]
sum=0
for i in M1[2][:]:
    sum+=i
    T4+=[sum]
f=[]
for i in M1[2][:]:
    f+=[i/sum]
T5=[]
for i in T4:
    T5+=[i/sum]

print("fi",end="\t")
for i in f:
    print(round(i,2),end="\t")
print("\n")

print("di",end="\t")
for i in T3:
    print(round(i,2),end="\t")
print("\n")

print("Ni",end="\t")
for i in T4:
    print(i,end="\t")
print("\n")

print("Fi",end="\t")
for i in T5:
    print(round(i,2),end="\t")
print("\n")

print("I-Valeurs de tendance centrale : \n")
print("Classe modale = [{} ; {}[".format(M1[0][classe_modale(T3,n)],M1[1][classe_modale(T3,n)]))
print("Mode = {}\nMoyenne = {}\nMédiane = {}\nQ1 = {}\nQ2 = {}\nQ3 = {}\n".format(round(mode2(M1,T3,n),2),round(moyenne2(M1,n),2),round(quartile2(M1,T5,n,0.5),2),round(quartile2(M1,T5,n,0.25),2),round(quartile2(M1,T5,n,0.5),2),round(quartile2(M1,T5,n,0.75),2)))
print("II-Valeur de dispersion : \n")
print("Variance = {}\nEcart-type = {}\nEIQ = {}\nEtendu = {}\nCoefficient de variation = {}".format(round(variance2(M1,n),2),round(ecartype2(M1,n),2),round(eiq2(M1,T5,n),2),etendu2(M1,n),round(coeffvar2(M1,n),2)))
print("\n") 