#Fonction qui valide si une chaine entrée est une séquence d'ADN
def ChaineValide(chaine):
    nucleotide="atcg"
    lower_str=chaine.lower()
    long=len(lower_str)
    i=0
    valide=lower_str[i] in nucleotide
    while((valide)and(i<long-1)):
        i+=1
        valide=lower_str[i] in nucleotide
    if(i!=long-1):
        valide=False
    return valide
#Fonction pour saisir une séquence valide
def Saisie():
    chaine=input("Chaîne : ")
    if (ChaineValide(chaine)):
        return chaine
    else:
        print("Saisie invalide")
        return ""
#Fonction qui renvoir la proportie d'une séquences dans la chaine
def proportion(chaine,seq):
    return 100*chaine.count(seq)/len(chaine)

print("Entrer votre séquence d'ADN :")
seq_adn=Saisie()
print("Entrer votre segment d'ADN :")
seq_adn2=Saisie()
if((seq_adn!="")and(seq_adn2!="")):
    print("Il y a {}% de '{}' dans '{}'".format(round(proportion(seq_adn,seq_adn2),2),seq_adn2,seq_adn))