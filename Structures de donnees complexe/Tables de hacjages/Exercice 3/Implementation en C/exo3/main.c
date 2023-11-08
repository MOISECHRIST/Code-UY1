#include<stdio.h>
#include <stdlib.h>
#include <string.h>
#include "header.h"

int main()
{
    int i;
    char d[100];
    strcpy(d,"Nsam");
    HashTable table=initHash(table);
    table=read(table);
    for(i=0;i<table.maxelt;i++)
    {
        printf("\n\n%d :\n",i+1);
        if (table.tab[i]!=NULL)
            print_list(table.tab[i]);
    }
    printf("\nLe resultat de la recherche de %s est %d\n",d,Hash_search(table,d));
    printf("\n(C) 2022 By MMCJ/INF-L1\n");
    return 0;
}
