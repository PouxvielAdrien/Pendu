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
    
    for lettre in mot:
        if lettre in lettreDevine:
            print(lettre, end=" ")
        else:
            print("_", end=" ")
    print('')

    
def Utilisateur():
    lettreUtilisateur=input("choisir une lettre: ")
    
    return lettreUtilisateur.lower()


def Correspondance(motDevine,testUtilisateur,Dites , compteur):
    
    if testUtilisateur in motDevine:
        occurence= motDevine.count(testUtilisateur)
        for i in range(occurence):
            Dites.append(testUtilisateur)
        
        Affichage(motDevine,Dites)
        
    else:
        compteur=compteur-1
        Affichage(motDevine,Dites)
        print("il vous reste: ",compteur,' vies')
    return Dites, compteur

def FinDEPArtie(vie,motadeviner,lettreDejaDevine):
    valRen=True
    if vie==0:
        valRen= False
        print('loser')
    elif len(motadeviner)== len(lettreDejaDevine):
        valRen=False
        print("bien joué")
    return valRen   



