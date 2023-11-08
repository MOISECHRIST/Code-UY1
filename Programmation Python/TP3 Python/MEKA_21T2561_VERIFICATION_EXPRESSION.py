class Pile:
    def __init__(self,n=100):
        self.tab=[]
        self.sommet=-1
        self.max_elt=n
    def pileVide(self):
        return self.sommet==-1
    def pilePleine(self):
        return self.sommet==(self.max_elt-1)
    def empiler(self,elt):
        if self.pilePleine()==False:
            self.tab+=[elt]
            self.sommet+=1
        else:
            print("Pile Pleine...")
    def depiler(self):
        if self.pileVide()==False:
            elt=self.tab[self.sommet]
            self.sommet-=1
            return elt
        else:
            print("Pile Vide...")
    def afficher(self):
        if self.pileVide()==False:
            for i in range(self.sommet+1):
                print(self.tab[i],end=" ")

def verif_chaine(chaine):
    dic={}
    dic["parenth_ouv"]=Pile()
    dic["parenth_ferm"]=Pile()
    dic["crochet_ouv"]=Pile()
    dic["crochet_ferm"]=Pile()
    dic["accolade_ouv"]=Pile()
    dic["accolade_ferm"]=Pile()
    for i in range(len(chaine)):
        if chaine[i]=="(":
            dic["parenth_ouv"].empiler(chaine[i])
        elif chaine[i]==")":
            dic["parenth_ferm"].empiler(chaine[i])
        elif chaine[i]=="[":
            dic["crochet_ouv"].empiler(chaine[i])
        elif chaine[i]=="]":
            dic["crochet_ferm"].empiler(chaine[i])
        elif chaine[i]=="{":
            dic["accolade_ouv"].empiler(chaine[i])
        elif chaine[i]=="}":
            dic["accolade_ferm"].empiler(chaine[i])
    test1=dic["parenth_ouv"].sommet==dic["parenth_ferm"].sommet
    test2=dic["crochet_ferm"].sommet==dic["crochet_ouv"].sommet
    test3=dic["accolade_ouv"].sommet==dic["accolade_ferm"].sommet 
    if(test1+test2+test3)==3:
        print("{} est bien formée".format(chaine))
    else:
        if dic["parenth_ouv"].sommet<dic["parenth_ferm"].sommet:
            print("{} est mal formée car il y a {} parenthèse(s) fermante(s) sont en plus".format(chaine),-dic["parenth_ouv"].sommet+dic["parenth_ferm"])
        elif dic["parenth_ouv"].sommet>dic["parenth_ferm"].sommet:
            print("{} est mal formée car il y a {} parenthèse(s) ouvrante(s) sont en plus".format(chaine),dic["parenth_ouv"].sommet-dic["parenth_ferm"])

        if dic["crochet_ouv"].sommet<dic["crochet_ferm"].sommet:
            print("{} est mal formée car il y a {} crochet(s) fermantes sont en plus".format(chaine),-dic["crochet_ouv"].sommet+dic["crochet_ferm"])
        elif dic["crochet_ouv"].sommet>dic["crochet_ferm"].sommet:
            print("{} est mal formée car il y a {} crochet(s) ouvrantes sont en plus".format(chaine),dic["crochet_ouv"].sommet-dic["crochet_ferm"])
        
        if dic["accolade_ouv"].sommet<dic["accolade_ferm"].sommet:
            print("{} est mal formée car il y a {} accolade(s) fermantes sont en plus".format(chaine),-dic["accolade_ouv"].sommet+dic["accolade_ferm"])
        elif dic["accolade_ouv"].sommet>dic["accolade_ferm"].sommet:
            print("{} est mal formée car il y a {} accolade(s) ouvrantes sont en plus".format(chaine), dic["accolade_ouv"].sommet-dic["accolade_ferm"])

chaine=input("Entrer la chaine")
verif_chaine(chaine)