

def afficher(grille):
	#permet d'afficher la grille
	for x in range(len(grille)):
		print(grille[x])




def cGrille():
	#création de grille
	grille=9*[0]
	for i in range(len(grille)):
		grille[i]=9*[0]
	afficher(grille)

	for x in range(len(grille)):
		#boucle permettant à l'utilisateur d'indiquer les nombres deja présents dans la grille.
		for y in range(len(grille[x])):
			grille[x][y] = input("case n°"+str(y+1)+" de la ligne n°"+str(x+1)+" : ")
	afficher(grille)