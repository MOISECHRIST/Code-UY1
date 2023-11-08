#ifndef HEADER_H_INCLUDED
#define HEADER_H_INCLUDED

//Definition de la structure de données pour manipuler les dates
struct Date{
    int jour;
    int mois;
    int annee;
};
typedef struct Date Date;
//Definition de la structure de données pour manipuler les données de nouriture
struct Food{
    char sexe[100];
    int age;
    Date date;
    char heure[10];
    char repas[100];
    char unite[100];
    char lieu[100];
    int nbpers;
};
typedef struct Food Food;
//Definition de la liste des trajets
struct Pile{
    Food data;
    struct Pile *next;
};
typedef struct Pile Pile;

//Fonction pour initialiser la pile
Pile *init();
//Fonction pour ajouter en tête
Pile *save_first(Pile * pile, Food elt);
//Fonction pour retourner la taille de la liste
int length_list(Pile *pile);
//Fonction pour supprimer un element
Pile *supp_elt(Pile * pile,char d[100]);
//Fonction pour lire les donnees par defaut et les stocker dans la pile
Pile *read(Pile * pile);
//Fonction pour rechercher un element
int search_elt(Pile * pile, char d[100]);
//On cherche le maximun des prix de la pile
Food minimum(Pile *pile);
//Fonction pour trier les trajets suivant la duree
Pile* sort_list(Pile * pile);
//Fonction pour afficher la liste
void print_list(Pile*pile);

#endif // HEADER_H_INCLUDED
