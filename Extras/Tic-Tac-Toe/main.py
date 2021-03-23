# Tic-Tac-Toe
# This program allows to play the classical tic-tac-toe game.
# There are two players 'X' and 'O' and the first one who
# make a line of 3 wins.

table = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
player_ = True  # If it's True is the turn of X player


def player():
    if player_:
        return "X"
    else:
        return "O"


def print_table():
    print("---------")
    for row in table:
        print(f"| {row[0]} {row[1]} {row[2]} |")
    print("---------")


def insert_player():
    while True:
        position = input(f"What position will player {player()} play (x y): Numbers must be 1, 2 or 3 ").split()
        if len(position) != 2:
            print("error: You should insert two numbers separated by an space")
        else:
            x = int(position[0]) - 1
            y = int(position[1]) - 1
            if not (0 <= x < 3) or not (0 <= y < 3):
                print("error: Invalid position. Numbers must be 1, 2 or 3")
            elif table[y][x] != "_":
                print("error: Invalid position. That position is already occupied")
            else:
                table[y][x] = player()
                global player_
                player_ = not player_  # It's the turn of the other player
                break


def check_table():
    if ["X", "X", "X"] in table:  # Check horizontal lines
        print("Player X won")
        return 1
    elif ["O", "O", "O"] in table:
        print("Player O won")
        return 1
    elif table[0][0] == table[1][1] == table[2][2] == "X":  # Check principal diagonal
        print("Player X won")
        return 1
    elif table[0][0] == table[1][1] == table[2][2] == "O":
        print("Player O won")
        return 1
    elif table[0][2] == table[1][1] == table[2][0] == "X":  # Check the other diagonal
        print("Player X won")
        return 1
    elif table[0][2] == table[1][1] == table[2][0] == "O":
        print("Player O won")
        return 1
    else:  # Check vertical lines
        for col in range(3):
            if table[0][col] == table[1][col] == table[2][col] == "X":
                print("Player X won")
                return 1
            elif table[0][col] == table[1][col] == table[2][col] == "O":
                print("Player O won")
                return 1
            else:
                print("The match continues")
                return 0


print("Welcome to Tic-Tac-Toe")

while True:
    insert_player()
    print_table()
    if check_table() == 1:  # There is a winner
        break
