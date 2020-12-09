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


"""
def Correspondance(motAdeviner,testUtilisateur,lettredevine,compteur,dites):

    if testUtilisateur in motAdeviner:     
        occurence= motAdeviner.count(testUtilisateur)  #compte le nombre de fois que la lettre rentrée est dans le mot a deviner
        lettredevine+=testUtilisateur*occurence
        print("Lettre trouvée")    
        dites.append(testUtilisateur)
        print("Les lettres que vous avez déjà dites sont : ", dites)

    elif testUtilisateur in lettredevine :
            print("Lettre déjà trouvée")
    
    elif testUtilisateur in dites :
            print("Lettre déjà dite")
        
    else:
        compteur=compteur-1
        print("La lettre n'est pas bonne")
        dites.append(testUtilisateur)
        print("Les lettres que vous avez déjà dites sont : ", dites)
        

    return lettredevine, compteur, dites
"""

def jeu():

    partie = True
 #   meilleurScore = 0
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
            partie=False
            print("Vous avez gagné")
            print("Le mot à deviner était : ", motAdeviner)
        else : 
            print("Le mot à deviner est : ", Affichage(motAdeviner,lettredevine))
            print("Il vous reste ",vie," vies")
            continuer = True
            
            
        while continuer :  

            testU=Utilisateur()

            if testU in motAdeviner:     
                occurence= motAdeviner.count(testU)  #compte le nombre de fois que la lettre rentrée est dans le mot a deviner
                lettredevine+=testU*occurence
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
                
    print("au revoir")            
            
jeu()
       
"""
#La fonction game est la fonction qui correspond à un tour de jeu    
def game ():
        score = 8 #chaque tour on a nos 8 chances
        listeLetter = [] # Liste des lettre utilisé lors du tour de jeu
        word = wordChoice(listeCreate()) #Récupère un mot du fichier texte
        
        
        searchedWord = StartWordPrint(word) #Créé le mot "caché" : la première lettre du mot et les tirets
              
        game = True #Création d'un flag (d'une condition du tour de jeu)
        
        while game == True :
                        
            print(searchedWord) #affihe à l'utilisateur le mot caché

 

            flag1= False #création d'un flag pour le choix de la lettre (redemande la lettre)
            
            while flag1== False:
                user_letter = input (" choisissez une lettre : ")
                if user_letter.isalpha() == True: # verifie si c'est bien un str qui est rentré
                        if len(user_letter) == 1: # verifie qu'il y a bien une lettre de rentré
                            if user_letter not in listeLetter: #verifie si la lettre a pas déja été utilié 
                                flag1=True #condition de sortie de la boucle 
                       
                    
                  
                
            listeLetter.append(user_letter) #on ajoute la lettre entré par l'utilisateur dans la liste des lettre utilisé
            
            position = letterPosition(user_letter , word) #retourne position si lettre dans le mot            
                   
            if position == []: #Si lettre pas dans le mot : perte d'une chance 
                score -= 1
                print("il vous restes : " , score , "chance(s)")
                if score <= 0: #si score est à 0 fin de partie
                    print ("vous perdez")
                    game = False #condition de sortie du tour de jeu

 

            else: #si lettre dans le mot on ajoute la ou les lettre(s) suivant les positions dans le mot "caché"
                searchedWord = appendLetters(position, user_letter, searchedWord)
         
            
            if  searchedWord == " ".join(word): #si le mot caché est le même que le mot choisie dans le fichier texte : il a trouvé toutes les lettre il gagne
                
                print("vous avez gagnez")
                game = False #condition de sortie du tour de jeu
                
        flag2 = False #flag pour redemander à l'utilisateur si il saisie une valeur incorecte       
        while flag2 == False:
            condition = input("voulez vous rejouer ? ")  
            if condition == "oui":
                flag2 = True 
                return(True) # permet de rejouer une partie (boucle while du Main)
                
            if condition == "non": #permet arreter la partie (condition de sortie de la boucle while du Main)
                flag2 = True
                return(False)

"""
"""
def FinDepartie(vie,motAdeviner,lettreDejaDevine):
    valRen=True
    if vie==0:
        valRen= False
        print('loser')
    elif len(motAdeviner)== len(lettreDejaDevine):
        valRen=False
        print("Vous avez gagné")
    return valRen   

def jeu():

partie = True
meilleurScore = 0

while partie :
    vie=8
    lettredevine = []
    continuer = True
    document = lectureDoc()
    lettresdites = []
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
    print("Le mot à deviner était : " motAdeviner)
    nouvellePartie = input('Voulez vous recommencer:(o/n): ')

    if nouvellePartie.lower() == "n":
        partie=False  

print("merci bye")





motAdevine=Mot(lectureDoc())
print(motAdevine)
print(Affichage(motAdevine,motAdevine[0]))
#print(Affichage(motAdevine,[motAdevine[0],Utilisateur()]))


print(Correspondance(motAdevine,Utilisateur(),motAdevine[0],8,[]))
"""

