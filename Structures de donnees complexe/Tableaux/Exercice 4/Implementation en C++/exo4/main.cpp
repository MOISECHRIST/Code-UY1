#include <iostream>
#include <cassert>
#include <cstring>

using namespace std;
//Definition de la structure de données pour manipuler les dates
struct Date{
    int jour;
    int mois;
    int annee;
};
//Definition de la structure de données pour manipuler les données de nouriture
struct Food{
    char sexe[100];
    int age;
    Date date;
    char heure[100];
    char repas[100];
    char unite[100];
    char lieu[100];
    int nbpers;
};
class Pile{
    public:
        Food data[100];
        int nbelt;
        Pile();//Initialisation du tableau
        void save(Food& elt);//Fonction pour ajouter en tete
        void print_list ();//Fonction qui affiche la liste des elements
        void echange(Food t[100],int i,int j);//Permuter deux elements d'un tableau
        int search_elt(char d[100]);//Fonction qui recherche un trajet dans la pile à partir de son point de depart et retoune 'true' si le trajet se trouve dans la pile et 'false' sinon
        void read();//Lire un ensemble de données
        void sort_pile();//Fonction pour trier le tableau
};
Pile :: Pile(): nbelt(0){}
void Pile :: save(Food& elt)
{
    if (nbelt==0)
    {
        data[0]=elt;
        nbelt++;
    }
    else {
        int i;
        for (i=nbelt;i>=0;i--)
        {
            data[i+1]=data[i];
        }
        data[0]=elt;
        nbelt++;
    }
}
void Pile :: read()
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
	    save(elt);
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
	    save(elt);
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
	    save(elt);
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
	    save(elt);
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
	    save(elt);
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
	    save(elt);
}
void Pile :: echange(Food t[100],int i,int j)
{
    Food c;
    c=t[i];
    t[i]=t[j];
    t[j]=c;
}
void Pile :: sort_pile()
{
    int i,j,m;
    for (i=0;i<nbelt-2;i++)
    {
    	m=i;
    	for(j=i+1;j<nbelt*1;j++)
    	{
    		if (data[m].age>data[j].age)
    		{
    			m=j;
    		}
    	}
    	echange(data,m,i);
    }
}
void Pile :: print_list()
{
    int i;
    for (i=0;i<nbelt-1;i++)
    {
        cout<<data[i].age<<"\t"<<data[i].repas<<"\t"<<data[i].lieu<<"\t"<<data[i].nbpers<<endl;
    }
}
int Pile :: search_elt(char d[100])
{
	int trouve=0,i=0;
	while ((i<nbelt-1)&&(trouve==0))
	{
		if (strcmp(data[i].repas,d)==0)
		{
			trouve=1;
		}
		i++;
	}
	return trouve;
}

int main()
{
    Pile pile;
    pile.read();
    cout<<"La pile de donnees est :"<<endl;
    cout<<"Taille : "<<pile.nbelt<<endl;
    pile.print_list();
    pile.sort_pile();
    cout<<"La pile de donnees est :"<<endl;
    cout<<"Taille : "<<pile.nbelt<<endl;
    pile.print_list();
    cout<<"(C) 2022 By MMCJ/INF-L1\n"<<endl;
    return 0;
}
