#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "gestion.h"
#include "statistique.h"


//Module 4: Statistiques

//Fonction pour compter le nombre totale de phrases dans le texte
int NBphrase()
{
    FILE *fichier;
    fichier=fopen("Texte_decripte.txt","r");
    if (fichier==NULL)
    {
        printf(">>Erreur d'ouverture du fichier Texte_decripte.txt\n");
        exit(1);
    }
    struct phrase Ph;
    int i,j=0;
    while ((fscanf(fichier,"%[^\n]\n",Ph.chaine)) != EOF)
    {
        Ph.taille=strlen(Ph.chaine);
        for (i=0;i<Ph.taille;i++)
        {
            if ((Ph.chaine[i]=='.')|(Ph.chaine[i]=='!')|(Ph.chaine[i]=='?'))
            {
                j++;
            }
        }
    }
    fclose(fichier);
    return j;
}


//Fonction pour compter le nombre totale de caractère alphanumérique
int NbAlphaNum()
{
    FILE *fichier;
    fichier=fopen("Texte_decripte.txt","r");
    if (fichier==NULL)
    {
        printf(">>Erreur d'ouverture du fichier Texte_decripte.txt\n");
        exit(1);
    }
    struct phrase Ph;
    int i,j=0;
    while ((fscanf(fichier,"%[^\n]\n",Ph.chaine)) != EOF)
    {
        Ph.taille=strlen(Ph.chaine);
        for (i=0;i<Ph.taille;i++)
        {
            if (((Ph.chaine[i]>='a')&&(Ph.chaine[i]<='z'))|((Ph.chaine[i]>='A')&&(Ph.chaine[i]<='Z'))|((Ph.chaine[i]>='0')&&(Ph.chaine[i]<='9')))
            {
                j++;
            }
        }
    }
    fclose(fichier);
    return j;
}

//Fonction pour retourner la longueur du mot le plus long
int MotLePlusLong()
{
    struct phrase Mot[1000];
    int i=0,j=0,n,k,p;
    ImportMot(Mot,&n);
    int max=0;
    for (i=0;i<n;i++)
    {
        if (Mot[i].taille>Mot[max].taille)
        {
            max=i;
        }
    }
    return Mot[max].taille;
}

//Fonction pour retourner la longueur du mot moyen
float LongMoyMot()
{
    struct phrase Mot[1000];
    int i=0,j=0,n,k;
    ImportMot(Mot,&n);
    float moy=0;
    for (i=0;i<n;i++)
    {
        moy+=Mot[i].taille;
    }
    moy/=n;
    return moy;
}

//Fonction pour compter le nombre totale de mots différents
int MotDifferents()
{
    struct phrase Mot[1000];
    int i=0,j=0,n;
    ImportMot(Mot,&n);
    int nb[1000];
    for (i=0;i<n-1;i++)
    {
        for (j=i+1;j<n;j++)
        {
            if (strcmp(Mot[i].chaine,Mot[j].chaine)==0)
            {
                n--;
            }
        }
    }
    return n;
}

//Fonction pour compter le nombre totale de caractères cryptés
int NbCaractereCrypte()
{
    struct phrase texte1[1000],texte2[1000];
    int nbre1,nbre2,i,j,k=0;
    LECTURE_DECRYPT(texte1,&nbre1);
    LECTURE_CRYPT(texte2,&nbre2);
    for (i=0;i<nbre1;i++)
    {
        for(j=0;j<texte1[i].taille;j++)
        {
            if (texte1[i].chaine[j]!=texte2[i].chaine[j])
            {
                k++;
            }
        }
    }
    return k;
}

//Fonction pour compter le nombre totale de caractères du texte
int NbCaractere()
{
    struct phrase texte[1000];
    int nbre,i,k=0;
    LECTURE_DECRYPT(texte,&nbre);
    for (i=0;i<nbre;i++)
    {
        k+=texte[i].taille;
    }
    return k;
}
