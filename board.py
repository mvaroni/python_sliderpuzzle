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

	#------------------------------
	# Next move
	#------------------------------
	
	def next_move(self, heu_value):

		next_board = Board(self.number_list)
		neighbors = [None] * 1

		# Finds all the neighbors of the cell with '0' (empty cell of the puzzle)
		for (empty, neigbr), value in self.cells_dist.iteritems():
			if value == 1 and self.cells[empty] == "0":
				neighbors.insert(len(neighbors), neigbr)
				empty_cell = empty

		neig_popped = neighbors.pop()
		#ta dando POP no F primeiro e depois ta fazendo a troca, ai isso entra no heu_value
		print "POPPED -------> %s" % (neig_popped)
		
		# Gets the min(heu_value) of actual neighbors after change
		#new_list = next_board.change_cells(neig_popped, next_board.cells)
		new_list = next_board.change_those_cells(neig_popped, empty_cell, next_board.cells, next_board.number_list)
		
		next_board.cells = new_list
		print "NEXT BOARD IS: \n %s" % (next_board.cells)

		print_board(next_board, True)
		# Nao ta printando certo pq o print_board() usa o number_list, nao o dict cells..........

		next_heu_value = next_board.heu()
		print "NEXT HEU VALUE: %s" % (next_heu_value)

	#------------------------------
	# Heuristic function
	#------------------------------
	
	def heu(self):

		heu_value = 0

		for cell, value in self.cells.iteritems():
			#print "CELL: %s \nVALUE: %s" % (cell, value)
			if self.goal[cell] != value:
				heu_value = heu_value + self.dist(cell)

		return heu_value

	#------------------------------
	# Distance of cell from goal
	#------------------------------

	def dist(self, cell):

		for (origin, destiny), value in self.cells_dist.iteritems():
			if origin == cell:
				if self.goal[destiny] == self.cells[cell]:
					# This print shows the cells origin and destiny, as it's distance from each other
					#print "DIST: %s ---- ORIGIN: %s // DESTINY: %s" % (self.cells_dist[(origin,destiny)], origin, destiny)
					#print "GOAL? %s --CELL? %s" % (self.goal[destiny], self.cells[cell])
					return self.cells_dist[(origin,destiny)]

	#------------------------------
	# Changes two cell's value, but it's always the first neighbor of "0"
	#------------------------------

	def change_cells(self, cell, list_of_cells):

		for k, v in list_of_cells.iteritems():
			if v == "0":
				list_of_cells[k] = list_of_cells[cell]
				list_of_cells[cell] = "0"
				break

		return list_of_cells

	#------------------------------
	# Changes two cell's value
	#------------------------------

	def change_those_cells(self, cell, empty_cell, list_of_cells, list_of_numbers):

		for k, v in list_of_cells.iteritems():
			if v == "0":
				list_of_numbers[k] = list_of_numbers[cell] #achar como fazer isso com o indice certo
				list_of_numbers[cell] = "0"

				list_of_cells[empty_cell] = list_of_cells[cell]
				list_of_cells[cell] = "0"

		return list_of_cells		