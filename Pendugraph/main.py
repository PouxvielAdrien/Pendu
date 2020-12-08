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





#Affiche le mot avec _  pour les lettres non devinées
def Affichage(motadeviner,lettreTestee):
    lettredevine=[]
    for lettre in motadeviner:
        if lettre in lettreTestee:
            lettredevine.append(lettre)

        else:
            lettredevine.append("_")
    return lettredevine





###Initialisation du jeu
motAdeviner=Mot(lectureDoc())
lettredevinee=[motAdeviner[0]]
gagne = False
perdu = False
dites = [] # liste des lettres deja dites
vie = 7

def envoyer():
    if boutton_valider['text'] == "Entrer une nouvelle lettre" :
        correspondance()
    elif boutton_valider['text'] == "Nouvelle partie" :
        print('vous avez perdu')
 #       rejouer()
        

#A enlever si vous ne voulez pas tricher
print(motAdeviner)

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
boutton_valider=Button(window,text="Entrer une nouvelle lettre", bg="white", fg="red")
boutton_valider.pack()

##Initialisation Images
hauteur=280
largeur=280
canvas = Canvas(window,width=largeur,height=hauteur,bg="#3c3e43",highlightthickness=0)
# on créer toutes les images du pendu
images=[]
for i in range(1,9):
    images.append(PhotoImage(file="images/bonhomme"+str(i)+".gif"))
images.reverse()

photopendu=canvas.create_image(0,0,anchor='nw' , image=images[0])
canvas.pack()

#affichage nombre de vies
nbvies=Label(window,text="Il vous reste 7 vies" ,bg='red',fg="black")
nbvies.pack





def nouvelle_image(vie):
    canvas.itemconfig(photopendu, image=images[vie])
    nbvies['text'] = "Il vous reste  : "+ str(vie)

def victory():
 #   global meilleurscore
    boutton_valider["text"] = "Nouvelle partie" 
    indications['text'] = "Vous avez gagné"
#Afficher meilleur score et le changer si noiveau meilleur score est mieux que lancien

def loose():
    global perdu
    perdu = True
    boutton_valider["text"] = "Nouvelle partie" 
    indications['text'] = "C'est perdu ! Le mot à deviner était "+motAdeviner

#meilleur score a afficher

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

    if gagne  :
        victory()
    else:
        nouvelle_image(vie)
        if vie==0:
            loose()
        else : 
            print('vous avez perdu')
 #           rejouer()




"""
def rejouer():
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
