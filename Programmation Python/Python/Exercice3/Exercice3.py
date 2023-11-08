from fonction import *
from random import randrange
list_player=readListPlayer()
dico_mots=readDictMots()
nom=input("Entrer votre nom : ")
if(nom in list_player.keys()):
    score=list_player[nom]
else:
    score=list_player[nom]=0
print("\nJoueur : {}\nScore : {}\n".format(nom,score))
liste_mot=[]
for i in dico_mots.keys():
    liste_mot+=[i]
mot_choisi=liste_mot[randrange(len(dico_mots))]
print("Mot a trouver comporte {} caractere(s)".format(len(mot_choisi)))
print("Description du mot :\n{}".format(dico_mots[mot_choisi]))
essaie=1
print("Essaie {}:".format(essaie))
mot_entre=input("Mot : ")
while(len(mot_entre)!=len(mot_choisi)):
    print("Le mot n'est pas de la bonne taille...\n veillez saisir un mot de {} caractere(s)".format(len(mot_choisi)))
    mot_entre=input("Mot : ")
mot_entre=mot_entre.lower()
result=CompareMots(mot_choisi,mot_entre)
print("Mot trouve : {}".format(result))
max_essaie=8
while((essaie<max_essaie)and(countDif(result)!=0)):
    essaie+=1
    print("Essaie {}:".format(essaie))
    mot_entre=input("Mot : ")
    mot_entre=mot_entre.lower()
    result=CompareMots(mot_choisi,mot_entre)
    print("Mot trouve : {}".format(result))
score+=(max_essaie-essaie)
list_player[nom]=score
print("\nJoueur : {}\nScore : {}\n".format(nom,score))
writeListPlayer(list_player)