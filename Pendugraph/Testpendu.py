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
    mot=[]
    for lt in choix:
        if lt in corresp:
            mot.append(corresp[lt])
        else:
            mot.append(lt)
    return mot



print(Mot(lectureDoc()))

"""
#affiche le mot avec _  pour les lettres non devinées
def Affichage(mot, lettreDevine):
    devine=[]
    for lt in mot:
        if lt in lettreDevine:
            devine.append(lt)

        else:
            devine.append("_")
    return devine

def Utilisateur():
    lettreUtilisateur=input("choisir une lettre: ")
    
    return lettreUtilisateur.lower()

print(Affichage(Mot(lectureDoc()),Utilisateur))
"""