# Four spaces as indentation [no tabs]

import collections
from util import *

#===============================
# Board
#===============================

class Board:

	#------------------------------
	# Initialize
	#------------------------------

	def __init__(self):

		self.cells = ["A","B","C","D","E","F","G","H","I"]
		self.next = [("A","B"),("A","D"),("B","A"),("B","C"),("B","E"),("C","B"),("C","F"),("D","A"),("D","E"),("D","G"),("E","B"),("E","D"),("E","F"),("E","H"),("F","C"),("F","E"),("F","I"),("G","D"),("G","H"),("H","E"),("H","G"),("H","I"),("I","F"),("I","H")]


"""A B C
   D E F
   G H I"""
