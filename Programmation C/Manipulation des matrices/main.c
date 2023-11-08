#include <stdio.h>
#include <stdlib.h>
#include "fonctions.h"
int main()
{
    float M1[100][100],M2[100][100],R[100][100];
    int n,choix;
    printf("\n\t---Bienvenu dans le programme de manipulation des matrices---\n");
    printf("\nEntrer l'ordre des matrices carrées a manipuler : ");
    scanf("%d",&n);
    while (n<=0)
    {
        printf("Erreur de saisie entrer\nReentrer l'ordre des matrices carrées a manipuler : ");
        scanf("%d",&n);
    }
    printf("\n1-Somme de deux matrices \n2-Produit de deux matrices \n3-Transposé d'une matrice \n4-Quitter le programme\n\n");
    printf("Faire votre choix : ");
    scanf("%d",&choix);
    while ((choix<1)|(choix>4))
	{
        printf("\nChoix non disponibre\nVeillez reessayer svp : ");
        scanf("%d",&choix);
	}
	while (choix!=4)
	{
        if (choix==1)
        {
                system("cls");
                printf("\nEntrer les elements de la premiere matrice :\n");
                SaisirMat(M1,n);
                AfficheMat(M1,n);
                printf("\nEntrer les elements de la seconde matrice :\n");
                SaisirMat(M2,n);
                AfficheMat(M2,n);
                printf("\nLa somme des deux matrices est :\n");
                SommeMat(M1,M2,n,R);
                AfficheMat(R,n);
        }
        if (choix==2){
                system("cls");
                printf("\nEntrer les elements de la premiere matrice :\n");
                SaisirMat(M1,n);
                AfficheMat(M1,n);
                printf("\nEntrer les elements de la seconde matrice :\n");
                SaisirMat(M2,n);
                AfficheMat(M2,n);
                printf("\nLe produit des deux matrice est :\n");
                ProduitMat(M1,M2,n,R);
                AfficheMat(R,n);
            }
        if (choix==3){
                printf("\nEntrer les elements de la matrice :\n");
                SaisirMat(M2,n);
                AfficheMat(M2,n);
                printf("\nLa transpose est : \n");
                TransposerMat(M2,n);
                AfficheMat(M2,n);
            }
        printf("\n1-Somme de deux matrices \n2-Produit de deux matrices \n3-Transposé d'une matrice \n4-Quitter le programme\n\n");
        printf("Faire votre choix : ");
        scanf("%d",&choix);
        while ((choix<1)|(choix>5))
        {
            printf("\nChoix non disponibre\nVeillez reessayer svp : ");
            scanf("%d",&choix);
        }
    }
    return 0;
}
