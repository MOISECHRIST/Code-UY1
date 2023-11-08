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
struct Pile{
  Food data[100];
  int nbelt;
};
typedef struct Pile Pile;

Pile init(Pile pile);
Pile save_first(Pile pile, Food elt);
Pile read(Pile pile);
void echange(Food t[100],int i,int j);
Pile sort_pile(Pile pile);
void print_list(Pile pile);

#endif // HEADER_H_INCLUDED
