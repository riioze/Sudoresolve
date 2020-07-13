from tkinter import *
import copy
fenetreInitiale = Tk()


Sudoku = Frame(fenetreInitiale, width=1000, height=1000, borderwidth=1)

l1 = Frame(Sudoku,width=1000,height=250,borderwidth=1)
l2 = Frame(Sudoku,width=1000,height=250,borderwidth=1)
l3 = Frame(Sudoku,width=1000,height=250,borderwidth=1)
l4 = Frame(Sudoku,width=1000,height=250,borderwidth=1)


v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
v6 = IntVar()
v7 = IntVar()
v8 = IntVar()
v9 = IntVar()
v10 = IntVar()
v11 = IntVar()
v12 = IntVar()
v13 = IntVar()
v14 = IntVar()
v15 = IntVar()
v16 = IntVar()

c1 = Entry(l1,textvariable=v1,width=2)
c2 = Entry(l1,textvariable=v2,width=2)
c3 = Entry(l1,textvariable=v3,width=2)
c4 = Entry(l1,textvariable=v4,width=2)
c5 = Entry(l2,textvariable=v5,width=2)
c6 = Entry(l2,textvariable=v6,width=2)
c7 = Entry(l2,textvariable=v7,width=2)
c8 = Entry(l2,textvariable=v8,width=2)
c9 = Entry(l3,textvariable=v9,width=2)
c10 = Entry(l3,textvariable=v10,width=2)
c11 = Entry(l3,textvariable=v11,width=2)
c12 = Entry(l3,textvariable=v12,width=2)
c13 = Entry(l4,textvariable=v13,width=2)
c14 = Entry(l4,textvariable=v14,width=2)
c15 = Entry(l4,textvariable=v15,width=2)
c16 = Entry(l4,textvariable=v16,width=2)


texteEntree = Label(fenetreInitiale, text = "Veuillez entrer le sudoku ci-dessous")

varTexte = IntVar()
ligneTexte = Entry(Sudoku, textvariable=varTexte, width=2)

boutonQuitter = Button(fenetreInitiale, text="Quitter", command=fenetreInitiale.destroy)

texteEntree.pack()
Sudoku.pack(fill=BOTH)
l1.pack(fill = X)
l2.pack(fill = X)
l3.pack(fill = X)
l4.pack(fill = X)

c1.pack(fill = Y, side="left")
c2.pack(fill = Y, side="left")
c3.pack(fill = Y, side="left")
c4.pack(fill = Y, side="left")
c5.pack(fill = Y, side="left")
c6.pack(fill = Y, side="left")
c7.pack(fill = Y, side="left")
c8.pack(fill = Y, side="left")
c9.pack(fill = Y, side="left")
c10.pack(fill = Y, side="left")
c11.pack(fill = Y, side="left")
c12.pack(fill = Y, side="left")
c13.pack(fill = Y, side="left")
c14.pack(fill = Y, side="left")
c15.pack(fill = Y, side="left")
c16.pack(fill = Y, side="left")
boutonQuitter.pack()


fenetreInitiale.mainloop()

liste=[]

for x in range(4):
	liste.append([])
	for y in range(4):
		liste[x].append([])

liste[0][0] = v1.get()
liste[0][1] = v2.get()
liste[0][2] = v3.get()
liste[0][3] = v4.get()
liste[1][0] = v5.get()
liste[1][1] = v6.get()
liste[1][2] = v7.get()
liste[1][3] = v8.get()
liste[2][0] = v9.get()
liste[2][1] = v10.get()
liste[2][2] = v11.get()
liste[2][3] = v12.get()
liste[3][0] = v13.get()
liste[3][1] = v14.get()
liste[3][2] = v15.get()
liste[3][3] = v16.get()

listeCarre = [[[0,0],[0,1],[1,0],[1,1]],[[0,2],[0,3],[1,2],[1,3]],[[2,0],[2,1],[3,0],[3,1]],[[2,2],[2,3],[3,2],[3,3]]] 

listeP = copy.deepcopy(liste)

for x in range(4):
	for y in range(4):
		if liste[x][y] == 0:
			listeP[x][y] = [1,2,3,4]
		else:
			listeP[x][y] = [liste[x][y]]
continuer = True

while continuer:
	for x in range(4):
		for y in range(4):
			if liste[x][y] != 0:
				for a in range(4):
					if liste[x][y] in listeP[x][a]:
						listeP[x][a].remove(liste[x][y])
				for b in range(4):
					if liste[x][y] in listeP[b][y]:
						listeP[b][y].remove(liste[x][y])
				for c in range(4):
					if [x,y] in listeCarre[c]:
						for d in range(4):
							if liste[x][y] in listeP[listeCarre[c][d][0]][listeCarre[c][d][1]]:
								listeP[listeCarre[c][d][0]][listeCarre[c][d][1]].remove(liste[x][y])

	for x in range(4):
		for y in range(4):
			if len(listeP[x][y]) == 1:
				liste[x][y] = listeP[x][y][0]

	continuer = False
	for x in range(4):
		for y in range(4):
			if liste[x][y] == 0:
				continuer = True



print(liste)
print(listeP)