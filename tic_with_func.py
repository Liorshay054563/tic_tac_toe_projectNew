
def print_board():
    print(b[0:3])  # prints the board with the actual places
    print(b[3:6])
    print(b[6:9])

def win_condition(win_con):
    win_con = [
        [b[0], b[1], b[2]],  # possibilities for win
        [b[3], b[4], b[5]],
        [b[6], b[7], b[8]],
        [b[0], b[3], b[6]],
        [b[1], b[4], b[7]],
        [b[2], b[5], b[8]],
        [b[0], b[4], b[8]],
        [b[2], b[4], b[6]]
    ]

b = [i for i in range(0, 9)]
turns = 0  # count turns to stop after tie
playerx = True  # switch turns between 'X' and 'O'


while turns < len(b):
    print_board()

    if playerx:  # now player 'X'
        print("'X' - turn")
    else:
        print("'O' - turn")

    a = int(input("insert your play in board (0-8): "))
    b[a] = "X" if playerx else "O"
    # Check for win
    check_win =[]
    for i in b:
        if isinstance(i,str) and i.isalpha():
            pass
        for l in win_condition():
            for indx in range(len(l)):
                if l[indx] == a:
                    l[indx] = b[a]

    for i in win_condition():
        if len(set(i)) == 1:
            print(f"Player {b[a]} - WIN")
            print(print_board())
            exit()

    playerx = not playerx
    turns += 1

print("It's a tie!")