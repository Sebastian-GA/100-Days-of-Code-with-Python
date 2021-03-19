# Tic-Tac-Toe
# This program allows to play the classical tic-tac-toe game.
# There are two players 'X' and 'O' and the first one who
# make a line of 3 wins.

table = list("_________")
player_ = True  # If it's True is the turn of X player

def player():
    if player_:
        return "X"
    else:
        return "O"

def print_table():
    print("---------")
    print(f"| {table[0]} {table[1]} {table[2]} |")
    print(f"| {table[3]} {table[4]} {table[5]} |")
    print(f"| {table[6]} {table[7]} {table[8]} |")
    print("---------")

def insert_player():
    while True:
        position = list(input(f"What position will player {player()} play (x y): "))
        if (len(position) != 3) or position[1] != " ":
            print("error: You should insert two numbers separated by an space")
        else:
            x = int(position[0])
            y = int(position[2])
            if not(0 <= x < 3) or not(0 <= y < 3):
                print("error: Invalid position. Numbers must be 0, 1 or 2")
            elif table[x + y*3] != "_":  # That space is occuped
                print("error: Invalid position. That position is alredy occuped")
            else:
                table[x + y*3] = player()
                global player_
                player_ = not player_  # It's the turn of the other player
                break
    
    return 0

def check_table():
    if "'X', 'X', 'X'" in str(table):  # Check horizontal lines
        print("Player X won")
        return 1
    elif "'O', 'O', 'O'" in str(table):
        print("Player O won")
        return 1
    elif table[0] == table [4] == table[8] == "X":  # Check principal diagonal
        print("Player X won")
        return 1
    elif table[0] == table [4] == table[8] == "O":
        print("Player O won")
        return 1
    elif table[2] == table [4] == table[6] == "X":  # Check the other diagonal
        print("Player X won")
        return 1
    elif table[2] == table [4] == table[6] == "O":
        print("Player O won")
        return 1
    else:
        
        # Check vertical lines

        print("The match continues")
        return 0

while True:
    insert_player()
    print_table()
    if check_table() == 1:  # There is a winner
        break
