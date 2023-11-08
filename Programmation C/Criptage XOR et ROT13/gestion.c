#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "gestion.h"
#include "statistique.h"

//Module 1: Manipulation des fichiers
//Lecture du texte dans le fichier Texte_decripte.txt



void LECTURE_DECRYPT(struct phrase texte[1000],int* nbre)
{
    FILE *fichier;
    fichier=fopen("Texte_decripte.txt","r");
    if (fichier==NULL)
    {
        printf(">>Erreur d'ouverture du fichier Texte_decripte.txt\n");
        exit(1);
    }
    struct phrase Ph;
    int i=0;
    while ((fscanf(fichier,"%[^\n]\n",Ph.chaine)) != EOF)
    {
        Ph.taille=strlen(Ph.chaine);
        texte[i]=Ph;
        i++;
    }
    fclose(fichier);
    *nbre=i;
}



//Lecture du texte dans le fichier Texte_cripte.txt
void LECTURE_CRYPT(struct phrase texte[1000],int* nbre)
{
    FILE *fichier;
    fichier=fopen("Texte_cripte.txt","r");
    if (fichier==NULL)
    {
        printf(">>Erreur d'ouverture du fichier Texte_cripte.txt\n");
        exit(1);
    }
    struct phrase Ph;
    int i=0;
    while ((fscanf(fichier,"%[^\n]\n",Ph.chaine)) != EOF)
    {
        Ph.taille=strlen(Ph.chaine);
        texte[i]=Ph;
        i++;
    }
    fclose(fichier);
  *nbre=i;
}



//Ecriture du texte dans le fichier Texte_decripte.txt
void ECRITURE_DECRYPT(struct phrase texte[1000],int nbre)
{
    FILE *fichier;
    fichier=fopen("Texte_decripte.txt","w");
    if (fichier==NULL)
    {
        printf(">>Erreur d'ouverture du fichier Texte_decripte.txt\n");
        exit(1);
    }
    int i;
    for (i=0;i<nbre;i++)
    {
        fprintf(fichier,"%s\n",texte[i].chaine);
    }
    fclose(fichier);
}


//Ecriture du texte dans le fichier Texte_cripte.txt
void ECRITURE_CRYPT(struct phrase texte[1000],int nbre)
{
    FILE *fichier;
    fichier=fopen("Texte_cripte.txt","w");
    if (fichier==NULL)
    {
        printf(">>Erreur d'ouverture du fichier Texte_cripte.txt\n");
        exit(1);
    }
    int i;
    for (i=0;i<nbre;i++)
    {
        fprintf(fichier,"%s\n",texte[i].chaine);
    }
    fclose(fichier);
}



//Importation du texte mot par mot
void ImportMot(struct phrase Mot[1000],int* n)
{
    FILE *fichier;
    fichier=fopen("Texte_decripte.txt","r");
    if (fichier==NULL)
    {
        printf(">>Erreur d'ouverture du fichier Texte_decripte.txt\n");
        exit(1);
    }
    int i=0,j=0,k,p;
    while ((fscanf(fichier,"%s",Mot[i].chaine)) != EOF)
    {
        for (j=0;j<strlen(Mot[i].chaine);j++)
        {
            if ((Mot[i].chaine[j]=='.')|(Mot[i].chaine[j]=='!')|(Mot[i].chaine[j]=='?')|(Mot[i].chaine[j]==',')|(Mot[i].chaine[j]==';')|(Mot[i].chaine[j]==')')|(Mot[i].chaine[j]=='(')|(Mot[i].chaine[j]==':'))
            {
                for (k=j+1;k<=strlen(Mot[i].chaine);k++)
                    Mot[i].chaine[k-1]=Mot[i].chaine[k];
            }
        }
        Mot[i].taille=strlen(Mot[i].chaine);
        i++;
    }
    fclose(fichier);
    *n=i;
}

//Ecriture du texte dans le fichier Cle-XOR.txt
void ECRITURE_CLE(char cle[1000])
{
    FILE *fichier;
    fichier=fopen("Cle-XOR.txt","w");
    if (fichier==NULL)
    {
        printf(">>Erreur d'ouverture du fichier Cle-XOR.txt\n");
        exit(1);
    }
    fprintf(fichier,"%s\n",cle);
    fclose(fichier);
}

//Importation de la clé
void LECTURE_CLE(char cle[1000])
{
    //struct phrase Mot[1000];
    FILE *fichier;
    int i=0;
    fichier=fopen("Cle-XOR.txt","r");
    if (fichier==NULL)
    {
        printf(">>Erreur d'ouverture du fichier Texte_decripte.txt\n");
        exit(1);
    }
    while ((fscanf(fichier,"%s",cle)) != EOF)
    {
    	i++;
    }
    fclose(fichier);
}
