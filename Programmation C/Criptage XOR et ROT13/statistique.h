#ifndef STATISTIQUE_H_INCLUDED
#define STATISTIQUE_H_INCLUDED
#include "gestion.h"
//Module 4: Statistiques

#ifdef __cplusplus
extern "C" {
#endif
//Fonction pour compter le nombre totale de phrases dans le texte
int NBphrase();

//Fonction pour compter le nombre totale de caractère alphanumérique
int NbAlphaNum();

//Fonction pour retourner la longueur du mot le plus long
int MotLePlusLong();

//Fonction pour retourner la longueur du mot moyen
float LongMoyMot();

//Fonction pour compter le nombre totale de mots différents
int MotDifferents();

//Fonction pour compter le nombre totale de caractères cryptés
int NbCaractereCrypte();

//Fonction pour compter le nombre totale de caractères du texte
int NbCaractere();

#ifdef __cplusplus
}
#endif

#endif // STATISTIQUE_H_INCLUDED
