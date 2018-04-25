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
		#self.gameboard.print_this_board()

	# ------------------------------------------
	# Generate board
	# ------------------------------------------

	#def generate_board(self):

		#self.board[9]
	# ------------------------------------------
	# Update
	# ------------------------------------------

	def update(self):

		actual_board = self.gameboard

		print_board(actual_board)
		print "\n\nSEARCHING FOR THE BEST ACTION"

		return verify(actual_board)


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

	import argparse

	parser = argparse.ArgumentParser(description="Execute slide puzzle.")
	parser.add_argument('-l','--list', nargs='+', help='Integers of the board', required=True)

	args = parser.parse_args()

	# Create game with chosen players
	game = Puzzle(args.list)

	# Clear the CMD window
	os.system('cls')

	# Print welcome
	print "\nWelcome to AI-SLIDE PUZZLE\n"

	while game.update() < 0:
		++movements
		print "-----------------------"

	print "THE GAME IS COMPLETE!! (%d MOVEMENTS DONE)" % movements
