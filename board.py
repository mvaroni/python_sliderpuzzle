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

		self.goal = ["1","2","3","4","5","6","7","8","0"]

		self.cells = {"A" : list[0],
					"B" : list[1],
					"C" : list[2],
					"D" : list[3],
					"E" : list[4],
					"F" : list[5],
					"G" : list[6],
					"H" : list[7],
					"I" : list[8]}

		self.adjacent = [("A","B"),("A","D"),
						 ("B","A"),("B","C"),("B","E"),
						 ("C","B"),("C","F"),
						 ("D","A"),("D","E"),("D","G"),
						 ("E","B"),("E","D"),("E","F"),("E","H"),
						 ("F","C"),("F","E"),("F","I"),
						 ("G","D"),("G","H"),
						 ("H","E"),("H","G"),("H","I"),
						 ("I","F"),("I","H")]

		# A B C
		# D E F
		# G H I

	#def print_this_board(self):

		#print self.cells

	# -------------------------------------------
	# Verify if gameboard cells are equal to goal
	# -------------------------------------------

	def verify(self):

		if(self.number_list == self.goal):
			return 1

		return -1

	#------------------------------
	# Next move
	#------------------------------
	
#	def next_move(self):


	#------------------------------
	# Heuristic function
	#------------------------------
	
	def heu(self):

		for cell, value in self.cells.iteritems():
			print "CELL: %s \nVALUE: %s" % (cell, value)
			if self.correct_value(cell) == value:
				print "IT'S FINE HERE..."
			else:
				print "SHIT HAPPENS..."

	#-----------------------------------
	# Check if a cell's value is correct
	#-----------------------------------

	def correct_value(self, cell):

		if cell == 'A':
			return self.goal[0]
		elif cell == 'B':
			return self.goal[1]
		elif cell == 'C':
			return self.goal[2]
		elif cell == 'D':
			return self.goal[3]
		elif cell == 'E':
			return self.goal[4]
		elif cell == 'F':
			return self.goal[5]
		elif cell == 'G':
			return self.goal[6]
		elif cell == 'H':
			return self.goal[7]
		elif cell == 'I':
			return self.goal[8]
		else:
			return "ERROR"