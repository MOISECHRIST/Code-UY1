import java.util.Scanner;

public class Madagascar{
	public static void main(String[] agrs)
	{
		Plat listPlat[] = new Plat[50];
		int nbPlat=0;
		//Plat(String IdPlat,String NomPlat,String DescriptionPlat,String TypePlat,String ListeIngredient,String SourcePlat,String RecettePlat)
		//AlimentPrincipal(String NomAliment, String TextureAliment, String CouleurAliment)
		//Data Entry
		/*-------------------------------------------------------------*/
		//Makatsia coco
		Plat plat = new Plat("Plat261Img34","Makatsia coco","Les petits pains se mangent encore chauds , ou tièdes , garnis servi avec de la pâte à tartiner au chocolat blanc et à la noix de coco","Patisserie","400 grammes de farine 20 grammes de levure de boulanger fraiche (ou 7 grammes sèche ) ","data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD","Dans le bol du pétrin de la machine à pain ( ou du robot , ou à la main , ça fonctionne aussi)  déposez l'eau tiède mélangée à la levure et à une cuillère à soupe du sucre.");
		AlimentPrincipal AlPrin = new AlimentPrincipal("Makatsia coco","Solide","marron");
		plat.ajouterAlPrin(AlPrin);
		listPlat[nbPlat]=plat;
		nbPlat++;
		//Godrogodro
		plat = new Plat("Plat261Img35","Godrogodro","plat sucré traditionnellement très calorique dont la recette s’est fixée au fur et à mesure.","Patisserie","400 grammes de sucre 100 centilitres d’eau Cannelle en poudre Noix de muscade 1 gousse de vanille 8 cuillères à soupe d’huile 0,5 litre de lait de coco 500 grammes de semoule de blé dur","https://www.marmitedumonde.com/wp-content/uploads/2016/09/Godrogodro-gateaux-madagascar.jpg","Faire un caramel avec 400 grammes de sucre et 20 centilitres d’eau. Faire bouillir le lait de coco dans une casserole. Baisser le feu lorsque le lait a bouilli puis rajouter la moitié du caramel seulement. (Attention : le lait s’émulsionne au contact du caramel donc il faut verser petit à petit). Remuer bien puis laisser refroidir dans un bain-marie d’eau froide ou à température ambiante. Verser la semoule de blé dans le liquide froid. Ajouter les épices, 40 centilitres d’eau puis 5 cuillères à soupe d’huile. Cuire à feu doux en remuant sans cesse jusqu’à obtenir une pâte lisse et homogène. Tourner la pâte régulièrement jusqu’à ce qu’elle ne colle plus sur les bords (pour assurer une bonne cuisson de la pâte de godrogodro, n’hésitez pas à ajouter un verre d’eau). Beurrer une moule et ajouter de l’huile. Verser la pâte dedans en tassant bien. Verser ensuite le caramel restant sur le dessus. Enfourner pendant 20 minutes à 200°C. Laisser refroidir avant de servir.");
		AlPrin = new AlimentPrincipal("Godrogodro","Solide", "marron");
		plat.ajouterAlPrin(AlPrin);
		listPlat[nbPlat]=plat;
		nbPlat++;
		//Langue de veau sauce tomate épicée, comme à Madagascar
		plat = new Plat("Plat261Img36","Langue de veau sauce tomate, comme à Madagascar","Repas traditionnel malgache avec la langue de bœuf et servi avec du riz","Ragout","1 langue de veau (1kg environ) 1 morceau de gingembre frais 2 feuilles de laurier 4 oignons 3 clous de girofle 2 boîtes de cubes de tomate de 400g 2 cuill à soupe d'huile  1 pincée de piment en poudre (facultatif) 3 gousses d'ail","https://recettes.de/images/blogs/un-peu-gay-dans-les-coings/langue-de-veau-sauce-tomate-epicee-comme-a-madagascar.640x480.jpg","Si vous le pouvez, faites tremper la langue dans un grand volume d'eau froide salée pendant la nuit. Le jour même, faites cuire la langue dans un grand volume d'eau salée, avec un oignon piqué de trois clous de girofle, les deux feuilles de laurier et trois belles tranches de gingembre frais. Après ébullition, laisser mijoter 1h30 à deux heures (j'aime la langue très fondante, donc je privilégie la cuisson longue, 2h ou plus). Pendant la cuisson de la langue, préparez la sauce tomate: faites revenir les 3 oignons restants finement émincés dans deux cuill à soupe d'huile dans une sauteuse. Quand ils sont bien dorés, ajoutez une à deux cuill à soupe de gingembre frais en purée, et les trois gousses d'ail pressées. Faites revenir encore quelques minutes, avant d'ajoutez le piment en poudre si vous en utilisez, puis le contenu des deux boîtes de cubes de tomates, en les rinçant avec un peu d'eau que vous ajoutez également dans la sauteuse. Salez, poivrez et ajoutez éventuellement une pincée de sucre. Laissez mijoter la sauce tomate 15 à 30 minutes (vous pouvez l'allonger de bouillon et la mixer si vous le voulez, je la préfèrer avec des morceaux). Réservez. Quand le langue est cuite, sortez la de son bouillon, laissez la tiédir 2-3 minutes avant de la peler (ça se fait très facilement à la main). Coupez la langue en tranches fines, que vous pouvez retourner dans le bouillon jusqu'au moment de servir. Servez 2-3 tranches de langue par personne, nappez de sauce et accompagner par exemple de riz blanc.");
		AlPrin = new AlimentPrincipal("Sauce tomate","Liquide","Rouge");
		plat.ajouterAlPrin(AlPrin);
		AlimentProteine AlProt = new AlimentProteine("Langue de veau",3,"Ebullition","Viande");
		plat.ajouterAlProt(AlProt);
		Complement Compl = new Complement("Riz",1,"Blanc");
		plat.ajouterCompl(Compl);
		listPlat[nbPlat]=plat;
		nbPlat++;
		/*-------------------------------------------------------------*/
		//Recherche de plat
		int infoTypePlat,infoAlProt1,infoAlProt2,infoCompl1,infoCompl2,infoEpice;
		String line1="",line2="",line3="";
		System.out.println("Caracteristiques du plat desire");
		System.out.println("Rubrique 1 : Plat");
		System.out.print("Quel type de plat desirez-vous ? [1=Ragout, 2=Soupe, 3=Patisserie] :");
		Scanner Console = new Scanner(System.in);
		infoTypePlat = Console.nextInt();
		switch(infoTypePlat)
		{
			case 1: 
				line1="Ragout";
				break;
			case 2: line1="Soupe";
				break;
			case 3: line1="Patisserie";
				break;
		}
		System.out.println("Rubrique 2 : Aliment proteine");
		System.out.print("Votre plat contient-il des aliments proteine ? [0=Non, 1=Oui] :");
		infoAlProt1 = Console.nextInt();
		if(infoAlProt1>0)
		{
			System.out.print("De quel type est cet aliment proteine avez vous envie ? [1=Viande, 2=Poisson, 3=Crustace] :");
			infoAlProt2 = Console.nextInt();
			switch(infoAlProt2)
			{
				case 1: 
					line2="Viande";
					break;
				case 2: line2="Poisson";
					break;
				case 3: line2="Crustace";
					break;
			}
		}
		System.out.println("Rubrique 3 : Complement");
		System.out.print("Votre plat contient-il des complements ? [0=Non, 1=Oui] :");
		infoCompl1 = Console.nextInt();
		if(infoCompl1>0)
		{
			System.out.print("De quel complement avez vous envie ? [1=Riz, 2=Pomme, 3=****] :");
			infoCompl2 = Console.nextInt();
			switch(infoCompl2)
			{
				case 1: 
					line3="Riz";
					break;
				case 2: line3="Pomme";
					break;
				case 3: line3="*****";
					break;
			}
		}
		System.out.println("Rubrique 4 : Epices");
		System.out.print("Votre plat a t-il des epices visibles ? [0=Non, 1=Oui] :");
		infoEpice = Console.nextInt();
		int i,j,k;
		int nbTrouve=0;
		for(i=0;i<nbPlat;i++)
		{
			if(listPlat[i].getTypePlat()==line1)
			{
				if(infoAlProt1!=0)
				{
					if(listPlat[i].nbAlProt!=0)
					{
						for(j=0;j<listPlat[i].nbAlProt;j++)
						{
							if(listPlat[i].tabAlProt[j].AfficherTypeProteine()==line2)
							{
								if(infoCompl1>0)
								{
									if(listPlat[i].nbCompl!=0)
									{
										for(k=0;k<listPlat[i].nbCompl;k++)
										{
											if(listPlat[i].tabCompl[k].AfficherNomComplement()==line3)
											{
												if(infoEpice!=0)
												{
													if(listPlat[i].nbEpices!=0)
													{
														System.out.println("\nPlat :\n"+listPlat[i].getNomPlat()+"\nDescription :\n"+listPlat[i].mDescriptionPlat+"\nRecette :\n"+listPlat[i].mRecettePlat);
														nbTrouve++;
													}
												}
												else
												{
													System.out.println("\nPlat :\n"+listPlat[i].getNomPlat()+"\nDescription :\n"+listPlat[i].mDescriptionPlat+"\nRecette :\n"+listPlat[i].mRecettePlat);
													nbTrouve++;
												}
											}
										}
									}
								}
								else
								{
									if(infoEpice!=0)
									{
										if(listPlat[i].nbEpices!=0)
										{
											System.out.println("\nPlat :\n"+listPlat[i].getNomPlat()+"\nDescription :\n"+listPlat[i].mDescriptionPlat+"\nRecette :\n"+listPlat[i].mRecettePlat);
											nbTrouve++;
										}
									}
									else
									{
										System.out.println("\nPlat :\n"+listPlat[i].getNomPlat()+"\nDescription :\n"+listPlat[i].mDescriptionPlat+"\nRecette :\n"+listPlat[i].mRecettePlat);
										nbTrouve++;
									}
								}
							}
						}
					}
				}
				else
				{
					if(infoCompl1>0)
					{
						if(listPlat[i].nbCompl!=0)
						{
							for(k=0;k<listPlat[i].nbCompl;k++)
							{
								if(listPlat[i].tabCompl[k].AfficherNomComplement()==line3)
								{
									if(infoEpice!=0)
									{
										if(listPlat[i].nbEpices!=0)
										{
											System.out.println("\nPlat :\n"+listPlat[i].getNomPlat()+"\nDescription :\n"+listPlat[i].mDescriptionPlat+"\nRecette :\n"+listPlat[i].mRecettePlat);
											nbTrouve++;
										}
									}
									else
									{
										System.out.println("\nPlat :\n"+listPlat[i].getNomPlat()+"\nDescription :\n"+listPlat[i].mDescriptionPlat+"\nRecette :\n"+listPlat[i].mRecettePlat);
										nbTrouve++;
									}
								}
							}
						}
					}
					else
					{
						if(infoEpice!=0)
						{
							if(listPlat[i].nbEpices!=0)
							{
								System.out.println("\nPlat :\n"+listPlat[i].getNomPlat()+"\nDescription :\n"+listPlat[i].mDescriptionPlat+"\nRecette :\n"+listPlat[i].mRecettePlat);
								nbTrouve++;
							}
						}
						else
						{
							System.out.println("\nPlat :\n"+listPlat[i].getNomPlat()+"\nDescription :\n"+listPlat[i].mDescriptionPlat+"\nRecette :\n"+listPlat[i].mRecettePlat);
							nbTrouve++;
						}
					}
				}
			}
		}
		if(nbTrouve==0)
		{
			System.out.println("Aucun plat trouve");
		}
	}
}
