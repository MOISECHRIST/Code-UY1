#include <stdio.h>
#include <stdlib.h>
#include "header.h"
#include <string.h>
int main()
{
    Pile pile;
    pile=init(pile);
    pile=read(pile);
    printf("La longueur de la liste est : %d\n",pile.nbelt);
    print_list(pile);
    pile=sort_pile(pile);
    printf("\nLa longueur de la liste est : %d\n",pile.nbelt);
    print_list(pile);
    return 0;
}
