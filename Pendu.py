import random

def test():
    print("c est une test")

def lectureDoc():
    fichier=open("bankdeMot.txt","r", encoding="utf8")
    listMOt=fichier.readlines()
    fichier.close()
    for i in range(len(listMOt)):
        listMOt[i]=listMOt[i].rstrip("\n")

    return listMOt

def Mot(listeMot):
    corresp={"è":"e","é":"e","â":"a","ê":"e","ï":"i"}
    i=random.randint(0, len(listeMot))
    choix=listeMot[i]
    lettre=[]
    for lt in choix:
        if lt in corresp:
            lettre.append(corresp[lt])
        else:
            lettre.append(lt)
    return lettre

def Affichage(mot, lettreDevine):
    listeAffiche=[]
    for lettre in mot:
        if lettre in lettreDevine:
            listeAffiche.append(lettre)
        else:
            listeAffiche.append("_")
    return listeAffiche

    


def Correspondance(motDevine,testUtilisateur,Devine , compteur):
    listeAffiche=[]
    if testUtilisateur in motDevine:
        occurence= motDevine.count(testUtilisateur)
        for i in range(occurence):
            Devine.append(testUtilisateur)
        
        listeAffiche= Affichage(motDevine,Devine)
        
    else:
        compteur=compteur-1
        listeAffiche=Affichage(motDevine,Devine)    
        return Devine, compteur,listeAffiche


def FinDEPArtie(vie,motadeviner,lettreDejaDevine):
    valRen=True
    if vie==0:
        valRen= False
        print('loser')
    elif len(motadeviner)== len(lettreDejaDevine):
        valRen=False
        print("bien joué")
    return valRen   



