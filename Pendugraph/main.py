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

couleur = "#3c3e43"
window = Tk()
window.title("Pendu")
window.geometry('600x300')
window.configure(bg=couleur)

# mot à trouver/afficher
mot_affiche=Label(window,text=Affichage(motAdeviner,lettredevinee),bg='red',fg="black",width=35)
mot_affiche.pack()

# indications
indications = Label(window,text="Entrez une lettre et appuyez sur Proposer",bg='red',fg="black")
indications.pack()

# lettres déjà dites
lettres_dites = Label(window,text="Lettres déjà dites "+str(dites),bg='red',fg="black")
lettres_dites.pack()

# pour entrer la lettre
entry = Entry(window,width=30)
entry.pack()

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



window.mainloop()
