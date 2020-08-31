from tkinter import *
import copy
w = 504
h = 504
ch = h/9
cw = w/9
CasesRect = []
préparation = True
fenetreInitiale = Tk()
fenetreInitiale.title("Résoudre des sudokus")
def delete(tag):
	cSudoku.delete(fenetreInitiale,tag)
def onClickEvent(evt):
	global Select
	print('touché')
	for x in range(9):
		for y in range(9):
			if int(evt.x) in range(Cases[x][y].x1,Cases[x][y].x2+1) and int(evt.y) in range(Cases[x][y].y1,Cases[x][y].y2+1):
				Select = Cases[x][y]
def Keycode(evt):
	global préparation
	touche = evt.keysym
	isint = True
	try:
		touche = int(touche)
	except ValueError as e:
		isint = False
	if isint:
		Select.valeur = int(evt.keysym)
	else:
		if touche == 'space':
			préparation = False

	print(touche)

Cases = []
cSudoku = Canvas(fenetreInitiale, width=w, height=h)
cSudoku.bind('<Button-1>',onClickEvent)
cSudoku.focus_set()
cSudoku.bind('<Key>',Keycode)
cSudoku.pack()
ligne = []
ligne.append(cSudoku.create_line(w/3,0,w/3,h,width = 5))
ligne.append(cSudoku.create_line(w/3*2,0,w/3*2,h,width = 5))
ligne.append(cSudoku.create_line(0,h/3,w,h/3,width = 5))
ligne.append(cSudoku.create_line(0,h/3*2,w,h/3*2,width = 5))
for x in range(9):
	CasesRect.append([])
	for y in range(9):
		CasesRect[x].append(None)
class Case:
	"""docstring for Case."""

	def __init__(self, x,y):
		self.x = x
		self.y = y
		self.valeur = None
		self.possibilitees = [[1,2,3],[4,5,6],[7,8,9]]
		self.x1 = int(self.x*ch)
		self.x2 = int((self.x+1)*ch)
		self.y1 = int(self.y*ch)
		self.y2 = int((self.y+1)*ch)
		self.cPossibilitees = []
		self.ligne = []
		self.colone = []
		self.carre = []
		for i in range(3):
			self.cPossibilitees.append([])
			for j in range(3):
				self.cPossibilitees[i].append(self.possibilitees[i][j])
	def show(self,color):
		CasesRect[self.x][self.y] = cSudoku.create_rectangle(self.x1,self.y1,self.x2,self.y2,outline = color)
		np = 0
		if self.valeur == None:
			if préparation == False:
				for i in range(3):
					for j in range(3):
						if self.possibilitees[i][j] != 0:
							self.cPossibilitees[i][j] = cSudoku.create_text(self.x1+((j+0.5)*ch/3),self.y1+((i+0.5)*(ch/3)),text = str(self.possibilitees[i][j]),font = ("Purisa",int(ch/3-3)),tags = str(self.x*9+self.y)+"-"+str(i*3+j))
						else:
							np +=1
			if np == 8:
				for i in range(3):
					for j in range(3):
						if self.possibilitees[i][j] != 0:
							self.valeur = self.possibilitees[i][j]
		else:
			for i in range(3):
				for j in range(3):
						delete(str(self.x*9+self.y)+"-"+str(i*3+j))
			self.av = cSudoku.create_text(self.x1+(0.5*ch),self.y1+(0.5*ch), text = int(self.valeur), font = ("Purisa",int(ch-5)))
	def creatNeighbors(self):
		for a in range(9):
			self.ligne.append(Cases[a][self.x])
			self.colone.append(Cases[self.y][a])
		if self.x in range(3):
			rx = [0,3]
		elif self.x in range(3,6):
			rx = [3,6]
		else:
			rx = [6,9]
		if self.y in range(3):
			ry = [0,3]
		elif self.y in range(3,6):
			ry = [3,6]
		else:
			ry = [6,9]
		for a in range(rx[0],rx[1]):
			for b in range(ry[0],ry[1]):
				self.carre.append(Cases[a][b])
	def pDelete(self,p):
		for i in range(len(self.possibilitees)):
			for j in range(len(self.possibilitees[i])):
				if p == self.possibilitees[i][j]:
					delete(str(self.x*9+self.y)+"-"+str(i*3+j))
					self.possibilitees[i][j] = 0
					return

for x in range(9):
	Cases.append([])
	for y in range(9):
		Cases[x].append(Case(x,y))

for x in range(9):
	for y in range(9):
		Cases[x][y].show('black')
Select = Cases[0][0]



while préparation:
	for x in range(9):
		for y in range(9):
			Cases[x][y].show('black')
	Select.show('green')
	fenetreInitiale.update()
for x in range(9):
	for y in range(9):
		Cases[x][y].creatNeighbors()
continuer = True
cx = 0
cy = 0
print('lancement de l\'algo')
for x in range(9):
	for y in range(9):
		Cases[x][y].show('black')
while continuer:


	Current = Cases[cx][cy]
	Current.show('green')
	fenetreInitiale.update()

	for x in range(9):
		if Current.ligne[x] !=  Current:
			if Current.valeur != None:
				for y in range(3):
					if Current.valeur in Current.ligne[x].possibilitees[y]:
						Current.ligne[x].pDelete(Current.valeur)
						Current.ligne[x].show('black')
		if Current.colone[x] != Current:
			if Current.valeur != None:
				for y in range(3):
					if Current.valeur in Current.colone[x].possibilitees[y]:
						Current.colone[x].pDelete(Current.valeur)
						Current.colone[x].show('black')
		if Current.carre[x] != Current:
			if Current.valeur != None:
				for y in range(3):
					if Current.valeur in Current.carre[x].possibilitees[y]:
						Current.carre[x].pDelete(Current.valeur)
						Current.carre[x].show('black')




	cy+=1
	if cy == 9:
		cy = 0
		cx+=1
		if cx == 9:
			cx = 0
	Current.show('black')


fenetreInitiale.mainloop()
