def readDictMots():
    dico={}
    file=open("liste_mot.txt","r")
    for line in file:
        x=line.split(",")
        dico[x[0]]=x[1]
    file.close()
    return dico

def CompareMots(mot1,mot2):
    result=""
    l=len(mot1)
    for i in range(l):
        if(mot1[i]==mot2[i]):
            result+=mot1[i]
        else:
            result+="*"
    return result

def readListPlayer():
    dico_player={}
    try:
        players=open("list_player.txt","r")
        for line in players:
            x=line.split(",")
            dico_player[x[0]]=int(x[1])
        players.close()
    except:
        print("Vous ête le premier joueur")
    return dico_player

def writeListPlayer(dico_player):
    file=open("list_player.txt","w")
    chaine=""
    for nom in dico_player.keys():
        chaine +=nom+","+str(dico_player[nom])+"\n"
    file.write(chaine)
    file.close()

def countDif(mot):
    return mot.count("*")