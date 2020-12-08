import random

#recupère les mots
def lectureDoc():
    fichier=open("bankdeMot.txt","r", encoding="utf8")
    listMOt=fichier.readlines()
    fichier.close()
    for i in range(len(listMOt)):
        listMOt[i]=listMOt[i].rstrip("\n")

    return listMOt



#Définit le mot, letrre par lettre dans une liste
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
def lettreU():  
    lettreUtilisateur=input("choisir une lettre: ")
    
    return lettreUtilisateur.lower()

#lettreU=Utilisateur()  

#affiche le mot avec _  pour les lettres non devinées
def Affichage(motadeviner,lettreTestee):
    lettredevine=[]
    for lettre in motadeviner:
        if lettre in lettreTestee:
            lettredevine.append(lettre)

        else:
            lettredevine.append("_")
    return lettredevine

#print(Affichage(motAdeviner,lettreU()))


#Initialisation du jeu



"""
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



"""
def FinDEPArtie(vie,motadeviner,lettreDejaDevine):
    valRen=True
    if vie==0:
        valRen= False
        print('loser')
    elif len(motadeviner)== len(lettreDejaDevine):
        valRen=False
        print("bien joué")
    return valRen   
"""