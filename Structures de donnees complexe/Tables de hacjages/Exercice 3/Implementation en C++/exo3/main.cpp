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
//Definition d'un noeud de trajet
struct Node
{
    Trajet data;
    Node * next;
};
//Definition de la classe pile de trajet
class Pile
{
    private:
        Node * tete;//La tete de pile

    public:

        Pile();//Initialiser de la tete de la pile à null
        void savePile (Trajet& valeur);//Fonction pour ajouter en tete
        void supp_elt (int p);//Fonction pour supprimer un element de la liste à partir de son point de depart
        Trajet minimum();//Fonction qui retourne le trajet de prix minimum
        void print_list ();//Fonction pour supprimer un element de la liste à partir
        int nbelt ();//Fonction qui retourne la taille de la pile
        bool search_(char d[100]);//Fonction qui recherche un trajet dans la pile à partir de son point de depart et retoune 'true' si le trajet se trouve dans la pile et 'false' sinon
};
Pile :: Pile(): tete(NULL){}
void Pile :: savePile (Trajet& valeur)
{
	Node *tmp= new Node;
	tmp->data=valeur;
	tmp->next=tete;
	tete=tmp;
}
void Pile :: supp_elt (int p)
{
	Node *prec, *cur;
	if (tete==NULL)
	{
		cout<<"La pile est vide..."<<endl;
	}
	else
	{
		cur=tete;
		Trajet elt=cur->data;
		int i=0;
		while((cur != NULL)&&(elt.prix!=p))
		{
			prec=cur;
			cur=cur->next;
			i++;
		}
		if(elt.prix==p)
		{
			if (i==0)
			{
				tete=tete->next;
				delete(cur);
			}
			else
			{
				prec->next=cur->next;
				delete(cur);
			}
		}
	}
}
Trajet Pile :: minimum()
{
	Trajet elt;
	if (tete==NULL)
	{
		cout<<"La pile est vide..."<<endl;
	}
	else
	{
		Node *tmp=tete;
		elt=tmp->data;
		while (tmp != NULL)
		{
			if (tmp->data.prix < elt.prix)
			{
				elt=tmp->data;
			}
			tmp=tmp->next;
		}
	}
	return elt;
}
int Pile :: nbelt ()
{
	int n=0;
	if (tete==NULL)
	{
		cout<<"La pile est vide..."<<endl;
	}
	else
	{
		Node *tmp=tete;
		while (tmp != NULL)
		{
			n++;
			tmp=tmp->next;
		}
	}
	return n;
}
bool Pile :: search_(char d[100])
{
	Node *cur;
	bool trouve=false;
	if (tete==NULL)
	{
		cout<<"La pile est vide..."<<endl;
	}
	else
	{
		cur=tete;
		Trajet elt=cur->data;
		while((cur != NULL)&&(strcmp(elt.depart,d)!=0))
		{
			cur=cur->next;
		}
		if(strcmp(elt.depart,d)==0)
		{
			trouve=true;
		}
	}
	return trouve;
}
void Pile :: print_list ()
{
	if (tete==NULL)
	{
		cout<<"La pile est vide..."<<endl;
	}
	else
	{
		Node *cur=tete;
		Trajet elt;
		while (cur != NULL)
		{
			elt=cur->data;
			cout<<elt.depart<<"\t"<<elt.prix<<"\t"<<elt.arrivee<<endl;
			cur=cur->next;
		}
	}
}
class HashTable
{
    public:
        Pile Data[4];
        int maxelt;
        HashTable();
        int HashingFunc(char elt[100]);
        void save(Trajet& valeur);
        void read();
        bool search_elt(char d[100]);
};
HashTable :: HashTable(): maxelt(4){}
int HashTable:: HashingFunc(char elt[100])
{
    return strlen(elt)%maxelt;
}
void HashTable ::save(Trajet& valeur)
{
    int i=HashingFunc(valeur.depart);
    Data[i].savePile(valeur);
}
void HashTable :: read()
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
	    save(elt);
	    //2
	    strcpy(elt.depart,"Mvan");
	    strcpy(elt.arrivee,"Ekounou");
	    elt.date.jour=1;
	    elt.date.mois=3;
	    elt.date.annee=2022;
	    elt.prix=250;
	    elt.duree=20;
	    save(elt);
	    //3
	    strcpy(elt.depart,"Ekounou");
	    strcpy(elt.arrivee,"Ngoa Ekele");
	    elt.date.jour=4;
	    elt.date.mois=3;
	    elt.date.annee=2022;
	    elt.prix=400;
	    elt.duree=30;
	    save(elt);
	    //4
	    strcpy(elt.depart,"Poste");
	    strcpy(elt.arrivee,"Ngoa Ekele");
	    elt.date.jour=20;
	    elt.date.mois=3;
	    elt.date.annee=2022;
	    elt.prix=100;
	    elt.duree=7;
	    save(elt);
	    //5
	    strcpy(elt.depart,"Pakita");
	    strcpy(elt.arrivee,"Olembe");
	    elt.date.jour=3;
	    elt.date.mois=4;
	    elt.date.annee=2022;
	    elt.prix=500;
	    elt.duree=60;
	    save(elt);
	    //6
	    strcpy(elt.depart,"Nsam");
	    strcpy(elt.arrivee,"Ekounou");
	    elt.date.jour=1;
	    elt.date.mois=3;
	    elt.date.annee=2022;
	    elt.prix=250;
	    elt.duree=20;
	    save(elt);
}
bool HashTable ::search_elt(char d[100])
{
    int i=HashingFunc(d);
    return Data[i].search_(d);
}
int main()
{
    HashTable tab;
    tab.read();
    int i;
    for(i=0;i<tab.maxelt;i++)
    {
        cout<<i+1<<" :"<<endl;
        tab.Data[i].print_list();
    }
    char d[100];
    strcpy(d,"Ekounou");
    cout<<"\nLe resultat de la recherche de "<<d<<" est "<<tab.search_elt(d)<<endl;
    cout<<"\n(C) 2022 By MMCJ/INF-L1\n"<<endl;
    return 0;
}
