#include<stdio.h>
#include <stdlib.h>
#include <string.h>
#include "header.h"
int main()
{
    Pile *pile=init();
    pile=read(pile);
    Food elt;
    int i;
    printf("Taille : %d\n",length_list(pile));
    print_list(pile);
    elt=minimum(pile);
    printf("\nLe repas consommé par le plus jeune est :\n");
    printf("%s\t%s\t%s\t%d\n",elt.heure,elt.lieu,elt.repas,elt.age);
    pile=sort_list(pile);
    printf("\nNouvelle liste trié par age décroissant est :\n");
    printf("Taille : %d\n",length_list(pile));
    print_list(pile);
    char d[100];
    strcpy(d,"Nkui");
    i=search_elt(pile,d);
    printf("\nResultat de la recherche de %s est : %d\n",d,i);
    printf("\n(C) 2022 By MMCJ/INF-L1\n");
    return 0;
}
