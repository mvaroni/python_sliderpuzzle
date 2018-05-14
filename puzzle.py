# Four spaces as indentation [no tabs]

import os, sys, inspect
import threading
from util import *
from board import *

#===============================
# Slide Puzzle
#===============================

movements = 0

class Puzzle:

	#------------------------------
	# Initialize
	#------------------------------

	def __init__(self, list, quiet):

		self.gameboard = Board(list)
		self.debug = quiet

	# ------------------------------------------
	# Update
	# ------------------------------------------

	def update(self):

		actual_board = self.gameboard

		print_board(actual_board, self.debug)

		heuristic_value = actual_board.heu()

		while heuristic_value > 0:
			
			actual_board.next_move(heuristic_value)

			if(not self.debug):
				#os.system('cls')
				print_board(actual_board, self.debug)
			print "\nSEARCHING FOR THE BEST ACTION"

		return heuristic_value


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

	import argparse

	parser = argparse.ArgumentParser(description="Execute slide puzzle.")
	parser.add_argument('-l','--list', nargs='+', help='Integers of the board', required=True)
	parser.add_argument('-q','--quiet', nargs='?', help='Debuger', const=True, default=False)

	args = parser.parse_args()

	# Create game with board passed
	game = Puzzle(args.list, args.quiet)

	# Clear the CMD window
	os.system('cls')

	# Print welcome
	print "\nWelcome to AI-SLIDE PUZZLE\n"

	while game.update() < 1:
		++movements
		print "-----------------------"

	# Print end game message and total number of movements
	print "\nTHE GAME IS COMPLETE!! (%d MOVEMENTS DONE)\n" % movements
