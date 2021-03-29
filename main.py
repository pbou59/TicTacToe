# Day 83 Tik Tac Toe Game
from os import system

print("Tic Tac Toe")

board = {
    1: ["   ", " | ", "   ", " | ", "   "],
    2: ["---", "---", "---", "---", "---"],
    3: ["   ", " | ", "   ", " | ", "   "],
    4: ["---", "---", "---", "---", "---"],
    5: ["   ", " | ", "   ", " | ", "   "]
}


def update_board():
    system('cls')
    for rows in board:
        print("".join(board[rows]))


update_board()
player = "X"
picks = 0
game_on = True


def check_for_win():
    # Horizontal win tests
    if board[1][0] == " X " and board[1][2] == " X " and board[1][4] == " X ":
        print("X Wins")
        return False
    elif board[1][0] == " O " and board[1][2] == " O " and board[1][4] == " O ":
        print("O Wins")
        return False
    elif board[3][0] == " X " and board[3][2] == " X " and board[3][4] == " X ":
        print("X Wins")
        return False
    elif board[3][0] == " O " and board[3][2] == " O " and board[3][4] == " O ":
        print("O Wins")
        return False
    elif board[5][0] == " X " and board[5][2] == " X " and board[5][4] == " X ":
        print("X Wins")
        return False
    elif board[5][0] == " O " and board[5][2] == " O " and board[5][4] == " O ":
        print("O Wins")
        return False

    # Vertical Win Tests
    elif board[1][0] == " X " and board[3][0] == " X " and board[5][0] == " X ":
        print("X Wins")
        return False
    elif board[1][0] == " O " and board[3][0] == " O " and board[5][0] == " O ":
        print("O Wins")
        return False
    elif board[1][2] == " X " and board[3][2] == " X " and board[5][2] == " X ":
        print("X Wins")
        return False
    elif board[1][2] == " O " and board[3][2] == " O " and board[5][2] == " O ":
        print("O Wins")
        return False
    elif board[1][4] == " X " and board[3][4] == " X " and board[5][4] == " X ":
        print("X Wins")
        return False
    elif board[1][4] == " O " and board[3][4] == " O " and board[5][4] == " O ":
        print("O Wins")
        return False

    # Diagonal Win Tests
    elif board[1][0] == " X " and board[3][2] == " X " and board[5][4] == " X ":
        print("X Wins")
        return False
    elif board[1][0] == " O " and board[3][2] == " O " and board[5][4] == " O ":
        print("O Wins")
        return False
    elif board[1][4] == " X " and board[3][2] == " X " and board[5][0] == " X ":
        print("X Wins")
        return False
    elif board[1][4] == " O " and board[3][2] == " O " and board[5][0] == " O ":
        print("O Wins")
        return False
    elif picks == 9:
        print("Draw")
    else:
        return True


while game_on:

    print(game_on)
    move = input(f"Player {player}, enter row and column y,x: ")
    row = int(move[0])
    column = int(move[-1])

    row = 2 * row - 1
    column = 2 * column - 2

    if board[row][column] == "   ":
        board[row][column] = str(f" {player} ")
    else:
        print("There is already a mark in that space.  Pick again")

    update_board()
    if player == "X":
        player = "O"
    else:
        player = "X"
    picks += 1
    game_on = check_for_win()
