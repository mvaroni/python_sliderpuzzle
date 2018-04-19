# Four spaces as indentation [no tabs]

import os, sys, inspect
import threading
from util import *
from ai_player import *

#===============================
# Slide Puzzle
#===============================

class Puzzle:

	#------------------------------
	# Initialize
	#------------------------------

	def __init__(self):

		#self.generate_board()
		self.board = [1,2,3,4,5,6,7,8,0]

	# ------------------------------------------
	# Generate board
	# ------------------------------------------

	#def generate_board(self):

		#self.board[9]
	# ------------------------------------------
	# Update
	# ------------------------------------------

	def update(self):

		actual_board = self.board

		print_board(actual_board)
		print "SEARCHING FOR THE BEST ACTION"

		return verify(actual_board)


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

	import argparse

	parser = argparse.ArgumentParser(description="Execute slide puzzle.")
	#parser.add_argument("--human", action="store_true", help="AI player")

	args = parser.parse_args()

	# Create game with chosen players
	game = Puzzle()

	# Clear the CMD window
	os.system('cls')

	# Print welcome
	print "\nWelcome to AI-SLIDE PUZZLE\n"

	while game.update() < 0:
		print "SEARCHING FOR THE BEST ACTION"

	print "THE GAME IS COMPLETE!!"