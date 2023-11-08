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
struct Pile{
  Trajet data[100];
  int nbelt;
};
typedef struct Pile Pile;

Pile init(Pile pile);
Pile save_first(Pile pile, Trajet elt);
Pile read(Pile pile);
void echange(Trajet t[100],int i,int j);
Pile sort_pile(Pile pile);
void print_list(Pile pile);
#endif // HEADER_H_INCLUDED
