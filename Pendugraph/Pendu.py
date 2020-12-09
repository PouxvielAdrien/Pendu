#Header
"""
Cette page contient les fonctions nécessaires pour jouer à une version du jeu Pendu sur tkinter
Auteur : Adrien Pouxviel
Il a été réalisé le 08/12/2020
To Do : Ajouter la fonctionnalité meilleur score

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
def Affichage(motadeviner,lettreTestee):
    lettredevine = []
    for lettre in motadeviner:
        if lettre in lettreTestee:
            lettredevine.append(lettre)

        else:
            lettredevine.append("_")
    return lettredevine