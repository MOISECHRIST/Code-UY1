#Ce module comporte toutes les fonction d'affichage des matrices

#Fonction pour afficher la matrice
def affiche_mat(mat):
    m=len(mat[0][:])
    n=len(mat)
    max_len=len(str(max(mat)))
    for i in range(n):
        for j in range(m):
            print(f'{mat[i][j]:{max_len}}',end='\t')
        print()