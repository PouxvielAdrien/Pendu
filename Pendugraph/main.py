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




"""
###Initialisation du jeu
L=lectureDoc()
motAdeviner=Mot(L)
lettredevinee=[motAdeviner[0]]
gagne = False
perdu = False
dites = [] # liste des essais ratés
vie = 7
"""

### Initialisation fenetre

couleur = "#3c3e43"
window = Tk()
window.title("Pendu")
window.geometry('600x300')
window.configure(bg=couleur)
window.mainloop()

'''
# mot à trouver
mot_affiche=Label(Affichage(motAdeviner,lettredevinee),bg=couleur,fg="white",width=35)
mot_affiche.pack()




mot_affiche.config(font=("Courier", 10))
#mot_affiche.pack(side="left")
mot_affiche.grid(row=1,column=1)


# cadre gauche
Cadre=Frame(window,relief="groove", bg=couleur)
Cadre.grid(row=2,column=1)

# indications
indices = Label(window,text="Entrez une lettre et appuyez sur Proposer",bg=couleur,fg="cyan")
indices.grid(row=3,column=1)


# nb d'essais restants
nb_essais = Label(window,text="Essais restants : 7",bg=couleur,fg="cyan")
nb_essais.grid(row=3,column=1,sticky="S")

# listes lettres
lettres_testes = Label(window,text='Lettres testées '+str(rate),bg=couleur,fg="white")
lettres_testes.grid(row=1,column=1,sticky='S')

# pour entrer la lettre
entry = Entry(Cadre)
entry.grid(row=1,column=1)

# pour valider la lettre
btn_propose = Button(Cadre,text='Proposer lettre',command=btn_press)
btn_propose.grid(row=1,column=2)

#bouton quitter
btnQuit = Button(window,text="Quitter le pendu",fg='red',command=window.destroy)
btnQuit.grid(row=4,column=1)


#imagependu
hauteur=280
largeur=280
Canevas = Canvas(window,width=largeur,height=hauteur,bg=couleur,highlightthickness=0)

images = []
for i in range(1,9):
    # on crée toutes les images du pendu
    images.append(PhotoImage(file="gif//bonhomme"+str(i)+".gif"))

# on affecte la première image
imagependu= Canevas.create_image(hauteur/2,largeur/2,image=images[0])
Canevas.grid(row=1,column=2,rowspan=4,padx=10,pady=10,sticky="E")
'''