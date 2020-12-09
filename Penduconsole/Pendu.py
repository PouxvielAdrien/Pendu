from random import randint

# Recupère les mots
def lectureDoc():
    fichier = open("bankdeMot.txt","r", encoding="utf8")
    listMOt = fichier.readlines()
    fichier.close()
    for i in range(len(listMOt)):
        listMOt[i] = listMOt[i].rstrip("\n")
 
    listMOt.sort() #trie des éléments selon leur ordres alphabétiques
    listMOt.sort(key=lambda element: len(element)) #trie des éléments selon leurs tailles
    return listMOt




# Définit aléatoirement le mot, letrre par lettre dans une liste
def Mot(listeMot):
    corresp = {"è":"e","é":"e","â":"a","ê":"e","ï":"i"}
    i = randint(0, len(listeMot))
    choix = listeMot[i]
    lettredumot = []
    for lt in choix:
        if lt in corresp:
            lettredumot.append(corresp[lt])
        else:
            lettredumot.append(lt)
    return lettredumot


# Affiche le mot avec des _  pour les lettres non devinées
def Affichage(motAdeviner,lettreTestee):
    lettredevine = []
    for lettre in motAdeviner:
        if lettre in lettreTestee:
            lettredevine.append(lettre)

        else:
            lettredevine.append("_")
    return lettredevine
    




def Correspondance(motAdeviner,testUtilisateur,lettresdevines , compteur):
    
    if testUtilisateur in motAdeviner:     
        occurence= motAdeviner.count(testUtilisateur)  #compte le nombre de fois que la lettre rentrée est dans le mot a deviner
        lettresdevines.append(testUtilisateur*occurence)
        
        Affichage(motAdeviner,lettresdevines)    
        
    else:
        compteur=compteur-1
        Affichage(motAdeviner,lettresdevines)
        print("il vous reste: ",compteur,' vies')

    return lettresdevines, compteur



def FinDepartie(vie,motAdeviner,lettreDejaDevine):
    valRen=True
    if vie==0:
        valRen= False
        print('loser')
    elif len(motAdeviner)== len(lettreDejaDevine):
        valRen=False
        print("bien joué")
    return valRen   
