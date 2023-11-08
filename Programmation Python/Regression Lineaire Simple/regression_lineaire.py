from math import sqrt
from matplotlib import pyplot as plt

def droite(x,a,b):
    '''Cette fonction prend en paramètre une serie de valeurs x\n
    et retourne une serie de valeur y=a+b*x'''
    y=[]
    for i in x:
        y+=[a+i*b]
    return y

def linspace(mi:int,ma:int,nb_elt=1):
    '''Cette fonction cree une serie de valeur uniformement espacé entre deux valeurs'''
    taille=ma-mi
    try:
        pas=taille/nb_elt
    except:
        print("Le nombre d'element doit etre > 0")
        return [mi,ma]
    i=mi
    line=[]
    while(i<ma):
        line+=[i]
        i+=pas
    line+=[ma]
    return line

def moyenne(x,n:int):
    '''Cette fonction retourne la moyenne d'une serie x de taille n'''
    moy=0
    for i in x:
        moy+=i
    return moy/n

def serie_carres(x):
    '''Cette fonction retourne la serie des carres d'une serie x'''
    x2=[]
    for i in x:
        x2+=[i*i]
    return x2

def serie_prod(x,y,n:int):
    '''Cette fonction retourne la serie des produits de deux series x et y de taille n'''
    i=0
    xy=[]
    while (i<n):
        xy+=[x[i]*y[i]]
        i+=1
    return xy

def variance(x,n):
    '''Cette fonction retourne la variance d'une serie x de taille n'''
    mcx=serie_carres(x)
    mcx=moyenne(mcx,n)
    moy=moyenne(x,n)
    moy=moy*moy
    return mcx-moy

def ecart_type(x,n):
    '''Cette fonction retourne l'ecart type d'une serie x de taille n'''
    return sqrt(variance(x,n))

def cov(x,y,n):
    '''Cette fonction retourne la covariance de deux series x et y de taille n'''
    c=serie_prod(x,y,n)
    c=moyenne(c,n)
    x_=moyenne(x,n)
    y_=moyenne(y,n)
    return c-x_*y_

def ecart_series(y_reel,y_pred,n):
    '''Cette fonction calcul les erreurs du modele de regression'''
    erreur=[]
    i=0
    while(i<n):
        erreur+=[y_reel[i]-y_pred[i]]
        i+=1
    return erreur

def borne_sup(a,sigma2,t):
    '''Cette fonction retourne la borne superieure de l'intervalle de confiance d'un parametre'''
    return a+sqrt(sigma2)*t
    
def borne_inf(a,sigma2,t):
    '''Cette fonction retourne la borne inferieure de l'intervalle de confiance d'un parametre'''
    return a-sqrt(sigma2)*t

def print_serie(x,intitule=None):
    '''Cette fonction affiche une serie'''
    print(intitule,end="\t")
    for i in x:
        if type(i)==str:
            print(f"{i}",end="\t")
        else:
            print(f"{round(i,3):6}",end='\t')
    print()

def regression_lineaire_simple(x,y,n,t,f,c1,c2):
    '''Implémentation de la regression lineaire simple y=a+b*x\n
    Estimation des parametre par les MCO et test de validation du modèle'''
    x2=serie_carres(x)
    y2=serie_carres(y)
    xy=serie_prod(x,y,n)
    moy_x=moyenne(x,n)
    var_x=variance(x,n)
    ecartype_x=sqrt(var_x)
    moy_y=moyenne(y,n)
    var_y=variance(y,n)
    ecartype_y=sqrt(var_y)
    covariance=cov(x,y,n)
    coeff_cor=covariance/(sqrt(var_x)*sqrt(var_y))
    b=covariance/var_x
    a=moy_y-b*moy_x
    y_pred=droite(x,a,b)
    e=ecart_series(y,y_pred,n)
    e2=serie_carres(e)
    var_e=n*moyenne(e2,n)/(n-2)
    sigma_a2=var_e*(moyenne(x2,n)/(n*var_x))
    sigma_b2=var_e/(n*var_x)
    t_a=abs(a/sqrt(sigma_a2))
    t_b=abs(b/sqrt(sigma_b2))
    bsup_a=borne_sup(a,sigma_a2,t)
    bsup_b=borne_sup(b,sigma_b2,t)
    binf_a=borne_inf(a,sigma_a2,t)
    binf_b=borne_inf(b,sigma_b2,t)
    coeff_deter=(n*var_y-(n-2)*var_e)/(n*var_y)
    print_serie(x,"Xi")
    print_serie(y,"Yi")
    print_serie(x2,"Xi2")
    print_serie(y2,"Yi2")
    print_serie(xy,"Xi*Yi")
    print_serie(y_pred,"ypi")
    print_serie(e,"ei")
    print_serie(e2,"ei2")

    print("\n1- Statistiques descriptives :")
    print("\tX\t  Y")
    print("Moy : {}\t{}\nVar : {}\t{}\nstd : {}\t{}\nCov : {}\nCoeff Corr : {}".format(round(moy_x,3),round(moy_y,3),round(var_x,3),round(var_y,3),round(ecartype_x,3),round(ecartype_y,3),round(covariance,3),round(coeff_cor,3)))

    print("\n2- Statistiques de regression :")
    print(f"Coeff determination : {round(coeff_deter*100,3)}%\nObservation : {n}")
    print("IC variance des erreurs du modele : [{};{}]".format(round((n-2)*var_e/c1,3),round((n-2)*var_e/c2,3)))
    print(f"Donc {round(coeff_deter*100,3)}% d'une note de l'Epreuve B est expliqué par une note de l'Epreuve A")
    
    print("\n3-ANOVA :")
    sce=n*var_y-(n-2)*var_e
    f_stat=sce/var_e
    if f_stat>f:
        test="*"
    else:
        test=""
    line1=[1,sce,sce,f_stat,f,test]
    line2=[n-2,(n-2)*var_e,var_e]
    line3=[n-1,n*var_y]
    print("\t    ddl\tSS\tMS\tF calcule F Theo")
    print_serie(line1,"predict")
    print_serie(line2,"erreurs")
    print_serie(line3,"total")
    print("\n* : le parametre estime est significativement different de zero (risque=5%)")
    
    print("\n4- Estimation des parametres du modele :")
    if t_a>t:
        test="*"
    else:
        test=""
    line1=[a,sqrt(sigma_a2),t_a,t,binf_a,bsup_a,test]
    if t_b>t:
        test="*"
    else:
        test=""
    line2=[b,sqrt(sigma_b2),t_b,t,binf_b,bsup_b,test]
    print("\t Coeff\t std\t t-Stat\tt-theo\t BInf\t BSup")
    print_serie(line1,"Const")
    print_serie(line2,"X")
    print("\n* : le parametre estime est significativement different de zero (risque=5%)")
    
    print("\n5-Conclusion :")
    if t_b<=t:
        print(f"On a {round(t_b,3)}<={round(t,3)}. Donc avec une confiance de 95%,\nnous pouvons affirmer que les notes de l'Epreuve A n'explique pas lineairement celle de l'Epreuve B\nCe resultat est aussi observe avec la valeur de F-Stat < F-Theo ({round(f_stat,3)}<{f})\n")
    else :
        print(f"On a {round(t_b,3)}>{round(t,3)}. Donc avec un risque de 5% de se tromper,\nnous pouvons affirmer que les notes de l'Epreuve A explique lineairement celle de l'Epreuve B\nCe resultat est aussi observe avec la valeur de F-Stat > F-Theo ({round(f_stat,3)}>{f})\n")
    return a,b

if __name__=='__main__':
    '''Implémentation de la regression lineaire simple y=a+b*x\n
    Estimation des parametre par les MCO et la vraisemblance puis test de validation du modèle'''
    print("##########################################################################################################")
    print("\nImplémentation avec les deux stagiaires\n")
    x=[3,4,6,7,9,10,9,11,12,13,15,4]
    y=[8,9,10,13,15,14,13,16,13,19,6,19]
    xi=linspace(3,15,100)
    plt.figure(figsize=(15,10))
    plt.scatter(x,y,s=25)
    n=12
    t=2.22813885198627
    f=4.96
    c1=20.48832
    c2=3.2470
    a1,b1=regression_lineaire_simple(x,y,n,t,f,c1,c2)
    yi=droite(xi,a1,b1)
    x=[3,4,6,7,9,10,9,11,12,13]
    y=[8,9,10,13,15,14,13,16,13,19]
    n=10
    t=2.30600413520417
    f=5.32
    c1=17.5345
    c2=2.1797
    print("##########################################################################################################")
    print("\nImplémentation sans les deux stagiaires\n")
    a2,b2=regression_lineaire_simple(x,y,n,t,f,c1,c2)
    y2i=droite(xi,a2,b2)
    plt.plot(xi,yi,c='r')
    plt.plot(xi,y2i,c='g',ls=':')
    plt.xlabel("Epreuve A")
    plt.ylabel("Epreuve B")
    plt.title("Nuage de point des notes des epreuves A et B")
    plt.legend(["nuage","Y=12+0.11X","Y=5.47+0.9X"],loc='lower center',ncol=3)
    plt.savefig("nuage_point.png")
    plt.close()