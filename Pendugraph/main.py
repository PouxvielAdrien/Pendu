#Header
"""
Ce programme permet via tkinter de jouer à une version du jeu Pendu
Auteur : Adrien Pouxviel
Il a été réalisé le 09/12/2020
To Do : aspect graphique à améliorer

Lien du git : https://github.com/PouxvielAdrien/Pendu
"""

# Importation des fonctions
from tkinter import Tk,Button,Entry,Label,Frame,Canvas,PhotoImage
import random
from Pendu import lectureDoc,Mot,Affichage


### Initialisation du jeu
vie = 7
motAdeviner = Mot(lectureDoc())
lettredevinee = [motAdeviner[0]] #liste des lettres devinées
dites = [] # liste des lettres deja dites
gagne = False
perdu = False


# Fonction qui permet de relancer correspondance tant qu'on a pas perdu ou de relancer une autre partie si on a gagné ou perdu
def envoyer():

    if boutton_valider['text'] == "Entrer une nouvelle lettre" :
        correspondance()
    elif boutton_valider['text'] == "Nouvelle partie" :
        rejouer()




### Initialisation fenêtre
window = Tk()
window.title("Pendu")
window.geometry('600x500')
window.configure(bg = "#3c3e43")

# Mot à trouver/afficher
mot_affiche = Label(window,text = Affichage(motAdeviner,lettredevinee),bg = "#3c3e43",fg = "white",width = 35)
mot_affiche.pack()

# Indications qu'on modifiera si la lettre proposée a déjà été dite
indications = Label(window,text = "Entrer une lettre",bg = "#3c3e43",fg = "white")
indications.pack()

# Lettres déjà dites
lettres_dites = Label(window,text = "Lettres déjà dites "+str(dites),bg = "#3c3e43",fg = "white")
lettres_dites.pack()

# Entrer la lettre
entree = Entry(window,width =30)
entree.pack()

# Valider la lettre
boutton_valider=Button(window,text = "Entrer une nouvelle lettre", bg ="white", fg ="black",command=envoyer)
boutton_valider.pack()

## Initialisation Images
hauteur = 300
largeur = 300
canvas = Canvas(window,width = largeur,height = hauteur,bg = "#3c3e43",highlightthickness = 0)

# On importe les images du pendu
images=[]
for i in range(1,9):
    images.append(PhotoImage(file = "images/bonhomme" + str(i) + ".gif"))
images.reverse()

photopendu=canvas.create_image(0,0,anchor = 'nw' , image=images[7])
canvas.pack()

# Affichage nombre de vies
nbvies=Label(window,text = "Il vous reste 7 vies" ,bg='red',fg="black")
nbvies.pack()



### Fonctions du jeu 

def nouvelle_image(vie):
    canvas.itemconfig(photopendu, image = images[vie])
    nbvies['text'] = "Il vous reste " + str(vie) + " vies"

def victory():
    boutton_valider["text"] = "Nouvelle partie" 
    indications['text'] = "Vous avez gagné"


def loose():
    global perdu
    perdu = True
    boutton_valider["text"] = "Nouvelle partie" 
    indications['text'] = "C'est perdu ! Le mot à deviner était " + motAdeviner



def correspondance():
    global motAdeviner,lettredevinee,gagne,perdu,vie,dites

    lettre = entree.get()[0] #au cas où l'utilisateur rentre plusieurs lettres
    if vie>0 :
        if lettre in lettredevinee:
            indications['text'] = "Lettre déjà trouvée"

        elif lettre in motAdeviner:
            dites+=[lettre]
            occurence=motAdeviner.count(lettre)
            lettredevinee+=lettre*occurence
            indications['text'] = "Lettre trouvée"
            lettres_dites['text'] = 'Lettres déjà proposées '+str(dites)
            if len(lettredevinee)==len(motAdeviner):
                gagne=True
                victory()

        elif lettre in dites :
            indications['text'] = "Lettre déjà dite"
        else:
                
            dites+=[lettre]
            lettres_dites['text'] = 'Lettres déjà proposées '+str(dites)
            vie-=1
            indications['text'] = "La lettre proposée n'est pas bonne"

        mot_affiche['text'] = Affichage(motAdeviner,lettredevinee)
        nouvelle_image(vie)
 
    else:
        loose()



# Fonction qui permet de relancer une partie mais la derniere lettre tapée doit etre effacée d'abbord
def rejouer():
    global motAdeviner,lettredevinee,gagne,perdu,vie,dites

    vie = 7
    motAdeviner = Mot(lectureDoc())
    lettredevinee = [motAdeviner[0]] 
    dites = [] 
    gagne = False
    perdu = False
    nouvelle_image(vie)
    boutton_valider["text"] = "Entrer une nouvelle lettre"
    mot_affiche['text'] = Affichage(motAdeviner,lettredevinee)
    indications['text'] = "Entrer une lettre"
    nbvies['text'] = "Il vous reste 7 vies"
    lettres_dites['text'] = 'Lettres déjà proposées '+str(dites)


# A enlever si vous ne voulez pas tricher
print(motAdeviner)

window.mainloop()
