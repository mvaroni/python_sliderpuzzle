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

	def __init__(self, list):

		self.gameboard = Board(list)

	# ------------------------------------------
	# Update
	# ------------------------------------------

	def update(self):

		actual_board = self.gameboard

		isgamecomplete = actual_board.verify()

		while isgamecomplete < 0:
			print_board(actual_board)
			print "\nSEARCHING FOR THE BEST ACTION"

			actual_board.heu()


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

	import argparse

	parser = argparse.ArgumentParser(description="Execute slide puzzle.")
	parser.add_argument('-l','--list', nargs='+', help='Integers of the board', required=True)

	args = parser.parse_args()

	# Create game with board passed
	game = Puzzle(args.list)

	# Clear the CMD window
	os.system('cls')

	# Print welcome
	print "\nWelcome to AI-SLIDE PUZZLE\n"

	while game.update() < 0:
		++movements
		print "-----------------------"

	# Print end game message and total number of movements
	print "\nTHE GAME IS COMPLETE!! (%d MOVEMENTS DONE)\n" % movements
