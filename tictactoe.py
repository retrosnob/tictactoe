winning_conditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
x_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
o_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
move_number = 0
winner = ''

def is_game_won():
    global winner
    for i in range(8):
        if x_board[winning_conditions[i][0]] and x_board[winning_conditions[i][1]] and x_board[winning_conditions[i][2]]:
            winner = 'X'
            return True
        elif o_board[winning_conditions[i][0]] and o_board[winning_conditions[i][1]] and o_board[winning_conditions[i][2]]:
            winner = 'O'
            return True
    return False

def is_game_drawn():
    return sum(x_board) + sum(o_board) == 9

def get_winner():
    return winner

def get_move():
    global move_number
    msg = ''
    if move_number % 2 == 0:
        print("It's X's turn.")
    else:
        print("It's O's turn.")

    while True:
        move = input("Enter your move (0-8): ")
        if move.isdigit():
            move = int(move)
            if move >= 0 and move <= 8:
                # Check to see if they square is free
                if x_board[move] != 1 and o_board[move] != 1:
                    break
                else:
                    msg = "Square " + move + " is already taken."
            else:
                msg = "Move number must be between 0 and 8."
        else:
            msg = move + " is not a number."
        print("Invalid move. " + msg)
    return move

def do_move(pos):
    global move_number

    # It's free so go ahead and process the move
    if move_number % 2 == 0:
        # It's crosses' go so add the move to the x_board
        x_board[pos] = 1
    else:
        # It's noughts' go so add the move to the o_board
        o_board[pos] = 1

    move_number += 1

def draw_board():
    for i in range(8):
        row, col = divmod(i, 3)
        print(str(row) + " " + str(col))

if __name__ == "__main__":
    print ("Hello and welcome to Tic Tac Toe")
    draw_board()
    while is_game_won() == False and is_game_drawn() == False:
        move_pos = get_move()
        do_move(move_pos)
    winner = get_winner()
    if winner == '':
        print("The game was a draw.")
    else:
        print(winner + " won.")
