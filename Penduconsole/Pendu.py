import random


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
    lettredumot=[]
    for lt in choix:
        if lt in corresp:
            lettredumot.append(corresp[lt])
        else:
            lettredumot.append(lt)
    return lettredumot


motAdeviner=Mot(lectureDoc())
#print(motAdeviner)

#utilisateur rentre une lettre
def Utilisateur():  
    lettreUtilisateur=input("choisir une lettre: ")
    
    return lettreUtilisateur.lower()

lettreU=Utilisateur()  


def Affichage(mot, lettreDevine):
    
    for lettre in mot:
        if lettre in lettreDevine:
            print(lettre, end=" ")
        else:
            print("_", end=" ")
    print('')

    



#motDevine=Mot(lectureDoc())    cest le mot à deviner
def Correspondance(motDevine,testUtilisateur,Dites , compteur):
    
    if testUtilisateur in motDevine:     #testUtilisateur=lettre rentrée par lutilisateur
        occurence= motDevine.count(testUtilisateur)  #compte le nombre de fois que la lettre rentrée est dans le mot a deviner
        for i in range(occurence):
            Dites.append(testUtilisateur)
        
        Affichage(motDevine,Dites)    #Dites=lettres deja devinée
        
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
