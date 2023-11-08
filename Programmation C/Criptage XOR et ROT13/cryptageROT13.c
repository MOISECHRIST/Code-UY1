#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "cryptageROT13.h"
#include "gestion.h"


//Module 2: Fonction de cryptage/decriptage ROT13

/*La fonction de cryptage ROT13 est une fonction involutive.
Elle peut servir au cryptage et au décriptage des textes*/

void CrypterROT13(char ch1[1000], char ch2[1000])
{
    int i,ligne;
    ligne=strlen(ch1);
    for (i=0;i<ligne;i++)
    {
        if ((ch1[i]>='a')&&(ch1[i]<='m'))
        {
            ch2[i]=ch1[i]+13;
        }
        else if ((ch1[i]>='n')&&(ch1[i]<='z'))
            {
                ch2[i]=ch1[i]-13;
            }
            else if ((ch1[i]>='A')&&(ch1[i]<='M'))
                {
                    ch2[i]=ch1[i]+13;
                }
                else if ((ch1[i]>='N')&&(ch1[i]<='Z'))
                {
                    ch2[i]=ch1[i]-13;
                }
                else
                {
                    ch2[i]=ch1[i];
                }
    }

}
