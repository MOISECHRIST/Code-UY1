//Definition de la classe Date
class Date
{
	constructor (jour,mois,annee)
	{
		this.jour=jour;
		this.mois=mois;
		this.annee=annee;
	}
}
//Definition de la classe Trajet
class Trajet
{
	constructor (depart,arrivee,date,prix,duree)
	{
		this.depart=depart;
		this.arrivee=arrivee;
		this.date=date;
		this.prix=prix;
		this.duree=duree;
	}
}
//Définition de la classe de noeud
class Node{
	constructor(elt)
	{
		this.data=elt;
		this.next=null;
	}
}
//Définition de la liste de noeuds
class LinkedList{
	constructor()
	{
		this.head=null;
	}
	//Fonction pour ajouter en tête de liste
	save_first(elt)
	{
		var node=new Node(elt);
		node.next=this.head;
		this.head=node;
	}
	//Fonction pour ajouter en fin de liste
	save_end(elt)
	{
		var node=new Node(elt);
		var tmp;
		if (this.head == null){
			this.head=node;
		}
		else
		{
			tmp=this.head;
			while(tmp.next)
			{
				tmp=tmp.next;
			}
			tmp.next=node;	
		}
	}
	//Fonction qui retourner la valeur minimale de la liste
	minimum()
	{
		var tmp,min,elt;
		if (this.head==null)
		{
			console.log("La liste est vide...");
			return null;
			
		}
		else
		{
			tmp=this.head;
			min=tmp.data;
			while(tmp)
			{
				elt=tmp.data;
				if (min.prix > elt.prix)
				{
					min=tmp.data;
				}
				tmp=tmp.next;
			}
			return min;
		}
	}
	//Fonction qui supprime un element de la liste
	remove_elt(elt)
	{
		var prec,cur,i;
		if (this.head==null)
		{
			console.log("La liste est vide...");
		}
		else
		{
			cur=this.head;
			i=0;
			while ((cur.next)&&(cur.data.prix!==elt))
			{
				prec=cur;
				cur=cur.next;
				i++;
			}
			if(cur.data.prix===elt)
			{
				if(i>0)
				{
					prec.next=cur.next;
				}
				else
				{
					this.head=cur.next;
				}
			}	
		}
		
	}
	//Fonction qui retourne la version triée de la liste
	sort_list()
	{
		var new_list=new LinkedList(),elt;
		while(this.head != null)
		{
			elt=this.minimum();
			this.remove_elt(elt.prix);
			new_list.save_first(elt);
		}
		return new_list;
	}
	//Fonction pour afficher la liste
	print_list()
	{
		var tmp=this.head;
		while(tmp)
		{
			console.log(tmp.data.depart+" "+tmp.data.prix);
			tmp=tmp.next;
		}
	}
	//Fonction qui retourne la taille de la liste
	size_of_list()
	{
		var tmp=this.head,nb=0;
		while(tmp)
		{
			nb++;
			tmp=tmp.next;
		}
		return nb
	}
	//Fonction qui indique si un element se trouve dans la liste
	search_elt(elt)
	{
		var tmp,min,elt,trouve;
		trouve=false;
		if (this.head==null)
		{
			console.log("La liste est vide...");
		}
		else
		{
			tmp=this.head;
			while ((tmp.next)&&(tmp.data.depart!==elt))
			{
				tmp=tmp.next;
			}
			if(tmp.data.depart===elt)
			{
				trouve=true;
			}	
		}
		return trouve;
	}
	//Fonction pour lire les données
	read()
	{
		var dat,elt;
		dat =new Date(15,2,2022);
		elt=new Trajet("Beatitude","Ngoa Ekele",dat,400,60);
		this.save_end(elt);
		dat =new Date(13,3,2022);
		elt=new Trajet("Mvan","Ngoa Ekele",dat,300,40);
		this.save_end(elt);
		dat =new Date(15,5,2022);
		elt=new Trajet("Melen","Poste",dat,250,30);
		this.save_end(elt);
		dat =new Date(15,7,2022);
		elt=new Trajet("Education","Ngoa Ekele",dat,100,10);
		this.save_end(elt);
	}
}

//la partir principale
var pile;
pile= new LinkedList();
pile.read();
console.log("La taille de la pile : "+pile.size_of_list());
pile.print_list();
var d="Beatitude";
console.log("Le resultat de la recherche de "+d+" est : "+pile.search_elt(d));
console.log("La taille de la pile : "+pile.size_of_list());
pile=pile.sort_list();
pile.print_list();
console.log("Le minimum est : "+pile.minimum().depart);
