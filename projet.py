from tkinter import*
def cercle(can):
	item=can.create_oval(0,0,120,120,fill="light blue",outline="dark blue")
	liste_cercle.append(item)
def carre(can):
	item=can.create_rectangle(0,0,120,120,fill="red",outline="pink")
def polygone(can):
	can.create_polygon(0,0,250,250,500,500,fill="gold",outline="black")
def effacer(can,liste_item):
		for w in lisite_item:can.delete(w)
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
B1=Button(fenetre,text="CERCLE",command=lambda:cercle(can))
B1.grid(row=1,column=1)
B2=Button(fenetre,text="CARRE",command=lambda:carre(can))
B2.grid(row=1,column=2)
B3=Button(fenetre,text="POLYGONE",command=lambda:polygone(can))
B3.grid(row=1,column=3)
fenetre.mainloop()