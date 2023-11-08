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
//Definition de la structure de données pour manipuler les Foods
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
//Definition d'un noeud de Food
struct Node
{
    Food data;
    Node * next;
};
//Definition de la classe pile de Food
class Pile
{
    private:
        Node * tete;//La tete de pile

    public:

        Pile();//Initialiser de la tete de la pile à null
        void savePile (Food& valeur);//Fonction pour ajouter en tete
        void supp_elt (int p);//Fonction pour supprimer un element de la liste à partir de son point de repas
        Food minimum();//Fonction qui retourne le Food de age minimum
        void print_list ();//Fonction pour supprimer un element de la liste à partir
        int nbelt ();//Fonction qui retourne la taille de la pile
        bool search_(char d[100]);//Fonction qui recherche un Food dans la pile à partir de son point de repas et retoune 'true' si le Food se trouve dans la pile et 'false' sinon
};
Pile :: Pile(): tete(NULL){}
void Pile :: savePile (Food& valeur)
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
		Food elt=cur->data;
		int i=0;
		while((cur != NULL)&&(elt.age!=p))
		{
			prec=cur;
			cur=cur->next;
			i++;
		}
		if(elt.age==p)
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
Food Pile :: minimum()
{
	Food elt;
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
			if (tmp->data.age < elt.age)
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
		Food elt=cur->data;
		while((cur != NULL)&&(strcmp(elt.repas,d)!=0))
		{
			cur=cur->next;
		}
		if(strcmp(elt.repas,d)==0)
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
		Food elt;
		while (cur != NULL)
		{
			elt=cur->data;
			cout<<elt.heure<<"\t"<<elt.repas<<"\t"<<elt.age<<"\t"<<elt.nbpers<<endl;
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
        void save(Food& valeur);
        void read();
        bool search_elt(char d[100]);
};
HashTable :: HashTable(): maxelt(4){}
int HashTable:: HashingFunc(char elt[100])
{
    return strlen(elt)%maxelt;
}
void HashTable ::save(Food& valeur)
{
    int i=HashingFunc(valeur.repas);
    Data[i].savePile(valeur);
}
void HashTable :: read()
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
    strcpy(d,"Nkui");
    cout<<"\nLe resultat de la recherche de "<<d<<" est "<<tab.search_elt(d)<<endl;
    cout<<"\n(C) 2022 By MMCJ/INF-L1\n"<<endl;
    return 0;
}
