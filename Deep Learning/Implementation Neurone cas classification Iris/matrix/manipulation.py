#from affichage import *

#Fonction pour afficher la matrice
def affiche_mat(mat):
    m=len(mat[0][:])
    n=len(mat)
    max_len=len(str(max(mat)))
    for i in range(n):
        for j in range(m):
            print(f'{mat[i][j]:{max_len}}',end='\t')
        print()
#Ce package contiendra toutes les fonctions pour la manipulation des matrices 

#Fonction pour calculer la somme d'une matrice avec un scalaire
def sum_scal(mat1,scal):
    m=len(mat1[0][:])
    n=len(mat1)
    result=[]
    for i in range(n):
        line=[]
        for j in range(m):
            line+=[mat1[i][j]+scal]
        result+=[line]
    return result

#Fonction pour calculer la somme d'un vecteur avec un scalaire
def sum_vect1(vect,scal):
    n=len(vect)
    result=[]
    for i in range(n):
        result+=[vect[i]+scal]
    return result


#Fonction pour calculer la somme de deux matrices
def sum_mat(mat1,mat2):
    result=[]
    if len(mat1[0][:])==len(mat2[0][:]) and len(mat1)==len(mat2):
        m=len(mat1[0][:])
        n=len(mat1)
        for i in range(n):
            line=[]
            for j in range(m):
                line+=[mat1[i][j]+mat2[i][j]]
            result+=[line]
    else:
        print("La somme est impossibles. Les matrices n'ont pas la meme dimension")
    return result

#Fonction pour calculer le produit d'une matrice et un scalaire
def prod_scal(mat,scal):
    result=[]
    m=len(mat[0][:])
    n=len(mat)
    for i in range(n):
        line=[]
        for j in range(m):
            line+=[mat[i][j]*scal]
        result+=[line]
    return result


#Fonction pour calculer la transposé d'une matrice
def transpose(mat):
    result=[]
    m=len(mat[0][:])
    n=len(mat)
    for j in range(m):
        line=[]
        for i in range(n):
            line+=[mat[j][i]]
        result+=[line]
    return result

#Fonction qui retourne la nature de la matrice :
#(Diagonale ='11'; Triangulaire_Sup = '10'; Triangulaire_inf = '01'; Quelconque = '00')
def nature_mat(mat):
    code={"Tri-Sup":0,"Tri-Inf":0}
    m=len(mat[0][:])
    n=len(mat)
    if(n==m):
        line=(n-1)*n/2
        col=(m-1)*m/2
        nb_line=nb_col=0
        for i in range(1,n):
            for j in range(i):
                if mat[i][j]==0:
                    nb_line+=1
                else:
                    break
        for i in range(n):
            for j in range(i+1,m):
                if mat[i][j]==0:
                    nb_col+=1
                else:
                    break
        if line==nb_line:
            code["Tri-Sup"]=1
        if col==nb_col:
            code["Tri-Inf"]=1
    return "{}{}".format(code["Tri-Sup"],code["Tri-Inf"])
    

#Fonction pour calculer l'elimination de Gauss
def reduction_mat(mat):
    m=len(mat[0][:])
    n=len(mat)
    deg=min(n,m)
    for k in range(deg):
        if (mat[k][k]!=0):
            for i in range(k+1,n):
                pivot=mat[i][k]/mat[k][k]
                for j in range(k,m):
                    mat[i][j]=mat[i][j]-pivot*mat[k][j]
    return mat


#Fonction pour calculer le produit de deux matrices 
def prod_mat(mat1,mat2):
    result=[]
    n=len(mat2)
    m=len(mat1[0][:])
    if n==m:
        for i in range(n):
            line=[]
            for j in range(m):
                s=0
                for k in range(m):
                    s+=mat1[i][k]*mat2[k][j]
                line+=[s]
            result+=[line]
    else :
        print("Le produit est impossibles. Les matrices n'ont pas les bonnes dimensions")
    return result

#Fonction pour calculer le produit d'une matrice et un vecteur
def prod_vect(mat1,vect):
    result=[]
    n=len(vect)
    m=len(mat1[0][:])
    nb=len(mat1)
    if n==m:
        for i in range(nb):
            s=0
            for k in range(m):
                s+=mat1[i][k]*vect[k]
            result+=[s]
    else :
        print("Le produit est impossibles. La matrice et le vecteur n'ont pas les bonnes dimensions")
    return result



if __name__=="__main__":
    mat1=[[1,2],[5,6],[7,8]]
    mat2=[[5,6],[7,8]]
    print("Matrice 1")
    affiche_mat(mat1)
    '''print("Matrice 2")
    affiche_mat(mat2)
    print("Somme matrice")
    affiche_mat(sum_mat(mat1,mat2))
    print("Produit scalaire")
    affiche_mat(prod_scal(mat2,10))
    print("Produit matriciel")
    affiche_mat(prod_mat(mat1,mat2))
    print("Reduction")
    affiche_mat(reduction_mat(mat2))'''
    X=[5,6]
    print(prod_vect(mat1,X))