def lecture(n,m):
    mat=[]
    for i in range(n):
        line=[]
        for j in range(m):
            print("Entrer l'element ({},{}) :".format(i+1,j+1),end="")
            elt=input("")
            try:
                elt=float(elt)
            except TypeError:
                print("Erreur de saisie !!!\nLa valeur doit etre numerique...")
                print("Entrer l'element ({},{}) : ".format(i,j),end="")
                elt=input("")
                elt=float(elt)
            line+=[elt]
        mat+=[line]
    return mat

def nature_mat(mat,n,m):
    code={"Tri-Sup":0,"Tri-Inf":0}
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
def max_mat(mat,n):
    new=[]
    for i in range(n):
        new+=[max(mat[i][:])]
    return max(new)
def affiche_diag(mat,n):
    taille=len(str(max_mat(mat,n)))
    for i in range(n):
        for j in range(i+1):
            if i==j:
                print(f"{mat[i][j]:{taille}}")
            elif j<i:
                vide=" "
                print(f"{vide:{taille}}",end='\t')

def affiche_trisup(mat,n,m):
    taille=len(str(max_mat(mat,n)))
    for i in range(n):
        for j in range(m):
            if i<=j:
                print(f'{mat[i][j]:{taille}}',end="\t")
            else:
                vide=" "
                print(f'{vide:{taille}}',end="\t")
        print()

def affiche_trinf(mat,n,m):
    taille=len(str(max_mat(mat,n)))
    for i in range(n):
        for j in range(i+1):
            print(f'{mat[i][j]:{taille}}',end="\t")
        print()

def affiche_mat(mat,n,m):
    print_mat=""
    for i in range(n):
        for j in range(m):
            print_mat+=str(mat[i][j])+"\t"
        print_mat+="\n"
    print(print_mat)

def afficher(mat,n,m):
    nat=nature_mat(mat,n,m)
    if nat=='00':
        print("Matrice quelcoque : \n")
        affiche_mat(mat,n,m)
    elif nat=='01':
        print("Matrice triangulaire Inferieure : \n")
        affiche_trinf(mat,n,m)
    elif nat=='10':
        print("Matrice Triangulaire Superieure : \n")
        affiche_trisup(mat,n,m)
    else :
        print("Matrice diagonale : \n")
        affiche_diag(mat,n)

def affiche_systeme(mat,b,n,m):
    print_mat=""
    for i in range(n):
        for j in range(m):
            if j<m-1:
                print_mat+="("+str(mat[i][j])+")*X{} + ".format(j+1)
            else :
                print_mat+="("+str(mat[i][j])+")*X{} = ".format(j+1)
        print_mat+=str(b[i][0])+"\n"
    print(print_mat)

def reduction_mat(mat,b,n,m):
    if (mat[0][0]!=0):
        deg=min(n,m)
        for k in range(deg):
            for i in range(k+1,n):
                pivot=mat[i][k]/mat[k][k]
                for j in range(m):
                    mat[i][j]=mat[i][j]-pivot*mat[k][j]
                b[i][0]=b[i][0]-pivot*b[k][0]

def resolution(mat,b,n,m):
    x={}
    fin=True
    for i in range(n):
        x[i]=0
    if mat[n-1][n-1]!=0:
        x[n-1]=b[n-1][0]/mat[n-1][n-1]
        for i in range(n-2,-1,-1):
            if mat[i][i]!=0:
                for j in range(i+1,m):
                    x[i]+=x[j]*mat[i][j]
                x[i]=(b[i][0]-x[i])/mat[i][i]
            else:
                print("Le systeme n'admet pas un {}-uplet de solution...".format(n))
                fin=False
                break
    else:
        fin=False
        print("Le systeme n'admet pas un {}-uplet de solution...".format(n))
    if fin==True:
        return x
    else:
        return {}

def resolution_diag(mat,b,n):
    x={}
    fin=True
    for i in range(n):
        if mat[i][i]!=0:
            x[i]=b[i][0]/mat[i][i]
        else:
            print("Le systeme n'admet pas un {}-uplet de solution...".format(n))
            fin=False
            break
    if fin==True:
        return x
    else:
        return {}

def resolution_inf(mat,b,n,m):
    reduction_mat(mat,b,n,m)
    x=resolution_diag(mat,b,n)
    return x



if __name__=="__main__":
    n=input("Entrer nombre de ligne : ")
    try:
        n=int(n)
    except ValueError:
        print("Erreur de saisie...")
        n=input("Entrer nombre de ligne : ")
        n=int(n)
    m=input("Entrer nombre de colonne : ")
    try:
        m=int(m)
    except ValueError:
        print("Erreur de saisie...")
        m=input("Entrer nombre de colonne : ")
        m=int(m)
    print("Lecture matrice :")
    mat=lecture(n,m)
    print()
    afficher(mat,n,m)
    print("\nLecture second membre :\n")
    b=lecture(n,1)
    print("Le systeme obtenu est : \n")
    affiche_systeme(mat,b,n,m)
    if nature_mat(mat,n,m)=="00":
        reduction_mat(mat,b,n,m)
        x=resolution(mat,b,n,m)
    elif nature_mat(mat,n,m)=="01":
        x=resolution_inf(mat,b,n,m)
    elif nature_mat(mat,n,m)=="10":
        x=resolution(mat,b,n,m)
    else:
        x=resolution_diag(mat,b,n)
    
    print("Le systeme reduit est : \n")
    affiche_systeme(mat,b,n,m)
    i=0
    if x != {}:
        print("Les solutions du systeme : \n")
        for value in x.values():
            i+=1
            print("X{}={:.2f}".format(i,value))