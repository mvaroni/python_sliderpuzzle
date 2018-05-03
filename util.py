# ------------------------------------------
# Print board on CMD
# ------------------------------------------

def print_board(gameboard, debug):

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