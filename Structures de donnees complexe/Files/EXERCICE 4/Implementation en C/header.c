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
//Fonction pour ajouter en tête
Pile *save_first(Pile * pile, Food elt)
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
Pile *supp_elt(Pile * pile,char d[100])
{
    Pile *curr=pile,*prec;
    int i=0;
    if (pile==NULL)
    {
        printf("Liste Vide...\n");
    }
    while((curr!=NULL)&&(strcmp(curr->data.repas,d)!=0))
    {
        prec=curr;
        curr=curr->next;
        i++;
    }
    if(strcmp(curr->data.repas,d)==0)
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
//Fonction pour lire les donnees par defaut et les stocker dans la pile
Pile *read(Pile * pile)
{
    Food elt;
    //1
    strcpy(elt.sexe,"Masculin");
    elt.age=21;
    elt.date.jour=14;
    elt.date.mois=5;
    elt.date.annee=2022;
    strcpy(elt.heure,"10h-16h");
    strcpy(elt.repas,"Okok");
    strcpy(elt.unite,"Plat");
    strcpy(elt.lieu,"Maison");
    elt.nbpers=5;
    pile=save_first(pile,elt);
    //2
    strcpy(elt.sexe,"Masculin");
    elt.age=19;
    elt.date.jour=14;
    elt.date.mois=5;
    elt.date.annee=2022;
    strcpy(elt.heure,"10h-16h");
    strcpy(elt.repas,"Poulet");
    strcpy(elt.unite,"Plat");
    strcpy(elt.lieu,"Maison");
    elt.nbpers=5;
    pile=save_first(pile,elt);
    //3
     strcpy(elt.sexe,"Masculin");
    elt.age=15;
    elt.date.jour=14;
    elt.date.mois=5;
    elt.date.annee=2022;
    strcpy(elt.heure,"10h-16h");
    strcpy(elt.repas,"Sanga");
    strcpy(elt.unite,"Plat");
    strcpy(elt.lieu,"Maison");
    elt.nbpers=5;
    pile=save_first(pile,elt);
    //4
     strcpy(elt.sexe,"Masculin");
    elt.age=18;
    elt.date.jour=14;
    elt.date.mois=5;
    elt.date.annee=2022;
    strcpy(elt.heure,"10h-16h");
    strcpy(elt.repas,"Pate saute");
    strcpy(elt.unite,"Plat");
    strcpy(elt.lieu,"Maison");
    elt.nbpers=5;
    pile=save_first(pile,elt);
    //5
     strcpy(elt.sexe,"Masculin");
    elt.age=25;
    elt.date.jour=14;
    elt.date.mois=5;
    elt.date.annee=2022;
    strcpy(elt.heure,"10h-16h");
    strcpy(elt.repas,"Eru");
    strcpy(elt.unite,"Plat");
    strcpy(elt.lieu,"Maison");
    elt.nbpers=5;
    pile=save_first(pile,elt);
    //6
     strcpy(elt.sexe,"Masculin");
    elt.age=16;
    elt.date.jour=14;
    elt.date.mois=5;
    elt.date.annee=2022;
    strcpy(elt.heure,"10h-16h");
    strcpy(elt.repas,"Nkui");
    strcpy(elt.unite,"Plat");
    strcpy(elt.lieu,"Maison");
    elt.nbpers=5;
    pile=save_first(pile,elt);
}
//Fonction pour rechercher un element a partir de l'element de depart
int search_elt(Pile * pile, char d[100])
{
    int trouve=0;
    Pile *tmp=pile;
    while((tmp!=NULL)&&(strcmp(tmp->data.repas,d)!=0))
    {
        tmp=tmp->next;
    }
    if(strcmp(tmp->data.repas,d)==0)
    {
        trouve=1;
    }
    return trouve;
}
//On cherche le maximun des prix de la pile
Food minimum(Pile *pile)
{
       Pile *tmp=pile;
       Food elt=pile->data,elt0;
        while(tmp!=NULL)
        {
            elt0=tmp->data;
            if((elt.age)>(elt0.age))
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
    Food elt;
    while(pile!=NULL)
    {
        elt=minimum(pile);
        //On stocke le minimum en tete de new_list
        new_list=save_first(new_list,elt);
        pile=supp_elt(pile,elt.repas);
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
        Food elt;
        while(tmp!=NULL)
        {
            elt=tmp->data;
            printf("%s\t%d\n",elt.repas,elt.age);
            tmp=tmp->next;
        }
    }
}
