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
    return a+sqrt(sigma2)*t
    
def borne_inf(a,sigma2,t):
    return a-sqrt(sigma2)*t

def print_serie(x,intitule=None):
    '''Cette fonction affiche une serie'''
    print(x)

def regression_lineaire_simple(x,y,n,t):
    '''Implémentation de la regression lineaire simple y=a+b*x\n
    Estimation des parametre par les MCO et la vraisemblance puis test de validation du modèle'''
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
    b=covariance/var_x
    a=moy_y-b*moy_x
    y_pred=droite(x,a,b)
    e=ecart_series(y,y_pred,n)
    e2=serie_carres(e)
    var_e=n*moyenne(e2,n)/(n-2)
    sigma_a2=var_e*(moyenne(x2,n)/(n*var_x))
    sigma_b2=var_e/(n*var_x)
    t_a=a/sqrt(sigma_a2)
    t_b=b/sqrt(sigma_b2)
    bsup_a=borne_sup(a,sigma_a2,t)
    bsup_b=borne_sup(b,sigma_b2,t)
    binf_a=borne_inf(a,sigma_a2,t)
    binf_b=borne_inf(b,sigma_b2,t)
    print(t_a)
    print(t_b)
    return a,b

if __name__=='__main__':
    '''Implémentation de la regression lineaire simple y=a+b*x\n
    Estimation des parametre par les MCO et la vraisemblance puis test de validation du modèle'''
    x=[3,4,6,7,9,10,9,11,12,13,15,4]
    y=[8,9,10,13,15,14,13,16,13,19,6,19]
    xi=linspace(3,15,100)
    n=12
    t=2.2281
    a1,b1=regression_lineaire_simple(x,y,n,t)
    yi=droite(x,a1,b1)
    x=[3,4,6,7,9,10,9,11,12,13]
    y=[8,9,10,13,15,14,13,16,13,19]
    n=10
    t=8
    a2,b2=regression_lineaire_simple(x,y,n,t)
    y2i=droite(x,a2,b2)
    plt.figure()
    plt.scatter(x,y,s=15)
    plt.plot(xi,yi,c='r')
    plt.plot(xi,y2i,c='g')
    plt.savefig("nuage_point.png")
    plt.show()
    
    