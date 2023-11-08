#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "cryptageXOR.h"
#include "gestion.h"



//Module 3: Fonction de cryptage/decriptage XOR

/*La fonction de cryptage XOR est une fonction involutive.
Elle peut servir au cryptage et au décriptage des textes*/

void CrypterXOR(char ch1[1000], char ch2[1000],char clef[1000])
{
    int i,j=0,ligne,n;
    ligne=strlen(ch1);
    n=strlen(clef);
    for (i=0;i<ligne;i++)
    {
        ch2[i]=ch1[i]^clef[j];
        j++;
        if (j==n)
            j=0;
    }

}
