from math import *
#Dans ce package se trouve l'implementation des fonctions d'activation

#Definition de la fonction d'activation sigmoide(Z)=(1/(1+exp(-Z)))
#Utilisé pour les classifications binaires
#Elle retourne des valeurs entre 0 et 1. Plus on est proche de 1 plus le critère considéré est choisi et inversement si non
def sigmoid(Z):
    n=len(Z)
    A=[]
    for i in range(n):
        A+=[1/(1+exp(-1*Z[i]))]
    return A

#definition de la fonction d'activation ReLU(Z)=max(Z,0)
#Utilisé pour filtrer les données positives d'une couche à la couche suivante
def relu(Z,pente=0.0,max_valeur=None,seuil=0):
    n=len(Z)
    A=[]
    if max_valeur==None:
        for i in range(n):
            if max(seuil,Z[i])==seuil:
                A+=[pente]
            else:
                A+=[Z[i]+pente]
    else:
        for i in range(n):
            if max(seuil,Z[i])==seuil:
                A+=[min(pente,max_valeur)]
            else:
                A+=[min(Z[i]+pente,max_valeur)]
    return A

#Definition de la fonction d'activation softmax(Z)=(exp(Z)/(sum(exp(Z))))
#Utilisé pour les classifications multiples (multiplaces)
def softmax(Z):
    n=len(Z)
    A=[]
    s=0
    for i in range(n):
        s+=exp(Z[i])
    for i in range(n):
        A+=[exp(Z[i])/s]
    return A

#Definition de la fonction d'activation softplus(Z)=log(exp(Z)+1)
#Utilisé pour filtrer les données positives d'une couche à la couche suivante
def softplus(Z):
    n=len(Z)
    A=[]
    for i in range(n):
        A+=[log(1+exp(Z[i]))]
    return A

#Definition de la fonction d'activation softsign(Z)=Z/(abs(Z)+1)
#Utilisé pour normaliser les données quand elles doivent être entre -1 et 1
def softsign(Z):
    n=len(Z)
    A=[]
    for i in range(n):
        A+=[Z[i]/(abs(Z[i])+1)]
    return A

#definition de la fonction d'activation tanh(Z)=(exp(Z)-exp(-Z))/(exp(Z)+exp(-Z))
#Utilisé pour les classifications binaires
#L'avantage par rapport à sigmoid c'est qu'elle conserve le signe des valeurs en entrée
#Elle retourne des valeurs entre -1 et 1. Plus on est proche de 1 plus le critère considéré est choisi et inversement si non
def tgh(Z):
    n=len(Z)
    A=[]
    for i in range(n):
        A+=[(exp(Z[i])-exp(-1*Z[i]))/(exp(Z[i])+exp(-1*Z[i]))]
    return A


#definition de la fonction d'activation ELU(Z)=Z si Z>0 et alpha*(exp(Z)-1) sinon
#Utilisé pour filtrer les données positives avec un lissage des valeurs lorsqu'elles sont < 0
def elu(Z,alpha):
    n=len(Z)
    A=[]
    for i in range(n):
        if Z[i]>0:
            A+=[Z[i]]
        else:
            A+=[alpha*(exp(Z[i])-1)]
    return A


#definition de la fonction d'activation SELU(Z)=scale*Z si Z>0 et alpha*scale*(exp(Z)-1) sinon
#Utilisé pour filtrer les données positives avec un lissage des valeurs lorsqu'elles sont < 0
def selu(Z):
    alpha=1.67326324
    scale=1.05070098
    n=len(Z)
    A=[]
    for i in range(n):
        if Z[i]>0:
            A+=[scale*Z[i]]
        else:
            A+=[alpha*scale*(exp(Z[i])-1)]
    return A