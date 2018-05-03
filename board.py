# Four spaces as indentation [no tabs]

from collections import defaultdict
from util import *

#===============================
# Board
#===============================

class Board:

	#------------------------------
	# Initialize
	#------------------------------

	def __init__(self, list):

		self.number_list = list

		self.goal = {"A" : "1",
					 "B" : "2",
					 "C" : "3",
					 "D" : "4",
					 "E" : "5",
					 "F" : "6",
					 "G" : "7",
					 "H" : "8",
					 "I" : "0"}

		self.cells = {"A" : list[0],
					  "B" : list[1],
					  "C" : list[2],
					  "D" : list[3],
					  "E" : list[4],
					  "F" : list[5],
					  "G" : list[6],
					  "H" : list[7],
					  "I" : list[8]}

		self.cells_dist = {
						#Distance of A to other cells
						("A","B"):1, ("A","C"):2, ("A","D"):1, ("A","E"):2, ("A","F"):3, ("A","G"):2, ("A","H"):3, ("A","I"):4,
						#Distance of B to other cells
						("B","A"):1, ("B","C"):1, ("B","D"):2, ("B","E"):1, ("B","F"):2, ("B","G"):3, ("B","H"):2, ("B","I"):3,
						#Distance of C to other cells
						("C","A"):2, ("C","B"):1, ("C","D"):3, ("C","E"):2, ("C","F"):1, ("C","G"):4, ("C","H"):3, ("C","I"):2,
						#Distance of D to other cells
						("D","A"):1, ("D","B"):2, ("D","C"):3, ("D","E"):1, ("D","F"):2, ("D","G"):1, ("D","H"):2, ("D","I"):3,
						#Distance of E to other cells
						("E","A"):2, ("E","B"):1, ("E","C"):2, ("E","D"):1, ("E","F"):1, ("E","G"):2, ("E","H"):1, ("E","I"):2,
						#Distance of F to other cells
						("F","A"):3, ("F","B"):2, ("F","C"):1, ("F","D"):2, ("F","E"):1, ("F","G"):3, ("F","H"):2, ("F","I"):1,
						#Distance of G to other cells
						("G","A"):2, ("G","B"):3, ("G","C"):4, ("G","D"):1, ("G","E"):2, ("G","F"):3, ("G","H"):1, ("G","I"):2,
						#Distance of H to other cells
						("H","A"):3, ("H","B"):2, ("H","C"):3, ("H","D"):2, ("H","E"):1, ("H","F"):2, ("H","G"):1, ("H","I"):1,
						#Distance of I to other cells
						("I","A"):4, ("I","B"):3, ("I","C"):2, ("I","D"):3, ("I","E"):2, ("I","F"):1, ("I","G"):2, ("I","H"):1}

		# A B C
		# D E F
		# G H I

	# -------------------------------------------
	# Verify if gameboard cells are equal to goal
	# -------------------------------------------

	"""def verify(self):

		if(self.number_list == self.goal):
			return 1

		return -1"""

	#------------------------------
	# Next move
	#------------------------------
	
#	def next_move(self):


	#------------------------------
	# Heuristic function
	#------------------------------
	
	def heu(self):

		heu_value = 0

		for cell, value in self.cells.iteritems():
			print "CELL: %s \nVALUE: %s" % (cell, value)
			if self.goal[cell] != value:
				heu_value = heu_value + self.dist(cell)

		return heu_value

	#------------------------------
	# Distance of cell from goal
	#------------------------------

	def dist(self, cell):

		for (origin, destiny), value in self.cells_dist.iteritems():
			if destiny == cell:
				print "DIST: %s" % (self.cells_dist[(origin,destiny)])
				return self.cells_dist[(origin,destiny)]