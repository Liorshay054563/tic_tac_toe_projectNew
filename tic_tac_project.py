# Tic - Tac - Toe - Game
# Start
from tic_tac_func import *

b = [i for i in range(0, 9)]
turns = 0  # count turns to stop after tie
playerx = True  # switch turns between 'X' and 'O'
win_condition = [
    [b[0], b[1], b[2]],  # possibilities for win
    [b[3], b[4], b[5]],
    [b[6], b[7], b[8]],
    [b[0], b[3], b[6]],
    [b[1], b[4], b[7]],
    [b[2], b[5], b[8]],
    [b[0], b[4], b[8]],
    [b[2], b[4], b[6]]
]
while turns < len(b):  # stop the loop - no more room in the board
    try:
        print_board(b)  # print the actual board play

        # player_turn return - the actual win_condition list, and the winner (if there is)
        win_condition, did_win = player_turn(b, playerx, win_condition)  # catch the returns

        if did_win:  # if there is a winner - finish the code
            exit()
    # catch if errors from user input
    except NameError as e:
        print(e)
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)

    playerx = not playerx  # switch to player "O"
    turns += 1  # add 1 to turns

print("It's a tie!")

# End
