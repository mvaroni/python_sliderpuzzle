# ------------------------------------------
# Print board
# ------------------------------------------

def print_board(gameboard):

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
""".format(b=gameboard.number_list).replace('0', ' ')

def verify(gameboard):

    goal = ["1","2","3","4","5","6","7","8","0"]

    if(gameboard.number_list == goal):
        return 1

    return -1