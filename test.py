import Pendu
import tkinter



def lettre(lettre,pDevine,pVie):
    pDevine,vie,lettre=Pendu.Correspondance("bonjour", entre.get(),pDevine,pVie)
    LabelMotRech["text"]=lettre

def  choixImg(pvie): 
    canvas.itemconfigure(item,image=(images[pvie]))
    
vie=7
dejaDevine=[]    


x = Pendu.Correspondance("bonjour", "b",dejaDevine,vie)

maFenetre= tkinter.Tk()
maFenetre.title("pendu")
images=[tkinter.PhotoImage(file="images/bonhomme1.gif"),tkinter.PhotoImage(file="images/bonhomme2.gif"),tkinter.PhotoImage(file="images/bonhomme3.gif"),tkinter.PhotoImage(file="images/bonhomme4.gif"),tkinter.PhotoImage(file="images/bonhomme5.gif"),tkinter.PhotoImage(file="images/bonhomme6.gif"),tkinter.PhotoImage(file="images/bonhomme7.gif"),tkinter.PhotoImage(file="images/bonhomme8.gif")]


print(images)    

value=tkinter.StringVar(maFenetre)
value.set("entrer votre lettre")

entre=tkinter.Entry(maFenetre,textvariable=True, width=30)
entre.pack()
btn=tkinter.Button(maFenetre,text="Changer",fg="red", command=lambda:lettre(x,dejaDevine,vie))
btn.pack()


    

LabelMotRech=tkinter.Label(maFenetre,text=x,fg='black',bg='white')
LabelMotRech.pack()

largeur=500
hauteur=500
canvas=tkinter.Canvas(maFenetre, width=largeur , height=hauteur, bg="#3c3e43" )
item=canvas.create_image(0,0,anchor='nw' , image=images[7])
canvas.pack()
boutton=tkinter.Button(maFenetre,text="Changer",fg="red", command=lambda:choixImg(vie))
boutton.pack()
maFenetre.mainloop()







"""
partie=True
meilleurScore=0

while partie:
    
    continuer=True
    document=Pendu.lectureDoc()
    toutesLettres=[]
    motADeviner=Pendu.Mot(document)

    dejaDevine, vie=Pendu.Correspondance(motADeviner,motADeviner[0], dejaDevine, vie)

    print(motADeviner)

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
"""








