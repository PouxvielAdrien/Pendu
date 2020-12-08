#Header
"""
Lien du git : https://github.com/PouxvielAdrien/Pendu
"""
#importation des fonctions
from tkinter import Tk,Button,Entry,Label,Frame,Canvas,PhotoImage
import random



#Recupère les mots
def lectureDoc():
    fichier=open("bankdeMot.txt","r", encoding="utf8")
    listMOt=fichier.readlines()
    fichier.close()
    for i in range(len(listMOt)):
        listMOt[i]=listMOt[i].rstrip("\n")

    return listMOt



#Définit aléatoirement le mot, letrre par lettre dans une liste
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

#motAdeviner=Mot(lectureDoc())
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

#print(Affichage(motAdeviner,motAdeviner[0]))


"""
def Correspondance(motadeviner,lettreTeste,trouvees,vie):
    
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
"""





###Initialisation du jeu
motAdeviner=Mot(lectureDoc())
lettredevinee=[motAdeviner[0]]
gagne = False
perdu = False
dites = [] # liste des lettres deja dites
vie = 7



### Initialisation fenetre
window = Tk()
window.title("Pendu")
window.geometry('600x300')
window.configure(bg="#3c3e43")

# mot à trouver/afficher
mot_affiche=Label(window,text=Affichage(motAdeviner,lettredevinee),bg='red',fg="black",width=35)
mot_affiche.pack()

# indications qu'on modifiera si lettre proposée a déjà été dites
indications = Label(window,text="Entrez une lettre et appuyez sur Proposer",bg='red',fg="black")
indications.pack()

# lettres déjà dites
lettres_dites = Label(window,text="Lettres déjà dites "+str(dites),bg='red',fg="black")
lettres_dites.pack()

# pour entrer la lettre
entree = Entry(window,width=30)
entree.pack()

# pour valider la lettre
"""btn_valider = Button(window,text='Valider lettre',command=btn_press)"""
boutton_valider=Button(window,text="Propser lettre", bg="white", fg="red", command=lambda:Affichage())
boutton_valider.pack()

##Initialisation Images
hauteur=280
largeur=280
canvas = Canvas(window,width=largeur,height=hauteur,bg=couleur,highlightthickness=0)

# on créer toutes les images du pendu
images=[]
for i in range(1,9):
    images.append(PhotoImage(file="images/bonhomme"+str(i)+".gif"))

photopendu=canvas.create_image(0,0,anchor='nw' , image=images[0])
canvas.pack()

"""

def correspondance():
    global motAdeviner,lettredevinee,gagne,perdu,vie,dites

    lettre = entree.get()[0] #au cas où l'utilisateur rentre plusieurs lettres

    if lettre in lettredevinee:
        indications['text'] = "Lettre déjà trouvée"
    else:
        if lettre in motAdeviner:
            lettredevinee+=[lettre]
            indications['text'] = "Lettre trouvée"
#            if motAdeviner==Affichage(motAdeviner,lettredevinee):
#                gagne=True

        elif lettre in dites :
            indications['text'] = "Lettre déjà dite"
        else:
            
            dites+=[lettre]
            lettres_dites['text'] = 'Lettres testées '+str(dites)
            vie-=1
            indications['text'] = "Lettre proposée n'est pas bonne"

    mot_affiche['text'] = Affichage(motAdeviner,lettredevinee)

    if gagne :
        victory()
    else:
        nouvelle_image(vie)
        if vie==0:
            loose()



def nouvelle_image(vie):
    Canevas.itemconfig(photopendu, image=images[essai])
    nb_essais['text'] = "Essais restants : "+ str(7-essai)

def game_over():
    global echoue
    echoue = True
    btn_propose["text"] = 'Recommencer'
    indices['text'] = "GAME OVER, le mot était "+mot
    label_secondes['text'] = 'Votre meilleur score est de : '+strftime('%Mmin %Ssec',gmtime(meilleurscore))

def you_win():
    global meilleurscore
    btn_propose["text"] = 'Recommencer'
    indices['text'] = "Bravo !"

    if (120 - secondes) < meilleurscore:
        meilleurscore = 120 - secondes
    label_secondes['text'] = 'Votre meilleur score est de : '+strftime('%Mmin %Ssec',gmtime(meilleurscore))

def try_again():
    global mot,reussi,trouve,essai,rate,secondes,echoue
    reussi = False
    echoue = False
    mot = choice(L)
    trouve = [mot[0]]
    rate = []
    essai = 0
    change_bonhomme(essai)
    btn_propose["text"] = 'Proposer lettre'
    mot_affiche['text'] = write_devine_avec_espaces(mot,trouve)
    indices['text'] = "Entrez une lettre et appuyez sur Proposer"
    nb_essais['text'] = "Essais restants : 7"
    lettres_testes['text'] = 'Lettres testées '+str(rate)
    secondes = 120

"""
window.mainloop()
