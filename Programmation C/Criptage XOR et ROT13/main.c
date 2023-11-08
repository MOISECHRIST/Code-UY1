//Modules du système...
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//Modules créés....
#include "gestion.h"
#include "cryptageXOR.h"
#include "cryptageROT13.h"
#include "statistique.h"

int main()
{
    int choix;
    struct phrase texte1[1000],texte2[1000],Mot[1000];
    int nbre,i,n;
    char clef[1000];
    printf("\n  -----------------------------------------------\n");
    printf("| Bienvenu dans le programme de cryptage de texte |\n");
    printf("  -----------------------------------------------\n");
    printf("\n\n\n>> NB: Il sagit d'un programme de cryptage de texte se trouvant\ndans un fichier en utilisant deux (2) methodes de cryptage :\n->le ROT13 et\n->le XOR.\nCe programme produit en outre des statistiques sur les textes manipules");
    printf("\n\n>>>>>>>>> Menu <<<<<<<<<<\n");
    printf("\n>> 1: Cryptage ROT13\n>> 2: Cryptage XOR\n>> 3: Quitter le programme\n");
    printf("\n>> Quelle Methode de cryptage voulez vous utiliser ? ");
    scanf("%d",&choix);
    while ((choix<1)|(choix>3))
    {
        printf("\n>>Erreur de saisie\n>>Veillez reessayer : ");
        scanf("%d",&choix);
    }
    while (choix!=3)
    {
        if (choix==1)
        {
            printf("\n\n>> Methode de cryptage ROT13\n");
            printf("\n>>>>>>>>> Menu <<<<<<<<<<\n");
            printf("\n>> 1: Crypter un texte\n>> 2: Decripter un texte\n>> 3: Statistiques\n>> 4: Retour au menu principal\n");
            printf("\n>> Que voulez vous faire ? ");
            scanf("%d",&choix);
            while ((choix<1)|(choix>4))
            {
                printf("\n>>Erreur de saisie\n>>Veillez reessayer : ");
                scanf("%d",&choix);
            }
            if (choix==1)
            {
                LECTURE_DECRYPT(texte1,&nbre);
                printf("\n\n>>Le texte a cripter est :\n\n");
                for (i=0;i<nbre;i++)
                {
                    printf("%s\n",texte1[i].chaine);
                }
                printf("\n\n>>Le texte cripté est :\n\n");
                for (i=0;i<nbre;i++)
                {
                    CrypterROT13(texte1[i].chaine,texte2[i].chaine);
                    texte2[i].taille=strlen(texte2[i].chaine);
                    printf("%s\n",texte2[i].chaine);
                }
                printf("\n>> Voulez vous enregistrer le resultat du cryptage ? [1=Oui/0=Non]  ");
                scanf("%d",&choix);
                while ((choix<0)|(choix>1))
                {
                    printf("\n>>Erreur de saisie\n>>Veillez reessayer : ");
                    scanf("%d",&choix);
                }
                if (choix==1)
                {
                    ECRITURE_CRYPT(texte2,nbre);
                }
            }
            if (choix==2)
            {
                LECTURE_CRYPT(texte1,&nbre);
                printf("\n\n>>Le texte a decripter est :\n\n");
                for (i=0;i<nbre;i++)
                {
                    printf("%s\n",texte1[i].chaine);
                }
                printf("\n\n>>Le texte decripté est :\n\n");
                for (i=0;i<nbre;i++)
                {
                    CrypterROT13(texte1[i].chaine,texte2[i].chaine);
                    texte2[i].taille=strlen(texte2[i].chaine);
                    printf("%s\n",texte2[i].chaine);
                }
                printf("\n>> Voulez vous enregistrer le resultat du decryptage ? [1=Oui/0=Non]  ");
                scanf("%d",&choix);
                while ((choix<0)|(choix>1))
                {
                    printf("\n>>Erreur de saisie\n>>Veillez reessayer : ");
                    scanf("%d",&choix);
                }
                if (choix==1)
                {
                    ECRITURE_DECRYPT(texte2,nbre);
                    printf("\n>> Sauvegarde du texte dans le fichier reussi...\n");
                }
            }
            if (choix==3)
            {
                LECTURE_DECRYPT(texte1,&nbre);
                for (i=0;i<nbre;i++)
                {
                CrypterROT13(texte1[i].chaine,texte2[i].chaine);
                texte2[i].taille=strlen(texte2[i].chaine);
                }
                ECRITURE_CRYPT(texte2,nbre);
                ImportMot(Mot,&n);
                printf("\n\n>> STATISTIQUES\n\n");
                printf("\n>> Total Caracteres : %d",NbCaractere());
                printf("\n>> Total Caractères Alphanumériques : %d",NbAlphaNum());
                printf("\n>> Total Mots : %d",n);
                printf("\n>> Longueur Mot le Plus Long : %d\n>> Longueur Mot moyen : %.2f\n>> Total Mot Different : %d",MotLePlusLong(),LongMoyMot(),MotDifferents());
                printf("\n>> Total Phrases : %d\n",NBphrase());
                printf(">> Total Caracteres Cryptés : %d\n",NbCaractereCrypte());
            }
        }
        if (choix==2)
        {
            printf("\n\n>> Methode de cryptage XOR\n");
            printf("\n>>>>>>>>> Menu <<<<<<<<<<\n");
            printf("\n>> 1: Crypter un texte\n>> 2: Decripter un texte\n>> 3: Statistiques\n>> 4: Retour au menu principal\n");
            printf("\n>> Que voulez vous faire ? ");
            scanf("%d",&choix);
            while ((choix<1)|(choix>4))
            {
                printf("\n>>Erreur de saisie\n>>Veillez reessayer : ");
                scanf("%d",&choix);
            }
            if (choix==1)
            {
                printf("\nEntrer la cle de cryptage : ");
                scanf("%s",&clef);
                ECRITURE_CLE(clef);
                LECTURE_DECRYPT(texte1,&nbre);
                printf("\n\n>>Le texte a cripter est :\n\n");
                for (i=0;i<nbre;i++)
                {
                    printf("%s\n",texte1[i].chaine);
                }
                printf("\n\n>>Le texte cripté est :\n\n");
                for (i=0;i<nbre;i++)
                {
                    CrypterXOR(texte1[i].chaine,texte2[i].chaine,clef);
                    texte2[i].taille=strlen(texte2[i].chaine);
                    printf("%s\n",texte2[i].chaine);
                }
                printf("\n>> Voulez vous enregistrer le resultat du cryptage ? [1=Oui/0=Non]  ");
                scanf("%d",&choix);
                while ((choix<0)|(choix>1))
                {
                    printf("\n>>Erreur de saisie\n>>Veillez reessayer : ");
                    scanf("%d",&choix);
                }
                if (choix==1)
                {
                    ECRITURE_CRYPT(texte2,nbre);
                }
            }
            if (choix==2)
            {
                printf("\nEntrer la cle de cryptage : ");
                scanf("%s",&clef);
                char cle[1000];
                LECTURE_CLE(cle);
                while (strcmp(cle,clef)!=0)
                {
                	printf("\n>>Cle incorrecte\n>>Veillez reessayer : ");
                	printf("\nEntrer la cle de cryptage : ");
                	scanf("%s",&clef);
                }
                LECTURE_CRYPT(texte1,&nbre);
                printf("\n\n>>Le texte a decripter est :\n\n");
                for (i=0;i<nbre;i++)
                {
                    printf("%s\n",texte1[i].chaine);
                }
                printf("\n\n>>Le texte decripté est :\n\n");
                for (i=0;i<nbre;i++)
                {
                    CrypterXOR(texte1[i].chaine,texte2[i].chaine,clef);
                    texte2[i].taille=strlen(texte2[i].chaine);
                    printf("%s\n",texte2[i].chaine);
                }
                printf("\n>> Voulez vous enregistrer le resultat du decryptage ? [1=Oui/0=Non]  ");
                scanf("%d",&choix);
                while ((choix<0)|(choix>1))
                {
                    printf("\n>>Erreur de saisie\n>>Veillez reessayer : ");
                    scanf("%d",&choix);
                }
                if (choix==1)
                {
                    ECRITURE_DECRYPT(texte2,nbre);
                    printf("\n>> Sauvegarde du texte dans le fichier reussi...\n");
                }
            }
            if (choix==3)
            {
                LECTURE_DECRYPT(texte1,&nbre);
                for (i=0;i<nbre;i++)
                {
                CrypterXOR(texte1[i].chaine,texte2[i].chaine,clef);
                texte2[i].taille=strlen(texte2[i].chaine);
                }
                ECRITURE_CRYPT(texte2,nbre);
                ImportMot(Mot,&n);
                printf("\n\n>> STATISTIQUES\n\n");
                printf("\n>> Total Caracteres : %d",NbCaractere());
                printf("\n>> Total Caractères Alphanumériques : %d",NbAlphaNum());
                printf("\n>> Total Mots : %d",n);
                printf("\n>> Longueur Mot le Plus Long : %d\n>> Longueur Mot moyen : %.2f\n>> Total Mot Different : %d",MotLePlusLong(),LongMoyMot(),MotDifferents());
                printf("\n>> Total Phrases : %d\n",NBphrase());
                printf(">> Total Caracteres Cryptés : %d\n",NbCaractereCrypte());
            }
        }
        printf("\n>>>>>>>>> Menu <<<<<<<<<<\n");
        printf("\n>> 1: Cryptage ROT13\n>> 2: Cryptage XOR\n>> 3: Quitter le programme\n");
        printf("\n>> Quelle Methode de cryptage voulez vous utiliser ? ");
        scanf("%d",&choix);
        while ((choix<1)|(choix>3))
        {
            printf("\n>>Erreur de saisie\n>>Veillez reessayer : ");
            scanf("%d",&choix);
        }
    }
    printf("\n>> Merci d'avoir utilisé ce programme...\n");
    return 0;
}
