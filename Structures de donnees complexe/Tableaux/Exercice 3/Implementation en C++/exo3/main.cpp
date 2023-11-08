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
//Definition de la structure de données pour manipuler les trajets
struct Trajet{
    char depart[100];
    char arrivee[100];
    Date date;
    int duree;
    int prix;
};
class Pile{
    public:
        Trajet data[100];
        int nbelt;
        Pile();//Initialisation du tableau
        void save_first(Trajet& elt);//Fonction pour ajouter en tete
        void print_list ();//Fonction qui affiche la liste des elements
        void echange(Trajet t[100],int i,int j);//Permuter deux elements d'un tableau
        int search_elt(char d[100]);//Fonction qui recherche un trajet dans la pile à partir de son point de depart et retoune 'true' si le trajet se trouve dans la pile et 'false' sinon
        void read();//Lire un ensemble de données
        void sort_pile();//Fonction pour trier le tableau
};
Pile :: Pile(): nbelt(0){}
void Pile :: save_first(Trajet& elt)
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
    Trajet elt;
    //1
    strcpy(elt.depart,"Odza");
    strcpy(elt.arrivee,"Mvan");
    elt.date.jour=12;
    elt.date.mois=2;
    elt.date.annee=2022;
    elt.prix=300;
    elt.duree=40;
    save_first(elt);
    //2
    strcpy(elt.depart,"Mvan");
    strcpy(elt.arrivee,"Ekounou");
    elt.date.jour=1;
    elt.date.mois=3;
    elt.date.annee=2022;
    elt.prix=250;
    elt.duree=20;
    save_first(elt);
    //3
    strcpy(elt.depart,"Ekounou");
    strcpy(elt.arrivee,"Ngoa Ekele");
    elt.date.jour=4;
    elt.date.mois=3;
    elt.date.annee=2022;
    elt.prix=400;
    elt.duree=30;
    save_first(elt);
    //4
    strcpy(elt.depart,"Poste");
    strcpy(elt.arrivee,"Ngoa Ekele");
    elt.date.jour=20;
    elt.date.mois=3;
    elt.date.annee=2022;
    elt.prix=100;
    elt.duree=7;
    save_first(elt);
    //5
    strcpy(elt.depart,"Pakita");
    strcpy(elt.arrivee,"Olembe");
    elt.date.jour=3;
    elt.date.mois=4;
    elt.date.annee=2022;
    elt.prix=500;
    elt.duree=60;
    save_first(elt);
    //6
    strcpy(elt.depart,"Nsam");
    strcpy(elt.arrivee,"Ekounou");
    elt.date.jour=1;
    elt.date.mois=3;
    elt.date.annee=2022;
    elt.prix=250;
    elt.duree=20;
    save_first(elt);
}
void Pile :: echange(Trajet t[100],int i,int j)
{
    Trajet c;
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
    		if (data[m].prix>data[j].prix)
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
        cout<<data[i].depart<<"\t"<<data[i].arrivee<<"\t"<<data[i].prix<<"\t"<<data[i].duree<<endl;
    }
}
int Pile :: search_elt(char d[100])
{
	int trouve=0,i=0;
	while ((i<nbelt-1)&&(trouve==0))
	{
		if (strcmp(data[i].depart,d)==0)
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
