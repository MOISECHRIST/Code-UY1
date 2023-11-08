#include<stdio.h>
#include <stdlib.h>
#include <string.h>
#include "header.h"
//MEKA MOISE CHRISTIAN JUNIOR
//21T2561


//Fonction pour initialiser la File
File *init()
{
    return NULL;
}
//Fonction pour ajouter en tête
File *save_end(File * file, Trajet elt)
{
    File*tmp,*cur=file;
    tmp=(File*)malloc(sizeof(File));
    tmp->data=elt;
    if (file==NULL)
    {
    	file=tmp;
    }
    else
    {
	    while (cur->next != NULL)
	    {
	    	cur=cur->next;
	    }
	    cur->next=tmp;
    }
    return file;
}
//Fonction pour retourner la taille de la liste
int length_list(File *file)
{
    int nb=0;
    File *tmp=file;
    while (tmp!=NULL)
    {
        tmp=tmp->next;
        nb++;
    }
    return nb;
}
//Fonction pour supprimer un element
File *supp_elt(File * file,int p)
{
    File *curr=file,*prec;
    int i=0;
    if (file==NULL)
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
            curr=file->next;
            free(file);
            file=curr;
        }
        else
        {
            prec->next=curr->next;
            free(curr);
        }
    }
    return file;
}
//Fonction pour lire les donnees par defaut et les stocker dans la File
File *read(File * file)
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
    file=save_end(file,elt);
    //2
    strcpy(elt.depart,"Mvan");
    strcpy(elt.arrivee,"Ekounou");
    elt.date.jour=1;
    elt.date.mois=3;
    elt.date.annee=2022;
    elt.prix=250;
    elt.duree=20;
    file=save_end(file,elt);
    //3
    strcpy(elt.depart,"Ekounou");
    strcpy(elt.arrivee,"Ngoa Ekele");
    elt.date.jour=4;
    elt.date.mois=3;
    elt.date.annee=2022;
    elt.prix=400;
    elt.duree=30;
    file=save_end(file,elt);
    //4
    strcpy(elt.depart,"Poste");
    strcpy(elt.arrivee,"Ngoa Ekele");
    elt.date.jour=20;
    elt.date.mois=3;
    elt.date.annee=2022;
    elt.prix=100;
    elt.duree=7;
    file=save_end(file,elt);
    //5
    strcpy(elt.depart,"Pakita");
    strcpy(elt.arrivee,"Olembe");
    elt.date.jour=3;
    elt.date.mois=4;
    elt.date.annee=2022;
    elt.prix=500;
    elt.duree=60;
    file=save_end(file,elt);
    //6
    strcpy(elt.depart,"Nsam");
    strcpy(elt.arrivee,"Ekounou");
    elt.date.jour=1;
    elt.date.mois=3;
    elt.date.annee=2022;
    elt.prix=250;
    elt.duree=20;
    file=save_end(file,elt);
    return file;
}
//Fonction pour rechercher un element a partir de l'element de depart
int search_elt(File * file, char d[100])
{
    int trouve=0;
    File *tmp=file;
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
//On cherche le maximun des prix de la File
Trajet minimum(File *file)
{
       File *tmp=file;
       Trajet elt=file->data,elt0;
       int n=length_list(file),i=0;
        while(i<n)
        {
            elt0=tmp->data;
            if((elt.prix)>(elt0.prix))
            {
                elt=elt0;
                
            }
            tmp=tmp->next;
            i++;
        }
     return elt;
}
//Fonction pour afficher la liste
void print_list(File*file)
{
    if (file==NULL)
    {
        printf("Liste vide...\n");
    }
    else
    {
        File *tmp=file;
        Trajet elt;
        while(tmp!=NULL)
        {
            elt=tmp->data;
            printf("%s\t%d\n",elt.depart,elt.prix);
            tmp=tmp->next;
        }
    }
}
//Fonction pour trier les trajets suivant le prix
File* sort_list(File * file)
{
    File *new_list=init();
    Trajet elt;
    while(file!=NULL)
    {
        elt=minimum(file);
        //On stocke le minimum en tete de new_list
        new_list=save_end(new_list,elt);
        file=supp_elt(file,elt.prix);
    }
    return new_list;
}
