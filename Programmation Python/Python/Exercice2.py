from random import randrange
def SaisirChoix():
    choix=input("Choisir un nombre entre 0 et 49 : ")
    try:
        choix=int(choix)
    except ValueError:
        while(not choix.isnumeric()):
            print("Erreur de saisie. La valeur entree doit etre numerique...\nVeillez reesayer :")
            choix=input("Choisir un nombre entre 0 et 49 : ")
        choix=int(choix)
    return choix
    
iteration="Y"
while(iteration=="Y"):
    mise=input("Quelle est votre mise : ")
    if mise.isnumeric():
            mise=int(mise)
    else:
        while(not mise.isnumeric()):
            print("Erreur de saisie. La valeur entree doit etre numerique...\nVeillez reesayer :")
            mise=input("Quelle est votre mise : ")
        mise=int(mise)
    print("Débutons le jeu !!!")
    choix=SaisirChoix()
    while ((choix<0)or(choix>49)):
        choix=SaisirChoix()
    courtier=randrange(50)
    print("La bille s'est arrete au numero {}".format(courtier))
    if(courtier==choix):
        gain=mise*3 
        print("Felicitation !!! Vous avez obtenu le numero gagnant...\nVotre gain est de {}".format(gain))
    elif(courtier%2==choix%2):
        gain=mise/2
        print("Mince !!! Vous y etiez presque...\nVous repartez quand même avec {}".format(gain))
    else:
        print("Dommage !!! Vous n'avez pas eu de chance...")
        gain=0
    iteration=input("Voulez vous rejouer [Y/N] : ")
    iteration=iteration.upper()
    while((iteration!="Y")and(iteration!="N")):
        iteration=input("Voulez vous rejouer [Y/N] : ")
        iteration=iteration.upper()
    if(iteration=="N"):
        print("A la prochaine...")
    else:
        print("Nous avons un joueur...")