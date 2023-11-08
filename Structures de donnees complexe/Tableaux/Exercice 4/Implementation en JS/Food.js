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
class Table
{
	constructor ()
	{
		this.data= new Array();
		this.nbelt=0;
	}
	//Fonction pour stocker dans le tableau
	save(elt)
	{
		
		this.data[this.nbelt]=elt;
		this.nbelt=this.nbelt+1;
	}
	//Fonction pour lire les données
	read()
	{
		var dat,elt;
		dat =new Date(15,2,2022);
		elt=new Repas("Masculin",15,dat,"10h-14h","Okok","plat","Maison",6);
		this.save(elt);
		dat =new Date(13,3,2022);
		elt=new Repas("Feminin",10,dat,"14h-16h","Poulet","plat","Maison",9);
		this.save(elt);
		dat =new Date(15,5,2022);
		elt=new Repas("Masculin",18,dat,"16h-18h","Poisson","plat","Maison",1);
		this.save(elt);
		dat =new Date(15,7,2022);
		elt=new Repas("Masculin",25,dat,"08h-10h","Haricot","plat","Maison",3);
		this.save(elt);
		dat =new Date(10,8,2022);
		elt=new Repas("Masculin",13,dat,"18h-22h","Eru","plat","Resto",2);
		this.save(elt);
		dat =new Date(15,7,2022);
		elt=new Repas("Masculin",11,dat,"10h-14h","Koki","plat","Resto",3);
		this.save(elt);
		dat =new Date(15,7,2022);
		elt=new Repas("Masculin",28,dat,"08h-10h","Sanga","plat","Maison",4);
		this.save(elt);
		dat =new Date(15,7,2022);
		elt=new Repas("Masculin",23,dat,"08h-10h","Nkui","plat","Maison",7);
		this.save(elt);
	}
	//Permuter deux elements d'une liste
	echange(i,j)
	{
		var c;
		c=this.data[i];
		this.data[i]=this.data[j];
		this.data[j]=c;
	}
	sort_list()
	{
		var i,j;
		for (i=0;i<this.nbelt-1;i++)
		{
			var mini=i;
			for (j=i+1;j<this.nbelt;j++)
			{
				if (this.data[j].age<this.data[mini].age)
				{
					mini=j;
				}
			}
			this.echange(i,mini);
		}
	}
	seqSearch(elt)
	{
		var trouve=false;
		i=0;
		while(this.data[i].repas!=elt)and(i<this.nbelt)
		{
			if (this.data[i].repas===elt)
			{
				trouve=true;
			}
			i++;
		}
		return trouve;
	}
	print_list()
	{
		var i,elt;
		for(i=0;i<this.nbelt;i++)
		{
			elt=this.data[i];
			console.log(elt.repas+"\t"+elt.lieu+"\t"+elt.age+"\t"+elt.nbpers);
		}
	}
}
var tab= new Table();
tab.read();
console.log("\nTaille \n"+tab.nbelt);
tab.print_list();
tab.sort_list();
console.log("\nTaille \n"+tab.nbelt);
tab.print_list();
