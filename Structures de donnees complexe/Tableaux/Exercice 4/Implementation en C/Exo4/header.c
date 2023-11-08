#include <stdio.h>
#include <stdlib.h>
#include "header.h"
#include <string.h>

Pile init(Pile pile)
{
    pile.nbelt=0;
    return pile;
}
Pile save_first(Pile pile, Food elt)
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
//Fonction pour lire les donnees par defaut et les stocker dans la pile
Pile read(Pile pile)
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
    return pile;
}
void echange(Food t[100],int i,int j)
{
    Food c;
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
    		if (pile.data[m].age>pile.data[j].age)
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
    if (pile.nbelt==0){
    	printf("La liste est vide\n");
    }
    else{
	    int i;
	    for (i=0;i<pile.nbelt-1;i++)
	    {
		printf("%s\t%s\t%s\t%d\t%d\n",pile.data[i].heure,pile.data[i].repas,pile.data[i].lieu,pile.data[i].age,pile.data[i].nbpers);
	    }
    }
}
int search_elt(Pile pile,char d[100])
{
	int trouve=0,i=0;
	while ((i<pile.nbelt-1)&&(trouve==0))
	{
		if (strcmp(pile.data[i].repas,d)==0)
		{
			trouve=1;
		}
		i++;
	}
	return trouve;
}
