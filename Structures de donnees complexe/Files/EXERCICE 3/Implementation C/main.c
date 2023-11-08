#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "header.h"

int main()
{
    File *file=init();
    file=read(file);
    Trajet elt;
    printf("Taille : %d\n",length_list(file));
    print_list(file);
    elt=minimum(file);
    printf("Le trajet dont le cout est minimal est :\n");
    printf("%s\t%d\n",elt.depart,elt.prix);
    //printf("Nouvelle liste :\n");
    char d[100];
    strcpy(d,"Ekounou");
    printf("Le resulata de la recherche de %s est %d\n", d,search_elt(file,d));
    //file=sort_list(file);
    //printf("Taille : %d\n",length_list(file));
   // print_list(file);
    printf("(C) 2022 By MMCJ/INF-L1\n");
    return 0;
}
