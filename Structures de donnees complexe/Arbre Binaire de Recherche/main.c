#include "abr.h"

int main()
{
    ABR *tr=init();
    //Question 1
    printf("1- Ajout des elements a la racine :\n11, 9, 0, 5, 4, 7, 3, 2, 8, 1, 10, 37, 21, 17, 3\n\n");
    tr=ajoutF(tr,11);
    tr=ajoutF(tr,9);
    tr=ajoutF(tr,0);
    tr=ajoutF(tr,5);
    tr=ajoutF(tr,4);
    tr=ajoutF(tr,7);
    tr=ajoutF(tr,3);
    tr=ajoutF(tr,2);
    tr=ajoutF(tr,8);
    tr=ajoutF(tr,1);
    tr=ajoutF(tr,10);
    tr=ajoutF(tr,37);
    tr=ajoutF(tr,21);
    tr=ajoutF(tr,17);
    tr=ajoutF(tr,3);

    printf("predecesseur de 8: %d\nSucesseur de 21: %d\n\n",predValeur(tr,8),succValeur(tr,21));
    printf("Resultat recherche de 5 : %d\n\n",recherche(tr,5));
    //Question 2
    printf("2- Affichage suivant les parcours :\n\n");
    printf("Prefixe\n");
    prefixe(tr);
    printf("\nInfixe\n");
    infixe(tr);
    printf("\nPostfixe\n");
    postfixe(tr);
    printf("\n\n");
    //Question 3:
    printf("3- Il sagit du parcours infixe\n\n");
    //Question 4
    printf("4- Supprimer la valeur 11\n\n");
    tr=suppElt(tr,11);


    //Question 5
    printf("5- Affichage suivant les parcours\n\n");
    printf("Prefixe\n");
    prefixe(tr);
    printf("\nInfixe\n");
    infixe(tr);
    printf("\nPostfixe\n");
    postfixe(tr);
    printf("\n\n");

    //Question 6
    printf("6- Ajouter 13 à la feuille \n");
    tr=ajoutF(tr, 13);


    //Question 7
    printf("\n7- Affichage suivant les parcours\n\n");
    printf("Prefixe\n");
    prefixe(tr);
    printf("\nInfixe\n");
    infixe(tr);
    printf("\nPostfixe\n");
    postfixe(tr);
    printf("\n\n");

    //Question 8
    printf("Ajouter 11 a la Feuille\n");
    tr=ajoutF(tr ,11);

    //Question 9
    printf("9- Affichage suivant les parcours:\n");
    printf("Prefixe\n");
    prefixe(tr);
    printf("\nInfixe\n");
    infixe(tr);
    printf("\nPostfixe\n");
    postfixe(tr);
    printf("\n\n");
    return 0;
}
