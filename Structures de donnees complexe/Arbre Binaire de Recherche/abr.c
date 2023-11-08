#include "abr.h"
//Fonction qui retourne le maximum d'un arbre binaire de recherche
int maxValeur(ABR *abr)
{
    if(abr==NULL)
    	printf("Arbre est vide !!\n");
    if(abr->FilsDroit==NULL)
        return abr->valeur;
    else
        return maxValeur(abr->FilsDroit);
}
ABR *init()
{
	return NULL;
}
//Fonction qui retourne le minimum d'un arbre binaire de recherche
int minValeur(ABR *abr)
{
    if(abr==NULL)
        printf("Arbre est vide !!\n");
    if(abr->FilsGauche==NULL)
        return abr->valeur;
    else
        return minValeur(abr->FilsGauche);
}
//Creer une racine
ABR *racine(int elt)
{
    ABR *abr=(ABR*)malloc(sizeof(ABR));
    abr->valeur=elt;
    abr->FilsDroit=NULL;
    abr->FilsGauche=NULL;
    return abr;
}
//Question 2:
ABR *creer_ABR(int elt,ABR *FilsG, ABR *FilsD)
{
    ABR *abr=(ABR*)malloc(sizeof(ABR));
    abr->valeur=elt;
    abr->FilsDroit=FilsD;
    if(FilsD!=NULL)
        FilsD->parent=abr;
    abr->FilsGauche=FilsG;
    if(FilsG!=NULL)
        FilsG->parent=abr;
}
//Question 3 :
void prefixe(ABR *abr)
{
    if(abr==NULL)
        return;
    printf("%d;\t",abr->valeur);
    prefixe(abr->FilsGauche);
    prefixe(abr->FilsDroit);
}
void infixe(ABR *abr)
{
    if(abr!=NULL)
    {
	    infixe(abr->FilsGauche);
	    printf("%d;\t",abr->valeur);
	    infixe(abr->FilsDroit);
     }
}
ABR *infixeR(ABR *abr,ABR *b)
{
    if(abr!=NULL)
    {
	    infixeR(abr->FilsGauche,b);
	    ajoutF(b,abr->valeur);
	    infixeR(abr->FilsDroit,b);
     }
     return b;
}
void postfixe(ABR *abr)
{
    if(abr==NULL)
        return;
    postfixe(abr->FilsGauche);
    postfixe(abr->FilsDroit);
    printf("%d;\t",abr->valeur);
}
//Question 4:
int succValeur(ABR *abr, int elt)
{
    if(abr==NULL)
        printf("Votre arbre est vide\n");
    else
    {
	    ABR *cur=abr;
	    while((cur->valeur!=elt)&&(cur!=NULL))
	    {
		    if(cur->valeur>elt)
		        cur=cur->FilsGauche;
		    if(cur->valeur<elt)
		        cur=cur->FilsDroit;
	    }
	    if(cur->valeur==elt)
	    {
            if(cur->FilsDroit==NULL)
            {
                ABR *succ=cur;
                while((succ->parent->valeur<cur->valeur)&&(succ!=NULL))
                {
                    succ=succ->parent;
                }
                if(succ==NULL)
                    printf("%d n'a pas de succcesseur\n\n",elt);
                else
                    return succ->parent->valeur;
            }
            else
                return minValeur(cur->FilsDroit);
	    }
	    else
	    {
		printf("%d ne se trouve pas dans l'arbre\n\n",elt);
	    }
	}
}
//Question 5:
int predValeur(ABR *abr, int elt)
{
    if(abr==NULL)
        printf("Votre arbre est vide\n");
    else
    {
	    ABR *cur=abr;
	    while((cur->valeur!=elt)&&(cur!=NULL))
	    {
            if(cur->valeur>elt)
                cur=cur->FilsGauche;
            if(cur->valeur<elt)
                cur=cur->FilsDroit;
	    }
	    if(cur->valeur==elt)
	    {
            if(cur->FilsGauche==NULL)
            {
                ABR *pred=cur;
                while((pred->parent->valeur>cur->valeur)&&(pred!=NULL))
                {
                    pred=pred->parent;
                }
                if(pred==NULL)
                    printf("%d n'a pas de predecesseur\n\n",elt);
                else
                    return pred->parent->valeur;
            }
            else
                return maxValeur(cur->FilsGauche);
	    }
	    else
	    {
		printf("%d ne se trouve pas dans l'arbre\n\n",elt);
	    }
    }
}
//Question 6:
int recherche(ABR *abr,int elt)
{
    int trouve=0;
    if(abr!=NULL)
    {
        if(elt>abr->valeur)
        {
            if(abr->FilsDroit!=NULL)
                return recherche(abr->FilsDroit,elt);
        }
        if(elt<abr->valeur)
        {
            if(abr->FilsGauche!=NULL)
                return recherche(abr->FilsGauche,elt);
        }
        if(elt==abr->valeur)
        {
            trouve=1;
        }
    }
    return trouve;
}
//Question 7:
ABR *ajoutR(ABR *abr,int elt)
{
	if(abr==NULL)
	    return racine(elt);
	else
	{
	    ABR *tmp=(ABR*)malloc(sizeof(ABR));
	    tmp=racine(elt);
	    tmp=infixeR(abr,tmp);
	    return tmp;
	 }
}
//Question 8:
ABR *ajoutF(ABR *abr,int elt)
{
    if(abr==NULL)
        return racine(elt);
    else
    {
        if(elt>abr->valeur)
        {
            abr->FilsDroit=ajoutF(abr->FilsDroit,elt);
            if(abr->FilsDroit!=NULL)
                abr->FilsDroit->parent=abr;
            return abr;
        }
        if(elt<=abr->valeur)
        {
            abr->FilsGauche=ajoutF(abr->FilsGauche,elt);
            if(abr->FilsGauche!=NULL)
                abr->FilsGauche->parent=abr;
            return abr;
        }
    }
}
//Question 9:
ABR *suppElt(ABR *abr, int elt)
{
    if(abr==NULL)
        return NULL;
    else
    {
        if(elt>abr->valeur)
        {
            abr->FilsDroit=suppElt(abr->FilsDroit,elt);
            return abr;
        }
        if(elt<abr->valeur)
        {
            abr->FilsGauche=suppElt(abr->FilsGauche,elt);
            return abr;
        }
        if(elt==abr->valeur)
        {
            if((abr->FilsDroit==NULL)&&(abr->FilsGauche==NULL))
                return NULL;
            else
            {
                if(abr->FilsGauche==NULL)
                    return  abr->FilsDroit;
                if(abr->FilsDroit==NULL)
                    return abr->FilsGauche;
                else
                {
                    int x=maxValeur(abr->FilsGauche);
                    ABR *tmp1=(ABR*)malloc(sizeof(ABR));
                    tmp1=abr->FilsDroit;
                    ABR *tmp2=(ABR*)malloc(sizeof(ABR));
                    tmp2=suppElt(abr->FilsGauche,x);
                    ABR *tmp3=racine(x);
                    tmp3->FilsDroit=tmp1;
                    tmp3->FilsGauche=tmp2;
                    return tmp3;
                }
            }
        }
    }
}
