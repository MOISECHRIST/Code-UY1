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
		elt=new Trajet("Beatitude","Ngoa Ekele",dat,400,60);
		this.save(elt);
		dat =new Date(13,3,2022);
		elt=new Trajet("Mvan","Ngoa Ekele",dat,300,40);
		this.save(elt);
		dat =new Date(15,5,2022);
		elt=new Trajet("Melen","Poste",dat,250,30);
		this.save(elt);
		dat =new Date(15,7,2022);
		elt=new Trajet("Education","Ngoa Ekele",dat,100,10);
		this.save(elt);
	}
	//
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
				if (this.data[j].prix<this.data[mini].prix)
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
		while(this.data[i].depart!=elt)and(i<this.nbelt)
		{
			if (this.data[i].depart===elt)
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
			console.log(elt.depart+"\t"+elt.arrivee+"\t"+elt.prix+"\t"+elt.duree);
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
