from tkinter import *
import copy
w = 504
h = 504
ch = h/9
cw = w/9
CasesRect = []
fenetreInitiale = Tk()
fenetreInitiale.title("Résoudre des sudokus")

Cases = []
cSudoku = Canvas(fenetreInitiale, width=w, height=h)
cSudoku.pack()
for x in range(9):
	CasesRect.append([])
	for y in range(9):
		CasesRect[x].append(None)
class Case(object):
	"""docstring for Case."""

	def __init__(self, x,y):
		self.x = x
		self.y = y
		self.valeur = None
		self.possibilitées = [1,2,3,4,5,6,7,8,9]
	def show(self,color):
		CasesRect[self.x][self.y] = cSudoku.create_rectangle(self.x*ch,self.y*ch,(self.x+1)*ch,(self.y+1)*ch)




def onClickEvent(evt):
	return



for x in range(9):
	for y in range(9):
		Cases.append(Case(x,y))
		Cases[x][y].show('Black')
fenetreInitiale.mainloop()
