#include <stdio.h>
#include <stdlib.h>
#include "fonctions.h"

int main()
{
    int n,i;
    float T[1000];
    printf("Entrer le nombre d'elements du tableau : ");
    scanf("%d",&n);
    for (i=0;i<n;i++)
    {
        printf("Entrer l'element %d : ",i+1);
        scanf("%f",&T[i]);
    }
    printf("Somme des elements : %.2f\n",som(T,n));
    printf("Produit des elements : %.2f\n",produit(T,n));
    printf("Moyenne des elements : %.2f\n",moyenne(T,n));
    printf("Le maximum des elements : %.2f\n",maximum(T,n));
    return 0;
}
