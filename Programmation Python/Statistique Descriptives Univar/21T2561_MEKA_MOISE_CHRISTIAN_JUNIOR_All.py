'''
MEKA Moise Christian Junior
21T2561
'''
from math import sqrt

#Fonction pour arrondir
def tronquer(n,m=0):
    return float(f"{n:.{m}f}")

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
    if ind == n-1:
        return M1[0][ind]+(M1[1][ind]-M1[0][ind])*(T3[ind]-T3[ind-1])/((T3[ind]-T3[ind-1])+(T3[ind]-0))
    elif n==0:
        return M1[0][ind]+(M1[1][ind]-M1[0][ind])*(T3[ind]-0)/((T3[ind]-0)+(T3[ind]-T3[ind+1]))
    else :
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
    maxi=M1[1][-1]
    mini=M1[0][0]
    return maxi-mini

print("Voulez-vous réaliser une etude \n1) Sur variable discrete ?\n2) Sur variable continue ?")
rep=True
while rep:
    choix=int(input("Faire votre choix [1 ou 2] : "))
    if choix<=2 and choix>=1:
        rep=False

if choix==1:
    test=True
    while test:
        n=input("Entrer le nombre de valeurs distinctes de la serie : ")
        try:
            n=int(n)
            test=False
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
        if x<0:
            while x<0:
                print("la valeur doit etre positive...")
                x=int(input("Valeur : "))
    
        y=int(input("Effectif : "))
        if y<0:
            while y<0:
                print("la valeur doit etre positive...")
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
        print(tronquer(i,2),end="\t")
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
        print(tronquer(i,2),end="\t")
    print("\n")

    print("I-Valeurs de tendance centrale : \n")
    print("Mode = {}\nMoyenne = {}\nMédiane = {}\nQ1 = {}\nQ2 = {}\nQ3 = {}\n".format(mode(M,n),tronquer(moyenne(M,n),2),quartile(M,T2,n,0.5),quartile(M,T2,n,0.25),quartile(M,T2,n,0.5),quartile(M,T2,n,0.75)))
    print("II-Valeur de dispersion : \n")
    print("Variance = {}\nEcart-type = {}\nEIQ = {}\nEtendu = {}\nCoefficient de variation = {}".format(tronquer(variance(M,n),2),tronquer(ecartype(M,n),2),eiq(M,T2,n),etendu(M,n),tronquer(coeffvar(M,n),2)))
    print("\n") 
else :
    test=True
    while test:
        n=input("Entrer le nombre de classes de la serie : ")
        try:
            n=int(n)
            test=False
        except ValueError:
            print("Erreur de saisir")
            n=input("Entrer le nombre de classes de la serie : ")
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
        if x1<0:
            while x1<0:
                print("la valeur doit etre positive...")
                x1=int(input("Valeur Minimum : "))
        x2=int(input("Valeur Maximum : "))
        if x2<0:
            while x2<0:
                print("la valeur doit etre positive...")
                x2=int(input("Valeur Maximum : "))
        y=int(input("Effectif : "))
        if y<0:
            while y<0:
                print("la valeur doit etre positive...")
                y=int(input("Effectif : "))
        l1+=[x1]
        l2+=[x2]
        l3+=[y]
        i+=1

    M1+=[l1]
    M1+=[l2]
    M1+=[l3]
    c=[]
    i=0
    while i<n:
        c+=[(M1[1][i]+M1[0][i])/2]
        i+=1
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
        print(tronquer(i,2),end="\t")
    print("\n")

    print("di",end="\t")
    for i in T3:
        print(tronquer(i,2),end="\t")
    print("\n")

    print("Ni",end="\t")
    for i in T4:
        print(i,end="\t")
    print("\n")

    print("Fi",end="\t")
    for i in T5:
        print(tronquer(i,2),end="\t")
    print("\n")

    print("I-Valeurs de tendance centrale : \n")
    i=classe_modale(T3,n)
    print("Classe modale = [{} ; {}[".format(M1[0][i],M1[1][i]))
    print("Mode = {}\nMoyenne = {}\nMédiane = {}\nQ1 = {}\nQ2 = {}\nQ3 = {}\n".format(tronquer(mode2(M1,T3,n),2),tronquer(moyenne2(M1,n),2),tronquer(quartile2(M1,T5,n,0.5),2),tronquer(quartile2(M1,T5,n,0.25),2),tronquer(quartile2(M1,T5,n,0.5),2),tronquer(quartile2(M1,T5,n,0.75),2)))
    print("II-Valeur de dispersion : \n")
    print("Variance = {}\nEcart-type = {}\nEIQ = {}\nEtendu = {}\nCoefficient de variation = {}".format(tronquer(variance2(M1,n),2),tronquer(ecartype2(M1,n),2),tronquer(eiq2(M1,T5,n),2),etendu2(M1,n),tronquer(coeffvar2(M1,n),2)))
    print("\n") 
