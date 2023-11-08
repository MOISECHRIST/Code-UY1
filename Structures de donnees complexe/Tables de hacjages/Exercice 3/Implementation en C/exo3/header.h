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
struct Pile{
    Trajet data;
    struct Pile *next;
};
typedef struct Pile Pile;
//Definition de la tables de hachage
struct HashTable{
    int maxelt;
    Pile *tab[4];
};
typedef struct HashTable HashTable;

//Fonction pour initialiser la pile
Pile *init();
//Fonction pour ajouter en tête
Pile *save_first(Pile * pile, Trajet elt);
//Fonction pour retourner la taille de la liste
int length_list(Pile *pile);
//Fonction pour supprimer un element
Pile *supp_elt(Pile * pile,int p);
//Fonction pour rechercher un element
int search_elt(Pile * pile, char d[100]);
//On cherche le maximun des prix de la pile
Trajet minimum(Pile *pile);
//Fonction pour trier les trajets suivant la duree
Pile* sort_list(Pile * pile);
//Fonction pour afficher la liste
void print_list(Pile*pile);
//Initialisation de la table de hachage
HashTable initHash(HashTable table);
//Fonction de Haching
int Hashing(HashTable table,char elt[100]);
//Fonction de sauvegarde dans la table de hachage
HashTable save(HashTable table,Trajet elt);
//Fonction pour lire les donnees par defaut et les stocker dans la pile
HashTable read(HashTable table);
//Rechercher un element dans la table de hachage
int Hash_search(HashTable table, char d[100]);
#endif // HEADER_H_INCLUDED
