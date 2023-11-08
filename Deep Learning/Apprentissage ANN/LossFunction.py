from math import *
#Dans ce package est implémenté des loss functions

#Probleme de classification

#Definition de la fonction log_loss pour un probleme de classification binaire 
def binary_crossEntropy(A,Y):
    l=0
    m=len(Y)
    for i in range(m):
        l+=(-Y[i]*log(A[i])-(1-Y[i])*log(1-A[i]))/m
    return l

#Definition de la fonction log_loss pour un probleme de classification binaire (-1 ou 1)
# Utilisé dans les SVM 
def hinge_loss(A,Y):
    l=0
    m=len(Y)
    for i in range(m):
        l+=max(0,(1-A[i]*Y[i]))
    return l/m


#Definition de la fonction log_loss pour un probleme de classification binaire et multiple 
def crossEntropy(A,Y):
    l=0
    m=len(Y)
    n=len(Y[0][:])
    for i in range(m):
        for j in range(n):
            l+=(-Y[i][j]*log(A[i][j]))/m
    return l


#Définition de la fonction log_loss pour un probleme de classification multiple
def kullback_divergence(A,Y):
    l=0
    m=len(Y)
    for i in range(m):
        l+=Y[i]*log(Y[i]/A[i])
    return l/m

#Probleme de regression

#Moyenne du carre des ecarts
def mean_squared_error(A,Y):
    l=0
    m=len(Y)
    for i in range(m):
        l+=(A[i]-Y[i])**2
    return l/m


#Moyenne de la valeur absolue des ecarts
def mean_absolue_error(A,Y):
    l=0
    m=len(Y)
    for i in range(m):
        l+=abs(A[i]-Y[i])
    return l/m