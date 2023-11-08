from matrix.manipulation import *
from random import normalvariate, randrange
from math import *
from matplotlib import pyplot as plt

#Initialisation des parametres du modele (W et b)
def init_param(X):
    m=len(X[0][:])
    W=[]
    b=normalvariate(mu=0,sigma=1)
    for i in range(m):
        W+=[normalvariate(mu=0,sigma=1)]
    return (W,b)

#Definition de l'application lineaire Z=W*X+b
def app_linear(X,W,b):
    Z=prod_vect(X,W)
    Z=sum_vect1(Z,b)
    return Z

#Definition de la fonction d'activation sigmoide(Z)=(1/(1+exp(-Z)))
#Utilisé pour les classifications binaires
def sigmoid(Z):
    n=len(Z)
    A=[]
    for i in range(n):
        A+=[1/(1+exp(-1*Z[i]))]
    return A

#Definition de la fonction log_loss pour un probleme de classification à 2 issues 
def class2log_loss(A,Y):
    l=0
    m=len(Y)
    for i in range(m):
        l+=(-Y[i]*log(A[i])-(1-Y[i])*log(1-A[i]))/m
    return l


#Calcul du gradient de la fonction log loss (cas A=tanh ou tgh)
def gradient_sig(A,X,Y):
    dW=[]
    n=len(X)
    m=len(X[0][:])
    for j in range(m):
        s=0
        for i in range(n):
            s+=(A[i]-Y[i])*X[i][j]
        dW+=[s/n]
    db=0
    for i in range(n):
        db+=(A[i]-Y[i])
    db=db/n
    return (dW,db)


#Fonction pour mettre a jour les parametres
def update_param(W,b,dW,db,learning_rate):
    b=b-learning_rate*db
    n=len(W)
    for i in range(n):
        W[i]=W[i]-learning_rate*dW[i]
    return (W,b)


#Creation d'un neurone artificiel pour la classification à 2 issues
def neurone_art_sig(X,Y,learning_rate=0.5, iteration=1000):
    #Initialisation des paramettres
    W,b=init_param(X)
    i=0
    loss=[]
    while i < iteration:
        Z=app_linear(X,W,b)
        A=sigmoid(Z)
        loss+=[class2log_loss(A,Y)]
        dW, db=gradient_sig(A,X,Y)
        W,b=update_param(W,b,dW,db,learning_rate)
        i+=1
    plt.figure()
    plt.plot(loss)
    plt.savefig("Loss function.png")
    return (W,b)

#Definition de la fonction de prédiction (cas de la fonction d'activation sigmoide)
def predict_sig(vect_X,W,b):
    z=0
    m=len(vect_X)
    for i in range(m):
        z+=vect_X[i]*W[i]
    z+=b
    a=1/(1+exp(z))
    return a<=0.5

if __name__=="__main__":

    X=[[5.1,3.5,1.4,0.2],[4.9,3.0,1.4,0.2],[4.7,3.2,1.3,0.2],[4.6,3.1,1.5,0.2],[5.0,3.6,1.4,0.2],[5.4,3.9,1.7,0.4],[4.6,3.4,1.4,0.3],[5.0,3.4,1.5,0.2],[4.4,2.9,1.4,0.2],[4.9,3.1,1.5,0.1],[5.4,3.7,1.5,0.2],[4.8,3.4,1.6,0.2],[4.8,3.0,1.4,0.1],[4.3,3.0,1.1,0.1],[5.8,4.0,1.2,0.2],[5.7,4.4,1.5,0.4],[5.4,3.9,1.3,0.4],[5.1,3.5,1.4,0.3],[5.7,3.8,1.7,0.3],[5.1,3.8,1.5,0.3],[5.4,3.4,1.7,0.2],[5.1,3.7,1.5,0.4],[4.6,3.6,1.0,0.2],[5.1,3.3,1.7,0.5],[4.8,3.4,1.9,0.2],[5.0,3.0,1.6,0.2],[5.0,3.4,1.6,0.4],[5.2,3.5,1.5,0.2],[5.2,3.4,1.4,0.2],[4.7,3.2,1.6,0.2],[4.8,3.1,1.6,0.2],[5.4,3.4,1.5,0.4],[5.2,4.1,1.5,0.1],[5.5,4.2,1.4,0.2],[4.9,3.1,1.5,0.2],[5.0,3.2,1.2,0.2],[5.5,3.5,1.3,0.2],[4.9,3.6,1.4,0.1],[4.4,3.0,1.3,0.2],[5.1,3.4,1.5,0.2],[5.0,3.5,1.3,0.3],[4.5,2.3,1.3,0.3],[4.4,3.2,1.3,0.2],[5.0,3.5,1.6,0.6],[5.1,3.8,1.9,0.4],[4.8,3.0,1.4,0.3],[5.1,3.8,1.6,0.2],[4.6,3.2,1.4,0.2],[5.3,3.7,1.5,0.2],[5.0,3.3,1.4,0.2],[7.0,3.2,4.7,1.4],[6.4,3.2,4.5,1.5],[6.9,3.1,4.9,1.5],[5.5,2.3,4.0,1.3],[6.5,2.8,4.6,1.5],[5.7,2.8,4.5,1.3],[6.3,3.3,4.7,1.6],[4.9,2.4,3.3,1.0],[6.6,2.9,4.6,1.3],[5.2,2.7,3.9,1.4],[5.0,2.0,3.5,1.0],[5.9,3.0,4.2,1.5],[6.0,2.2,4.0,1.0],[6.1,2.9,4.7,1.4],[5.6,2.9,3.6,1.3],[6.7,3.1,4.4,1.4],[5.6,3.0,4.5,1.5],[5.8,2.7,4.1,1.0],[6.2,2.2,4.5,1.5],[5.6,2.5,3.9,1.1],[5.9,3.2,4.8,1.8],[6.1,2.8,4.0,1.3],[6.3,2.5,4.9,1.5],[6.1,2.8,4.7,1.2],[6.4,2.9,4.3,1.3],[6.6,3.0,4.4,1.4],[6.8,2.8,4.8,1.4],[6.7,3.0,5.0,1.7],[6.0,2.9,4.5,1.5],[5.7,2.6,3.5,1.0],[5.5,2.4,3.8,1.1],[5.5,2.4,3.7,1.0],[5.8,2.7,3.9,1.2],[6.0,2.7,5.1,1.6],[5.4,3.0,4.5,1.5],[6.0,3.4,4.5,1.6],[6.7,3.1,4.7,1.5],[6.3,2.3,4.4,1.3],[5.6,3.0,4.1,1.3],[5.5,2.5,4.0,1.3],[5.5,2.6,4.4,1.2],[6.1,3.0,4.6,1.4],[5.8,2.6,4.0,1.2],[5.0,2.3,3.3,1.0],[5.6,2.7,4.2,1.3],[5.7,3.0,4.2,1.2],[5.7,2.9,4.2,1.3],[6.2,2.9,4.3,1.3],[5.1,2.5,3.0,1.1],[5.7,2.8,4.1,1.3]
]
    Y=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    W,b=neurone_art_sig(X,Y)
    Y_predic=[]
    i=0
    for line in X:
        if int(predict_sig(line,W,b))==Y[i]:
            Y_predic+=[predict_sig(line,W,b)]
        else:
            x1=line[0]
            y1=line[1]
            x2=line[2]
            y2=line[3]
        i+=1
    succ=100*len(Y_predic)/len(Y)
    print(f"Success : {succ:.2f}%")
    ind=randrange(0,len(X))
    print("prediction :",int(predict_sig(X[ind][:],W,b)))
    print("Valeur reelle :",X[ind][:],Y[ind])
    print("Parametre : \nW=",W,"\nb=",b)
    sepal_long=[]
    sepal_lar=[]
    petal_long=[]
    petal_lar=[]
    for i in range(len(X)):
        sepal_long+=[X[i][0]]
        sepal_lar+=[X[i][1]]
        petal_long+=[X[i][2]]
        petal_lar+=[X[i][3]]
    plt.figure()
    plt.scatter(x=sepal_long,y=sepal_lar,c=Y,cmap="Accent")
    plt.xlabel("Longueur sepal")
    plt.ylabel("Largeur sepal")
    plt.scatter(x=x1,y=y1,c='r')
    plt.savefig("Loss point.png")
    plt.figure()
    plt.scatter(x=petal_long,y=petal_lar,c=Y,cmap="Accent")
    plt.xlabel("Longueur petal")
    plt.ylabel("Largeur petal")
    plt.scatter(x=x2,y=y2,c='r')
    plt.savefig("Loss point2.png")
