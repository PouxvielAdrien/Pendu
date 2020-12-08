import Pendu


partie=True
meilleurScore=0

while partie:
    vie=8
    dejaDevine=[]
    continuer=True
    document=Pendu.lectureDoc()
    toutesLettres=[]
    motADeviner=Pendu.Mot(document)

    dejaDevine, vie=Pendu.Correspondance(motADeviner,motADeviner[0], dejaDevine, vie)

    #print(motADeviner)

    while continuer:
        testU=Pendu.Utilisateur()
        if testU not in toutesLettres:
            toutesLettres.append(testU)
            dejaDevine, vie =Pendu.Correspondance(motADeviner,testU, dejaDevine, vie)
            continuer=Pendu.FinDEPArtie(vie,motADeviner,dejaDevine)
            print(toutesLettres)
        else:
            print("la lettre a deja ete dite")  
            print(toutesLettres) 
    
    if vie> meilleurScore:
        meilleurScore=vie
    
    print("c'est fini")
    print("le mot a deviner était: "+"".join(motADeviner))
    nouvellePartie=input('voulez vous recommencer:(o/n): ')
    if nouvellePartie.lower()=="n":
        partie=False  

print("merci bye")



