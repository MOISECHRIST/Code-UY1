#ifndef GESTION_H_INCLUDED
#define GESTION_H_INCLUDED

//La structure de données pour gerer le texte
struct phrase
{
    char chaine[1000];
    int taille;
};

//Module 1: Manipulation des fichiers


//Lecture du texte dans le fichier Texte_decripte.txt

extern void LECTURE_DECRYPT(struct phrase *,int* );

//Lecture du texte dans le fichier Texte_cripte.txt


extern void LECTURE_CRYPT(struct phrase *,int* );

//Ecriture du texte dans le fichier Texte_decripte.txt

extern void ECRITURE_DECRYPT(struct phrase *,int);

//Ecriture du texte dans le fichier Texte_cripte.txt

extern void ECRITURE_CRYPT(struct phrase *,int);

//Importation du texte mot par mot

extern void ImportMot(struct phrase *,int* );

//Ecriture du texte dans le fichier Cle-XOR.txt

void ECRITURE_CLE(char *);

//Importation de la clé
void LECTURE_CLE(char *);

#endif // GESTION_H_INCLUDED
