from tkinter import*
fenetre=Tk()
liste_cercle=[]
largeur=600
hauteur=600
couleur="light blue"
fenetre.title("Space Invaders")
fenetre.geometry(str(largeur)+"x"+str(hauteur))
fenetre.configure(bg=couleur)
can=Canvas(fenetre,width=largeur,height=hauteur-100,bg="orange")
can.grid(row=0,column=0,columnspan=4)
Bstart=Button(fenetre,text="Start Game",command=lambda:cercle(can))
Bstart.grid(row=1,column=1)
Bquit=Button(fenetre,text="Quit",command=fenetre.destroy)
Bquit.grid(row=1,column=2)
Bquit=Button()
create_image('espace')
fenetre.mainloop()