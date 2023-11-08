#include<stdio.h>
#include <stdlib.h>
#include <string.h>
#include "header.h"
//MEKA MOISE CHRISTIAN JUNIOR
//21T2561


//Fonction pour initialiser la pile
Pile *init()
{
    return NULL;
}
//Fonction pour ajouter en fin
Pile *save_first(Pile * pile, Trajet elt)
{
    Pile*tmp;
    tmp=(Pile*)malloc(sizeof(Pile));
    tmp->data=elt;
    tmp->next=pile;
    pile=tmp;
    return pile;
}
//Fonction pour retourner la taille de la liste
int length_list(Pile *pile)
{
    int nb=0;
    Pile *tmp=pile;
    while (tmp!=NULL)
    {
        tmp=tmp->next;
        nb++;
    }
    return nb;
}
//Fonction pour supprimer un element
Pile *supp_elt(Pile * pile,int p)
{
    Pile *curr=pile,*prec;
    int i=0;
    if (pile==NULL)
    {
        printf("Liste Vide...\n");
    }
    while((curr!=NULL)&&(curr->data.prix != p))
    {
        prec=curr;
        curr=curr->next;
        i++;
    }
    if(curr->data.prix == p)
    {
        if (i==0)
        {
            curr=pile->next;
            free(pile);
            pile=curr;
        }
        else
        {
            prec->next=curr->next;
            free(curr);
        }
    }
    return pile;
}
//Fonction pour rechercher un element a partir de l'element de depart
int search_elt(Pile * pile, char d[100])
{
    int trouve=0;
    Pile *tmp=pile;
    while((tmp!=NULL)&&(strcmp(tmp->data.depart,d)!=0))
    {
        tmp=tmp->next;
    }
    if(strcmp(tmp->data.depart,d)==0)
    {
        trouve=1;
    }
    return trouve;
}
//On cherche le maximun des prix de la pile
Trajet minimum(Pile *pile)
{
       Pile *tmp=pile;
       Trajet elt=pile->data,elt0;
        while(tmp!=NULL)
        {
            elt0=tmp->data;
            if((elt.prix)>(elt0.prix))
            {
                elt=elt0;
            }
            tmp=tmp->next;
        }
     return elt;
}
//Fonction pour trier les trajets suivant le prix
Pile* sort_list(Pile * pile)
{
    Pile *new_list=init();
    Trajet elt;
    while(pile!=NULL)
    {
        elt=minimum(pile);
        //On stocke le minimum en tete de new_list
        new_list=save_first(new_list,elt);
        pile=supp_elt(pile,elt.prix);
    }
    return new_list;
}
//Fonction pour afficher la liste
void print_list(Pile*pile)
{
    if (pile==NULL)
    {
        printf("Liste vide...\n");
    }
    else
    {
        Pile *tmp=pile;
        Trajet elt;
        while(tmp!=NULL)
        {
            elt=tmp->data;
            printf("%s\t%s\t%d\t%d\n",elt.depart,elt.arrivee,elt.duree,elt.prix);
            tmp=tmp->next;
        }
    }
}
//Initialisation de la table de hachage
HashTable initHash(HashTable table)
{
    int i;
    table.maxelt=4;
    for(i=0;i<table.maxelt;i++)
    {
        table.tab[i]=init();
    }
    return table;
}
//Fonction de Haching
int Hashing(HashTable table, char elt[100])
{
    return strlen(elt)%table.maxelt;
}
//Fonction de sauvegarde dans la table de hachage
HashTable save(HashTable table, Trajet elt)
{
    int i;
    Pile *p=init();
    i=Hashing(table,elt.depart);
    p=table.tab[i];
    p=save_first(p,elt);
    table.tab[i]=p;
    return table;
}
//Fonction pour lire les donnees par defaut et les stocker dans la pile
HashTable read(HashTable table)
{
    Trajet elt;
    //1
    strcpy(elt.depart,"Odza");
    strcpy(elt.arrivee,"Mvan");
    elt.date.jour=12;
    elt.date.mois=2;
    elt.date.annee=2022;
    elt.prix=300;
    elt.duree=40;
    table=save(table,elt);
    //2
    strcpy(elt.depart,"Mvan");
    strcpy(elt.arrivee,"Ekounou");
    elt.date.jour=1;
    elt.date.mois=3;
    elt.date.annee=2022;
    elt.prix=250;
    elt.duree=20;
    table=save(table,elt);
    //3
    strcpy(elt.depart,"Ekounou");
    strcpy(elt.arrivee,"Ngoa Ekele");
    elt.date.jour=4;
    elt.date.mois=3;
    elt.date.annee=2022;
    elt.prix=400;
    elt.duree=30;
    table=save(table,elt);
    //4
    strcpy(elt.depart,"Poste");
    strcpy(elt.arrivee,"Ngoa Ekele");
    elt.date.jour=20;
    elt.date.mois=3;
    elt.date.annee=2022;
    elt.prix=100;
    elt.duree=7;
    table=save(table,elt);
    //5
    strcpy(elt.depart,"Pakita");
    strcpy(elt.arrivee,"Olembe");
    elt.date.jour=3;
    elt.date.mois=4;
    elt.date.annee=2022;
    elt.prix=500;
    elt.duree=60;
    table=save(table,elt);
    //6
    strcpy(elt.depart,"Nsam");
    strcpy(elt.arrivee,"Ekounou");
    elt.date.jour=1;
    elt.date.mois=3;
    elt.date.annee=2022;
    elt.prix=250;
    elt.duree=20;
    table=save(table,elt);
    return table;
}
//Rechercher un element dans la table de hachage
int Hash_search(HashTable table, char d[100])
{
    int trouve=0,i;
    i=Hashing(table,d);
    if(i<table.maxelt){
        trouve=search_elt(table.tab[i],d);
    }
    return trouve;
}
