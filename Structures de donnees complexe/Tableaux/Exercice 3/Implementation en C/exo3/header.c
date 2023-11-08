#include <stdio.h>
#include <stdlib.h>
#include "header.h"
#include <string.h>

Pile init(Pile pile)
{
    pile.nbelt=0;
    return pile;
}
Pile save_first(Pile pile, Trajet elt)
{
    if (pile.nbelt==0)
    {
        pile.data[0]=elt;
        pile.nbelt++;
    }
    else {
        int i;
        for (i=pile.nbelt;i>=0;i--)
        {
            pile.data[i+1]=pile.data[i];
        }
        pile.data[0]=elt;
        pile.nbelt++;
    }
    return pile;
}
Pile read(Pile pile)
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
    pile=save_first(pile,elt);
    //2
    strcpy(elt.depart,"Mvan");
    strcpy(elt.arrivee,"Ekounou");
    elt.date.jour=1;
    elt.date.mois=3;
    elt.date.annee=2022;
    elt.prix=250;
    elt.duree=20;
    pile=save_first(pile,elt);
    //3
    strcpy(elt.depart,"Ekounou");
    strcpy(elt.arrivee,"Ngoa Ekele");
    elt.date.jour=4;
    elt.date.mois=3;
    elt.date.annee=2022;
    elt.prix=400;
    elt.duree=30;
    pile=save_first(pile,elt);
    //4
    strcpy(elt.depart,"Poste");
    strcpy(elt.arrivee,"Ngoa Ekele");
    elt.date.jour=20;
    elt.date.mois=3;
    elt.date.annee=2022;
    elt.prix=100;
    elt.duree=7;
    pile=save_first(pile,elt);
    //5
    strcpy(elt.depart,"Pakita");
    strcpy(elt.arrivee,"Olembe");
    elt.date.jour=3;
    elt.date.mois=4;
    elt.date.annee=2022;
    elt.prix=500;
    elt.duree=60;
    pile=save_first(pile,elt);
    //6
    strcpy(elt.depart,"Nsam");
    strcpy(elt.arrivee,"Ekounou");
    elt.date.jour=1;
    elt.date.mois=3;
    elt.date.annee=2022;
    elt.prix=250;
    elt.duree=20;
    pile=save_first(pile,elt);
    return pile;
}
void echange(Trajet t[100],int i,int j)
{
    Trajet c;
    c=t[i];
    t[i]=t[j];
    t[j]=c;
}
Pile sort_pile(Pile pile)
{
    int i,j,m;
    for (i=0;i<pile.nbelt-2;i++)
    {
    	m=i;
    	for(j=i+1;j<pile.nbelt*1;j++)
    	{
    		if (pile.data[m].prix>pile.data[j].prix)
    		{
    			m=j;
    		}
    	}
    	echange(pile.data,m,i);
    }
    return pile;
}
void print_list(Pile pile)
{
    int i;
    for (i=0;i<pile.nbelt-1;i++)
    {
        printf("%s\t%s\t%d\t%d\n",pile.data[i].depart,pile.data[i].arrivee,pile.data[i].prix,pile.data[i].duree);
    }
}
int search_elt(Pile pile,char d[100])
{
	int trouve=0,i=0;
	while ((i<pile.nbelt-1)&&(trouve==0))
	{
		if (strcmp(pile.data[i].depart,d)==0)
		{
			trouve=1;
		}
		i++;
	}
	return trouve;
}
