#Header
"""
Ce programme permet de jouer à une version du jeu Pendu sur console
Auteur : Adrien Pouxviel
Il a été réalisé le 08/12/2020

Lien du git : https://github.com/PouxvielAdrien/Pendu
"""

# Importation des fonctions

from Pendu import lectureDoc,Mot,Affichage,Correspondance,Utilisateur, FinDepartie

### Initialisation du jeu
partie = True
meilleurScore = 0

while partie :
    vie=8
    lettredevine = []
    continuer = True
    document = lectureDoc()
    toutesLettres = []
    motAdeviner = Mot(document)

    lettredevine, vie = Correspondance(motAdeviner,motAdeviner[0], lettredevine, vie)


# Définit la boucle pour continuer a jouer
    while continuer:
        testU = Utilisateur()
        if testU not in toutesLettres :
            toutesLettres.append(testU)
            lettredevine, vie = Correspondance(motAdeviner, testU, lettredevine, vie)
            continuer = FinDepartie(vie, motAdeviner, lettredevine)
            print(toutesLettres)
        else:
            print("La lettre a déjà été dite")  
            print(toutesLettres) 
    
    if vie > meilleurScore:
        meilleurScore=vie
    
    print("C'est fini")
    print("Le mot à deviner était : " (motAdeviner))
    nouvellePartie = input('Voulez vous recommencer:(o/n): ')
    if nouvellePartie.lower() == "n":
        partie=False  

print("merci bye")



