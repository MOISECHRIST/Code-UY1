from math import *
#Dans ce package est implémenté les gradients des loss fonction

#Calcul du gradient de la fonction loss classification binomiale binary cross Entropy (cas Activation = sigmoide)
def BCE_gradient_sig(A,X,Y):
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

#Calcul du gradient de la fonction loss classification binomiale hinge loss (cas Activation = tanh)
def hinge_loss_tgh(A,X,Y):
    dW=[]
    n=len(X)
    m=len(X[0][:])
    for j in range(m):
        s=0
        for i in range(n):
            s+=(-Y[i]*(1-A[i]**2)*X[i][j])
        dW+=[s]
    db=0
    for i in range(n):
        db+=(-Y[i]*(1-A[i]**2))
    return (dW,db)