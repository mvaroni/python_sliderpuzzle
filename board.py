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

	def print_this_board(self):

		print self.cells