#projet
#amoros guilhem et meynard alexandre
from tkinter import*
from random import randrange
#-----------------------------------#
#definition des fonctions
def move():
    global x,y,pX,pY, Serpent
    can.delete('all')
    i=len(Serpent)-1
    j=0
    while i > 0:
        Serpent[i][0]=Serpent[i-1][0]
        Serpent[i][1]=Serpent[i-1][1]
        can.create_rectangle(Serpent[i][0], Serpent[i][1], Serpent[i][0] +10, Serpent[i][1]+10,outline='deep sky blue', fill='black') 
        i=i-1
 
 
 
    #Serpent[1][0]=Serpent[0][0]
    #Serpent[1][1]=Serpent[0][1]
    #can.create_rectangle(Serpent[1][0], Serpent[1][1], Serpent[1][0] +10, Serpent[1][1]+10,
    can.create_oval(pX, pY, pX+10, pY+10, outline='firebrick', fill='firebrick')
    #print(Serpent[0],Serpent[1],Serpent[2])
 
    if direction  == 'gauche':
        Serpent[0][0]  = Serpent[0][0] - dx
        if Serpent[0][0] < 0:
            Serpent[0][0] = 493
    elif direction  == 'droite':
        Serpent[0][0]  = Serpent[0][0] + dx
        if Serpent[0][0] > 493:
            Serpent[0][0] = 0
    elif direction  == 'haut':
        Serpent[0][1]  = Serpent[0][1] - dy
        if Serpent[0][1] < 0:
            Serpent[0][1] = 493
    elif direction  == 'bas':
        Serpent[0][1]  = Serpent[0][1] + dy
        if Serpent[0][1] > 493:
            Serpent[0][1] = 0
    can.create_rectangle(Serpent[0][0], Serpent[0][1], Serpent[0][0]+10, Serpent[0][1]+10,outline='black', fill='deep sky blue')
    test()
    print("longueur du serpent",len(Serpent),Serpent)
    if flag != 0:
        fen.after(90, move)
 
def newGame():
    global pX,pY
    global flag
    if flag == 0:
        flag = 1
    move()
 
def touche(event):
	global direction
	code=event.keycode
	if code==38:
		direction='haut'
	elif code==40:
		direction='bas'
	elif code==37:
		direction='gauche'
	elif code==39:
		direction='droite'
 
def test():
    global pomme
    global x,y,pX,pY
    global Serpent
    if Serpent[1][0]>pX-10 and  Serpent[1][0]<pX+10:        
        if Serpent[1][1]>pY-10 and Serpent[1][1]<pY+10:
            #On remet une pomme au hasard
            pX = randrange(5, 495)
            pY = randrange(5, 495)
            can.coords(pomme,pX, pY, pX+5, pY+5)
            #On joute un nouveau point au serpent
            Serpent.append([0,0])
            Serpent.append([1,1])
            Serpent.append([2,2])
            Serpent.append([3,3])
			#print(Serpent)

x = 245
y = 24        
dx, dy = 10, 10
flag = 0
direction = 'bas'
Serpent=[[x,y],[x+2.5,y+2.5],[x+5,y+5],[0,0]]
 
pX = randrange(5, 495)
pY = randrange(5, 495)
 
fen = Tk()
can = Canvas(fen, width=500, height=500, bg='black')
can.pack(side=TOP, padx=5, pady=5) 
 
#rectangle2=can.create_rectangle(Serpent[2][0], Serpent[2][1], Serpent[2][0] +10, Serpent[2][1]+10, outline='navy blue', fill='sky blue')
 
rectangle1=can.create_rectangle(Serpent[1][0], Serpent[1][1], Serpent[1][0] +10, Serpent[1][1]+10, outline='black', fill='deep sky blue')
 
rectangle = can.create_rectangle(Serpent[0][0], Serpent[0][1], Serpent[0][0]+10, Serpent[0][1]+10, outline='dark slate gray', fill='deep sky blue')
 
pomme = can.create_oval(pX, pY, pX+10, pY+10, outline='firebrick', fill='firebrick')
 
b1 = Button(fen, text='Lancer', command=newGame, bg='black' , fg='sky blue')
b1.pack(side=LEFT, padx=5, pady=5)
 
b2 = Button(fen, text='Quitter', command=fen.destroy, bg='black' , fg='sky blue')
b2.pack(side=RIGHT, padx=5, pady =5)

fen.bind_all('<Key>',touche)
 
fen.mainloop()





#---------------------------------------#
#programme principal
#---------------------------------------#
#déclaration des variables
