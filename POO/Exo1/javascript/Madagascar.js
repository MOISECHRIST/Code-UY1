//definition de la classe plat pour pouvoir organiser notre programme
const prompt = require("prompt-sync")({sigint:true});
class Plat{
    #TypePlat;
    #NomPlat;
    #IdPlat;
    constructor(IdPlat,NomPlat,DescriptionPlat,TypePlat,ListeIngredient,SourcePlat,RecettePlat){
        this.#IdPlat=IdPlat;
        this.#NomPlat=NomPlat;
        this.DescriptionPlat=DescriptionPlat;
        this.#TypePlat=TypePlat;
        this.ListeIngredient=ListeIngredient;
        this.SourcePlat=SourcePlat;
        this.RecettePlat=RecettePlat;
        this.tabAlPrin=[];
		this.nbAlPrin=0;
		this.tabAlProt=[];
		this.nbAlProt=0;
		this.tabCompl=[];
		this.nbCompl=0;
		this.tabEpices=[];
		this.nbEpices=0;
    }
    setNomPlat(NomPlat){
        this.#NomPlat=NomPlat;
    }
    setTypePlat(TypePlat){
        this.#TypePlat=TypePlat;
    }
    getNomPlat(){
        return this.#NomPlat;
    }
    getTypePlat(){
        return this.#TypePlat;
    }
    ajouterAlPrin(AlPrin){
        this.tabAlPrin=[AlPrin];
        this.nbAlPrin+=1;
    }
    ajouterAlProt(AlProt){
        this.tabAlProt=[AlProt];
        this.nbAlProt+=1;
    }
    ajouterCompl(compl){
        this.tabCompl=[compl];
        this.nbCompl+=1;
    }
    ajouterEpice(Epice){
        this.tabEpices=[Epice];
        this.nbEpices+=1;
    }
}
//definition de la class pour les epices 
class Epices{
    #NomEpice;
    constructor(NomEpice){
        this.#NomEpice=NomEpice;
    }
    afficherEpice(){
        return this.#NomEpice;
    } 
}
//definition de la classe complement
class Complement{
    #NomComplement;
    #QteComplement;
    #CouleurComplement;
    constructor(NomComplement, QteComplement,CouleurComplement){
        this.#NomComplement=NomComplement;
        this.#QteComplement=QteComplement;
        this.#CouleurComplement=CouleurComplement;
    }
    AfficherNomcomplement(){
        return this.#NomComplement;
    }
    AfficherQteComplement(){
        return this.#QteComplement;
    }
    afficherCouleurComplement(){
        return this.#CouleurComplement;
    }
}
//definition de la classe des aliments proteinées
class AlimentProteine{
    #NomProteine;
    #QteProteine;
    #MethodeCuissonProteine; 
    #TypeProteine;
    constructor(NomProteine, QteProteine, MethodeCuissonProteine, TypeProteine){
        this.#NomProteine=NomProteine;
        this.#QteProteine=QteProteine;
        this.#MethodeCuissonProteine=MethodeCuissonProteine;
        this.#TypeProteine=TypeProteine;
    }
    afficherNomProtine(){
        return this.#NomProteine;
    }
    afficherQteProteine(){
        return this.#QteProteine;
    }
    afficherTypeProteine(){
        return this.#TypeProteine;
    }
    afficherMethodeCuisson(){
        return this.#MethodeCuissonProteine;
    }
}
//definition de la class aliment principale
class AlimentPrincipal{
    #NomAliment;
    #TextureAliment;
    #CouleurAliment;
    constructor(NomAliment,TextureAliment,CouleurAliment){
        this.#NomAliment=NomAliment;
        this.#TextureAliment=TextureAliment;
        this.#CouleurAliment=CouleurAliment;
    }
    afficherNomAliment(){
        return this.#NomAliment;
    }
    modifierNomAliment(NomAliment){
        this.NomAliment=NomAliment;
    }
    afficherTextureAliment(){
        return this.#TextureAliment;
    }
    affichercouleurAliment(){
        return this.#CouleurAliment;
    }
}
//ecriture de la fonction main
var listPlat=[];
var nbPlat=0;
/*-------------------------------------------------------------*/
//Makatsia coco
var plat1= new Plat("Plat261Img34","Makatsia coco","Les petits pains se mangent encore chauds , ou tièdes , garnis servi avec de la pâte à tartiner au chocolat blanc et à la noix de coco","Patisserie","400 grammes de farine 20 grammes de levure de boulanger fraiche (ou 7 grammes sèche ) ","data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD","Dans le bol du pétrin de la machine à pain ( ou du robot , ou à la main , ça fonctionne aussi)  déposez l'eau tiède mélangée à la levure et à une cuillère à soupe du sucre.");
var AlPrin= new AlimentPrincipal("Makatsia coco","Solide","marron");
plat1.ajouterAlPrin(AlPrin);
listPlat.push(plat1);
nbPlat+=1;

/*-------------------------------------------------------------*/
//Godrogodro
var plat2= new Plat("Plat261Img35","Godrogodro","plat sucré traditionnellement très calorique dont la recette s’est fixée au fur et à mesure.","Patisserie","400 grammes de sucre 100 centilitres d’eau Cannelle en poudre Noix de muscade 1 gousse de vanille 8 cuillères à soupe d’huile 0,5 litre de lait de coco 500 grammes de semoule de blé dur","https://www.marmitedumonde.com/wp-content/uploads/2016/09/Godrogodro-gateaux-madagascar.jpg","Faire un caramel avec 400 grammes de sucre et 20 centilitres d’eau. Faire bouillir le lait de coco dans une casserole. Baisser le feu lorsque le lait a bouilli puis rajouter la moitié du caramel seulement. (Attention : le lait s’émulsionne au contact du caramel donc il faut verser petit à petit). Remuer bien puis laisser refroidir dans un bain-marie d’eau froide ou à température ambiante. Verser la semoule de blé dans le liquide froid. Ajouter les épices, 40 centilitres d’eau puis 5 cuillères à soupe d’huile. Cuire à feu doux en remuant sans cesse jusqu’à obtenir une pâte lisse et homogène. Tourner la pâte régulièrement jusqu’à ce qu’elle ne colle plus sur les bords (pour assurer une bonne cuisson de la pâte de godrogodro, n’hésitez pas à ajouter un verre d’eau). Beurrer une moule et ajouter de l’huile. Verser la pâte dedans en tassant bien. Verser ensuite le caramel restant sur le dessus. Enfourner pendant 20 minutes à 200°C. Laisser refroidir avant de servir.");
var AlPrin= new AlimentPrincipal("Godrogodro","Solide", "marron");
plat2.ajouterAlPrin(AlPrin);
listPlat.push(plat2);
nbPlat+=1;
/*-------------------------------------------------------------*/
//Langue de veau sauce tomate épicée, comme à Madagascar
var plat3= new Plat("Plat261Img36","Langue de veau sauce tomate, comme à Madagascar","Repas traditionnel malgache avec la langue de bœuf et servi avec du riz","Ragout","1 langue de veau (1kg environ) 1 morceau de gingembre frais 2 feuilles de laurier 4 oignons 3 clous de girofle 2 boîtes de cubes de tomate de 400g 2 cuill à soupe d'huile  1 pincée de piment en poudre (facultatif) 3 gousses d'ail","https://recettes.de/images/blogs/un-peu-gay-dans-les-coings/langue-de-veau-sauce-tomate-epicee-comme-a-madagascar.640x480.jpg","Si vous le pouvez, faites tremper la langue dans un grand volume d'eau froide salée pendant la nuit. Le jour même, faites cuire la langue dans un grand volume d'eau salée, avec un oignon piqué de trois clous de girofle, les deux feuilles de laurier et trois belles tranches de gingembre frais. Après ébullition, laisser mijoter 1h30 à deux heures (j'aime la langue très fondante, donc je privilégie la cuisson longue, 2h ou plus). Pendant la cuisson de la langue, préparez la sauce tomate: faites revenir les 3 oignons restants finement émincés dans deux cuill à soupe d'huile dans une sauteuse. Quand ils sont bien dorés, ajoutez une à deux cuill à soupe de gingembre frais en purée, et les trois gousses d'ail pressées. Faites revenir encore quelques minutes, avant d'ajoutez le piment en poudre si vous en utilisez, puis le contenu des deux boîtes de cubes de tomates, en les rinçant avec un peu d'eau que vous ajoutez également dans la sauteuse. Salez, poivrez et ajoutez éventuellement une pincée de sucre. Laissez mijoter la sauce tomate 15 à 30 minutes (vous pouvez l'allonger de bouillon et la mixer si vous le voulez, je la préfèrer avec des morceaux). Réservez. Quand le langue est cuite, sortez la de son bouillon, laissez la tiédir 2-3 minutes avant de la peler (ça se fait très facilement à la main). Coupez la langue en tranches fines, que vous pouvez retourner dans le bouillon jusqu'au moment de servir. Servez 2-3 tranches de langue par personne, nappez de sauce et accompagner par exemple de riz blanc.");
var AlPrin= new AlimentPrincipal("Sauce tomate","Liquide","Rouge");
plat3.ajouterAlPrin(AlPrin);
var AlProt= new AlimentProteine("Langue de veau",3,"Ebullition","Viande");
plat3.ajouterAlProt(AlProt);
var compl= new Complement("Riz",1,"Blanc");
plat3.ajouterCompl(compl);
listPlat.push(plat3);
nbPlat+=1;
/*-------------------------------------------------------------*/
//Carri de Crevette
var plat4= new Plat("Plat261Img37","carri de crevette","crevette a la sauce tomate servi avec du riz","Ragout","400 g de grosses crevettes 200 g de tomates 1 petit oignon 2 gousses d'ail 2 cm de gingembre frais 10 cl d'eau 1 c. à s. de beurre clarifié 1 c. à s. de curry en poudre 1/2 bouquet de coriandre fraîche 2 cubes de bouillon Kub Cari de crevettes","https://recettes.de/images/blogs/un-peu-gay-dans-les-coings/langue-de-veau-sauce-tomate-epicee-comme-a-madagascar.640x480.jpg","Si vous le pouvez, faites tremper la langue dans un grand volume d'eau froide salée pendant la nuit. Le jour même, faites cuire la langue dans un grand volume d'eau salée, avec un oignon piqué de trois clous de girofle, les deux feuilles de laurier et trois belles tranches de gingembre frais. Après ébullition, laisser mijoter 1h30 à deux heures (j'aime la langue très fondante, donc je privilégie la cuisson longue, 2h ou plus). Pendant la cuisson de la langue, préparez la sauce tomate: faites revenir les 3 oignons restants finement émincés dans deux cuill à soupe d'huile dans une sauteuse. Quand ils sont bien dorés, ajoutez une à deux cuill à soupe de gingembre frais en purée, et les trois gousses d'ail pressées. Faites revenir encore quelques minutes, avant d'ajoutez le piment en poudre si vous en utilisez, puis le contenu des deux boîtes de cubes de tomates, en les rinçant avec un peu d'eau que vous ajoutez également dans la sauteuse. Salez, poivrez et ajoutez éventuellement une pincée de sucre. Laissez mijoter la sauce tomate 15 à 30 minutes (vous pouvez l'allonger de bouillon et la mixer si vous le voulez, je la préfèrer avec des morceaux). Réservez. Quand le langue est cuite, sortez la de son bouillon, laissez la tiédir 2-3 minutes avant de la peler (ça se fait très facilement à la main). Coupez la langue en tranches fines, que vous pouvez retourner dans le bouillon jusqu'au moment de servir. Servez 2-3 tranches de langue par personne, nappez de sauce et accompagner par exemple de riz blanc.");
var AlPrin= new AlimentPrincipal("Sauce tomate","Liquide","Rouge");
plat4.ajouterAlPrin(AlPrin);
var AlProt= new AlimentProteine("crevette",3,"soupé","crustace");
plat4.ajouterAlProt(AlProt);
var compl= new Complement("Riz",1,"Blanc");
plat4.ajouterCompl(compl);
listPlat.push(plat4);
nbPlat+=1;
/*-------------------------------------------------------------*/
//Carri de Poulet
var plat5= new Plat("Plat261Img38","carri de poulet","viande de poulet qui se mange avec du riz,l’haricot st des feuilles de dose de safran","Soupe","1 poulet 2 cs d’huiles 2 oignons 6 tomates boite de haricot rouge 1 brin de thym 3 gousses d’ail 1 morceau de gingembre","https://recettes.de/images/blogs/un-peu-gay-dans-les-coings/langue-de-veau-sauce-tomate-epicee-comme-a-madagascar.640x480.jpg","Si vous le pouvez, faites tremper la langue dans un grand volume d'eau froide salée pendant la nuit. Le jour même, faites cuire la langue dans un grand volume d'eau salée, avec un oignon piqué de trois clous de girofle, les deux feuilles de laurier et trois belles tranches de gingembre frais. Après ébullition, laisser mijoter 1h30 à deux heures (j'aime la langue très fondante, donc je privilégie la cuisson longue, 2h ou plus). Pendant la cuisson de la langue, préparez la sauce tomate: faites revenir les 3 oignons restants finement émincés dans deux cuill à soupe d'huile dans une sauteuse. Quand ils sont bien dorés, ajoutez une à deux cuill à soupe de gingembre frais en purée, et les trois gousses d'ail pressées. Faites revenir encore quelques minutes, avant d'ajoutez le piment en poudre si vous en utilisez, puis le contenu des deux boîtes de cubes de tomates, en les rinçant avec un peu d'eau que vous ajoutez également dans la sauteuse. Salez, poivrez et ajoutez éventuellement une pincée de sucre. Laissez mijoter la sauce tomate 15 à 30 minutes (vous pouvez l'allonger de bouillon et la mixer si vous le voulez, je la préfèrer avec des morceaux). Réservez. Quand le langue est cuite, sortez la de son bouillon, laissez la tiédir 2-3 minutes avant de la peler (ça se fait très facilement à la main). Coupez la langue en tranches fines, que vous pouvez retourner dans le bouillon jusqu'au moment de servir. Servez 2-3 tranches de langue par personne, nappez de sauce et accompagner par exemple de riz blanc.");
var AlPrin= new AlimentPrincipal("harricot","solide","ecarlate");
plat5.ajouterAlPrin(AlPrin);
var AlProt= new AlimentProteine("Poulet",1,"soupé","viande");
plat5.ajouterAlProt(AlProt);
var compl= new Complement("Riz",1,"Blanc");
plat5.ajouterCompl(compl);
listPlat.push(plat5);
nbPlat+=1;

/*-------------------------------------------------------------*/
//Carri de crevette
var plat6= new Plat("Plat261Img39","carri au lait de coco","Crevettes soupé servie avec du riz","ragou","1 poulet 2 cs d’huiles 2 oignons 6 tomates boite de haricot rouge 1 brin de thym 3 gousses d’ail 1 morceau de gingembre","https://recettes.de/images/blogs/un-peu-gay-dans-les-coings/langue-de-veau-sauce-tomate-epicee-comme-a-madagascar.640x480.jpg","Si vous le pouvez, faites tremper la langue dans un grand volume d'eau froide salée pendant la nuit. Le jour même, faites cuire la langue dans un grand volume d'eau salée, avec un oignon piqué de trois clous de girofle, les deux feuilles de laurier et trois belles tranches de gingembre frais. Après ébullition, laisser mijoter 1h30 à deux heures (j'aime la langue très fondante, donc je privilégie la cuisson longue, 2h ou plus). Pendant la cuisson de la langue, préparez la sauce tomate: faites revenir les 3 oignons restants finement émincés dans deux cuill à soupe d'huile dans une sauteuse. Quand ils sont bien dorés, ajoutez une à deux cuill à soupe de gingembre frais en purée, et les trois gousses d'ail pressées. Faites revenir encore quelques minutes, avant d'ajoutez le piment en poudre si vous en utilisez, puis le contenu des deux boîtes de cubes de tomates, en les rinçant avec un peu d'eau que vous ajoutez également dans la sauteuse. Salez, poivrez et ajoutez éventuellement une pincée de sucre. Laissez mijoter la sauce tomate 15 à 30 minutes (vous pouvez l'allonger de bouillon et la mixer si vous le voulez, je la préfèrer avec des morceaux). Réservez. Quand le langue est cuite, sortez la de son bouillon, laissez la tiédir 2-3 minutes avant de la peler (ça se fait très facilement à la main). Coupez la langue en tranches fines, que vous pouvez retourner dans le bouillon jusqu'au moment de servir. Servez 2-3 tranches de langue par personne, nappez de sauce et accompagner par exemple de riz blanc.");
var AlPrin= new AlimentPrincipal("crevette soupé","solide","bleu marine");
plat6.ajouterAlPrin(AlPrin);
var AlProt= new AlimentProteine("crevette",3,"soupé","crustace");
plat6.ajouterAlProt(AlProt);
var compl= new Complement("Riz",1,"Blanc");
plat6.ajouterCompl(compl);
listPlat.push(plat6);
nbPlat+=1;

/*-------------------------------------------------------------*/
//Makatsia coco
var plat7=new Plat("Plat261Img40","Salade de mangue","Des immences de mangue avec des oignons rouge","salade","belle mangue verte et ferme (fruit pas mûr ou à peine, ceci n'est pas une variété de mangue),3 c à s d'huile de tournesol, le zeste d'1 petit citron jaune bio,1 c à s de jus de citron jaune, 1 petite gousse d'ail","data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD","Dans le bol du pétrin de la machine à pain ( ou du robot , ou à la main , ça fonctionne aussi)  déposez l'eau tiède mélangée à la levure et à une cuillère à soupe du sucre.");
var AlPrin= new AlimentPrincipal("Makatsia coco","Solide","marron");
plat7.ajouterAlPrin(AlPrin);
listPlat.push(plat7);
nbPlat+=1;

/*-------------------------------------------------------------*/
//Poulet vega
var plat8= new Plat("Plat261Img41","Poulet vega","C’est du poulet saucé a l’oignon qui est servie avec du riz et des petits poids","ragou","400g de substitut de poulet de votre choix De l’huile d’olive 6 petites tomates (ou 2 cuillères à soupe de concentré de tomates) 2 oignons, en quartiers 3 gousses d’ail 2 cm de gingembre frais, râpé 200ml de bouillon de légumes 400g de petits pois frais ou surgelés Épices de votre choix: cumin, curry doux,coriandre Sel et poivre","https://recettes.de/images/blogs/un-peu-gay-dans-les-coings/langue-de-veau-sauce-tomate-epicee-comme-a-madagascar.640x480.jpg","Si vous le pouvez, faites tremper la langue dans un grand volume d'eau froide salée pendant la nuit. Le jour même, faites cuire la langue dans un grand volume d'eau salée, avec un oignon piqué de trois clous de girofle, les deux feuilles de laurier et trois belles tranches de gingembre frais. Après ébullition, laisser mijoter 1h30 à deux heures (j'aime la langue très fondante, donc je privilégie la cuisson longue, 2h ou plus). Pendant la cuisson de la langue, préparez la sauce tomate: faites revenir les 3 oignons restants finement émincés dans deux cuill à soupe d'huile dans une sauteuse. Quand ils sont bien dorés, ajoutez une à deux cuill à soupe de gingembre frais en purée, et les trois gousses d'ail pressées. Faites revenir encore quelques minutes, avant d'ajoutez le piment en poudre si vous en utilisez, puis le contenu des deux boîtes de cubes de tomates, en les rinçant avec un peu d'eau que vous ajoutez également dans la sauteuse. Salez, poivrez et ajoutez éventuellement une pincée de sucre. Laissez mijoter la sauce tomate 15 à 30 minutes (vous pouvez l'allonger de bouillon et la mixer si vous le voulez, je la préfèrer avec des morceaux). Réservez. Quand le langue est cuite, sortez la de son bouillon, laissez la tiédir 2-3 minutes avant de la peler (ça se fait très facilement à la main). Coupez la langue en tranches fines, que vous pouvez retourner dans le bouillon jusqu'au moment de servir. Servez 2-3 tranches de langue par personne, nappez de sauce et accompagner par exemple de riz blanc.");
var AlPrin=new AlimentPrincipal("poulet soupé","solide","griée");
plat8.ajouterAlPrin(AlPrin);
var AlProt= new AlimentProteine("poulet",1,"soupé","viande");
plat8.ajouterAlProt(AlProt);
var compl =new Complement("Riz",1,"Blanc");
plat8.ajouterCompl(compl);
listPlat.push(plat8);
nbPlat+=1;

/*-------------------------------------------------------------*/
//Recherche de plat
console.log("caracteristique du plat desire");
console.log("Rubrique 1: Plat");
var infoPlat=prompt("quel type de plat desirez vous? [1=Ragout, 2=Soupe, 3=Patisserie, 4=Salade]:");
var infoPlat1=parseInt(infoPlat);
var line1;
var line2;
var line3;
if(infoPlat1==1){
    line1="Ragout";
}else if(infoPlat1==2){
     line1="Soupe";
}else if(infoPlat1==3){
    line1="Patisserie";
}else if(infoPlat1==4){
    line1="Salade";
}

console.log("Rubrique 2: Aliment Proteiné");
var infoProt=prompt("Votre plat contient'il des aliments proteinées? [0=Non, 1=Oui] :");
var infoProt1=parseInt(infoProt);
if(infoProt1>0){
    var infoProt=prompt("de quel type d'aliment proteiné avez vous envie? [1=Viande, 2=poisson, 3=Crustacé] :");
    var infoProt2=parseInt(infoProt);
    
    if(infoProt2==1){
        line2="viande";
    }else if(infoProt2==2){
       line2="Poisson";
    }else if(infoProt2==3){
       line2="Crustacer";
    }
}
console.log("Rubrique 3 :Complement");
var infocomp=prompt("votre plat contient-il des complements ? [0=Non, 1=Oui]:");
var infocomp1=parseInt(infocomp);
if(infocomp1>0){
    var info=prompt("De quel complement avez vous envie ?[1=Riz,2=Pomme,3=***]:");
    var infocomp2=parseInt(info);
    if(infocomp2==1){
        line3="Riz";
    }else if(infocomp2==2){
        line3="Pomme";
    }else if(infocomp2==3){
        line3="****";
    }
}
console.log("Rubrique4 :Epices");
var info=prompt("Votre plat a t-il des epices visibles ? [0=Non, 1=Oui] :");
var infoEpice=parseInt(info);
var nbTrouver=0;
var i,j,k;
for(i=0;i<nbPlat;i++){
    if(listPlat[i].getTypePlat()==line1){
        if(infoProt1!=0){
            if(listPlat[i].nbAlProt!=0){
                for(j=0;j<listPlat[i].nbAlProt;j++){
                    if(listPlat[i].tabAlProt[j].afficherTypeProteine()==line2){
                        if(infocomp1>1){
                            if(listPlat[i].nbCompl!=0){
                                for(k=1;k<=listPlat[i].nbCompl;k++){
                                    if(listPlat[i].tabCompl[k].AfficherNomComplement()==line3){
                                        if(infoEpice!=0){
                                            if(listPlat[i].nbEpices!=0){
                                                console.log("\nPlat :\n",listPlat[i].getNomPlat(),"\nDescritpion :\n",listPlat[i].DescriptionPlat,"\nRecette :\n"+listPlat[i].RecettePlat);
                                                nbTrouver+=1;
                                            }
                                        }else{
                                            console.log("\nPlat :\n",listPlat[i].getNomPlat(),"\nDescription :\n",listPlat[i].DescriptionPlat,"\nRecette :\n"+listPlat[i].RecettePlat);
                                            nbTrouver+=1;
                                        }
                                    }
                                }
                            }
                        }else if(infoEpice!=0){
                                if(listPlat[i].nbEpices!=0){
                                    console.log("\nPlat :\n",listPlat[i].getNomPlat(),"\nDescription :\n",listPlat[i].DescriptionPlat,"\nRecette :\n",listPlat[i].RecettePlat);
                                    nbTrouver+=1;
                                }
                            }else{
                                console.log("\nPlat :\n",listPlat[i].getNomPlat(),"\nDescription :\n",listPlat[i].DescriptionPlat,"\nRecette :\n",listPlat[i].RecettePlat);
                                nbTrouver+=1;
                            }
                        }
                }
            }else if(infocomp1>0){
                if(listPlat[i].nbCompl!=0){
                    for(k=0;k<listPlat[i].nbCompl;k++){
                        if(listPlat[i].tabCompl[k].AfficherNomComplement()==line3){
                            if(infoEpice!=0){
                                if(listPlat[i].nbEpices!=0){
                                    console.log("\nPlat :\n",listPlat[i].getNomPlat(),"\nDescription :\n",listPlat[i].DescriptionPlat,"\nRecette :\n",listPlat[i].RecettePlat);
                                    nbTrouver+=1;
                                }
                            }else{
                                console.log("\nPlat :\n",listPlat[i].getNomPlat(),"\nDescription :\n",listPlat[i].DescriptionPlat,"\nRecette :\n",listPlat[i].RecettePlat);
                                nbTrouver+=1;
                            }
                        }
                    }
                }else if(infoEpice!=0){
                    if(listPlat[i].nbEpices!=0){
                        console.log("\nPlat :\n",listPlat[i].getNomPlat(),"\nDescription :\n",listPlat[i].DescriptionPlat,"\nRecette :\n",listPlat[i].RecettePlat);
                        nbTrouver+=1;
                    }
                }else{
                    console.log("\nPlat :\n",listPlat[i].getNomPlat(),"\nDescription :\n",listPlat[i].DescriptionPlat,"\nRecette :\n",listPlat[i].RecettePlat);
                    nbTrouver+=1;
                }
            }
        }
    }
}
if(nbTrouver==0){
    console.log("Aucun plat Trouver");
}
//a = (Math.random() * nbplats)% (nbplats - 1)