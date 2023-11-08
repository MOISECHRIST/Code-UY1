#include <stdio.h>
#include <stdlib.h>
#include "fonctions.h"

float som(float T[1000],int n)
{
    int i;
    float S=0;
    for (i=0;i<n;i++)
    {
        S=S+T[i];
    }
    return S;
}
float produit(float T[1000],int n)
{
   int i;
    float P=1;
    for (i=0;i<n;i++)
    {
        P=P*T[i];
    }
    return P;
}
float moyenne(float T[1000],int n)
{
    float moy;
    moy=som(T,n)/n;
    return moy;
}
float maximum(float T[1000],int n)
{
    int i,maxi=0;
    for (i=1;i<n;i++)
    {
        if (T[i]>T[maxi])
        {
            maxi=i;
        }
    }
    return T[maxi];
}
