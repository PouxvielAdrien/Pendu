#Header
"""
Cette page contient les fonctions nécessaires pour jouer à une version du jeu Pendu sur console
Auteur : Adrien Pouxviel
Il a été réalisé le 08/12/2020

Lien du git : https://github.com/PouxvielAdrien/Pendu
"""

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
    for lettre in motAdeviner:  # la variable lettre parcourt le mot à deviner lettre par lettre
        if lettre in lettreTestee:
            lettredevine.append(lettre)

        else:
            lettredevine.append("_")
    return lettredevine
    


# Utilisateur rentre une lettre
def Utilisateur():  
    lettreUtilisateur=input("choisir une lettre: ")
    
    return lettreUtilisateur.lower()



def jeu():

    partie = True
    vie = 8
    document = lectureDoc()
    dites = []
    motAdeviner = Mot(document) 
    lettredevine = [motAdeviner[0]]
    

    while partie :

        print(motAdeviner)

        if vie == 0 :
            partie=False
            print('Vous avez perdu')
            
        elif len(lettredevine)==len(motAdeviner):
            print("Vous avez gagné")
            print("Vous avez deviné le mot : ", motAdeviner) 
            partie=False

        else : 
            print("Le mot à deviner est : ", Affichage(motAdeviner,lettredevine))
            print("Il vous reste ",vie," vies")
            continuer = True
            
            
        while continuer :  

            testU=Utilisateur()

            if testU in motAdeviner:     
                occurence = motAdeviner.count(testU)  #compte le nombre de fois que la lettre rentrée est dans le mot a deviner
                lettredevine += testU*occurence
                dites.append(testU)
                print("Lettre trouvée")    
                print("Les lettres que vous avez déjà dites sont : ", dites)
                continuer = False

            elif testU in lettredevine :
                print("Lettre déjà trouvée")
                continuer = False
    
            elif testU in dites :
                print("Lettre déjà dite")
                continuer = False
                          
            else:
                vie = vie - 1
                dites.append(testU)
                print("La lettre n'est pas bonne")
                print("Les lettres que vous avez déjà dites sont : ", dites)
                continuer = False


    nouvellePartie = input('Voulez vous recommencer:(o/n): ')

    if nouvellePartie.lower() == "n":
        partie = False    
        print("Au revoir")   

    elif nouvellePartie.lower() == "o":
        jeu()


             
            

       



