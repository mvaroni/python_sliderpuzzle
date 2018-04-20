# ------------------------------------------
# Print board
# ------------------------------------------

def print_board(board):

    # .format() -> format string using the board numbers
    # .replace() -> format string changing '0' into a blank space

    print """
   -----------
  | {b[0]} | {b[1]} | {b[2]} |
  |-----------|
  | {b[3]} | {b[4]} | {b[5]} |
  |-----------|
  | {b[6]} | {b[7]} | {b[8]} |
   -----------
""".format(b=board).replace('0', ' ')

def verify(board):

	goal = [1,2,3,4,5,6,7,8,0]
	
	if(board == goal):
		return 1

	return -1
