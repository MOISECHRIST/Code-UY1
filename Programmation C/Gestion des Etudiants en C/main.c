#include <stdio.h>
#include <stdlib.h>
#include<string.h>
/*NOM &PRENOM : MEKA MOISE CHRISTIAN JUNIOR
MATRICULE : 21T2561*/
//Question 1: Fonction saisir()
struct etudiant
{
    int ncin;
    char nom[20];
    char prenom[20];
    int age;
    char filiere[20];
    char niveau[5];
    float cotisation[5];
};
//Question 2 : Fonction Saisir
void saisir()
{
    FILE *fichier;
    fichier=fopen("Etudiants.txt","a");
    if (fichier==NULL)
    {
        printf("\nErreur lors de l'ouverture du fichier\n");
        exit(1);
    }
    printf("Fichier ouvert avec succes");
    struct etudiant E;
    int i=1,j,choix=1;
    while (choix!=0)
    {
        printf("\nEntrer les donnees de l'etudiant numero %d\n",i);
        printf("Numero CNI : ");
        scanf("%d",&E.ncin);
        printf("Nom : ");
        scanf("%s",&E.nom);
        printf("Prenom : ");
        scanf("%s",&E.prenom);
        printf("Age : ");
        scanf("%d",&E.age);
        printf("Filiere : ");
        scanf("%s",&E.filiere);
        printf("Niveau : ");
        scanf("%s",&E.niveau);
        printf("Entrer les cotisations :\n");
        for (j=0;j<=4;j++)
        {
            printf("%d : ",j+1);
            scanf("%f",&E.cotisation[j]);
        }
        i++;
        fprintf(fichier,"%d ;%s ;%s ;%d ;%s ;%s ;%f ;%f ;%f ;%f ;%f \n",E.ncin,E.nom,E.prenom,E.age,E.filiere,E.niveau,E.cotisation[0],E.cotisation[1],E.cotisation[2],E.cotisation[3],E.cotisation[4]);
        printf("\nVoulez vous entrer un nouvel etudiant ? 1=Oui/0=Non : ");
        scanf("%d",&choix);
        while ((choix!=0)&&(choix!=1))
        {
            printf("\nErreur. Veillez reessayer !");
            printf("\nVoulez vous entrer un nouvel etudiant ? 1=Oui/0=Non : ");
            scanf("%d",&choix);
        }
    }
    fclose(fichier);
}
//Question 3 : Fonction Ajouter(), Modifier() et supprimer() dans ficher concours.txt
//1- Ajouter()
void ajouter()
{
    FILE *fichier;
    fichier=fopen("Etudiants.txt","a");
    if (fichier==NULL)
    {
        printf("\nErreur lors de l'ouverture du fichier\n");
        exit(1);
    }
    printf("Fichier ouvert avec succes");
    struct etudiant E;
    int j;
    printf("\nEntrer les donnees de l'etudiant :\n");
    printf("Numero CNI : ");
    scanf("%d",&E.ncin);
    printf("Nom : ");
    scanf("%s",&E.nom);
    printf("Prenom : ");
    scanf("%s",&E.prenom);
    printf("Age : ");
    scanf("%d",&E.age);
    printf("Filiere : ");
    scanf("%s",&E.filiere);
    printf("Niveau : ");
    scanf("%s",&E.niveau);
    printf("Entrer les cotisations :\n");
    for (j=0;j<=4;j++)
    {
        printf("%d : ",j+1);
        scanf("%f",&E.cotisation[j]);
    }
    fprintf(fichier,"%d ;%s ;%s ;%d ;%s ;%s ;%f ;%f ;%f ;%f ;%f \n",E.ncin,E.nom,E.prenom,E.age,E.filiere,E.niveau,E.cotisation[0],E.cotisation[1],E.cotisation[2],E.cotisation[3],E.cotisation[4]);
    fclose(fichier);
}
//Fonction lecture() pour copier les données du fichierconcours dans la structure de données
void  lecture(struct etudiant T[100],int* n)
{
    FILE *fichier;
    fichier=fopen("Etudiants.txt","r");
    if (fichier==NULL)
    {
        printf("\nErreur lors de l'ouverture du fichier\n");
        exit(1);
    }
    struct etudiant E;
    int i=0;
    printf("Fichier Etudiants.txt ouvert avec succes\n");
    while(fscanf(fichier,"%d ;%s ;%s ;%d ;%s ;%s ;%f ;%f ;%f ;%f ;%f \n",&E.ncin,&E.nom,&E.prenom,&E.age,&E.filiere,&E.niveau,&E.cotisation[0],&E.cotisation[1],&E.cotisation[2],&E.cotisation[3],&E.cotisation[4])!=EOF)
    {
        T[i]=E;
        i++;
    }
    *n=i;
    fclose(fichier);
    printf("\n   %d Etudiant(s) retrouvé(s) dans le fichiers\n",*n);
}
//2- Modifier()
void modifier()
{
    struct etudiant T[100];
    int i,j,n;
    lecture(T,&n);
    int CNI;
	printf("\nEntrer le numero de la CNI de l'etudiant recherche : ");
	scanf("%d",&CNI);
	FILE *fichier;
    fichier=fopen("Etudiants.txt","w");
    if (fichier==NULL)
    {
        printf("\nErreur lors de l'ouverture du fichier\n");
        exit(1);
    }
    int choix;
	//On cherche d'abord les données du candidat
	for (i=0;i<n;i++)
    {
        if (CNI==T[i].ncin)
        {
            printf("L'etudiant dont on veut modifier les donnees est à la position %d :\n",i+1);
            printf("Numero CNI : %d\n",T[i].ncin);
            printf("Nom :%s\n",T[i].nom);
            printf("Prenom :%s\n",T[i].prenom);
            printf("Age :%d\n",T[i].age);
            printf("Filiere :%s\n",T[i].filiere);
            printf("Niveau :%s\n",T[i].niveau);
            for (j=0;j<5;j++)
            {
                printf("cotisation numero %d : %.2f\n",j+1,T[i].cotisation[j]);
            }
            printf("\nEntrer l'element à modifier\n");
            printf("-->0:Numero CNI\n-->1: Nom\n-->2: Prenom\n-->3: Age\n-->4:Filiere\n-->5:Niveau\n-->6:Cotisation 1\n-->7:Cotisation 2\n-->8:Cotisation 3\n-->9:Cotisation 4\n-->10:Cotisation 5\n-->11:Plusieurs information \n");
            printf("Choix : ");
            scanf("%d",&choix);
            switch (choix)
            {
                case 0:scanf("%d",&T[i].ncin);break;
                case 1:scanf("%s",&T[i].nom);break;
                case 2:scanf("%s",&T[i].prenom);break;
                case 3:scanf("%d",&T[i].age);break;
                case 4:scanf("%s",&T[i].filiere);break;
                case 5:scanf("%s",&T[i].niveau);break;
                case 6:scanf("%f",&T[i].cotisation[0]);break;
                case 7:scanf("%f",&T[i].cotisation[1]);break;
                case 8:scanf("%f",&T[i].cotisation[2]);break;
                case 9:scanf("%f",&T[i].cotisation[3]);break;
                case 10:scanf("%f",&T[i].cotisation[4]);break;
                case 11:
                {
                    scanf("%d",&T[i].ncin);
                    scanf("%s",&T[i].nom);
                    scanf("%s",&T[i].prenom);
                    scanf("%d",&T[i].age);
                    scanf("%s",&T[i].filiere);
                    scanf("%s",&T[i].niveau);
                    scanf("%f",&T[i].cotisation[0]);
                    scanf("%f",&T[i].cotisation[1]);
                    scanf("%f",&T[i].cotisation[2]);
                    scanf("%f",&T[i].cotisation[3]);
                    scanf("%f",&T[i].cotisation[4]);
                }break;
            };
            for (j=0;j<n;j++)
                fprintf(fichier,"%d ;%s ;%s ;%d ;%s ;%s ;%f ;%f ;%f ;%f ;%f \n",T[j].ncin,T[j].nom,T[j].prenom,T[j].age,T[j].filiere,T[j].niveau,T[j].cotisation[0],T[j].cotisation[1],T[j].cotisation[2],T[j].cotisation[3],T[j].cotisation[4]);
            break;
        }
        else if (i==n-1)
        {
            printf("Numero CIN ne se trouve pas dans le fichier !!!\n");
            for (j=0;j<n;j++)
                fprintf(fichier,"%d ;%s ;%s ;%d ;%s ;%s ;%f ;%f ;%f ;%f ;%f \n",T[j].ncin,T[j].nom,T[j].prenom,T[j].age,T[j].filiere,T[j].niveau,T[j].cotisation[0],T[j].cotisation[1],T[j].cotisation[2],T[j].cotisation[3],T[j].cotisation[4]);

        }
    }
	fclose(fichier);
}
//3- Supprimer()
void supprimer(CNI)
{
	struct etudiant T[100];
	int j,i,n;
	//On cherche d'abord les données du candidat
	lecture(T,&n);
	FILE *fichier;
    fichier=fopen("Etudiants.txt","w");
    if (fichier==NULL)
    {
        printf("\nErreur lors de l'ouverture du fichier\n");
        exit(1);
    }
    for (i=0;i<n;i++)
    {
        if (CNI==T[i].ncin)
        {
            printf("L'etudiant recherché est à la position %d\n",i+1);
            printf("Numero CNI : %d\n",T[i].ncin);
            printf("Nom :%s\n",T[i].nom);
            printf("Prenom :%s\n",T[i].prenom);
            printf("Age :%d\n",T[i].age);
            printf("Filiere :%s\n",T[i].filiere);
            printf("Niveau :%s\n",T[i].niveau);
            for (j=0;j<5;j++)
            {
                printf("cotisation numero %d : %.2f\n",j+1,T[i].cotisation[j]);
            }
            for (j=i+1;j<n;j++)
            {
                T[j-1]=T[j];
            }
            n--;
            for (j=0;j<n;j++)
                fprintf(fichier,"%d ;%s ;%s ;%d ;%s ;%s ;%f ;%f ;%f ;%f ;%f \n",T[j].ncin,T[j].nom,T[j].prenom,T[j].age,T[j].filiere,T[j].niveau,T[j].cotisation[0],T[j].cotisation[1],T[j].cotisation[2],T[j].cotisation[3],T[j].cotisation[4]);
            break;
        }
        else if (i==n-1)
        {
            printf("Numero CIN ne se trouve pas dans le fichier !!!\n");
            for (j=0;j<n;j++)
                fprintf(fichier,"%d ;%s ;%s ;%d ;%s ;%s ;%f ;%f ;%f ;%f ;%f \n",T[j].ncin,T[j].nom,T[j].prenom,T[j].age,T[j].filiere,T[j].niveau,T[j].cotisation[0],T[j].cotisation[1],T[j].cotisation[2],T[j].cotisation[3],T[j].cotisation[4]);

        }
    }
	fclose(fichier);
}
//Question 4: Fonction Afficher()
void afficher()
{
	struct etudiant T[100];
	int j,i=0,n;
	//On cherche d'abord les données du candidat
    lecture(T,&n);
	float som[100];
	for (i=0;i<n;i++)
	{
		som[i]=0;
		printf("\nDonnees de l'etudiant numero %d :\n",i+1);
		printf("Numero CNI : %d\n",T[i].ncin);
		printf("Nom : %s\n",T[i].nom);
		printf("Prenom : %s\n",T[i].prenom);
		printf("Age : %d\n",T[i].age);
		printf("Filiere : %s\n",T[i].filiere);
		printf("Niveau : %s\n",T[i].niveau);
		for (j=0;j<5;j++)
		{
			printf("cotisation numero %d : %.2f\n",j+1,T[i].cotisation[j]);
			som[i]+=T[i].cotisation[j];
		}
		printf("Total cotisation est : %.2f",som[i]);
		printf("\n\n");
	}
}
//Question 5: Fonction solvable()
void solvable()
{
    struct etudiant T[100];
    int j,i,n;
    lecture(T,&n);
	float som[100];
    for (i=0;i<n;i++)
    {
        som[i]=0;
		printf("\nDonnees de l'etudiant numero %d :\n",i+1);
		printf("Numero CNI : %d\n",T[i].ncin);
		printf("Nom :%s\n",T[i].nom);
		printf("Prenom :%s\n",T[i].prenom);
		printf("Age :%d\n",T[i].age);
		printf("Filiere :%s\n",T[i].filiere);
		printf("Niveau :%s\n",T[i].niveau);
        for (j=0;j<=4;j++)
        {
            printf("cotisation numero %d : %.2f\n",j+1,T[i].cotisation[j]);
			som[i]+=T[i].cotisation[j];
        }
        printf("Total cotisation est : %.2f\n",som[i]);
    }
    FILE *g;
    g=fopen("Etat.txt","w");
    if (g==NULL)
    {
        printf("Erreur lors de l'ouverture du fichier Etat.txt");
        exit(1);
    }
    for (i=0;i<n;i++)
        fprintf(g,"%d ;%s ;%s ;%d ;%s ;%s ;%f ;%f ;%f ;%f ;%f ;%f \n",T[i].ncin,T[i].nom,T[i].prenom,T[i].age,T[i].filiere,T[i].niveau,T[i].cotisation[0],T[i].cotisation[1],T[i].cotisation[2],T[i].cotisation[3],T[i].cotisation[4],som[i]);
    fclose(g);
}
//Question 6: Fonction insolvable()
void insolvable()
{
    FILE *fichier;
    struct etudiant T[100],I[100];
    int j,i,k=0,n;
    lecture(T,&n);
	int nbre;
    for (i=0;i<n;i++)
    {
        nbre=0;
        for (j=0;j<=4;j++)
        {
            if (T[i].cotisation[j]==0)
                 nbre+=1;
        }
        if (nbre!=0)
        {
            I[k]=T[i];
            k++;
        }
    }
    FILE *g;
    g=fopen("Mauvais.txt","w");
    if (g==NULL)
    {
        printf("Erreur lors de l'ouverture du fichier Mauvais.txt");
        exit(1);
    }
    printf("\nOuverture du fichier Mauvais.txt reussi\n");
    printf("Liste des etudiants insolvable :\n");
    for (i=0;i<k;i++)
    {
        printf("%s\t%s\t%d\n",I[i].nom,I[i].prenom,I[i].ncin);
        fprintf(g,"%d ;%s ;%s ;%d ;%s ;%s ;%f ;%f ;%f ;%f ;%f \n",I[i].ncin,I[i].nom,I[i].prenom,I[i].age,I[i].filiere,I[i].niveau,I[i].cotisation[0],I[i].cotisation[1],I[i].cotisation[2],I[i].cotisation[3],I[i].cotisation[4]);
    }
    fclose(g);
}
//Question 7: Fonction Statistique()
float statistiques()
{

    struct etudiant T1[100];
    float som=0;
    int i,j,n1;
	lecture(T1,&n1);
	for (i=0;i<n1;i++)
	{
        for (j=0;j<5;j++)
            som+=T1[i].cotisation[j];
	}
	FILE *g;
	struct etudiant T2[100],p;
    g=fopen("Mauvais.txt","r");
    if (g==NULL)
    {
        printf("Erreur lors de l'ouverture du fichier Mauvais.txt");
        exit(1);
    }
    printf("Ouverture du fichier Mauvais.txt reussi");
    int n2;
    i=0;
	while(fscanf(g,"%d ;%s ;%s ;%d ;%s ;%s ;%f ;%f ;%f ;%f ;%f,\n",&p.ncin, &p.nom, &p.prenom, &p.age, &p.filiere, &p.niveau, &p.cotisation[0], &p.cotisation[1], &p.cotisation[2], &p.cotisation[3], &p.cotisation[4])!=EOF)
	{
		T2[i];
		i++;
	}
	n2=i;
	fclose(g);
	float pourcentage;
	pourcentage =n2*100/n1;
	printf("\nStatistique sur la solvabilité des etudiants\n");
	printf("\n>>>> Etudiants insolvables : %.2f%\n>>>> Etudiants solvables : %.2f%\n>>>> Montant total cotisation : %.2f",pourcentage,100-pourcentage,som);
	return pourcentage;
}
//Question 8: Fonction Supprimer()
void supprimer2()
{
    FILE *f;
    struct etudiant T1[100],T2[100];
    int i=0,n,k,j;
	lecture(T1,&n);
	int som;
    for (i=0;i<n;i++)
    {
        som=0;
        for (j=0;j<=4;j++)
        {
            som+=T1[i].cotisation[j];
        }
        if (som!=0)
        {
            T2[k]=T1[i];
            k++;
        }
    }
	f=fopen("Etudiants.txt","w");
	if (f==NULL)
    {
        printf("Erreur lors de l'ouverture du fichier Etudiants.txt");
        exit(1);
    }
    for (j=0;j<k;j++)
    {
            fprintf(f,"%d ;%s ;%s ;%d ;%s ;%s ;%f ;%f ;%f ;%f ;%f\n",T2[j].ncin,T2[j].nom,T2[j].prenom,T2[j].age,T2[j].filiere,T2[j].niveau,T2[j].cotisation[0],T2[j].cotisation[1],T2[j].cotisation[2],T2[j].cotisation[3],T2[j].cotisation[4]);
    }
    printf("Suppression etudiants sans cotisation reussi !!!");
    fclose(f);
}
//Question 9: Fonction recherche()
void recherche(CNI)
{
    int j,i,n,k=0;
    struct etudiant T[100];
    //On charge les données du fichier dans un tableau d'enregistrement
    lecture(T,&n);
/*On teste si la CIN se trouve dans le trableau des étudiants si l'etudiant est retrouvé on renvoie son rang sur la liste
si non on signale qu'in n'a pas été retrouvé*/
    for (k=0;k<n;k++)
    {
        if (CNI==T[k].ncin)
        {
            printf("L'etudiant recherché est à la position %d\n",k+1);
            printf("Numero CNI : %d\n",T[k].ncin);
            printf("Nom :%s\n",T[k].nom);
            printf("Prenom :%s\n",T[k].prenom);
            printf("Age :%d\n",T[k].age);
            printf("Filiere :%s\n",T[k].filiere);
            printf("Niveau :%s\n",T[k].niveau);
            for (j=0;j<5;j++)
            {
                printf("cotisation numero %d : %.2f\n",j+1,T[k].cotisation[j]);
            }
            break;
        }
        else if (k==n-1)
        {
            printf("Numero CIN ne se trouve pas dans le fichier !!!\n");
        }
    }
}
int main()
{
    int choix;
	float P_insolv;
	int CNI;
	printf("\t  ***********************************************************\n");
	printf("\t**Bienvenu dans le programme de gestion du Club des Etudiants**\n");
	printf("\t  ***********************************************************\n");
	printf("\n\n\t**********************Menu principal****************************\n");
	printf("\n\t-->1:   Saisir les donnees\n\t-->2:   Ajouter un etudiant\n\t-->3:   Modifier les donnees d'un etudiant\n\t-->4:   Supprimer les données d'un etudiant\n\t-->5:   Afficher tous les etudiants\n\t-->6:   Solvabilités de chaque etudiant\n\t-->7:   Etudiants Insolvables\n\t-->8:   Statistiques de solvabilité\n\t-->9:   Supprimer les etudiants totalement insolvables\n\t-->10:  Rechercher un etudiant\n\t-->11:  Quitter le programme\n");
	printf("\nQue voulez vous faire ?\n");
	scanf("%d",&choix);
	while ((choix<1)|(choix>11))
	{
        printf("\nChoix non disponibre\nVeillez reessayer svp : ");
        scanf("%d",&choix);
	}
	while (choix!=11)
	{
        switch (choix)
        {
            case 1:system("cls");saisir();system("cls");break;
            case 2:system("cls");ajouter();system("cls");break;
            case 3:system("cls");modifier();break;
            case 4:system("cls");printf("Entrer le nomero de la CNI : ");scanf("%d",&CNI);supprimer(CNI);break;
            case 5:system("cls");afficher();break;
            case 6:system("cls");solvable();break;
            case 7:system("cls");insolvable();break;
            case 8:system("cls");P_insolv=statistiques();break;
            case 9:system("cls");supprimer2();system("cls");break;
            case 10:system("cls");printf("Entrer le numero de la CNI : ");scanf("%d",&CNI);recherche(CNI);break;
        };
        printf("\n\n\t**********************Menu principal****************************\n");
        printf("\n\t-->1:   Saisir les donnees\n\t-->2:   Ajouter un etudiant\n\t-->3:   Modifier les donnees d'un etudiant\n\t-->4:   Supprimer les données d'un etudiant\n\t-->5:   Afficher tous les etudiants\n\t-->6:   Solvabilités de chaque etudiant\n\t-->7:   Etudiants Insolvables\n\t-->8:   Statistiques de solvabilité\n\t-->9:   Supprimer les etudiants totalement insolvables\n\t-->10:  Rechercher un etudiant\n\t-->11:  Quitter le programme\n");
        printf("\nQue voulez vous faire ?\n");
        scanf("%d",&choix);
        while ((choix<1)|(choix>11))
        {
            printf("\nChoix non disponibre\nVeillez reessayer svp : ");
            scanf("%d",&choix);
        }

	}
    return 0;
}
