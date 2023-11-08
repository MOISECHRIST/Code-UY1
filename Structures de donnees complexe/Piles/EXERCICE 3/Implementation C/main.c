#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "header.h"

int main()
{
    Pile *pile=init();
    pile=read(pile);
    Trajet elt;
    char d[100];
    strcpy(d,"Odza");
    printf("\nTaille : %d\n",length_list(pile));
    print_list(pile);
    elt=minimum(pile);
    printf("\nLe trajet dont le cout est minimal est :\n");
    printf("%s\t%s\t%d\t%d\n",elt.depart,elt.arrivee,elt.duree,elt.prix);
    if (search_elt(pile,d)==1)
    {
    	printf("\nOn a un trajet avec pour depart %s dans la Pile\n",d);
    }
    else 
    {
    	printf("\nOn n'a pas de trajet avec pour depart %s dans la Pile\n",d);
    }
    pile=sort_list(pile);
    printf("\nNouvelle liste :\n");
    printf("Taille : %d\n",length_list(pile));
    print_list(pile);
    printf("\n(C) 2022 By MMCJ/INF-L1\n");
    return 0;
}
