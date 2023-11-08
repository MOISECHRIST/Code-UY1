#include <stdio.h>
#include <stdlib.h>
#include "fonctions.h"
void SaisirMat(float M[100][100],int n)
{
    int i,j;
    printf("\nEntrer les coefficients de la matrice d'orde %d \n",n);
    for (i=0;i<n;i++)
    {
        for (j=0;j<n;j++)
        {
            printf("Entrer l'element %d de la ligne %d : ",j+1,i+1);
            scanf("%f",&M[i][j]);
        }
    }
}
void SommeMat(float M1[100][100],float M2[100][100],int n,float SOM[100][100])
{
    int i,j;
    for (i=0;i<n;i++)
    {
        for (j=0;j<=n;j++)
        {
            SOM[i][j]=M1[i][j]+M2[i][j];
        }
    }
}
void TransposerMat(float M[100][100],int n)
{
    int i,j,t;
    for (i=0;i<n;i++)
    {
        for (j=i;j<=n;j++)
        {
            t=M[i][j];
            M[i][j]=M[j][i];
            M[j][i]=t;
        }
    }
}
void ProduitMat(float M1[100][100],float M2[100][100],int n,float Prod[100][100])
{
    int i,j,k;
    for (i=0;i<n;i++)
    {
        for (j=0;j<=n;j++)
        {
            Prod[i][j]=0;
            for (k=0;k<n;k++)
            {
                Prod[i][j]+=M1[i][k]*M2[k][j];
            }
        }
    }
}
void AfficheMat(float M2[100][100],int n)
{
    int i,j;
    for (i=0;i<n;i++)
    {
        for (j=0;j<n;j++)
        {
            printf("%.0f  ",M2[i][j]);
        }
        printf("\n");
    }
}
