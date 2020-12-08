#Lien du git
#https://github.com/PouxvielAdrien/Pendu

import Pendu
import tkinter


def Affichage():
    global entre ,motADeviner, texteAffiche,devine,vie
    print(entre.get()[0])
    devine,vie,texteAffiche=Pendu.Correspondance(motADeviner,entre.get()[0],devine,vie)
    print(texteAffiche)


document=Pendu.lectureDoc()
motADeviner=Pendu.Mot(document)
print(motADeviner)
devine=[]
vie=7
x=Pendu.Affichage(motADeviner,motADeviner[0])
devine.append(motADeviner[0])



maFenetre= tkinter.Tk()
maFenetre.title("pendu")

texteAffiche=tkinter.StringVar()
texteAffiche=devine

motAffiche=tkinter.Label(maFenetre,textvariable=texteAffiche,fg='black',bg='white')
motAffiche.pack()


entre=tkinter.Entry(maFenetre, width=30)
entre.pack()
y=Pendu.Correspondance(motADeviner,entre.get(),devine,vie)




largeur=500
hauteur=500
images=[tkinter.PhotoImage(file="images/bonhomme1.gif")]

canvas=tkinter.Canvas(maFenetre, width=largeur , height=hauteur, bg="#3c3e43" )
item=canvas.create_image(0,0,anchor='nw' , image=images[0])
canvas.pack()
boutton=tkinter.Button(maFenetre,text="Propser",fg="red", command=lambda:Affichage())
boutton.pack()



maFenetre.mainloop()