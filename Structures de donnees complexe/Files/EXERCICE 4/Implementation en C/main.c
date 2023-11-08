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
    printf("Le trajet dont le cout est minimal est :\n");
    printf("%s\t%d\n",elt.repas,elt.age);
    pile=sort_list(pile);
    printf("Nouvelle liste :\n");
    printf("Taille : %d\n",length_list(pile));
    print_list(pile);
    i=search_elt(pile,"Nkui");
    printf("Resultat de la recherche  de Nkui est : %d\n",i);
    printf("(C) 2022 By MMCJ/INF-L1\n");
    return 0;
}
