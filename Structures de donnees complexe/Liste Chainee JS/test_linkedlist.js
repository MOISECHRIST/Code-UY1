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
				if (min > elt)
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
			while ((cur.next)&&(cur.data!==elt))
			{
				prec=cur;
				cur=cur.next;
				i++;
			}
			if(cur.data===elt)
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
			this.remove_elt(elt);
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
			console.log(tmp.data);
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
			while ((tmp.next)&&(tmp.data!==elt))
			{
				tmp=tmp.next;
			}
			if(tmp.data===elt)
			{
				trouve=true;
			}	
		}
		return trouve;
	}
}

//la partir principale

var i,pile=new LinkedList();
pile.save_first(15);
pile.save_first(23);
pile.save_first(18);
pile.save_first(16);
pile.save_first(25);
pile.save_first(13);
pile.save_first(5);
pile.save_first(12);
for (let i=0;i<10;i++)
{
	pile.save_end(i+20);
}
console.log("La taille de la pile : "+pile.size_of_list());
pile.print_list();
console.log("La taille de la pile : "+pile.size_of_list());
pile=pile.sort_list();
pile.print_list();
console.log("Le minimum est : "+pile.minimum());
