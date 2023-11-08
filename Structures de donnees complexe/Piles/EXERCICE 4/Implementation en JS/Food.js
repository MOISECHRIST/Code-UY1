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
//Definition de la classe pour stocker les donnees de nourriture
class Repas{
	constructor (sexe,age,date,heure,repas,unite,lieu,nbpers)
	{
		this.sexe=sexe;
		this.age=age;
		this.date=date;
		this.heure=heure;
		this.repas=repas;
		this.unite=unite;
		this.lieu=lieu;
		this.nbpers=nbpers;
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
				if (min.age > elt.age)
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
			while ((cur.next)&&(cur.data.age!==elt))
			{
				prec=cur;
				cur=cur.next;
				i++;
			}
			if(cur.data.age===elt)
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
			this.remove_elt(elt.age);
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
			console.log(tmp.data.heure+"\t"+tmp.data.repas+"\t"+tmp.data.lieu+"\t"+tmp.data.age+"\t"+tmp.data.nbpers);
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
			while ((tmp.next)&&(tmp.data.repas!==elt))
			{
				tmp=tmp.next;
			}
			if(tmp.data.repas===elt)
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
		elt=new Repas("Masculin",15,dat,"10h-14h","Okok","plat","Maison",6);
		this.save_first(elt);
		dat =new Date(13,3,2022);
		elt=new Repas("Feminin",10,dat,"14h-16h","Poulet","plat","Maison",9);
		this.save_first(elt);
		dat =new Date(15,5,2022);
		elt=new Repas("Masculin",18,dat,"16h-18h","Poisson","plat","Maison",1);
		this.save_first(elt);
		dat =new Date(15,7,2022);
		elt=new Repas("Masculin",25,dat,"08h-10h","Haricot","plat","Maison",3);
		this.save_first(elt);
		dat =new Date(10,8,2022);
		elt=new Repas("Masculin",13,dat,"18h-22h","Eru","plat","Resto",2);
		this.save_first(elt);
		dat =new Date(15,7,2022);
		elt=new Repas("Masculin",11,dat,"10h-14h","Koki","plat","Resto",3);
		this.save_first(elt);
		dat =new Date(15,7,2022);
		elt=new Repas("Masculin",28,dat,"08h-10h","Sanga","plat","Maison",4);
		this.save_first(elt);
		dat =new Date(15,7,2022);
		elt=new Repas("Masculin",23,dat,"08h-10h","Nkui","plat","Maison",7);
		this.save_first(elt);
	}
}

//la partir principale
var pile;
pile= new LinkedList();
pile.read();
console.log("La taille de la pile : "+pile.size_of_list());
pile.print_list();
console.log("\nLa taille de la pile : "+pile.size_of_list());
pile=pile.sort_list();
pile.print_list();
console.log("\nLe repas consommé par le plus jeune est : \n"+pile.minimum().heure+"\t"+pile.minimum().repas+"\t"+pile.minimum().lieu+"\t"+pile.minimum().age+"\t"+pile.minimum().nbpers);
console.log("\nResultat de la recherche : "+pile.search_elt("Koki"));
console.log("\n(C) 2022 By MMCJ/INF-L1");
