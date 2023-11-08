#ifndef ABR_H_INCLUDED
#define ABR_H_INCLUDED

#include <stdio.h>
#include <stdlib.h>

//Question 1: Definir la structure de données
typedef struct ABR
{
    int valeur;
    struct ABR *FilsGauche;
    struct ABR *FilsDroit;
    struct ABR *parent;
} ABR;
ABR *init();
//Question 2 : Ecrire une fonction creer_ABR
ABR *creer_ABR(int elt,ABR *FilsG, ABR *FilsD);
//Question 3 : Ecrire les fonctions d'affichage
//Prefixe
void prefixe(ABR *abr);
//Infixe
void infixe(ABR *abr);
//Postfixe
void postfixe(ABR *abr);
//Question 4:Successeur d'un element dans un arbre
int succValeur(ABR *abr, int elt);
//Question 5: Predecesseur d'un element dans un arbre
int predValeur(ABR *abr, int elt);
//Question 6: Fonction de recherche
int recherche(ABR *abr,int elt);
//Question 7: Ajout en racine
ABR *ajoutR(ABR *abr,int elt);
//Question 8: Ajout en feuille
ABR *ajoutF(ABR *abr,int elt);
//Question 9: Supression element
ABR *suppElt(ABR *abr, int elt);
#endif // ABR_H_INCLUDED
