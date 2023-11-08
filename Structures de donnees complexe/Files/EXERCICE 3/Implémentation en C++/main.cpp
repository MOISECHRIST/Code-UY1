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
//Definition de la classe file de trajet
class File
{
    private:
        Node * tete;//La tete de file 
     
    public:
        
        File();//Initialiser de la tete de la file à null
        void save (Trajet& valeur);//Fonction pour ajouter en tete
        void supp_elt (int p);//Fonction pour supprimer un element de la liste à partir de son point de depart
        Trajet minimum();//Fonction qui retourne le trajet de prix minimum
        void print_list ();//Fonction pour supprimer un element de la liste à partir
        int nbelt ();//Fonction qui retourne la taille de la file
        int search(char d[100]);//Fonction qui recherche un trajet dans la file à partir de son point de depart et retoune 'true' si le trajet se trouve dans la file et 'false' sinon
        void read();//Lire un ensemble de données
        //sort();//Fonction pour trier la file suivant les prix
};

File :: File(): tete(NULL){}
void File :: save (Trajet& valeur)
{
	Node *tmp= new Node, *cur=tete;
	tmp->data=valeur;
	if (tete==NULL)
	    {
	    	tete=tmp;
	    }
	else
	    {
		    while (cur->next != NULL)
		    {
		    	cur=cur->next;
		    }
		    cur->next=tmp;
	    }
}
void File :: supp_elt (int p)
{
	Node *prec, *cur;
	if (tete==NULL)
	{
		cout<<"La file est vide..."<<endl;
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
Trajet File :: minimum()
{
	Trajet elt;
	if (tete==NULL)
	{
		cout<<"La file est vide..."<<endl;
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
int File :: nbelt ()
{
	int n=0;
	if (tete==NULL)
	{
		cout<<"La file est vide..."<<endl;
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
int File :: search(char d[100])
{
	    int trouve=0;
	    Node *tmp=tete;
	    while((tmp!=NULL)&&(strcmp(tmp->data.depart,d)!=0))
	    {
		tmp=tmp->next;
	    }
	    if(strcmp(tmp->data.depart,d)==0)
	    {
		trouve=1;
	    }
	    return trouve;
	return trouve;
}
void File :: print_list ()
{
	if (tete==NULL)
	{
		cout<<"La file est vide..."<<endl;
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
void File :: read()
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
/*File :: sort():
{
	Node *tmp;
	File trie;
	trie.tete=tete;
	tmp=tete;
	Trajet elt;
	while(tete!=NULL)
	{
		elt=minimum();
		trie.supp_elt(elt.prix);
		save(elt);
	}
	tete=trie.tete;
}*/
int main()
{
    File file;
    file.read();
    cout<<"La file de donnees est :"<<endl;
    cout<<"Taille : "<<file.nbelt()<<endl;
    file.print_list();
    char d[100];
    strcpy(d,"Ekounou");
    cout<<"Le resultat de la recherche de "<<d<<" est : "<<file.search(d)<<endl;
    //file.sort();
    //cout<<"La file de donnees est :"<<endl;
    //cout<<"Taille : "<<file.nbelt()<<endl;
    //file=file.print_list();
    cout<<"(C) 2022 By MMCJ/INF-L1"<<endl;
    return 0;
}
