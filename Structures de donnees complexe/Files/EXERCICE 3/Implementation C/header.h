#ifndef HEADER_H_INCLUDED
#define HEADER_H_INCLUDED
//Definition de la structure de données pour manipuler les dates
struct Date{
    int jour;
    int mois;
    int annee;
};
typedef struct Date Date;
//Definition de la structure de données pour manipuler les trajets
struct Trajet{
    char depart[100];
    char arrivee[100];
    Date date;
    int duree;
    int prix;
};
typedef struct Trajet Trajet;
//Definition de la liste des trajets
struct File{
    Trajet data;
    struct File *next;
};
typedef struct File File;

//Fonction pour initialiser la file
File *init();
//Fonction pour ajouter en tête
File *save_end(File * file, Trajet elt);
//Fonction pour retourner la taille de la liste
int length_list(File *file);
//Fonction pour supprimer un element
File *supp_elt(File * file,int p);
//Fonction pour lire les donnees par defaut et les stocker dans la pile
File *read(File * file);
//Fonction pour rechercher un element
int search_elt(File * file, char d[100]);
//On cherche le maximun des prix de la pile
Trajet minimum(File *file);
//Fonction pour trier les trajets suivant la duree
File* sort_list(File * file);
//Fonction pour afficher la liste
void print_list(File*file);
#endif // HEADER_H_INCLUDED
